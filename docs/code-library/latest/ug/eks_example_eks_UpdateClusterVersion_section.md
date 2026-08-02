---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/eks_example_eks_UpdateClusterVersion_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateClusterVersion` with a CLI
<a name="eks_example_eks_UpdateClusterVersion_section"></a>

The following code examples show how to use `UpdateClusterVersion`.

------
#### [ CLI ]

**AWS CLI**
**To updates an Amazon EKS cluster named `my-eks-cluster` to the specified Kubernetes version**
The following `update-cluster-version` example updates an Amazon EKS cluster to the specified Kubernetes version.

```
aws eks update-cluster-version \
    --name {{my-eks-cluster}} \
    --kubernetes-version {{1.27}}
```
Output:

```
{
    "update": {
        "id": "e4091a28-ea14-48fd-a8c7-975aeb469e8a",
        "status": "InProgress",
        "type": "VersionUpdate",
        "params": [
            {
                "type": "Version",
                "value": "1.27"
            },
            {
                "type": "PlatformVersion",
                "value": "eks.16"
            }
        ],
        "createdAt": "2024-04-12T16:56:01.082000-04:00",
        "errors": []
    }
}
```
For more information, see [Updating an Amazon EKS cluster Kubernetes version](https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html) in the *Amazon EKS User Guide*.
+  For API details, see [UpdateClusterVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/update-cluster-version.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This cmdlet updates an Amazon EKS cluster to the specified Kubernetes version. Your cluster continues to function during the update.**

```
Update-EKSClusterVersion -Name "PROD-KUBE-CL" -Version 1.14
```
**Output:**

```
CreatedAt : 12/26/2019 9:50:37 AM
Errors    : {}
Id        : ef186eff-3b3a-4c25-bcfc-3dcdf9e898a8
Params    : {Amazon.EKS.Model.UpdateParam, Amazon.EKS.Model.UpdateParam}
Status    : InProgress
Type      : VersionUpdate
```
+  For API details, see [UpdateClusterVersion](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This cmdlet updates an Amazon EKS cluster to the specified Kubernetes version. Your cluster continues to function during the update.**

```
Update-EKSClusterVersion -Name "PROD-KUBE-CL" -Version 1.14
```
**Output:**

```
CreatedAt : 12/26/2019 9:50:37 AM
Errors    : {}
Id        : ef186eff-3b3a-4c25-bcfc-3dcdf9e898a8
Params    : {Amazon.EKS.Model.UpdateParam, Amazon.EKS.Model.UpdateParam}
Status    : InProgress
Type      : VersionUpdate
```
+  For API details, see [UpdateClusterVersion](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
