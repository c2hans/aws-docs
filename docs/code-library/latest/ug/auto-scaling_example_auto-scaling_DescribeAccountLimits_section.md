---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_DescribeAccountLimits_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeAccountLimits` with a CLI
<a name="auto-scaling_example_auto-scaling_DescribeAccountLimits_section"></a>

The following code examples show how to use `DescribeAccountLimits`.

------
#### [ CLI ]

**AWS CLI**
**To describe your Amazon EC2 Auto Scaling account limits**
This example describes the Amazon EC2 Auto Scaling limits for your AWS account.

```
aws autoscaling describe-account-limits
```
Output:

```
{
    "NumberOfLaunchConfigurations": 5,
    "MaxNumberOfLaunchConfigurations": 100,
    "NumberOfAutoScalingGroups": 3,
    "MaxNumberOfAutoScalingGroups": 20
}
```
For more information, see [Amazon EC2 Auto Scaling service quotas](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-account-limits.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [DescribeAccountLimits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-account-limits.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example describes the Auto Scaling resource limits for your AWS account.**

```
Get-ASAccountLimit
```
**Output:**

```
MaxNumberOfAutoScalingGroups    : 20
MaxNumberOfLaunchConfigurations : 100
```
+  For API details, see [DescribeAccountLimits](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example describes the Auto Scaling resource limits for your AWS account.**

```
Get-ASAccountLimit
```
**Output:**

```
MaxNumberOfAutoScalingGroups    : 20
MaxNumberOfLaunchConfigurations : 100
```
+  For API details, see [DescribeAccountLimits](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
