---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/eks_example_eks_UntagResource_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UntagResource` with a CLI
<a name="eks_example_eks_UntagResource_section"></a>

The following code examples show how to use `UntagResource`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To deletes the specified tags from an Amazon EKS Cluster**
The following `untag-resource` example deletes the specified tags from an Amazon EKS Cluster.

```
aws eks untag-resource \
    --resource-arn {{arn:aws:eks:us-east-2:111122223333:cluster/my-eks-cluster}} \
    --tag-keys {{"my-eks-cluster-test-1"}} {{"my-eks-cluster-dev-1"}}
```
This command produces no output.
**Example 2: To deletes the specified tags from an Amazon EKS Node group**
The following `untag-resource` example deletes the specified tags from an Amazon EKS Node group.

```
aws eks untag-resource \
    --resource-arn {{arn:aws:eks:us-east-2:111122223333:nodegroup/my-eks-cluster/my-eks-managed-node-group/60c71ed2-2cfb-020f-a5f4-ad32477f198c}} \
    --tag-keys {{"my-eks-nodegroup-test-1"}} {{"my-eks-nodegroup-dev-1"}}
```
This command produces no output.
+  For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/untag-resource.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This cmdlet deletes specified tags from an EKS resource.**

```
Remove-EKSResourceTag -ResourceArn "arn:aws:eks:us-west-2:012345678912:cluster/PROD" -TagKey "Name"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EKSResourceTag (UntagResource)" on target "arn:aws:eks:us-west-2:012345678912:cluster/PROD".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [UntagResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This cmdlet deletes specified tags from an EKS resource.**

```
Remove-EKSResourceTag -ResourceArn "arn:aws:eks:us-west-2:012345678912:cluster/PROD" -TagKey "Name"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EKSResourceTag (UntagResource)" on target "arn:aws:eks:us-west-2:012345678912:cluster/PROD".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [UntagResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
