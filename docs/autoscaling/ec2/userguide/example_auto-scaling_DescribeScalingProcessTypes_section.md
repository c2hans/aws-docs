---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeScalingProcessTypes_section.html
---

# Use `DescribeScalingProcessTypes` with a CLI
<a name="example_auto-scaling_DescribeScalingProcessTypes_section"></a>

The following code examples show how to use `DescribeScalingProcessTypes`.

------
#### [ CLI ]

**AWS CLI**
**To describe the available process types**
This example describes the available process types.

```
aws autoscaling describe-scaling-process-types
```
Output:

```
{
    "Processes": [
        {
            "ProcessName": "AZRebalance"
        },
        {
            "ProcessName": "AddToLoadBalancer"
        },
        {
            "ProcessName": "AlarmNotification"
        },
        {
            "ProcessName": "HealthCheck"
        },
        {
            "ProcessName": "InstanceRefresh"
        },
        {
            "ProcessName": "Launch"
        },
        {
            "ProcessName": "ReplaceUnhealthy"
        },
        {
            "ProcessName": "ScheduledActions"
        },
        {
            "ProcessName": "Terminate"
        }
    ]
}
```
For more information, see [Suspending and resuming scaling processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [DescribeScalingProcessTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-scaling-process-types.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists the process types that are supported by Auto Scaling.**

```
Get-ASScalingProcessType
```
**Output:**

```
ProcessName
-----------
AZRebalance
AddToLoadBalancer
AlarmNotification
HealthCheck
Launch
ReplaceUnhealthy
ScheduledActions
Terminate
```
+  For API details, see [DescribeScalingProcessTypes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example lists the process types that are supported by Auto Scaling.**

```
Get-ASScalingProcessType
```
**Output:**

```
ProcessName
-----------
AZRebalance
AddToLoadBalancer
AlarmNotification
HealthCheck
Launch
ReplaceUnhealthy
ScheduledActions
Terminate
```
+  For API details, see [DescribeScalingProcessTypes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.
