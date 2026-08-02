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
**To list the updates for a cluster**
This example command lists the current updates for a cluster named `example` in your default region.
Command:

```
aws eks list-updates --name {{example}}
```
Output:

```
{
    "updateIds": [
        "10bddb13-a71b-425a-b0a6-71cd03e59161"
    ]
}
```
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
