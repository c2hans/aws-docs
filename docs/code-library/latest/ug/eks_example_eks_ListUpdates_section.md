---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/eks_example_eks_ListUpdates_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListUpdates` with a CLI
<a name="eks_example_eks_ListUpdates_section"></a>

The following code examples show how to use `ListUpdates`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To list the updates for a cluster**
The following `list-updates` example lists the current updates for a cluster named `example` in your default region.

```
aws eks list-updates \
    --name {{example}}
```
Output:

```
{
    "updateIds": [
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    ]
}
```
**Example 2: To list all the update IDs for an Amazon EKS Node group**
The following `list-updates` example lists all the update IDs for an Amazon EKS Node group.

```
aws eks list-updates \
    --name {{my-eks-cluster}} \
    --nodegroup-name {{my-eks-managed-node-group}}
```
Output:

```
{
    "updateIds": [
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    ]
}
```
**Example 3: To list all the update IDs for an Amazon EKS add-on**
The following `list-updates` example lists all the update IDs for an Amazon EKS Add-on.

```
aws eks list-updates \
    --name {{my-eks-cluster}} \
    --addon-name {{vpc-cni}}
```
Output:

```
{
    "updateIds": [
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
    ]
}
```
For more information, see [Update existing cluster to new Kubernetes version](https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html) in the *Amazon EKS User Guide*.
+  For API details, see [ListUpdates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-updates.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This cmdlet lists the updates associated with an Amazon EKS cluster or managed node group in your AWS account, in the specified Region.**

```
Get-EKSUpdateList -Name "PROD"
```
**Output:**

```
ee708232-7d2e-4ed7-9270-d0b5176f0726
```
+  For API details, see [ListUpdates](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This cmdlet lists the updates associated with an Amazon EKS cluster or managed node group in your AWS account, in the specified Region.**

```
Get-EKSUpdateList -Name "PROD"
```
**Output:**

```
ee708232-7d2e-4ed7-9270-d0b5176f0726
```
+  For API details, see [ListUpdates](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
