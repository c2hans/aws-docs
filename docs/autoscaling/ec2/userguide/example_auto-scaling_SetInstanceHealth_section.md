---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_SetInstanceHealth_section.html
---

# Use `SetInstanceHealth` with a CLI
<a name="example_auto-scaling_SetInstanceHealth_section"></a>

The following code examples show how to use `SetInstanceHealth`.

------
#### [ CLI ]

**AWS CLI**
**To set the health status of an instance**
This example sets the health status of the specified instance to `Unhealthy`.

```
aws autoscaling set-instance-health \
    --instance-id {{i-061c63c5eb45f0416}} \
    --health-status {{Unhealthy}}
```
This command produces no output.
+  For API details, see [SetInstanceHealth](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/set-instance-health.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example sets the status of the specified instance to 'Unhealthy', taking it out of service. Auto Scaling terminates and replaces the instance.**

```
Set-ASInstanceHealth -HealthStatus Unhealthy -InstanceId i-93633f9b
```
**Example 2: This example sets the status of the specified instance to 'Healthy', keeping it in service. Any health check grace period for the Auto Scaling group is not honored.**

```
Set-ASInstanceHealth -HealthStatus Healthy -InstanceId i-93633f9b -ShouldRespectGracePeriod $false
```
+  For API details, see [SetInstanceHealth](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example sets the status of the specified instance to 'Unhealthy', taking it out of service. Auto Scaling terminates and replaces the instance.**

```
Set-ASInstanceHealth -HealthStatus Unhealthy -InstanceId i-93633f9b
```
**Example 2: This example sets the status of the specified instance to 'Healthy', keeping it in service. Any health check grace period for the Auto Scaling group is not honored.**

```
Set-ASInstanceHealth -HealthStatus Healthy -InstanceId i-93633f9b -ShouldRespectGracePeriod $false
```
+  For API details, see [SetInstanceHealth](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.
