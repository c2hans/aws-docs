---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/agents-cluster-setup.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Set up an Amazon EKS cluster for agent workloads

## Overview
<a name="agents-cluster-setup-overview"></a>

Agents on a cluster need a few controls in place before the first agent runs. Agent pods need a runtime that isolates model-generated code from the node. Their egress needs a boundary that they can’t edit. Their IAM roles need a ceiling that no single role grant can exceed.

The base setup in the reference sample puts those controls in place, and it’s the same on both paths. It’s an EKS Auto Mode cluster with network policy enforced, a container registry, and a permissions boundary for agent IAM roles. The reference sample creates it with Terraform, and each later page turns on one more component by changing one variable and applying again. The EKS cluster in the reference sample is created with a private Kubernetes API that is not accessible to the internet.

The reference sample shows one way to run agents on Amazon EKS. It isn’t a production-ready deployment. Use it to learn the pattern, then adapt, review, and test what you adopt. See the note on sample templates in [Overview of AI agents on Amazon EKS](agents.md).

The following diagram shows what the base setup in the reference sample creates, which includes the EKS Auto Mode cluster with a private Kubernetes API endpoint, a bastion instance for interacting with the private Kubernetes API, the Amazon ECR repositories for agent images, an AWS CodeBuild project that builds them, the permissions boundary, and the EKS Capabilities.

![A platform engineer provisions the base: an EKS Auto Mode cluster with a private API endpoint, network policy enforced from node boot, and Nitro Sandboxes, plus Amazon ECR, a CodeBuild project that builds agent images, a permissions boundary, a bastion or a workstation, and EKS Capabilities.](https://docs.aws.amazon.com/eks/latest/userguide/images/agents-cluster-setup.png)

## Quick start
<a name="agents-cluster-quickstart"></a>

These steps take you from an empty AWS account to a running agent. The rest of this page, [Set up EKS Capabilities and in-cluster components for agents](agents-capabilities-setup.md), and [Deploy an agent on Amazon EKS](agents-application-setup.md) explain each step in detail.

Before you start, you need the following:
+ An AWS IAM Identity Center instance and a user in it, for Argo CD. See [Set up IAM Identity Center for Argo CD](#agents-cluster-identity-center).
+ Amazon Bedrock access to Claude Sonnet 5.5 in us-east-1, us-east-2, and us-west-2, the Regions that the default US inference profile routes to.
+ The AWS CLI v2, Terraform 1.9 or later, `kubectl`, Python 3, Git, `jq`, and `curl`. With the bastion, which the base setup creates for its private-only endpoint, also the AWS Systems Manager Session Manager plugin for the AWS CLI.

Then follow these steps:

1.  **Get the sample.** Clone the reference sample and change to its `agents` directory. Run every command in this guide from this directory.

   ```bash
   git clone https://github.com/aws-samples/sample-eks-docs.git
   cd sample-eks-docs/agents
   ```

1.  **Choose your path.** Set `PAVED_PATH` to the path you deploy. Every later command in this guide uses it, so set it again in any new shell.

------
#### [ Open source ]

   ```bash
   export PAVED_PATH=open-source
   ```

------
#### [  AWS services ]

   ```bash
   export PAVED_PATH=aws-services
   ```

------

1.  **Create your variables file.** Copy the minimal example, then replace `my-identity-center-user` with your Identity Center user:

   ```bash
   cp terraform/$PAVED_PATH/minimal.tfvars terraform/$PAVED_PATH/my.tfvars
   ```

   The file has four values:

   ```hcl
   region                           = "us-west-2"
   name                             = "my-agents"
   enable_argocd                    = true
   argocd_admin_existing_user_names = ["my-identity-center-user"]
   ```

   By default, the cluster’s API endpoint is private, and the commands that need the cluster run on a bastion in the VPC. To run them from your workstation instead, also add the three variables in [Run from your workstation (optional)](#agents-cluster-public-endpoint).

1.  **Create the cluster.** `apply.sh` shows the plan and waits for you to type `yes`. The apply takes about 18 minutes.

   ```bash
   terraform -chdir=terraform/$PAVED_PATH init
   ./scripts/apply.sh --root terraform/$PAVED_PATH -var-file=my.tfvars
   ```

   If you added the public endpoint variables, also run `aws eks update-kubeconfig --name my-agents --region us-west-2`.

1.  **Install the components.** Build the agent images, then let Argo CD install the in-cluster components:

   ```bash
   ./scripts/build-images.sh --root terraform/$PAVED_PATH
   ./scripts/run-stack.sh --root terraform/$PAVED_PATH -- ./scripts/bootstrap-gitops.sh --path $PAVED_PATH --sync
   ```

1.  **Deploy your first agent.** Follow [Deploy an agent on Amazon EKS](agents-application-setup.md).

1.  **Check that it works.** Run the sample’s checks:

   ```bash
   ./scripts/exercise.sh --path $PAVED_PATH
   ```

   Each check prints one of the following marks. A base setup ends with `all exercised phases passed`.
   +  `✓` The check passed.
   +  `✗` The check failed.
   +  `!` Skipped, because that layer is off. The line says which variable turns it on.
   +  `?` Not checked, because the script can’t verify that layer from where it runs. Add `--strict` to count these as failures.

The resources incur charges while they exist, including the EKS cluster, its nodes, NAT gateways, the bastion, and any managed service you turn on. When you finish, follow [Clean up](#agents-cluster-setup-cleanup).

### Where commands run
<a name="agents-cluster-kubectl"></a>

Commands in this guide run in one of two places:
+  **Scripts and commands that use the reference sample’s files**, such as `apply.sh`, `build-images.sh`, `exercise.sh`, and anything that starts with `./scripts/run-stack.sh`, run on your workstation, from the `agents` directory of your clone. `run-stack.sh` passes its command on to the bastion if your cluster has one, and runs it on your workstation otherwise, so you type the same command either way:

  ```bash
  ./scripts/run-stack.sh --root terraform/$PAVED_PATH -- kubectl get pods -A
  ```
+  **Commands that start with `kubectl` ** run wherever `kubectl` reaches the cluster. With the default private endpoint, that’s a shell on the bastion, an EC2 instance in the VPC where `kubectl` is already configured. With a public endpoint, it’s your workstation. To open a shell on the bastion, run the following from the `agents` directory:

  ```bash
  aws ssm start-session --region {{region-code}} --target "$(terraform -chdir=terraform/$PAVED_PATH output -json bastion | jq -r .instance_id)"
  ```

**Note**
Through the bastion, a command’s output appears only when the command finishes, and `run-stack.sh` stops a command after 3600 seconds by default. Avoid commands that never end on their own, such as `kubectl get -w` or `kubectl logs -f`. Use `kubectl wait` with a timeout instead.

## What the base setup includes
<a name="agents-cluster-what-you-get"></a>

 **EKS Auto Mode**
Agents need a sandboxed runtime, and a sandbox can only run on an instance type that supports it. With self-managed nodes, you’d have to match runtime classes, node pools, and instance types yourself, and install the components that enforce network policy and deliver per-pod credentials. EKS Auto Mode provides the sandbox runtime classes, network policy enforcement, the EKS Pod Identity agent, and the AWS Load Balancer Controller as part of the cluster. It provisions a sandbox-capable instance from the pod’s runtime class, so an agent’s pod spec needs no node selector, toleration, or sidecar. See [Automate cluster infrastructure with EKS Auto Mode](automode.md).

 **Network policy**
An agent can be told by a prompt to connect anywhere, so its egress has to be limited by something outside the agent’s control. Network policy is the only networking layer in the base setup. It’s built in three tiers so that the guarantee doesn’t depend on objects an agent team can edit: a cluster-scoped policy over every agent namespace, a namespaced default-deny policy, and a policy for each agent with that agent’s own destinations. Agent nodes also enforce policy strictly from boot, so a new pod can’t make an outbound call in the moment before its policies are programmed. See [Restrict agent egress with network policy](agents-network-policies.md).

 **A container registry**
The sandbox isolates what an image does, but it doesn’t decide which image runs. In isolated sandbox mode, the sandbox policy doesn’t pin a pod’s image digest, arguments, environment, or mounts, so control which images run through the registry, admission control, and your delivery pipeline. The base setup uses Amazon ECR repositories with immutable tags, so a tag can’t be repointed at a different image, and scan-on-push. See [Isolate agent workloads on Amazon EKS](agents-isolation.md).

 **A permissions boundary**
Each agent gets its own IAM role, and teams that declare agents shouldn’t be able to grant an agent more than the platform team allows. An IAM permissions boundary attached to every agent role sets that ceiling. Whatever a role’s own policy says, it can’t exceed the boundary. See [Give each agent its own identity with EKS Pod Identity](agents-identity-agent.md).

 **A GitOps control plane**
Everything inside the cluster that later pages add, including the network policies, the `Agent` resource definition, and the in-cluster components, is delivered from Git, so a change is reviewed before it reaches the cluster and drift is corrected. The base setup uses the Argo CD EKS Capability, which AWS runs and upgrades outside the cluster. It signs users in through AWS IAM Identity Center and can’t be created without an Identity Center instance. [Set up EKS Capabilities and in-cluster components for agents](agents-capabilities-setup.md) bootstraps it. See [Continuous Deployment with Argo CD](argocd.md).

 **Access to a private API endpoint**
The Kubernetes API controls every agent, so the base setup keeps its endpoint private. Operators reach it from inside the VPC. The base setup adds a bastion for that, an EC2 instance that you reach through AWS Systems Manager Session Manager with no inbound security group rules, so there’s no SSH port to expose. To run every step from your workstation instead, use workstation mode, which turns on the public endpoint restricted to the addresses you name and turns off the bastion. Requests to the public endpoint still need an IAM principal with an access entry. See [Run from your workstation (optional)](#agents-cluster-public-endpoint).

The reference sample controls the last two with `enable_argocd` and `enable_bastion`, both `true` in the base setup. Set `enable_argocd = false` only if your organization can’t have an Identity Center instance. Every other resource still applies, but nothing from the GitOps directory reaches the cluster until you install it with the reference sample’s `scripts/install-platform.sh`. `enable_bastion = false` requires the public endpoint, because the bastion is otherwise the only path to `kubectl`. `enable_network_policy` is `true` in the base setup.

## What the base setup does not include
<a name="agents-cluster-later"></a>

Each of the following components is off in the base setup. The linked page turns it on.

| Component | Base value | Turned on in |
| --- | --- | --- |
| Egress gateway |  `enable_gateway = false`  |  [Route agent egress through a gateway](agents-gateway.md)  |
| Telemetry and dashboards |  `enable_observability = false`  |  [Observe agent workloads on Amazon EKS](agents-observability.md)  |
| Service mesh |  `mesh_mode = "none"`  |  [Choose a service mesh mode for agents](agents-mesh.md)  |
| Authenticated ingress |  `enable_ingress = false`  |  [Expose an agent through an authenticated Application Load Balancer](agents-ingress.md)  |
| Durable conversation storage |  `enable_checkpoints = false`  |  [Store agent session state](agents-session-state.md)  |
| Session cache |  `enable_session_state = false`  |  [Store agent session state](agents-session-state.md)  |
| Memory | Off |  [Choose an agent’s memory components](agents-memory.md)  |
| Evaluation |  `enable_evaluations = false`  |  [Evaluate agent output on Amazon EKS](agents-evaluations.md)  |

**Note**
The egress gateway differs by path:
 **Open source path.** AgentGateway, running in the cluster.
 ** AWS services path.** AgentCore Gateway, a managed service outside the cluster.
Until you turn it on in [Route agent egress through a gateway](agents-gateway.md), agents call Amazon Bedrock directly with their own IAM role, and the egress policy permits the Amazon Bedrock runtime endpoint as the model destination.

## Prerequisites
<a name="agents-cluster-prerequisites"></a>

**Important**
The resources in this section incur charges even when no agent is serving requests: the EKS cluster and its EKS Auto Mode management fee, the nodes that run in-cluster components, NAT gateways, the bastion, and any managed service you turn on. The CodeBuild project is billed only for the minutes it builds. To stop charges, follow [Clean up](#agents-cluster-setup-cleanup) when you finish.
+ Terraform 1.9 or later. For installation instructions, see [Install Terraform](https://developer.hashicorp.com/terraform/install) on the HashiCorp Developer website.
+  `kubectl` within one minor version of the EKS cluster. For installation instructions, see [Set up `kubectl` and `eksctl`](install-kubectl.md).
+ The AWS CLI v2, Python 3, `jq`, `curl`, and `git`. With the default bastion, also the [Session Manager plugin](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html) for the AWS CLI.
+ An IAM principal that can create EKS clusters, VPC resources, IAM roles and IAM policies, and the managed services your path uses. The apply creates a permissions boundary and the roles that other roles are created under, so it fails without IAM write permissions. Scope the principal down after the first apply.
+ Amazon Bedrock model access for every model your agents call. Access is per account and per Region. The default model, `direct_model_id`, is the Claude Sonnet 5.5 US inference profile `us.anthropic.claude-sonnet-5-5`, which routes to us-east-1, us-east-2, and us-west-2, so turn on access in all three. A model you haven’t requested access to returns `AccessDeniedException`. See [Access Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) in the *Amazon Bedrock User Guide*.
+ An AWS IAM Identity Center instance, and at least one user in it to administer Argo CD. See [Set up IAM Identity Center for Argo CD](#agents-cluster-identity-center).
+ An AWS Region that has every service your path uses. Isolated pods are available in the US commercial AWS Regions on Kubernetes version 1.36 or later. The templates default to 1.36. The AWS services path also needs Amazon Bedrock AgentCore and Amazon S3 Vectors in the same Region. See [Sandboxing on Amazon EKS with isolated and confidential pods](sandboxing.md).

### Set up IAM Identity Center for Argo CD
<a name="agents-cluster-identity-center"></a>

The Argo CD capability has no local users and signs users in through IAM Identity Center, so it requires an Identity Center instance even if nobody uses the Argo CD console. Reconciliation runs as the capability’s IAM role. Terraform finds the instance, creates an Argo CD administrator group, adds the users you name, and maps the group to the Argo CD `ADMIN` role. Terraform can’t create the instance, so check for one first.

1. Look for an existing instance in the Region where you will create the EKS cluster.

   ```bash
   aws sso-admin list-instances --region {{region-code}} \
     --query 'Instances[].[InstanceArn,IdentityStoreId]' --output text
   ```

   An organization has at most one instance, and it’s often in a different Region from your cluster. If the command returns nothing, run it again with your organization’s Identity Center Region, commonly `us-east-1`. If you find the instance there, set that Region as `argocd_idc_region` in the next step.

   The instance must be visible from the account where you create the cluster. If your organization instance is managed only from another account, Terraform can’t create the administrator group. In that case, ask your Identity Center administrator for the instance ARN and a group to map, and set `argocd_idc_instance_arn` and `argocd_rbac_role_mappings` instead. The first points the capability at the instance without looking it up, and the second maps a group that already exists to an Argo CD role, so Terraform doesn’t need to create a group.

1. If you have no instance, create an account instance in the cluster’s Region. The Terraform AWS provider has no resource for this. If your organization’s policies block account instances, ask your Identity Center administrator.

   ```bash
   aws sso-admin create-instance --region {{region-code}} --name my-agents-identity
   ```

1. Choose the Argo CD administrators. To use existing Identity Center users, list their user names:

   ```bash
   aws identitystore list-users --region {{region-code}} \
     --identity-store-id {{identity-store-id}} \
     --query 'Users[].UserName' --output text
   ```

   Terraform adds the users named in `argocd_admin_existing_user_names` to the Argo CD administrator group. On a new instance with no users, have Terraform create one with `argocd_admin_users` in the next step. Identity Center emails each new user an invitation to set a password.

## Step 1: Set the base variables
<a name="agents-cluster-setup-step1"></a>

Clone the [reference sample’s repository](https://github.com/aws-samples/sample-eks-docs) on GitHub. Its `agents` directory holds this section’s code, and the commands in this section run from that directory.

```bash
git clone https://github.com/aws-samples/sample-eks-docs.git
cd sample-eks-docs/agents
```

Argo CD reads the stack’s charts from this public repository, at the revision that `gitops_repo_revision` names, `main` by default. Set it to a release tag or a commit, so that a later change to the repository reaches your cluster only when you move it. Nothing from your account goes to any repository. The apply renders your stack’s values into files beside the root chart, and the bootstrap script in [Set up EKS Capabilities and in-cluster components for agents](agents-capabilities-setup.md) passes them to the cluster in the root Application.

You don’t need a Git repository of your own. To run templates you’ve changed, use a fork, as described in [(Optional) Use your own fork](#agents-cluster-own-repo).

Create a variables file, such as `terraform/open-source/my.tfvars` or `terraform/aws-services/my.tfvars`, from the sample’s `minimal.tfvars` in that root. It holds the four base values:

```hcl
region                           = "us-west-2"
name                             = "my-agents"                   # becomes the cluster name
enable_argocd                    = true
argocd_admin_existing_user_names = ["my-identity-center-user"]   # Identity Center users who administer Argo CD
# gitops_repo_revision           = "tag-or-commit"               # pin the stack's code
```

Every other variable has a default, and the base turns every optional component off, so each later page changes one line. The sample’s `example.tfvars` annotates every option, including `argocd_admin_users` for an Identity Center instance with no users and `argocd_idc_region` for an instance in another Region. To use an existing cluster, add the settings from [Use an existing cluster](#agents-cluster-existing). To change control plane logging, see [Control plane logging](#agents-cluster-logging). To choose the cluster’s administrators, see [Cluster administration](#agents-cluster-variables).

The plan in the next step validates the file and reports any variable it rejects. Agents without a gateway call `direct_model_id`, the Claude Sonnet 5.5 US inference profile `us.anthropic.claude-sonnet-5-5` by default.

### Run from your workstation (optional)
<a name="agents-cluster-public-endpoint"></a>

The private endpoint stays on in every configuration, so nodes always use it. In workstation mode, you also turn on the public endpoint, restricted to the addresses that need it, and turn off the bastion, so every step in this section runs from your workstation:

```hcl
cluster_endpoint_public_access       = true
cluster_endpoint_public_access_cidrs = []   # empty: the public IPv4 address of the machine running Terraform
enable_bastion                       = false
```

The plan refuses `enable_bastion = false` with a private-only endpoint. On an existing cluster, it checks that cluster’s actual endpoint setting.

With an empty list, Terraform looks up the public address of the machine that runs it from `checkip.amazonaws.com` and `api.ipify.org`, and allows each address it finds as a `/32`. Every apply reads the addresses again, so an apply from a new address moves the allowlist. The default is for a network with a single public address. On a corporate network or VPN that sends traffic from several public addresses, name those addresses' CIDRs in `cluster_endpoint_public_access_cidrs`. If your network uses addresses you can’t name, use the bastion, or apply from a connection with one public address. The endpoint can see one of those addresses that neither lookup reported, and requests from that address time out, even after an apply that worked before. The addresses can also change over time, so addresses that an earlier apply stored can go stale. `check-endpoint.sh` names the missing addresses. The templates refuse `0.0.0.0/0`, and the setting applies only when the reference sample creates the cluster. After the apply, point `kubectl` at the cluster:

```bash
aws eks update-kubeconfig --region {{region-code}} --name my-agents
```

The reference sample’s scripts reach the stack through `scripts/run-stack.sh`, which reads the Terraform root’s outputs. With a bastion, it runs the command on the bastion through Session Manager. Without one, it runs the command on your workstation with a kubeconfig for that cluster only, so it never uses your current `kubectl` context.

A public endpoint doesn’t refuse an address outside its allowlist. The connection times out, which looks like a network fault. If `kubectl` or `run-stack.sh` times out against the public endpoint, run the sample’s `check-endpoint.sh` before you apply again. `run-stack.sh` also runs it when the endpoint doesn’t answer.

```bash
./scripts/check-endpoint.sh --root terraform/$PAVED_PATH
```

The script prints the cluster’s allowlist, this machine’s address as two lookup services see it, whether each address is in the list, and whether the endpoint answers. It then names the fix. If the endpoint is private, use the bastion. If your address isn’t in the list, name your network’s CIDRs, or use the bastion or a connection with one public address. If the two lookups disagree, it prints each missing `/32`. If your address is in the list but the endpoint doesn’t answer, EKS is still rolling out the change, so wait and run the script again. If your network changes during an apply, such as the first apply of the base setup, the allowlist can name an address your machine no longer uses. Run the script, apply again, and wait for EKS to roll out the change.

Your workstation needs the AWS CLI version 2, Terraform 1.9 or later, `kubectl`, Python 3, Git, `jq`, and `curl`. Building images needs Docker or Finch only with `enable_image_build = false`. Workstation mode differs from the bastion in the following ways:
+  **Image builds, with `enable_image_build = false`.** By default, images build in CodeBuild in both modes. With it off, the bastion builds natively for x86\_64, and an Arm workstation builds `linux/amd64` images through emulation.
+  **Ingress.** The ingress load balancer is internal by default, and its names resolve only inside the VPC. To reach agents and the chat interface from your workstation, make it internet-facing, which needs a public hosted zone. Without a zone, keep it internal: the sample’s exercise script runs its ingress checks from a short-lived pod in the cluster, so they work from your workstation too. See [Internet-facing load balancer for workstation mode](agents-ingress.md#agents-ingress-internet-facing).
+  **OAuth consent.** `consent.sh` port-forwards from your workstation instead of tunneling through the bastion.
+  **Teardown.** Every step runs with your own credentials.
+  **VPC endpoints.** Leave out `ssm`, `ssmmessages`, `ec2messages`, `eks`, `elasticloadbalancing`, and `bedrock`. They serve the bastion and the scripts that run on it. See [Keep AWS traffic in the VPC](#agents-cluster-vpc-endpoints).

See [Cluster API server endpoint](cluster-endpoint.md).

### (Optional) Use your own fork
<a name="agents-cluster-own-repo"></a>

Argo CD reads the stack’s code from the reference sample’s public repository by default. To run templates you’ve changed, fork `sample-eks-docs` on GitHub, commit your changes to a branch of the fork, and point the stack at it in your variables file:

```hcl
gitops_repo_url      = "https://github.com/my-org/sample-eks-docs.git"
gitops_repo_revision = "my-changes"   # your branch, tag, or commit
gitops_repo_path     = "agents/"
```

Argo CD reads a public fork with no credential. A fork of a public repository is public, so don’t commit anything that names your account, such as an `Agent` manifest with your image URL. The stack’s own values never go to Git.

#### Use a private repository
<a name="agents-cluster-private-repo"></a>

For files that must stay private, such as the `Agent` manifests in [Deploy an agent on Amazon EKS](agents-application-setup.md), use a private repository instead, such as a private copy of `sample-eks-docs`. Give Argo CD access to it through an AWS CodeConnections connection to your Git host, in `argocd_codeconnections_arns`, so no credential enters the cluster. For a Git host that CodeConnections doesn’t support, store the credential in Secrets Manager and list its ARN in `argocd_secrets_manager_secret_arns`. The sample’s `gitops-mirror.sh` can also create a private AWS CodeCommit repository, which Argo CD reads with no stored credential. Its `create` command prints the variables to set.

## Step 2: Apply
<a name="agents-cluster-setup-step2"></a>

The first `terraform init` downloads providers and modules, which a local plugin cache speeds up. The apply creates the cluster first, then the ACK and Argo CD EKS Capabilities in parallel.

Initialize the root module, review the plan, and apply it. The reference sample’s `scripts/apply.sh` plans to a file, refuses a plan that would replace a stateful or security resource or that reads one as deleted during refresh, and otherwise applies exactly that plan. A single bad refresh can make a plain `terraform apply` delete a bucket’s public access block, policy, and encryption, so use the script for this and every later apply. Pass `--allow-replace` only after you review a replacement it refused. The script shows the plan and waits for you to type `yes`, and `--yes` skips the prompt.

```bash
terraform -chdir=terraform/$PAVED_PATH init
./scripts/apply.sh --root terraform/$PAVED_PATH -var-file=my.tfvars
```

The apply creates the cluster, the VPC, the ECR repositories, the permissions boundary, the kro, ACK, and Argo CD EKS Capabilities, the Argo CD administrator group and its role mapping, an AWS CodeBuild project for agent images with its role, source bucket, and log group, and, unless you turned it off for a public endpoint, the bastion. The apply doesn’t build any images. It also writes your stack’s values, every ARN, endpoint, and name the in-cluster components need, into the `*-values.yaml` files beside the root chart in `gitops/platform/$PAVED_PATH/`. These files are the only interface between Terraform and the in-cluster configuration, so you never copy an ARN into a manifest by hand. There’s nothing to commit or push. The bootstrap script passes the files to the cluster in the root Application.

**Important**
The rendered files contain your account ID, OIDC issuer, Amazon ECR repository URLs, and cluster name, over the placeholders that the repository commits. Don’t commit them. Restore the placeholders with `git checkout` before you commit a change of your own. The sample’s `scripts/validate.sh` fails when a value from your account reaches the tree.

Print the outputs:

```bash
terraform -chdir=terraform/$PAVED_PATH output next_steps
terraform -chdir=terraform/$PAVED_PATH output ecr_repository_urls
```

 `next_steps` first says how to reach the cluster, and then lists four numbered steps in order. The first says there’s nothing to commit or push. The others build the agent images, install the in-cluster components with `bootstrap-gitops.sh --sync` through `run-stack.sh`, and deploy your first agent and run `exercise.sh`. `ecr_repository_urls` lists the repositories that hold agent images.

## Step 3: Verify the EKS cluster
<a name="agents-cluster-setup-step3"></a>

Confirm that the cluster can run Nitro Sandbox pods before anything is installed on it. `run-stack.sh` runs the command on the bastion or your workstation:

```bash
./scripts/run-stack.sh --root terraform/$PAVED_PATH -- kubectl get runtimeclass isolated-sandbox
```

The output lists `isolated-sandbox`. If the bastion was just created, its bootstrap configures `kubectl` shortly after the apply returns, so run the command again if it can’t reach the cluster. Without the bastion, a timeout here usually means the public endpoint’s allowlist doesn’t include this machine’s address. Run `./scripts/check-endpoint.sh --root terraform/$PAVED_PATH`, as described in [Run from your workstation (optional)](#agents-cluster-public-endpoint).

Argo CD installs the network policies in the next step, so you verify them in [Set up EKS Capabilities and in-cluster components for agents](agents-capabilities-setup.md).

## Additional configuration
<a name="agents-cluster-additional"></a>

The following settings are optional. Add them to the variables file from [Step 1: Set the base variables](#agents-cluster-setup-step1) before you apply, or apply again after you change them.

### Cluster administration
<a name="agents-cluster-variables"></a>

Who can administer the cluster decides who can change every agent’s identity, network policy, and workload, so the list of administrators should be explicit and reviewable. Two Amazon EKS defaults work against that. The `aws-auth` ConfigMap maps IAM principals to Kubernetes permissions, and anything that can write to `kube-system` can edit it. Cluster creator admin silently makes whoever created the cluster an administrator, which is often a CI role that nobody reviews.

The base setup avoids both. The cluster uses the `API` authentication mode, so IAM principals get Kubernetes permissions only through EKS access entries, and the creator gets no implicit access. Administrators are the principals you list, each with an access entry that grants `AmazonEKSClusterAdminPolicy` scoped to the cluster. See [Grant IAM users access to Kubernetes with EKS access entries](access-entries.md).

In the reference sample, `cluster_admin_principal_arns` holds that list. Left empty, it grants the IAM role or user that runs Terraform, so a first apply returns a cluster you can administer. For a shared cluster, name the platform team’s roles, so the list of administrators is reviewable in Git. The `argocd_*` variables name the Identity Center users who administer Argo CD, as described in [Set up IAM Identity Center for Argo CD](#agents-cluster-identity-center).

### Control plane logging
<a name="agents-cluster-logging"></a>

Agents that hold Kubernetes API access act on the cluster themselves, so you need a record of what each one did that the agent can’t alter. EKS control plane logs, sent to Amazon CloudWatch Logs, are that record. The `authenticator` log records which IAM principal each Kubernetes request maps to. The `audit` log records every API request, including which agent’s service account made it. Audit logging is the highest-volume stream, which is why it’s often left off, but turn it on for production agents. An agent can’t delete it. See [Send control plane logs to CloudWatch Logs](control-plane-logs.md).

Create the log group yourself, with a retention period, before EKS writes to it. A log group that EKS creates on first write outlives the cluster and never expires.

The reference sample sends `api` and `authenticator` by default. The open source root doesn’t expose a setting to change them. On the AWS services root, set `enable_cluster_log_types` to the log types to send and `cluster_log_retention_days`, 30 by default, to how long the `/aws/eks/<name>/cluster` log group keeps them. For example, to add the audit log:

```hcl
enable_cluster_log_types = ["api", "audit", "authenticator"]
```

Apply with `scripts/apply.sh`. The apply changes only the cluster, so there’s nothing to sync.

To stop sending the audit log, remove `"audit"` from `enable_cluster_log_types` and apply again. The log group keeps the records it already has until its retention period expires.

### (Optional) Record VPC traffic with flow logs
<a name="agents-cluster-flow-logs"></a>

To record the VPC’s traffic, set `enable_vpc_flow_logs = true`. The reference sample then sends VPC Flow Logs for the VPC it creates to a CloudWatch Logs group under `/aws/vpc/my-agents/flow-logs`, which keeps records for `vpc_flow_logs_retention_days`, 90 days by default. It’s off by default, because flow logs are billed per gigabyte and many organizations collect them centrally. With an existing VPC, the setting has no effect, so record that VPC’s traffic the way your network already does.

### Deploy into an existing VPC
<a name="agents-cluster-existing-vpc"></a>

On either path, the stack can create its cluster in a VPC that you already run, instead of creating a VPC. Set the VPC, its CIDR, and its private subnets:

```hcl
vpc_id     = "vpc-0123456789abcdef0"
vpc_cidr   = "10.20.0.0/16"
subnet_ids = ["subnet-0123456789abcdef0", "subnet-0fedcba9876543210", "subnet-0a1b2c3d4e5f60718"]   # private subnets
```

The VPC needs the following:
+  **Private subnets with a route to a NAT gateway.** Nothing in the stack is meant to be reachable from the internet, and some traffic always needs the NAT gateway. Set `vpc_id` and `subnet_ids` together. The plan refuses one without the other.
+  **The VPC’s CIDR in `vpc_cidr`.** The bastion’s security group and the interface VPC endpoints admit traffic from that range.
+  **The `kubernetes.io/role/internal-elb` tag with the value `1` on each private subnet**, so that an internal load balancer for ingress can use it. The stack tags the subnets it creates the same way.
+  **DNS support and DNS hostnames turned on**, which the private DNS of the interface VPC endpoints requires.
+  **An Amazon S3 gateway endpoint on the private subnets' route tables**, if you want image layers to reach nodes without crossing the NAT gateway. The stack adds one only to a VPC it creates.

### Use an existing cluster
<a name="agents-cluster-existing"></a>

On the open source path, the root module can use an existing EKS Auto Mode cluster. Set `create_cluster = false` and set `name` to the cluster’s name.

```hcl
create_cluster = false
name           = "existing-cluster-name"
```

The module reads the cluster’s endpoint, certificate data, OIDC issuer, security group, subnets, and node role. It doesn’t create a cluster, cluster IAM role, node role, Pod Identity add-on, cluster administrator access entries, or VPC. It still creates the capabilities and their roles (EKS creates their access entries), the permissions boundary, the ECR repositories, the bastion and its access entry, and, with `enable_checkpoints = true`, the checkpoint bucket.

 **Agent nodes use private subnets only.** A cluster’s configuration often includes public subnets. The module selects the private subnets and fails the plan if there are none, so pods that run model-generated code never get public addresses. With the bastion on, set `vpc_id`, `vpc_cidr`, and `subnet_ids` to the cluster’s VPC, its CIDR, and its private subnets. The bastion runs in that VPC with its security group scoped to that CIDR, and the plan rejects `vpc_id` without `subnet_ids`, or `subnet_ids` without `vpc_id`, so the stack never runs in a network you only partly specified. With the bastion off, set `vpc_id` and `subnet_ids` only to choose the subnets yourself:

```hcl
vpc_id     = "vpc-0123456789abcdef0"
vpc_cidr   = "192.168.0.0/16"
subnet_ids = ["subnet-0123456789abcdef0", "subnet-0fedcba9876543210"]   # private subnets
```

**Cluster-wide objects the stack installs**
 **Network policy enforcement for every namespace.** Enforcement is a cluster-wide setting, so every existing `NetworkPolicy` on the cluster starts being enforced, including policies that previously had no effect.
 **A default StorageClass**, which replaces the existing default.
 **Cluster-scoped network policies**, evaluated before every namespaced policy. One accepts all traffic for the system namespaces, including `kube-system`. See [Restrict agent egress with network policy](agents-network-policies.md).
Review these with the cluster’s owner before you apply in [Step 2: Apply](#agents-cluster-setup-step2). When you keep the cluster, the teardown script removes all three, and removes the enforcement setting only if this stack created it. With `enable_network_policy = false`, the stack installs neither the enforcement setting nor the cluster-scoped policies, and agents run with no network policy. Use that only to test other components.

### Keep AWS traffic in the VPC
<a name="agents-cluster-vpc-endpoints"></a>

Agents, nodes, and in-cluster components call AWS services at their public endpoints through the NAT gateway by default. To keep that traffic inside the VPC, list the services in `vpc_endpoints`. Terraform creates an interface VPC endpoint for each one with private DNS turned on, so each service’s host name resolves to addresses in the VPC and nothing in the cluster changes its configuration or network policy.

------
#### [ Open source ]

```hcl
vpc_endpoints = [
  "bedrock-runtime", "sts", "secretsmanager",            # agents
  "sqs",                                                 # task queues, with agents run as tasks
  "ecr-api", "ecr-dkr", "eks-auth",                      # nodes and EKS Pod Identity
  "oidc-eks",                                            # service account token checks
  "ssm", "ssmmessages", "ec2messages",                   # the bastion only
  "eks", "elasticloadbalancing", "bedrock",              # the scripts, on the bastion
]
```

------
#### [  AWS services ]

```hcl
vpc_endpoints = [
  "bedrock-runtime", "agentcore", "s3vectors", "sts", "secretsmanager",   # agents
  "sqs",                                                                  # task queues, with agents run as tasks
  "ecr-api", "ecr-dkr", "eks-auth",                                       # nodes and EKS Pod Identity
  "oidc-eks",                                                             # service account token checks
  "logs", "monitoring", "xray",                                           # telemetry
  "ssm", "ssmmessages", "ec2messages",                                    # the bastion only
  "eks", "elasticloadbalancing", "bedrock",                               # the scripts, on the bastion
]
```

------

Without the bastion, as described in [Run from your workstation (optional)](#agents-cluster-public-endpoint), leave out the last six keys. `ssm`, `ssmmessages`, and `ec2messages` serve the bastion’s Session Manager connection, and `eks`, `elasticloadbalancing`, and `bedrock` serve the EKS API, load balancer, and inference profile lookups of the scripts that run on the bastion.

On the AWS services path, `agentcore` in the list also gives you `agentcore-gateway` whenever the gateway is on, whichever you turned on first, and attaches the gateway’s resource policy. See [Step 3: (Optional) Keep gateway traffic in the VPC](agents-gateway.md#agents-gateway-vpc-endpoint). The `agentcore` endpoint’s private DNS covers `bedrock-agentcore.<region>.amazonaws.com`, which includes every gateway’s host name, so without the gateway’s own endpoint that host name would stop resolving in the VPC. The open source path doesn’t use `agentcore-gateway`, `agentcore`, or `s3vectors`, and it sends telemetry to Prometheus and Langfuse in the cluster, so it doesn’t need `logs`, `monitoring`, or `xray` either. `sqs` carries the task queues of agents that run as tasks, for the task pods, KEDA, and anything in the VPC that sends tasks. See [Run an agent as tasks](agents-lifecycle.md#agents-lifecycle-tasks-run). When the stack creates the VPC, it also gives Amazon S3 a gateway endpoint. In a VPC you bring, add one yourself, as described in [Deploy into an existing VPC](#agents-cluster-existing-vpc). `oidc-eks` serves the cluster’s OIDC issuer, whose discovery document and signing keys every service account token check reads. With `eks` in the list, the templates add `oidc-eks` for you. The EKS endpoint’s private DNS covers `eks.<region>.amazonaws.com`, which includes the issuer’s host name, so without the issuer’s own endpoint every token check in the cluster would fail.

Some traffic still needs the NAT gateway with every endpoint in place. Route 53, which ExternalDNS calls, has no VPC endpoint. Neither do public container registries, so a pod that pulls from one on a new node can’t start, including the Istio CNI and ztunnel pods, whose images come from `docker.io/istio`. The chat UI reads the load balancer’s signing key from a public host to verify a signed-in person’s claims, and image builds on the bastion pull their base image and packages from the internet. Each interface endpoint is billed for every hour in every Availability Zone it serves. To remove the endpoints, set `vpc_endpoints = []` and apply. Nothing in the cluster changes, and the traffic goes back through the NAT gateway, including the bastion’s Session Manager connection. See [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the * AWS PrivateLink Guide*.

## Next steps
<a name="agents-cluster-setup-next"></a>

Continue to [Set up EKS Capabilities and in-cluster components for agents](agents-capabilities-setup.md) to bootstrap Argo CD, which installs the network policies and every later component. To confirm sandbox isolation on this cluster first, see [Get started with sandboxes](sandboxing-getting-started.md).

## Clean up
<a name="agents-cluster-setup-cleanup"></a>

To stop charges, delete everything this section created. Run the reference sample’s teardown script, which also runs `terraform destroy` when you pass `--destroy-with`. Controllers in the cluster create some resources outside Terraform, and `terraform destroy` leaves them behind; the script finds and deletes them. It’s a dry run unless you pass `--yes`.

**Important**
Before you run `terraform destroy`, delete any Amazon EC2 instances or security groups you created manually in the VPC. They block VPC deletion, and Terraform retries the delete without reporting an error.

The commands are the same on both paths. Run them from the `agents` directory.

```bash
./scripts/teardown.sh --path $PAVED_PATH --cluster my-agents --region {{region-code}} \
  --root terraform/$PAVED_PATH --cluster-going-away
./scripts/teardown.sh --path $PAVED_PATH --cluster my-agents --region {{region-code}} \
  --root terraform/$PAVED_PATH --cluster-going-away --yes --destroy-with my.tfvars
```

The teardown, including `terraform destroy` and the final sweep, takes about 15 to 20 minutes for the base setup and about 20 to 25 minutes with every component on.

On both paths, the script deletes the `Agent` objects first so that ACK deletes each agent’s IAM role, then the load balancers, persistent volumes, ECR images, and the checkpoint and person-data buckets that block `terraform destroy`. Its final sweep also reports a leftover image-build project, log groups, and Identity Center objects. On the AWS services path, the sweep also checks for an ElastiCache Serverless cache, Amazon S3 Vectors buckets, and AgentCore gateways, memory stores, and policy engines, which a destroy that fails partway leaves running.

 `--destroy-with` runs `terraform destroy` in the path’s Terraform root with that variables file, then sweeps the account. It refuses when the Terraform workspace isn’t `default` or when the file’s `name` isn’t the `--cluster` value. Without it, run `terraform -chdir=terraform/$PAVED_PATH destroy -var-file=my.tfvars` yourself from the `agents` directory, then the script again with `--sweep-only`.

Omit `--cluster-going-away` when you keep the cluster and remove only this stack, such as on an existing cluster. The script then also removes the cluster-wide objects listed in [Use an existing cluster](#agents-cluster-existing), the three EKS Capabilities this stack created and the access entries EKS created for them, the `argocd` namespace and custom resource definitions that the Argo CD capability leaves behind, and the Gateway API custom resource definitions that this stack’s Applications installed. It leaves other capabilities on the cluster, a self-managed Argo CD, and an EKS-managed Gateway API installation alone. Don’t pass `--destroy-with` either, because it destroys the cluster. The following command runs a dry run first, and `--yes` then makes the changes:

```bash
./scripts/teardown.sh --path $PAVED_PATH --cluster my-agents --region {{region-code}} \
  --root terraform/$PAVED_PATH
./scripts/teardown.sh --path $PAVED_PATH --cluster my-agents --region {{region-code}} \
  --root terraform/$PAVED_PATH --yes
```

To install the in-cluster components on that cluster again, see [Clean up](agents-capabilities-setup.md#agents-capabilities-cleanup).

 `--root` names the stack’s Terraform root, and the script reaches the cluster through it the same way as the other scripts. Run it from your workstation. The account steps always run there with your own credentials. `--sweep-only` repeats only the sweep.

The teardown keeps the third-party credentials you stored with `scripts/set-credential.sh`, under `my-agents/consent/` and `my-agents/agentcore/` in Secrets Manager, because they can’t be regenerated. It reports each one with the command that deletes it. With `--delete-operator-secrets` and `--yes`, it deletes them too, with no recovery window. It always deletes the generated passwords under `my-agents/platform/`.

If you created a CodeCommit repository with `gitops-mirror.sh` for templates you changed, it isn’t part of the stack, so the teardown leaves it, and the sweep reports it while it exists. Delete it after the teardown:

```bash
./scripts/gitops-mirror.sh delete --name my-agents --region {{region-code}}
```

### How the teardown script works
<a name="agents-cluster-setup-cleanup-how"></a>

The script needs two credentials:
+  **In-cluster steps** need `kubectl`. They run on the bastion when the stack has one, and on your workstation otherwise. The bastion’s role can reach the cluster but little else.
+  **Account steps** run with a credential that can read the whole account. They empty the Amazon ECR repositories and the checkpoint bucket, which the bastion’s role can’t read, and sweep the account for remaining resources, such as the AgentCore log groups that carry the cluster’s name.

The script has these safeguards:
+ If the bastion step can’t start, the script stops before deleting anything. Deleting the EKS Capabilities while agents still exist leaves each agent’s IAM role behind.
+ It stops Argo CD first, because a self-healing Application re-creates resources as they’re deleted.
+ It runs in-cluster steps only when `kubectl` reaches the cluster named by `--cluster`, so a stale context can’t target another cluster.

If a teardown stalls, the usual cause is a credential or network problem on the workstation. Run `--sweep-only` to see what’s left.

What the script looks for:
+  **Load balancers** created by controllers in the cluster.
+  **Amazon EBS volumes** behind any stateful component you turned on.
+  **Amazon ECR repositories** holding agent images.
+  ** AWS X-Ray Transaction Search**, an account-level setting that `terraform destroy` removes from state but leaves on. The script turns it off only with `--revert-account-settings`, and only after confirming no other cluster from this stack in the account uses it.
+  **Cluster-scoped Kubernetes objects** on a cluster you keep: custom resource definitions, admission webhook configurations, and validating admission policies. A leftover webhook configuration with failure policy `Fail` and no backing service blocks unrelated API calls on the cluster.
