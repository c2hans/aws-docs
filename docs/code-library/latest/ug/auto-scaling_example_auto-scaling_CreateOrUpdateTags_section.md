---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_CreateOrUpdateTags_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateOrUpdateTags` with a CLI
<a name="auto-scaling_example_auto-scaling_CreateOrUpdateTags_section"></a>

The following code examples show how to use `CreateOrUpdateTags`.

------
#### [ CLI ]

**AWS CLI**
**To create or update tags for an Auto Scaling group**
This example adds two tags to the specified Auto Scaling group.

```
aws autoscaling create-or-update-tags \
    --tags {{ResourceId=my-asg,ResourceType=auto-scaling-group,Key=Role,Value=WebServer,PropagateAtLaunch=true}} {{ResourceId=my-asg,ResourceType=auto-scaling-group,Key=Dept,Value=Research,PropagateAtLaunch=true}}
```
This command produces no output.
For more information, see [Tagging Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-tagging.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [CreateOrUpdateTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-or-update-tags.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds a single tag to the specified Auto Scaling group. The tag key is 'myTag' and the tag value is 'myTagValue'. Auto Scaling propagates this tag to the subsequent EC2 instances launched by the Auto Scaling group. The syntax used by this example requires PowerShell version 3 or later.**

```
Set-ASTag -Tag @( @{ResourceType="auto-scaling-group"; ResourceId="my-asg"; Key="myTag"; Value="myTagValue"; PropagateAtLaunch=$true} )
```
**Example 2: With PowerShell version 2, you must use New-Object to create the tag for the Tag parameter.**

```
$tag = New-Object Amazon.AutoScaling.Model.Tag
$tag.ResourceType = "auto-scaling-group"
$tag.ResourceId = "my-asg"
$tag.Key = "myTag"
$tag.Value = "myTagValue"
$tag.PropagateAtLaunch = $true
Set-ASTag -Tag $tag
```
+  For API details, see [CreateOrUpdateTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds a single tag to the specified Auto Scaling group. The tag key is 'myTag' and the tag value is 'myTagValue'. Auto Scaling propagates this tag to the subsequent EC2 instances launched by the Auto Scaling group. The syntax used by this example requires PowerShell version 3 or later.**

```
Set-ASTag -Tag @( @{ResourceType="auto-scaling-group"; ResourceId="my-asg"; Key="myTag"; Value="myTagValue"; PropagateAtLaunch=$true} )
```
**Example 2: With PowerShell version 2, you must use New-Object to create the tag for the Tag parameter.**

```
$tag = New-Object Amazon.AutoScaling.Model.Tag
$tag.ResourceType = "auto-scaling-group"
$tag.ResourceId = "my-asg"
$tag.Key = "myTag"
$tag.Value = "myTagValue"
$tag.PropagateAtLaunch = $true
Set-ASTag -Tag $tag
```
+  For API details, see [CreateOrUpdateTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
