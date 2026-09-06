---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_ExecutePolicy_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ExecutePolicy` with a CLI
<a name="auto-scaling_example_auto-scaling_ExecutePolicy_section"></a>

The following code examples show how to use `ExecutePolicy`.

------
#### [ CLI ]

**AWS CLI**
**To execute a scaling policy**
This example executes the scaling policy named `my-step-scale-out-policy` for the specified Auto Scaling group.

```
aws autoscaling execute-policy \
    --auto-scaling-group-name {{my-asg}} \
    --policy-name  {{my-step-scale-out-policy}} \
    --metric-value {{95}} \
    --breach-threshold {{80}}
```
This command produces no output.
For more information, see [Step and simple scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [ExecutePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/execute-policy.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example executes the specified policy for the specified Auto Scaling group.**

```
Start-ASPolicy -AutoScalingGroupName my-asg -PolicyName "myScaleInPolicy"
```
**Example 2: This example executes the specified policy for the specified Auto Scaling group, after waiting for the cooldown period to complete.**

```
Start-ASPolicy -AutoScalingGroupName my-asg -PolicyName "myScaleInPolicy" -HonorCooldown $true
```
+  For API details, see [ExecutePolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example executes the specified policy for the specified Auto Scaling group.**

```
Start-ASPolicy -AutoScalingGroupName my-asg -PolicyName "myScaleInPolicy"
```
**Example 2: This example executes the specified policy for the specified Auto Scaling group, after waiting for the cooldown period to complete.**

```
Start-ASPolicy -AutoScalingGroupName my-asg -PolicyName "myScaleInPolicy" -HonorCooldown $true
```
+  For API details, see [ExecutePolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
