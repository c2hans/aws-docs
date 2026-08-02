---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_SetInstanceProtection_section.html
---

# Use `SetInstanceProtection` with a CLI
<a name="example_auto-scaling_SetInstanceProtection_section"></a>

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

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.
