---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-resource-ownership.html
---

# Resource ownership

Resource ownership lets users control whether a resource they created within a particular namespace can be modified or deleted by other users in that namespace. It is an additional setting on top of RBAC for the supported resource kinds.

Currently, ownership is supported for the following workload kinds: `RayJob`, `HyperPodPyTorchJob`, `InferenceEndpointConfig`, and `JumpStartModel`.

## Prerequisites
<a name="sagemaker-hyperpod-studio-resource-ownership-prereqs"></a>

Before you can use resource ownership, the following must be in place on your cluster:
+ Kubernetes 1.30 or later.
+ amd64 HyperPod nodes.
+ cert-manager is installed on the cluster, either as the cert-manager Amazon EKS add-on or through the HyperPod Helm chart (`cert-manager.enabled=true`), and its webhook is running. To check, run the following command and confirm the deployment is available:

  ```bash
  kubectl -n cert-manager get deployment cert-manager-webhook
  ```
+ The domain's `ExecutionRoleSessionNameMode` is set to `USER_IDENTITY`. Without this setting, the ownership dropdown, **Created by** column, and **Ownership** column do not appear. For more information, see [Execution role session name mode](execution-roles-and-spaces.md#sagemaker-execution-role-session-name).

Install the HyperPod CLI by cloning the repository and checking out the latest release tag:

```bash
git clone https://github.com/aws/sagemaker-hyperpod-cli.git
cd sagemaker-hyperpod-cli
git checkout $(git tag --sort=-v:refname | head -n 1)
```

Then install the resource ownership Helm chart once per cluster into the `aws-hyperpod` namespace:

```bash
helm upgrade --install hyperpod-resource-ownership \
    helm_chart/HyperPodHelmChart/charts/hyperpod-resource-ownership \
    --namespace aws-hyperpod --create-namespace \
    --set region={{region}} \
    --wait
```

To verify the installation:

```bash
kubectl -n aws-hyperpod get deploy | grep resource-ownership
kubectl get mutatingwebhookconfiguration | grep resource-ownership
kubectl get validatingadmissionpolicy sagemaker-hyperpod-user-resource-ownership-policy
```

## Choosing an ownership type
<a name="sagemaker-hyperpod-studio-resource-ownership-choose"></a>

When you submit a training job or deploy a model, the form includes an **Ownership** field. Choose **Public** or **OwnerOnly**. Public is the default.

## Public ownership
<a name="sagemaker-hyperpod-studio-resource-ownership-public"></a>

Any user with access to the namespace can stop, edit, or delete the workload. Teams that must be isolated from one another should not share a namespace. Give them separate namespaces and separate Amazon EKS access entries.

## OwnerOnly ownership
<a name="sagemaker-hyperpod-studio-resource-ownership-owneronly"></a>

Only the creator and cluster administrators can stop, edit, or delete that object. A cluster administrator is a member of one of the Kubernetes groups in the chart's `policy.adminGroups` value, which defaults to `system:masters`. Ownership applies to the object carrying resource ownership annotations. It does not extend to other Kubernetes objects created from it, or to network access to a running workload.

Amazon EKS access policies, such as `AmazonEKSClusterAdminPolicy`, grant permissions without adding the caller to a Kubernetes group. An administrator whose access comes only from an access policy therefore can't modify other users' OwnerOnly objects. To give administrators this access, add their Kubernetes group to `policy.adminGroups` when you install the chart. For example: `--set 'policy.adminGroups={system:masters,<your-admin-group>}'`.

## What resource ownership does not cover
<a name="sagemaker-hyperpod-studio-resource-ownership-not-covered"></a>

Ownership is enforced at admission time on the four supported kinds listed above, and only on the object you created. The following are not covered.

**Objects that operators create from your workload.**
When you create an `InferenceEndpointConfig`, the HyperPod inference operator creates further objects to register and expose the endpoint. Those objects are not governed by resource ownership. Another user with access to the namespace can delete them, which stops your endpoint, even when your `InferenceEndpointConfig` is set to `OwnerOnly`.

**Network access to a running workload.**
Ownership governs the workload lifecycle: create, edit, stop, delete. It does not restrict who can reach a workload that is already running. Anyone with namespace access and network reachability can connect to a running Ray dashboard or invoke an inference endpoint deployed without authentication configured.

**Reads.**
Ownership does not hide your workloads from others in the namespace. Any user who can list a governed kind sees every object of that kind in the namespace, including its name, configuration, and status. Kubernetes admission does not run on reads.

**Important**
A namespace is not a security boundary. Resource ownership is a guardrail against accidental and casual interference between users who already share a namespace and already hold Kubernetes permissions on these kinds. It is not an authorization boundary.

## Workload tables
<a name="sagemaker-hyperpod-studio-resource-ownership-tables"></a>

The **Training**, **Inference**, and **Queue** tables show a **Created by** column and an **Ownership** column for all supported workload kinds.

**Note**
The resource ownership webhook fails closed. If the webhook pods are unavailable, creating any of the supported workload kinds is rejected cluster-wide.
