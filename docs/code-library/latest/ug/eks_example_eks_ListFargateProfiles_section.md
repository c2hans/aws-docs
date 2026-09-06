---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/eks_example_eks_ListFargateProfiles_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListFargateProfiles` with a CLI
<a name="eks_example_eks_ListFargateProfiles_section"></a>

The following code examples show how to use `ListFargateProfiles`.

------
#### [ CLI ]

**AWS CLI**
**To list all the fargate profiles in your Amazon EKS cluster named `my-eks-cluster`**
The following `list-fargate-profiles` example lists all the fargate profiles in your Amazon EKS cluster named my-eks-cluster.

```
aws eks list-fargate-profiles \
    --cluster-name {{my-eks-cluster}}
```
Output:

```
{
    "fargateProfileNames": [
        "my-fargate-profile"
    ]
}
```
+  For API details, see [ListFargateProfiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-fargate-profiles.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This cmdlet lists the AWS Fargate profiles associated with the specified cluster in your AWS account in the specified Region.**

```
Get-EKSFargateProfileList -ClusterName "TEST"
```
**Output:**

```
EKSFargate
EKSFargateProfile
```
+  For API details, see [ListFargateProfiles](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This cmdlet lists the AWS Fargate profiles associated with the specified cluster in your AWS account in the specified Region.**

```
Get-EKSFargateProfileList -ClusterName "TEST"
```
**Output:**

```
EKSFargate
EKSFargateProfile
```
+  For API details, see [ListFargateProfiles](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
