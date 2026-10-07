---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

This solution deploys to Amazon Elastic Kubernetes Service (Amazon EKS). The Amazon EKS deployment is the recommended deployment for Migration Assistant 3.0 and is the deployment used throughout the rest of this implementation guide. A legacy Amazon ECS deployment remains available in support-only mode for existing deployments.

Before you begin, review the [cost](cost.md), [architecture](architecture-overview.md), [network security](security-1.md), and other considerations discussed earlier in this guide.

**Important**
To update to a newer version of this solution, [uninstall](uninstall-the-solution.md) and redeploy it. This solution isn’t backwards-compatible.

**Important**
This solution sends operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered through this survey. Data collection is subject to the [Privacy Notice](https://aws.amazon.com/privacy/).

## Prerequisites
<a name="prerequisites"></a>

To deploy this solution on Amazon EKS, you need:
+ An AWS account with permissions for AWS CloudFormation, Amazon EKS, AWS IAM, Amazon EC2, Amazon ECR, Amazon S3, Amazon CloudWatch, AWS Secrets Manager, and related services.
+ Either [AWS CloudShell](https://aws.amazon.com/cloudshell/) or a local terminal with AWS CLI v2, `kubectl`, and Helm 3 installed. AWS CloudShell is recommended because it comes pre-configured with the required tools and avoids platform-specific issues (for example, the `tac` command used by the bootstrap script is not available on macOS by default).
+ Network connectivity from the Amazon EKS cluster to your source cluster and your Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

The bootstrap script handles cluster creation, IAM role wiring (EKS Pod Identity), private image mirroring, VPC endpoint setup, and Helm chart installation.

## Deployment options
<a name="deployment-options"></a>

Choose one of the following CloudFormation templates to deploy the Amazon EKS infrastructure:
+  [Launch with a new VPC](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/migration-assistant-for-amazon-opensearch-service/latest/migration-assistant-for-amazon-opensearch-service-create-vpc-eks.template) — Creates a new VPC with the required networking, public and private subnets, NAT gateway, and Amazon EKS cluster.
+  [Launch into an existing VPC](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/migration-assistant-for-amazon-opensearch-service/latest/migration-assistant-for-amazon-opensearch-service-import-vpc-eks.template) — Uses an existing VPC. The selected subnets must be in different Availability Zones and must allow outbound connectivity (either through a NAT gateway or VPC endpoints, depending on whether you are deploying into isolated subnets).

After the CloudFormation stack deploys, run the bootstrap script to install the Migration Assistant Helm chart and configure the Amazon EKS cluster.

## Step 1: Download the bootstrap script
<a name="bootstrap-script"></a>

Throughout this guide, `<STAGE>` is a short label such as `dev`, `staging`, or `prod`. It is used in cluster and resource names so you can keep multiple deployments separate.

```
curl -sL -o aws-bootstrap.sh \
  "https://solutions-reference.s3.amazonaws.com/migration-assistant-for-amazon-opensearch-service/latest/aws-bootstrap.sh" \
  && chmod +x aws-bootstrap.sh
```

### Bootstrap flag reference
<a name="bootstrap-flag-reference"></a>

The following table highlights the flags most users need first:

| Group | Flag | Typical use |
| --- | --- | --- |
|  **Help**  |  ** `--help` **  |  **Show all of the options, including those not shown here**  |
| Mode |  `--deploy-create-vpc-cfn`  | Create a new VPC and Amazon EKS cluster |
|  |  `--deploy-import-vpc-cfn`  | Reuse an existing VPC with `--vpc-id` and `--subnet-ids`  |
|  |  `--skip-cfn-deploy`  | Re-bootstrap an existing cluster without rerunning AWS CloudFormation |
| Identity |  `--stack-name <name>`  | Set the AWS CloudFormation stack name for `--deploy-*-cfn`  |
|  |  `--stage <name>`  | Set the environment label used in resource names |
|  |  `--region <region>`  | Choose the AWS Region |
| Networking |  `--vpc-id <id>`  | Identify the existing VPC to reuse |
|  |  `--subnet-ids <id1,id2>`  | Provide subnets in different Availability Zones |
| Access |  `--grant-eks-access-only`  | Grant access to an existing cluster and exit |
|  |  `--eks-access-principal-arn <arn>`  | Specify the IAM principal to grant cluster-admin access |
| Versioning |  `--version <tag>`  | Pin to a specific published release for reproducible deployments |

## Step 2: Deploy into a new or existing VPC
<a name="step-2-deploy"></a>

### New VPC (latest published release)
<a name="deploy-new-vpc"></a>

```
./aws-bootstrap.sh \
  --deploy-create-vpc-cfn \
  --stack-name MA \
  --stage dev \
  --region us-east-2
```

### New VPC pinned to a specific release
<a name="deploy-new-vpc-pinned"></a>

```
./aws-bootstrap.sh \
  --deploy-create-vpc-cfn \
  --stack-name MA \
  --stage prod \
  --region us-east-2 \
  --version 3.0.1
```

**Note**
Pinning a version makes the deployment reproducible. Customers and CI runs that need to deploy the same artifacts again should always pass `--version`.

### Existing VPC
<a name="deploy-existing-vpc"></a>

```
./aws-bootstrap.sh \
  --deploy-import-vpc-cfn \
  --stack-name MA \
  --stage dev \
  --vpc-id vpc-0abc123 \
  --subnet-ids subnet-111,subnet-222 \
  --region us-east-2
```

When the script finishes, it has already installed the Helm chart and configured the core platform pieces.

## Step 3: Verify the deployment
<a name="step-3-verify"></a>

Update your kubeconfig to point at the new Amazon EKS cluster:

```
aws eks update-kubeconfig --region <REGION> --name migration-eks-cluster-<STAGE>-<REGION>
```

Then list the pods in the `ma` namespace:

```
kubectl get pods -n ma
```

You should see the Migration Console (`migration-console-0`), the Argo workflow controller, and the Argo server in `Running` state.

## Step 4: Access the Migration Console
<a name="step-4-access-console"></a>

```
kubectl exec -it migration-console-0 -n ma -- /bin/bash
```

Once you are in the Migration Console pod, the migration flow is the same regardless of source: confirm the version, load the sample workflow configuration, run a pilot, validate, and then run the full migration. See [Configure and run workflows](use-the-solution.md).

## Step 5: Use the AWS helpers the deployment created for you
<a name="step-5-aws-helpers"></a>

The Amazon EKS deployment provides a default Amazon S3 bucket and snapshot-role wiring so you do not have to build this manually.

### Default Amazon S3 bucket
<a name="default-s3-bucket"></a>

The deployment creates a default Amazon S3 bucket for migration artifacts and snapshots:

```
s3://migrations-default-<ACCOUNT_ID>-<STAGE>-<REGION>
```

The default bucket is mounted read-only on the Migration Console pod at `/s3/artifacts` for direct artifact access.

### Snapshot role output
<a name="snapshot-role-output"></a>

If your workflow needs a snapshot role ARN, look it up from the AWS CloudFormation outputs:

```
aws cloudformation describe-stacks \
  --stack-name <YOUR_STACK_NAME> \
  --query "Stacks[0].Outputs[?contains(OutputKey,'MigrationsExportString')].OutputValue" \
  --output text
```

## Authentication on Amazon EKS
<a name="authentication-on-eks"></a>

### Basic authentication
<a name="basic-auth"></a>

For sources that require basic authentication, create managed HTTP Basic credentials from the Migration Console pod and reference the name in `authConfig.basic.secretName` in your workflow configuration:

```
workflow configure credentials create source-credentials
```

For non-interactive setup, use `workflow configure credentials create source-credentials --stdin` and pass one `USERNAME:PASSWORD` line on stdin. If you already manage the value in an external secrets system, sync it into a Kubernetes Secret in the `ma` namespace and reference that Kubernetes Secret name from `authConfig.basic.secretName`.

### AWS Signature Version 4 (SigV4)
<a name="sigv4-auth"></a>

For Amazon OpenSearch Service domains, Amazon OpenSearch Serverless NextGen collections, and other AWS services that authenticate with SigV4, the Amazon EKS stack uses [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) to give two sets of pods an AWS identity:
+ The Migration Console pod (`migration-console-0`), which runs under the `migration-console-access-role` Kubernetes service account.
+ The Argo workflow executor pods, which run under the `argo-workflow-executor` Kubernetes service account.

The Migration Console and the migration jobs can authenticate to Amazon OpenSearch Service, Amazon OpenSearch Serverless NextGen, and other AWS services without manually distributing long-lived AWS credentials.

Use `es` as the SigV4 service name when targeting an Amazon OpenSearch Service domain, and `aoss` when targeting an Amazon OpenSearch Serverless NextGen collection. Verify the identity inside the Migration Console pod with `aws sts get-caller-identity`.

### Cluster mutual TLS
<a name="cluster-mtls-auth"></a>

Do not confuse cluster mTLS with Capture Proxy listener mTLS. Proxy listener mTLS controls client connections into the capture proxy and is configured under `traffic.proxies.<proxy>.proxyConfig.tls.clientAuth`. See [TLS behavior](reroute-to-proxy.md#reroute-tls).

The workflow schema exposes `authConfig.mtls` with `caCert` and `clientSecretName`, but the current documented workflow path is centered on basic authentication and SigV4. The standard workflow templates do not mount and pass the `clientSecretName` certificate and key pair through every migration phase, and the Traffic Replayer target-auth path derives request authentication for SigV4 and basic auth only. Treat cluster mTLS as an advanced custom-wiring path and validate the exact phases you plan to run before using it.

## Private or isolated networks
<a name="private-isolated-networks"></a>

If your subnets do not have direct internet access, the bootstrap script mirrors images into private Amazon ECR by default and creates the VPC endpoints needed to pull from inside the cluster:

```
./aws-bootstrap.sh \
  --deploy-import-vpc-cfn \
  --create-vpc-endpoints \
  --stack-name MA-Prod \
  --stage prod \
  --vpc-id vpc-xxx \
  --subnet-ids subnet-aaa,subnet-bbb \
  --region us-east-1 \
  --version 3.0.1
```

The mirroring step runs from your machine (which has internet access), copies the release images and Helm charts to Amazon ECR, then the Amazon EKS cluster pulls everything through VPC endpoints. The endpoints created are: Amazon ECR API, Amazon ECR Docker, Amazon S3, Amazon CloudWatch Logs, Amazon EFS, AWS STS, and Amazon EKS Auth.

If you prefer to manage VPC endpoints with another tool, omit `--create-vpc-endpoints`. The script still mirrors images and uses your existing endpoints.

## Grant kubectl access to a CI role or teammate
<a name="grant-additional-access"></a>

After the cluster is already bootstrapped, run the script in grant-only mode to add a second admin principal:

```
./aws-bootstrap.sh \
  --grant-eks-access-only \
  --eks-access-principal-arn arn:aws:iam::123456789012:role/MyCIRole \
  --stage dev \
  --region us-east-2
```

This applies the Amazon EKS access entry and policy association for the principal, then exits. It does not redeploy AWS CloudFormation, mirror images, run Helm, or update your `kubeconfig`, and it skips the `jq`, `kubectl`, and `helm` prerequisite checks.

Verify the access entry from the account that owns the cluster:

```
aws eks list-access-entries \
  --cluster-name <CLUSTER_NAME> \
  --region <REGION>

aws eks list-associated-access-policies \
  --cluster-name <CLUSTER_NAME> \
  --principal-arn arn:aws:iam::123456789012:role/MyCIRole \
  --region <REGION>
```

## Recovery if the bootstrap fails
<a name="recovery"></a>

If AWS CloudFormation fails, check the stack status first:

```
aws cloudformation describe-stacks --stack-name <STACK_NAME> --query "Stacks[0].StackStatus"
```

If the stack is stuck in `ROLLBACK_COMPLETE` or `CREATE_FAILED`, delete it and rerun the bootstrap script:

```
aws cloudformation delete-stack --stack-name <STACK_NAME>
aws cloudformation wait stack-delete-complete --stack-name <STACK_NAME>
```

If AWS CloudFormation succeeded but the Helm portion failed, rerun only the bootstrap’s cluster-side steps:

```
./aws-bootstrap.sh --skip-cfn-deploy --stage <STAGE> --region <REGION>
```

For additional troubleshooting, see [Troubleshooting](troubleshooting.md).

## Legacy Amazon ECS deployment (support only)
<a name="ecs-deployment"></a>

**Important**
The legacy Amazon ECS deployment has reached end of support (**July 15, 2026**). No new features will be developed for the Amazon ECS deployment. New deployments should use the Amazon EKS deployment described in this guide.

The Amazon ECS deployment has been available since Migration Assistant 1.0. Existing Amazon ECS deployments will continue to function, but customers are encouraged to migrate to the Amazon EKS deployment for access to new features and ongoing support.
