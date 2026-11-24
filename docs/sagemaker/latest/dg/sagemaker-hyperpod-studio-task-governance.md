---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-task-governance.html
---

# Task queue and priority

In Amazon SageMaker Studio, choose **HyperPod** in the navigation pane, select a cluster, and open the **Queue** tab. The **Queue** tab shows all pending tasks consuming your quota across spaces, training jobs, and model deployments in your cluster.

Queue status derives from Kueue, which HyperPod Task Governance provides. For the concepts behind queueing, quotas, and priority, see [SageMaker HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance.md).

## Viewing and filtering tasks
<a name="sagemaker-hyperpod-studio-task-governance-view"></a>

**Note**
The **Queue** tab requires task governance on your cluster. For information on enabling task governance, see [SageMaker HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance.md).

To view all pending tasks:

1. In Studio, choose **HyperPod** in the navigation pane and select your cluster.

1. Choose the **Queue** tab. The list shows tasks from spaces, training jobs, and model deployments.

1. Use the filters to narrow the list by type, resource, or priority class.

## Changing a task's priority class
<a name="sagemaker-hyperpod-studio-task-governance-priority"></a>

To change the priority class of a task:

1. In the queue list, locate the task.

1. Choose **Edit**.

1. Select a new priority class, then choose **Save**.

**Note**
Changing a task's priority class stops the task and restarts it at the new priority.

## Permissions
<a name="sagemaker-hyperpod-studio-task-governance-permissions"></a>

The **Queue** tab is visible only to cluster admins. Users whose execution role does not pass the cluster admin check do not see the tab.

Studio acts on the cluster as the domain (or user-profile) execution role. That role needs:
+ IAM permissions, attached to the execution role.
+ Kubernetes permissions on the cluster that make the role a cluster admin (see [Who counts as a cluster admin](#sagemaker-hyperpod-studio-task-governance-cluster-admin)).

### Who counts as a cluster admin
<a name="sagemaker-hyperpod-studio-task-governance-cluster-admin"></a>

Studio shows the **Queue** tab when the execution role can update `clusterqueues` (`kueue.x-k8s.io`) cluster-wide. Studio runs this check when the cluster details page loads. The tab is available only for clusters orchestrated by Amazon EKS.

The `clusterqueues` resource is cluster-scoped. Only a `ClusterRole` bound with a `ClusterRoleBinding` can grant `update` on it. A `Role` or `RoleBinding` in a namespace cannot grant it, and neither can an Amazon EKS access policy associated at namespace scope.

Studio's admin check does not specify a namespace. It asks only whether the role can update `ClusterQueues` anywhere on the cluster.

As a result, namespace-scoped team admins do not see the **Queue** tab. For example, a role with `AmazonSagemakerHyperpodComputeConfigurationAdminPolicy` at namespace scope is a team admin, but it does not pass the check. Only cluster admins pass.

This is intentional. The **Queue** tab shows workloads from every team's namespace, and changing a workload's priority affects how the cluster schedules work across all teams. Both are cluster-level actions, so the tab is limited to roles that can manage the cluster's queues.

### How to grant cluster admin access
<a name="sagemaker-hyperpod-studio-task-governance-grant-admin"></a>

There are two ways:

| Option | What to grant |
| --- | --- |
| EKS access policy | Associate AmazonEKSClusterAdminPolicy with the execution role at cluster scope. It grants full access to the cluster, which covers everything the Queue tab needs. |
| Custom RBAC | A ClusterRole with update on clusterqueues, plus the view and edit permissions described in [Kubernetes permissions (custom RBAC)](#sagemaker-hyperpod-studio-task-governance-rbac). |

The HyperPod access policies (`AmazonSagemakerHyperpodUserClusterPolicy`, `AmazonSagemakerHyperpodTrainingPolicy`, `AmazonSagemakerHyperpodInferencePolicy`, `AmazonSagemakerHyperpodSpacePolicy`) don't grant `update` on `clusterqueues`, so on their own they don't show the **Queue** tab. This applies at both namespace and cluster scope. `AmazonEKSAdminPolicy` doesn't grant it either, because it covers only built-in Kubernetes API groups.

### IAM permissions
<a name="sagemaker-hyperpod-studio-task-governance-iam-perms"></a>

| Action | Purpose |
| --- | --- |
| eks:DescribeCluster | Resolve the EKS cluster |
| eks:AccessKubernetesApi | All Kubernetes reads, including the admin check |
| eks:MutateViaKubernetesApi | Kubernetes writes (priority edits) |
| sagemaker:ListClusterSchedulerConfigs | Find the cluster's scheduler configuration |
| sagemaker:DescribeClusterSchedulerConfig | Load the priority classes offered when editing |

### Kubernetes permissions (custom RBAC)
<a name="sagemaker-hyperpod-studio-task-governance-rbac"></a>

Customers who associate `AmazonEKSClusterAdminPolicy` can skip this section. The tables list the underlying permissions for customers who manage their own RBAC.

#### To show the tab (admin check)
<a name="sagemaker-hyperpod-studio-task-governance-rbac-admin-check"></a>

These are custom RBAC rules. If you associate `AmazonEKSClusterAdminPolicy` with the access entry, these permissions are already included.

| Resource (API group) | Verbs | Scope | Purpose |
| --- | --- | --- | --- |
| clusterqueues (kueue.x-k8s.io) | update | Cluster | Identifies the user as a cluster admin. Without it, the tab is hidden. |
| selfsubjectaccessreviews (authorization.k8s.io) | create | Cluster | Lets Studio run the admin check. Kubernetes grants this to all authenticated users by default (system:basic-user), so you only need to add it if that default binding was removed. |

#### To view the queue
<a name="sagemaker-hyperpod-studio-task-governance-rbac-view"></a>

These are custom RBAC rules. If you associate `AmazonEKSClusterAdminPolicy` with the access entry, these permissions are already included.

| Resource (API group) | Verbs | Scope | Purpose |
| --- | --- | --- | --- |
| customresourcedefinitions (apiextensions.k8s.io) | get | Cluster | Find which Kueue API version the cluster serves |
| workloads (kueue.x-k8s.io) | list | Cluster | List queued and admitted workloads in all namespaces |
| pods (core) | list | Cluster | Identify inference workloads |
| rayclusters (ray.io) | list | Cluster | Identify RayService workloads |

Notes:
+ Without the `customresourcedefinitions` `get`, the tab shows an error instead of the workload list.
+ Without `list` on `pods` or `rayclusters`, the tab still loads, but inference or RayService workloads are missing from the list.

#### To edit a workload's priority
<a name="sagemaker-hyperpod-studio-task-governance-rbac-edit"></a>

Editing changes the priority class label on the workload's parent object.

These are custom RBAC rules. If you associate `AmazonEKSClusterAdminPolicy` with the access entry, these permissions are already included.

Verbs: `get` and `patch` on the parent object, in the workload's namespace (or cluster-wide).

| Workload kind | Resource (API group) |
| --- | --- |
| PyTorchJob | pytorchjobs (kubeflow.org) |
| HyperPodPyTorchJob | hyperpodpytorchjobs (sagemaker.amazonaws.com) |
| RayCluster | rayclusters (ray.io) |
| Inference deployment | inferenceendpointconfigs, jumpstartmodels (inference.sagemaker.aws.amazon.com) |
| Space | workspaces (workspace.jupyter.org) |

Notes:
+ Other kinds (for example MPIJob, TFJob, RayJob, RayService) are shown read-only, with no **Edit** action.
+ The **Edit** action is shown only when the cluster has a scheduler configuration with priority classes (task governance).

### How to grant the permissions
<a name="sagemaker-hyperpod-studio-task-governance-grant-perms"></a>

#### Option 1: EKS cluster admin access policy
<a name="sagemaker-hyperpod-studio-task-governance-grant-perms-option1"></a>

Associate `AmazonEKSClusterAdminPolicy` with the execution role at cluster scope. If the role has no access entry yet, create one first:

```bash
aws eks create-access-entry \
  --cluster-name {{eks-cluster-name}} \
  --principal-arn arn:aws:iam::{{account-id}}:role/{{studio-execution-role}}

aws eks associate-access-policy \
  --cluster-name {{eks-cluster-name}} \
  --principal-arn arn:aws:iam::{{account-id}}:role/{{studio-execution-role}} \
  --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy \
  --access-scope type=cluster
```

You can also do this in the [Amazon EKS console](https://console.aws.amazon.com/eks/), on the cluster's **Access** tab.

#### Option 2: Custom RBAC and an EKS access entry
<a name="sagemaker-hyperpod-studio-task-governance-grant-perms-option2"></a>

Create a `ClusterRole` with the rules in [Kubernetes permissions (custom RBAC)](#sagemaker-hyperpod-studio-task-governance-rbac), bind it to a Kubernetes group, then map the execution role to that group:

```bash
aws eks create-access-entry \
  --cluster-name {{eks-cluster-name}} \
  --principal-arn arn:aws:iam::{{account-id}}:role/{{studio-execution-role}} \
  --kubernetes-groups '["hyperpod-queue-admins"]'
```

Example ClusterRole:

```yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: hyperpod-queue-admin
rules:
# Admin check: required to show the Queue tab.
- apiGroups: ["kueue.x-k8s.io"]
  resources: ["clusterqueues"]
  verbs: ["update"]
- apiGroups: ["authorization.k8s.io"]
  resources: ["selfsubjectaccessreviews"]
  verbs: ["create"]
# View the queue.
- apiGroups: ["apiextensions.k8s.io"]
  resources: ["customresourcedefinitions"]
  resourceNames: ["workloads.kueue.x-k8s.io"]
  verbs: ["get"]
- apiGroups: ["kueue.x-k8s.io"]
  resources: ["workloads"]
  verbs: ["list"]
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["list"]
- apiGroups: ["ray.io"]
  resources: ["rayclusters"]
  verbs: ["get", "list", "patch"]
# Edit a workload's priority.
- apiGroups: ["kubeflow.org"]
  resources: ["pytorchjobs"]
  verbs: ["get", "patch"]
- apiGroups: ["sagemaker.amazonaws.com"]
  resources: ["hyperpodpytorchjobs"]
  verbs: ["get", "patch"]
- apiGroups: ["inference.sagemaker.aws.amazon.com"]
  resources: ["inferenceendpointconfigs", "jumpstartmodels"]
  verbs: ["get", "patch"]
- apiGroups: ["workspace.jupyter.org"]
  resources: ["workspaces"]
  verbs: ["get", "patch"]
```

Bind the `ClusterRole` to the group used in `--kubernetes-groups` with a `ClusterRoleBinding`.

### References
<a name="sagemaker-hyperpod-studio-task-governance-references"></a>
+ [Associating access policies with access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html)
+ [Setting up Kubernetes role-based access control](sagemaker-hyperpod-eks-setup-rbac.md) (Setting up Kubernetes role-based access control)
+ [Task governance setup](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-setup-task-governance.html)
