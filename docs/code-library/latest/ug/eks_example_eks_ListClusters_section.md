---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/eks_example_eks_ListClusters_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListClusters` with a CLI
<a name="eks_example_eks_ListClusters_section"></a>

The following code examples show how to use `ListClusters`.

------
#### [ CLI ]

**AWS CLI**
**To list all the installed add-ons in your Amazon EKS cluster named `my-eks-cluster`**
The following `list-clusters` example lists all the installed add-ons in your Amazon EKS cluster named my-eks-cluster.

```
aws eks list-clusters
```
Output:

```
{
    "clusters": [
        "prod",
        "qa",
        "stage",
        "my-eks-cluster"
    ]
}
```
+  For API details, see [ListClusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-clusters.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This cmdlet lists the Amazon EKS clusters in your AWS account in the specified Region.**

```
Get-EKSClusterList
```
**Output:**

```
 PROD
```
+  For API details, see [ListClusters](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This cmdlet lists the Amazon EKS clusters in your AWS account in the specified Region.**

```
Get-EKSClusterList
```
**Output:**

```
 PROD
```
+  For API details, see [ListClusters](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
