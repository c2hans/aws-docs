---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_DescribeMetricCollectionTypes_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeMetricCollectionTypes` with a CLI
<a name="auto-scaling_example_auto-scaling_DescribeMetricCollectionTypes_section"></a>

The following code examples show how to use `DescribeMetricCollectionTypes`.

------
#### [ CLI ]

**AWS CLI**
**To describe the available metric collection types**
This example describes the available metric collection types.

```
aws autoscaling describe-metric-collection-types
```
Output:

```
{
    "Metrics": [
        {
            "Metric": "GroupMinSize"
        },
        {
            "Metric": "GroupMaxSize"
        },
        {
            "Metric": "GroupDesiredCapacity"
        },
        {
            "Metric": "GroupInServiceInstances"
        },
        {
            "Metric": "GroupInServiceCapacity"
        },
        {
            "Metric": "GroupPendingInstances"
        },
        {
            "Metric": "GroupPendingCapacity"
        },
        {
            "Metric": "GroupTerminatingInstances"
        },
        {
            "Metric": "GroupTerminatingCapacity"
        },
        {
            "Metric": "GroupStandbyInstances"
        },
        {
            "Metric": "GroupStandbyCapacity"
        },
        {
            "Metric": "GroupTotalInstances"
        },
        {
            "Metric": "GroupTotalCapacity"
        }
    ],
    "Granularities": [
        {
            "Granularity": "1Minute"
        }
    ]
}
```
For more information, see [Auto Scaling group metrics](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html#as-group-metrics) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [DescribeMetricCollectionTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-metric-collection-types.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists the metric collection types that are supported by Auto Scaling.**

```
(Get-ASMetricCollectionType).Metrics
```
**Output:**

```
Metric
------
GroupMinSize
GroupMaxSize
GroupDesiredCapacity
GroupInServiceInstances
GroupPendingInstances
GroupTerminatingInstances
GroupStandbyInstances
GroupTotalInstances
```
**Example 2: This example lists the corresponding granularities.**

```
(Get-ASMetricCollectionType).Granularities
```
**Output:**

```
Granularity
-----------
1Minute
```
+  For API details, see [DescribeMetricCollectionTypes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example lists the metric collection types that are supported by Auto Scaling.**

```
(Get-ASMetricCollectionType).Metrics
```
**Output:**

```
Metric
------
GroupMinSize
GroupMaxSize
GroupDesiredCapacity
GroupInServiceInstances
GroupPendingInstances
GroupTerminatingInstances
GroupStandbyInstances
GroupTotalInstances
```
**Example 2: This example lists the corresponding granularities.**

```
(Get-ASMetricCollectionType).Granularities
```
**Output:**

```
Granularity
-----------
1Minute
```
+  For API details, see [DescribeMetricCollectionTypes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
