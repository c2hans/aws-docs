---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_PutScheduledUpdateGroupAction_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `PutScheduledUpdateGroupAction` with a CLI
<a name="auto-scaling_example_auto-scaling_PutScheduledUpdateGroupAction_section"></a>

The following code examples show how to use `PutScheduledUpdateGroupAction`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To add a scheduled action to an Auto Scaling group**
This example adds the specified scheduled action to the specified Auto Scaling group.

```
aws autoscaling put-scheduled-update-group-action \
    --auto-scaling-group-name {{my-asg}} \
    --scheduled-action-name {{my-scheduled-action}} \
    --start-time {{"2023-05-12T08:00:00Z"}} \
    --min-size {{2}} \
    --max-size {{6}} \
    --desired-capacity {{4}}
```
This command produces no output. If a scheduled action with the same name already exists, it will be overwritten by the new scheduled action.
For more examples, see [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html) in the *Amazon EC2 Auto Scaling User Guide*.
**Example 2: To specify a recurring schedule**
This example creates a scheduled action to scale on a recurring schedule that is scheduled to execute at 00:30 hours on the first of January, June, and December every year.

```
aws autoscaling put-scheduled-update-group-action \
    --auto-scaling-group-name {{my-asg}} \
    --scheduled-action-name {{my-recurring-action}} \
    --recurrence {{"30 0 1 1,6,12 *"}} \
    --min-size {{2}} \
    --max-size {{6}} \
    --desired-capacity {{4}}
```
This command produces no output. If a scheduled action with the same name already exists, it will be overwritten by the new scheduled action.
For more examples, see [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [PutScheduledUpdateGroupAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-scheduled-update-group-action.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates or updates a one-time scheduled action to change the desired capacity at the specified start time.**

```
Write-ASScheduledUpdateGroupAction -AutoScalingGroupName my-asg -ScheduledActionName "myScheduledAction" -StartTime "2015-12-01T00:00:00Z" -DesiredCapacity 10
```
+  For API details, see [PutScheduledUpdateGroupAction](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates or updates a one-time scheduled action to change the desired capacity at the specified start time.**

```
Write-ASScheduledUpdateGroupAction -AutoScalingGroupName my-asg -ScheduledActionName "myScheduledAction" -StartTime "2015-12-01T00:00:00Z" -DesiredCapacity 10
```
+  For API details, see [PutScheduledUpdateGroupAction](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
