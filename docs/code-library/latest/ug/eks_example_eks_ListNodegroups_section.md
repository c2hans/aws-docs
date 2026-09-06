---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/eks_example_eks_ListNodegroups_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListNodegroups` with a CLI
<a name="eks_example_eks_ListNodegroups_section"></a>

The following code examples show how to use `ListNodegroups`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Getting started with managed kubernetes clusters](eks_example_eks_GettingStarted_034_section.md)

------
#### [ CLI ]

**AWS CLI**
**List all the node groups in an Amazon EKS cluster**
The following `list-nodegroups` example list all the node groups in an Amazon EKS cluster.

```
aws eks list-nodegroups \
    --cluster-name {{my-eks-cluster}}
```
Output:

```
{
    "nodegroups": [
        "my-eks-managed-node-group",
        "my-eks-nodegroup"
    ]
}
```
+  For API details, see [ListNodegroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-nodegroups.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This cmdlet lists the Amazon EKS node groups associated with the specified cluster in your AWS account in the specified Region. **

```
Get-EKSNodegroupList -ClusterName PROD
```
**Output:**

```
 ProdEKSNodeGroup
```
+  For API details, see [ListNodegroups](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This cmdlet lists the Amazon EKS node groups associated with the specified cluster in your AWS account in the specified Region. **

```
Get-EKSNodegroupList -ClusterName PROD
```
**Output:**

```
 ProdEKSNodeGroup
```
+  For API details, see [ListNodegroups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
