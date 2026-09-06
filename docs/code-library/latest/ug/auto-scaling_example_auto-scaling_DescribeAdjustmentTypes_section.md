---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_DescribeAdjustmentTypes_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeAdjustmentTypes` with a CLI
<a name="auto-scaling_example_auto-scaling_DescribeAdjustmentTypes_section"></a>

The following code examples show how to use `DescribeAdjustmentTypes`.

------
#### [ CLI ]

**AWS CLI**
**To describe the available scaling adjustment types**
This example describes the available adjustment types.

```
aws autoscaling describe-adjustment-types
```
Output:

```
{
    "AdjustmentTypes": [
        {
            "AdjustmentType": "ChangeInCapacity"
        },
        {
            "AdjustmentType": "ExactCapacity"
        },
        {
            "AdjustmentType": "PercentChangeInCapacity"
        }
    ]
}
```
For more information, see [Scaling adjustment types](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#as-scaling-adjustment) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [DescribeAdjustmentTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-adjustment-types.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example describes the adjustment types that are supported by Auto Scaling.**

```
Get-ASAdjustmentType
```
**Output:**

```
Type
----
ChangeInCapacity
ExactCapacity
PercentChangeInCapacity
```
+  For API details, see [DescribeAdjustmentTypes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example describes the adjustment types that are supported by Auto Scaling.**

```
Get-ASAdjustmentType
```
**Output:**

```
Type
----
ChangeInCapacity
ExactCapacity
PercentChangeInCapacity
```
+  For API details, see [DescribeAdjustmentTypes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
