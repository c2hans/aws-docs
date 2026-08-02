---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_ResumeProcesses_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ResumeProcesses` with a CLI
<a name="auto-scaling_example_auto-scaling_ResumeProcesses_section"></a>

The following code examples show how to use `ResumeProcesses`.

------
#### [ CLI ]

**AWS CLI**
**To resume suspended processes**
This example resumes the specified suspended scaling process for the specified Auto Scaling group.

```
aws autoscaling resume-processes \
    --auto-scaling-group-name {{my-asg}} \
    --scaling-processes {{AlarmNotification}}
```
This command produces no output.
For more information, see [Suspending and resuming scaling processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [ResumeProcesses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/resume-processes.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example resumes the specified Auto Scaling process for the specified Auto Scaling group.**

```
Resume-ASProcess -AutoScalingGroupName my-asg -ScalingProcess "AlarmNotification"
```
**Example 2: This example resumes all suspended Auto Scaling processes for the specified Auto Scaling group.**

```
Resume-ASProcess -AutoScalingGroupName my-asg
```
+  For API details, see [ResumeProcesses](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example resumes the specified Auto Scaling process for the specified Auto Scaling group.**

```
Resume-ASProcess -AutoScalingGroupName my-asg -ScalingProcess "AlarmNotification"
```
**Example 2: This example resumes all suspended Auto Scaling processes for the specified Auto Scaling group.**

```
Resume-ASProcess -AutoScalingGroupName my-asg
```
+  For API details, see [ResumeProcesses](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
