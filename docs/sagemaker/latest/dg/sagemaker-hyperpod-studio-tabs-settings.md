---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-tabs-settings.html
---

# Settings

In Amazon SageMaker Studio, choose **HyperPod** in the navigation pane, select a cluster, and open the **Settings** tab to view cluster configuration and manage compute configurations.

## Cluster configuration
<a name="sagemaker-hyperpod-studio-tabs-settings-cluster"></a>
+ Instances details, including instance ID, status, instance type, and instance group
+ Instance groups details, including instance group name, type, counts, and compute information
+ Orchestration details, including the orchestrator, version, and certificate authority
+ Governance details, including task priority classes and their weights
+ Cluster resiliency details
+ Security details, including subnets and security groups

## Compute configurations
<a name="sagemaker-hyperpod-studio-tabs-settings-compute-templates"></a>

A compute configuration is a reusable preset that defines a compute allocation. You can select a configuration when you submit a training job or deploy a model, instead of entering resource values manually each time.

**Note**
Compute configurations rely on Kueue to count a workload's requested resources against your quota when the workload is admitted. If you run a tool that resizes pods after they are scheduled, for example the Vertical Pod Autoscaler, that tool can change a pod's resources after Kueue has counted them, so the running pods can exceed the quota counted at admission. Compute configurations is an opt-in feature that you install on your cluster; installing other pod-layer mutators that rewrite pods after scheduling can interfere with how quota is enforced.

### Prerequisites
<a name="sagemaker-hyperpod-studio-tabs-settings-compute-templates-prereqs"></a>

Before you can use compute configurations, the following must be in place on your cluster:
+ Kubernetes 1.30 or later.
+ amd64 HyperPod nodes.
+ The cert-manager HyperPod Amazon EKS add-on is installed and the webhook deployment is available.

Verify cert-manager is ready:

```bash
kubectl -n cert-manager get deployment cert-manager-webhook
```

Install the HyperPod CLI by cloning the repository and checking out the latest release tag:

```bash
git clone https://github.com/aws/sagemaker-hyperpod-cli.git
cd sagemaker-hyperpod-cli
git checkout $(git tag --sort=-v:refname | head -n 1)
```

Then install the compute configuration Helm chart once per cluster into the `aws-hyperpod` namespace:

```bash
helm upgrade --install hyperpod-compute-configuration charts/hyperpod-compute-configuration/0.1.0 \
  -n aws-hyperpod --create-namespace \
  --set webhook.image.repository={{account}}.dkr.ecr.{{region}}.amazonaws.com/hyperpod-compute-configuration-webhook \
  --set webhook.image.tag={{tag}} \
  --wait
```

To verify the installation:

```bash
kubectl get crd computeconfigurations.compute.configuration.sagemaker.amazonaws.com
kubectl -n aws-hyperpod get deploy hyperpod-compute-configuration-webhook
kubectl get mutatingwebhookconfiguration,validatingwebhookconfiguration hyperpod-compute-configuration-webhook
kubectl get validatingadmissionpolicies | grep hyperpod-compute-configuration
```

### Enforced and open compute configurations
<a name="sagemaker-hyperpod-studio-tabs-settings-compute-templates-enforcement"></a>

A compute configuration can be enforced or open at the namespace level. The enforcement mode determines whether a compute configuration is required when submitting a workload and whether it can be modified.

#### Enforced compute configurations
<a name="sagemaker-hyperpod-studio-tabs-settings-compute-templates-enforcement-enforced"></a>

A namespace labeled `compute.configuration.sagemaker.amazonaws.com/enforcement=enabled` is enforced. In an enforced namespace, every new training job and model deployment must use a compute configuration. This applies to the `RayJob`, `HyperPodPyTorchJob`, and `InferenceEndpointConfig` kinds (except JumpStart). Submitting a workload without one is rejected.

If an admin enables enforcement on a namespace after workloads are already running, those workloads keep running and are not rewritten. After enforcement is turned on:
+ An existing workload that uses a compute configuration can't have its compute edited or its configuration removed.
+ A workload without a compute configuration can still be updated.

#### Open compute configurations
<a name="sagemaker-hyperpod-studio-tabs-settings-compute-templates-enforcement-open"></a>

A namespace without the enforcement label is open. In an open namespace, a compute configuration is optional. Users can submit workloads without one, and can also manually edit the compute fields of a workload even if it was created using a configuration.

#### Enabling and disabling enforcement
<a name="sagemaker-hyperpod-studio-tabs-settings-compute-templates-enforcement-toggle"></a>

To enable enforcement on a namespace:

```bash
kubectl label ns {{namespace}} compute.configuration.sagemaker.amazonaws.com/enforcement=enabled
```

To disable enforcement on a namespace:

```bash
kubectl label ns {{namespace}} compute.configuration.sagemaker.amazonaws.com/enforcement=disabled
```

### Creating a compute configuration
<a name="sagemaker-hyperpod-studio-tabs-settings-compute-templates-create"></a>

The create form groups the settings into three sections: **Details**, **Namespace**, and **Compute**. The following procedure describes how to create a configuration in Studio.

1. In Studio, choose **HyperPod** in the navigation pane, select your cluster, and choose the **Settings** tab. Scroll down to **Configurations**, and then click **Create**.

1. Under **Details**, for **Name**, enter a name for the configuration. A name is required. You can also add a **Description** and **Tags**, which are optional.

1. Under **Namespace**, assign the configuration to one or more namespaces. Only the users with access to those namespaces can select the configuration.

1. Under **Compute**, specify the allocation: the instance type, number of GPUs, the number of vCPUs, the vCPU memory, and EFA.

1. Click **Create**.

### Editing and deleting a compute configuration
<a name="sagemaker-hyperpod-studio-tabs-settings-compute-templates-manage"></a>

To change a configuration, select the configuration, and click on **Actions** > **Edit**. You can update the description, tags, namespace assignments, and compute allocation. Editing a configuration does not change workloads that you already launched from it.

To remove a configuration, select it and click on **Actions** > **Delete**. After you delete a configuration, users can no longer select it for new workloads.

In an enforced namespace, workloads still using a deleted configuration can no longer be updated. The webhook rejects them with the error `Compute configuration "<name>" not found`, including attempts to suspend or resume them. Before you delete a configuration that is used in an enforced namespace, switch its workloads to another configuration.

### Selecting a compute configuration for a workload
<a name="sagemaker-hyperpod-studio-tabs-settings-compute-templates-select"></a>

When you submit a training job or deploy a model, select a configuration to apply its allocation to the request. The list shows the configurations assigned to the namespaces you have access to.

To switch a running workload to a different compute configuration, suspend the workload, update the configuration, then resume it.

If you edit a compute configuration after a workload is already running, the workload continues to use the values it was created with. To apply the updated values to an existing workload, suspend the workload, add the following annotation, then resume it:

```yaml
compute.configuration.sagemaker.amazonaws.com/apply-latest: "true"
```

For information about submitting a training job, see [Submitting training jobs in Studio](sagemaker-hyperpod-studio-training.md). For information about deploying a model, see [Deploying models in Studio](sagemaker-hyperpod-studio-inference.md).

### Permissions
<a name="sagemaker-hyperpod-studio-tabs-settings-compute-templates-permissions"></a>

Studio acts on the cluster as the domain (or user-profile) execution role. That role needs:
+ IAM permissions, attached to the execution role.
+ Kubernetes permissions on the cluster, granted with the HyperPod access policies in [Which access policies to associate](#sagemaker-hyperpod-studio-tabs-settings-perms-policies), or with custom RBAC.

#### Which access policies to associate
<a name="sagemaker-hyperpod-studio-tabs-settings-perms-policies"></a>

| Access policy | Scope | Who it's for | What it allows |
| --- | --- | --- | --- |
| AmazonSagemakerHyperpodComputeConfigurationAdminPolicy | Namespace | Team admin | Create, update, and delete compute configurations in the team's namespace |
| AmazonSagemakerHyperpodComputeConfigurationAdminPolicy | Cluster | Super admin | Create, update, and delete compute configurations in every namespace |
| AmazonSagemakerHyperpodComputeConfigurationPolicy | Namespace | Data scientist | Read the compute configurations in the team's namespace, to pick one when launching a workload. Associate it alongside the team's Training or Inference policy. |
| AmazonSagemakerHyperpodUserClusterPolicy | Cluster | Admins and data scientists | Lists the cluster's namespaces, so Studio can show the namespaces an admin can create configurations in |

Notes:
+ With the admin policy at namespace scope, the **Namespaces** field on the Create page lists only the namespaces where the admin can create compute configurations.

#### IAM permissions
<a name="sagemaker-hyperpod-studio-tabs-settings-perms-iam"></a>

| Action | Purpose |
| --- | --- |
| eks:DescribeCluster | Resolve the EKS cluster |
| eks:AccessKubernetesApi | Kubernetes reads (namespaces, access checks, reading compute configurations) |
| eks:MutateViaKubernetesApi | Kubernetes writes (creating and deleting compute configurations) |

#### Kubernetes permissions (custom RBAC)
<a name="sagemaker-hyperpod-studio-tabs-settings-perms-rbac"></a>

Customers who use the access policies in [Which access policies to associate](#sagemaker-hyperpod-studio-tabs-settings-perms-policies) can skip this section. The tables list the underlying permissions for customers who manage their own RBAC.

##### To create a compute configuration
<a name="sagemaker-hyperpod-studio-tabs-settings-perms-rbac-create"></a>

| Resource (API group) | Verbs | Scope | Purpose |
| --- | --- | --- | --- |
| computeconfigurations (compute.configuration.sagemaker.amazonaws.com) | create | Each target namespace | Create the configuration. Studio creates one object per selected namespace. |
| namespaces (core) | list | Cluster | List the cluster's namespaces for the Namespaces field |
| selfsubjectaccessreviews (authorization.k8s.io) | create | Cluster | Check which namespaces the admin can create configurations in. Kubernetes grants this to all authenticated users by default (system:basic-user), so you only need to add it if that default binding was removed. |

Notes:
+ Without `list` on `namespaces`, the **Namespaces** field shows an error and the admin can't choose a namespace.
+ Studio creates the configuration in each selected namespace in turn and stops at the first failure. The error message names the namespace that failed and the namespaces it already created the configuration in. Those namespaces keep their copy, so before retrying, the admin should remove them from the selection or choose a different name.

##### To delete a compute configuration
<a name="sagemaker-hyperpod-studio-tabs-settings-perms-rbac-delete"></a>

| Resource (API group) | Verbs | Scope | Purpose |
| --- | --- | --- | --- |
| computeconfigurations (compute.configuration.sagemaker.amazonaws.com) | delete | Every namespace the configuration is assigned to | Delete the configuration. Studio deletes one object per namespace. |

##### To view and edit compute configurations
<a name="sagemaker-hyperpod-studio-tabs-settings-perms-rbac-view"></a>

| Resource (API group) | Verbs | Scope | Purpose |
| --- | --- | --- | --- |
| computeconfigurations (compute.configuration.sagemaker.amazonaws.com) | get, list, watch | Each namespace | List and view configurations |
| namespaces (core) | list | Cluster | Find the namespaces to list configurations in when the user can't list them cluster-wide |
| computeconfigurations (compute.configuration.sagemaker.amazonaws.com) | update, patch | Each namespace | Edit a configuration (admins only) |

#### How to grant the permissions
<a name="sagemaker-hyperpod-studio-tabs-settings-perms-grant"></a>

##### Option 1: HyperPod access policies (recommended for Studio)
<a name="sagemaker-hyperpod-studio-tabs-settings-perms-grant-option1"></a>

1. In the SageMaker console, choose **HyperPod clusters**, then choose the cluster.

1. On the **Configuration** tab, under **Cluster access for SageMaker domains**, choose **Manage access**.

1. Select the policies from [Which access policies to associate](#sagemaker-hyperpod-studio-tabs-settings-perms-policies). Scope them to the team namespace, or to the whole cluster for a super admin.

1. Choose **Save**. The Amazon EKS access entry for the execution role is created automatically.

##### Option 2: Custom RBAC and an EKS access entry
<a name="sagemaker-hyperpod-studio-tabs-settings-perms-grant-option2"></a>

To see the team's configurations on the cluster's **Settings** tab, also grant the cluster-scoped rules in [Kubernetes permissions (custom RBAC)](#sagemaker-hyperpod-studio-tabs-settings-perms-rbac) (`list` on `namespaces` and `create` on `selfsubjectaccessreviews`).

Create `Roles` or `ClusterRoles` with the rules in [Kubernetes permissions (custom RBAC)](#sagemaker-hyperpod-studio-tabs-settings-perms-rbac), bind them to Kubernetes groups, then map the execution role to those groups:

```bash
aws eks create-access-entry \
  --cluster-name {{eks-cluster-name}} \
  --principal-arn arn:aws:iam::{{account-id}}:role/{{studio-execution-role}} \
  --kubernetes-groups '["hyperpod-compute-config-admins"]'
```

Example rules for a team admin in one namespace:

```yaml
# Cluster-scoped rules (needed even for namespace-scoped admins).
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: hyperpod-compute-config-admin-cluster
rules:
- apiGroups: [""]
  resources: ["namespaces"]
  verbs: ["list"]
- apiGroups: ["authorization.k8s.io"]
  resources: ["selfsubjectaccessreviews"]
  verbs: ["create"]
---
# Namespace-scoped rules (repeat per team namespace, or use a ClusterRole for a super admin).
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: hyperpod-compute-config-admin
  namespace: hyperpod-ns-team-a
rules:
- apiGroups: ["compute.configuration.sagemaker.amazonaws.com"]
  resources: ["computeconfigurations"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

For a data scientist, grant only `get`, `list`, and `watch` on `computeconfigurations` in the team's namespace.

Bind each role to the group used in `--kubernetes-groups` with a `ClusterRoleBinding` or `RoleBinding`.

#### Versioning
<a name="sagemaker-hyperpod-studio-tabs-settings-perms-versioning"></a>

Compute configurations have no version field. When a workload is created from a compute configuration, the workload's metadata stores a snapshot of the configuration's values. In an enforced namespace, the webhook rejects edits to a workload's compute; groups added later get the snapshot's values.

#### References
<a name="sagemaker-hyperpod-studio-tabs-settings-perms-references"></a>
+ [Setting up Kubernetes role-based access control](sagemaker-hyperpod-eks-setup-rbac.md) (Setting up Kubernetes role-based access control)
+ [Associating access policies with access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html)
