---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_DeleteTags_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteTags` with a CLI
<a name="auto-scaling_example_auto-scaling_DeleteTags_section"></a>

The following code examples show how to use `DeleteTags`.

------
#### [ CLI ]

**AWS CLI**
**To delete a tag from an Auto Scaling group**
This example deletes the specified tag from the specified Auto Scaling group.

```
aws autoscaling delete-tags \
    --tags {{ResourceId=my-asg,ResourceType=auto-scaling-group,Key=Dept,Value=Research}}
```
This command produces no output.
For more information, see [Tagging Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-tagging.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [DeleteTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-tags.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example removes the specified tag from the specified Auto Scaling group. You are prompted for confirmation before the operation proceeds. The syntax used by this example requires PowerShell version 3 or later.**

```
Remove-ASTag -Tag @( @{ResourceType="auto-scaling-group"; ResourceId="my-asg"; Key="myTag" } )
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-ASTag (DeleteTags)" on target "Amazon.AutoScaling.Model.Tag".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASTag -Tag @( @{ResourceType="auto-scaling-group"; ResourceId="my-asg"; Key="myTag" } ) -Force
```
**Example 3: With Powershell version 2, you must use New-Object to create the tag for the Tag parameter.**

```
$tag = New-Object Amazon.AutoScaling.Model.Tag
$tag.ResourceType = "auto-scaling-group"
$tag.ResourceId = "my-asg"
$tag.Key = "myTag"
Remove-ASTag -Tag $tag -Force
```
+  For API details, see [DeleteTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example removes the specified tag from the specified Auto Scaling group. You are prompted for confirmation before the operation proceeds. The syntax used by this example requires PowerShell version 3 or later.**

```
Remove-ASTag -Tag @( @{ResourceType="auto-scaling-group"; ResourceId="my-asg"; Key="myTag" } )
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-ASTag (DeleteTags)" on target "Amazon.AutoScaling.Model.Tag".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASTag -Tag @( @{ResourceType="auto-scaling-group"; ResourceId="my-asg"; Key="myTag" } ) -Force
```
**Example 3: With Powershell version 2, you must use New-Object to create the tag for the Tag parameter.**

```
$tag = New-Object Amazon.AutoScaling.Model.Tag
$tag.ResourceType = "auto-scaling-group"
$tag.ResourceId = "my-asg"
$tag.Key = "myTag"
Remove-ASTag -Tag $tag -Force
```
+  For API details, see [DeleteTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
