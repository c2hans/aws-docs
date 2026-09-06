---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/eks_example_eks_TagResource_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `TagResource` with a CLI
<a name="eks_example_eks_TagResource_section"></a>

The following code examples show how to use `TagResource`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To add the specified tags to an Amazon EKS Cluster**
The following `tag-resource` example adds the specified tags to an Amazon EKS Cluster.

```
aws eks tag-resource \
    --resource-arn {{arn:aws:eks:us-east-2:111122223333:cluster/my-eks-cluster}} \
    --tag '{{my-eks-cluster-test-1=test-value-1,my-eks-cluster-dev-1=dev-value-2}}'
```
This command produces no output.
**Example 2: To add the specified tags to an Amazon EKS Node group**
The following `tag-resource` example adds the specified tags to an Amazon EKS Node group.

```
aws eks tag-resource \
    --resource-arn {{arn:aws:eks:us-east-2:111122223333:nodegroup/my-eks-cluster/my-eks-managed-node-group/60c71ed2-2cfb-020f-a5f4-ad32477f198c}} \
    --tag '{{my-eks-nodegroup-test-1=test-value-1,my-eks-nodegroup-dev-1=dev-value-2}}'
```
This command produces no output.
+  For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/tag-resource.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This cmdlet associates the specified tags to a resource with the specified resourceArn. **

```
Add-EKSResourceTag -ResourceArn "arn:aws:eks:us-west-2:012345678912:cluster/PROD" -Tag @{Name = "EKSPRODCLUSTER"}
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This cmdlet associates the specified tags to a resource with the specified resourceArn. **

```
Add-EKSResourceTag -ResourceArn "arn:aws:eks:us-west-2:012345678912:cluster/PROD" -Tag @{Name = "EKSPRODCLUSTER"}
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
