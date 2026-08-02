---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_application-auto-scaling_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Application Auto Scaling examples using Tools for PowerShell V5
<a name="powershell_application-auto-scaling_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Application Auto Scaling.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-AASScalableTarget`
<a name="application-auto-scaling_RegisterScalableTarget_powershell_topic"></a>

The following code example shows how to use `Add-AASScalableTarget`.

**Tools for PowerShell V5**
**Example 1: This cmdlet registers or updates a scalable target. A scalable target is a resource that Application Auto Scaling can scale out and scale in.**

```
Add-AASScalableTarget -ServiceNamespace AppStream -ResourceId fleet/MyFleet -ScalableDimension appstream:fleet:DesiredCapacity -MinCapacity 2 -MaxCapacity 10
```
+  For API details, see [RegisterScalableTarget](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-AASScalableTarget`
<a name="application-auto-scaling_DescribeScalableTargets_powershell_topic"></a>

The following code example shows how to use `Get-AASScalableTarget`.

**Tools for PowerShell V5**
**Example 1: This example will provide information about the Application Autoscaling Scalable targets in the specified namespace.**

```
Get-AASScalableTarget -ServiceNamespace "AppStream"
```
**Output:**

```
CreationTime      : 11/7/2019 2:30:03 AM
MaxCapacity       : 5
MinCapacity       : 1
ResourceId        : fleet/Test
RoleARN           : arn:aws:iam::012345678912:role/aws-service-role/appstream.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_AppStreamFleet
ScalableDimension : appstream:fleet:DesiredCapacity
ServiceNamespace  : appstream
SuspendedState    : Amazon.ApplicationAutoScaling.Model.SuspendedState
```
+  For API details, see [DescribeScalableTargets](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-AASScalingActivity`
<a name="application-auto-scaling_DescribeScalingActivities_powershell_topic"></a>

The following code example shows how to use `Get-AASScalingActivity`.

**Tools for PowerShell V5**
**Example 1: Provides descriptive information about the scaling activities in the specified namespace from the previous six weeks.**

```
Get-AASScalingActivity -ServiceNamespace AppStream
```
**Output:**

```
ActivityId        : 2827409f-b639-4cdb-a957-8055d5d07434
Cause             : monitor alarm Appstream2-MyFleet-default-scale-in-Alarm in state ALARM triggered policy default-scale-in
Description       : Setting desired capacity to 2.
Details           :
EndTime           : 12/14/2019 11:32:49 AM
ResourceId        : fleet/MyFleet
ScalableDimension : appstream:fleet:DesiredCapacity
ServiceNamespace  : appstream
StartTime         : 12/14/2019 11:32:14 AM
StatusCode        : Successful
StatusMessage     : Successfully set desired capacity to 2. Change successfully fulfilled by appstream.
```
+  For API details, see [DescribeScalingActivities](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-AASScalingPolicy`
<a name="application-auto-scaling_DescribeScalingPolicies_powershell_topic"></a>

The following code example shows how to use `Get-AASScalingPolicy`.

**Tools for PowerShell V5**
**Example 1: This cmdlet describe the Application Auto Scaling scaling policies for the specified service namespace.**

```
Get-AASScalingPolicy -ServiceNamespace AppStream
```
**Output:**

```
Alarms                                   : {Appstream2-LabFleet-default-scale-out-Alarm}
CreationTime                             : 9/3/2019 2:48:15 AM
PolicyARN                                : arn:aws:autoscaling:us-west-2:012345678912:scalingPolicy:5659b069-b5cd-4af1-9f7f-3e956d36233e:resource/appstream/fleet/LabFleet:
                                           policyName/default-scale-out
PolicyName                               : default-scale-out
PolicyType                               : StepScaling
ResourceId                               : fleet/LabFleet
ScalableDimension                        : appstream:fleet:DesiredCapacity
ServiceNamespace                         : appstream
StepScalingPolicyConfiguration           : Amazon.ApplicationAutoScaling.Model.StepScalingPolicyConfiguration
TargetTrackingScalingPolicyConfiguration :

Alarms                                   : {Appstream2-LabFleet-default-scale-in-Alarm}
CreationTime                             : 9/3/2019 2:48:15 AM
PolicyARN                                : arn:aws:autoscaling:us-west-2:012345678912:scalingPolicy:5659b069-b5cd-4af1-9f7f-3e956d36233e:resource/appstream/fleet/LabFleet:
                                           policyName/default-scale-in
PolicyName                               : default-scale-in
PolicyType                               : StepScaling
ResourceId                               : fleet/LabFleet
ScalableDimension                        : appstream:fleet:DesiredCapacity
ServiceNamespace                         : appstream
StepScalingPolicyConfiguration           : Amazon.ApplicationAutoScaling.Model.StepScalingPolicyConfiguration
TargetTrackingScalingPolicyConfiguration :
```
+  For API details, see [DescribeScalingPolicies](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-AASScheduledAction`
<a name="application-auto-scaling_DescribeScheduledActions_powershell_topic"></a>

The following code example shows how to use `Get-AASScheduledAction`.

**Tools for PowerShell V5**
**Example 1: This cmdlet lists the actions scheduled for your Auto Scaling group that haven't run or that have not reached their end time. **

```
Get-AASScheduledAction -ServiceNamespace AppStream
```
**Output:**

```
CreationTime         : 12/22/2019 9:25:52 AM
EndTime              : 1/1/0001 12:00:00 AM
ResourceId           : fleet/MyFleet
ScalableDimension    : appstream:fleet:DesiredCapacity
ScalableTargetAction : Amazon.ApplicationAutoScaling.Model.ScalableTargetAction
Schedule             : cron(0 0 8 ? * MON-FRI *)
ScheduledActionARN   : arn:aws:autoscaling:us-west-2:012345678912:scheduledAction:4897ca24-3caa-4bf1-8484-851a089b243c:resource/appstream/fleet/MyFleet:scheduledActionName
                       /WeekDaysFleetScaling
ScheduledActionName  : WeekDaysFleetScaling
ServiceNamespace     : appstream
StartTime            : 1/1/0001 12:00:00 AM
```
+  For API details, see [DescribeScheduledActions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-AASScalableTarget`
<a name="application-auto-scaling_DeregisterScalableTarget_powershell_topic"></a>

The following code example shows how to use `Remove-AASScalableTarget`.

**Tools for PowerShell V5**
**Example 1: This cmdlet deregisters an Application Auto Scaling scalable target.Deregistering a scalable target deletes the scaling policies that are associated with it.**

```
Remove-AASScalableTarget -ResourceId fleet/MyFleet -ScalableDimension appstream:fleet:DesiredCapacity -ServiceNamespace AppStream
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-AASScalableTarget (DeregisterScalableTarget)" on target "fleet/MyFleet".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeregisterScalableTarget](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-AASScalingPolicy`
<a name="application-auto-scaling_DeleteScalingPolicy_powershell_topic"></a>

The following code example shows how to use `Remove-AASScalingPolicy`.

**Tools for PowerShell V5**
**Example 1: This cmdlet deletes the specified scaling policy for an Application Auto Scaling scalable target.**

```
Remove-AASScalingPolicy -ServiceNamespace AppStream -PolicyName "default-scale-out" -ResourceId fleet/Test -ScalableDimension appstream:fleet:DesiredCapacity
```
+  For API details, see [DeleteScalingPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-AASScheduledAction`
<a name="application-auto-scaling_DeleteScheduledAction_powershell_topic"></a>

The following code example shows how to use `Remove-AASScheduledAction`.

**Tools for PowerShell V5**
**Example 1: This cmdlet deletes the specified scheduled action for an Application Auto Scaling scalable target.**

```
Remove-AASScheduledAction -ServiceNamespace AppStream -ScheduledActionName WeekDaysFleetScaling -ResourceId fleet/MyFleet -ScalableDimension appstream:fleet:DesiredCapacity
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-AASScheduledAction (DeleteScheduledAction)" on target "WeekDaysFleetScaling".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteScheduledAction](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Set-AASScalingPolicy`
<a name="application-auto-scaling_PutScalingPolicy_powershell_topic"></a>

The following code example shows how to use `Set-AASScalingPolicy`.

**Tools for PowerShell V5**
**Example 1: This cmdlet creates or updates a policy for an Application Auto Scaling scalable target. Each scalable target is identified by a service namespace, resource ID, and scalable dimension.**

```
Set-AASScalingPolicy -ServiceNamespace AppStream -PolicyName ASFleetScaleInPolicy -PolicyType StepScaling  -ResourceId fleet/MyFleet -ScalableDimension appstream:fleet:DesiredCapacity -StepScalingPolicyConfiguration_AdjustmentType ChangeInCapacity -StepScalingPolicyConfiguration_Cooldown 360 -StepScalingPolicyConfiguration_MetricAggregationType Average -StepScalingPolicyConfiguration_StepAdjustments @{ScalingAdjustment = -1; MetricIntervalUpperBound = 0}
```
**Output:**

```
Alarms    PolicyARN
------    ---------
{}        arn:aws:autoscaling:us-west-2:012345678912:scalingPolicy:4897ca24-3caa-4bf1-8484-851a089b243c:resource/appstream/fleet/MyFleet:policyName/ASFleetScaleInPolicy
```
+  For API details, see [PutScalingPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Set-AASScheduledAction`
<a name="application-auto-scaling_PutScheduledAction_powershell_topic"></a>

The following code example shows how to use `Set-AASScheduledAction`.

**Tools for PowerShell V5**
**Example 1: This cmdlet creates or updates a scheduled action for an Application Auto Scaling scalable target. Each scalable target is identified by a service namespace, resource ID, and scalable dimension.**

```
Set-AASScheduledAction -ServiceNamespace AppStream -ResourceId fleet/MyFleet -Schedule "cron(0 0 8 ? * MON-FRI *)" -ScalableDimension appstream:fleet:DesiredCapacity -ScheduledActionName WeekDaysFleetScaling -ScalableTargetAction_MinCapacity 5 -ScalableTargetAction_MaxCapacity 10
```
+  For API details, see [PutScheduledAction](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
