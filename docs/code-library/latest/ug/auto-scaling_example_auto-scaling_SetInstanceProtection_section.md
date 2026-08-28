---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_SetInstanceProtection_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `SetInstanceProtection` with a CLI
<a name="auto-scaling_example_auto-scaling_SetInstanceProtection_section"></a>

The following code examples show how to use `SetInstanceProtection`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To enable the instance protection setting for an instance**
This example enables instance protection for the specified instance.

```
aws autoscaling set-instance-protection \
    --instance-ids {{i-061c63c5eb45f0416}} \
    --auto-scaling-group-name {{my-asg}} --protected-from-scale-in
```
This command produces no output.
**Example 2: To disable the instance protection setting for an instance**
This example disables instance protection for the specified instance.

```
aws autoscaling set-instance-protection \
    --instance-ids {{i-061c63c5eb45f0416}} \
    --auto-scaling-group-name {{my-asg}} \
    --no-protected-from-scale-in
```
This command produces no output.
+  For API details, see [SetInstanceProtection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/set-instance-protection.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example enables instance protection for the specified instance.**

```
Set-ASInstanceProtection -AutoScalingGroupName my-asg -InstanceId i-12345678 -ProtectedFromScaleIn $true
```
**Example 2: This example disables instance protection for the specified instance.**

```
Set-ASInstanceProtection -AutoScalingGroupName my-asg -InstanceId i-12345678 -ProtectedFromScaleIn $false
```
+  For API details, see [SetInstanceProtection](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example enables instance protection for the specified instance.**

```
Set-ASInstanceProtection -AutoScalingGroupName my-asg -InstanceId i-12345678 -ProtectedFromScaleIn $true
```
**Example 2: This example disables instance protection for the specified instance.**

```
Set-ASInstanceProtection -AutoScalingGroupName my-asg -InstanceId i-12345678 -ProtectedFromScaleIn $false
```
+  For API details, see [SetInstanceProtection](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
