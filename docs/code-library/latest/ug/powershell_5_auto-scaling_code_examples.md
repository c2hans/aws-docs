---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_5_auto-scaling_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Auto Scaling examples using Tools for PowerShell V5
<a name="powershell_5_auto-scaling_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Auto Scaling.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-ASLoadBalancer`
<a name="auto-scaling_AttachLoadBalancers_powershell_5_topic"></a>

The following code example shows how to use `Add-ASLoadBalancer`.

**Tools for PowerShell V5**
**Example 1: This example attaches the specified load balancer to the specified Auto Scaling group.**

```
Add-ASLoadBalancer -LoadBalancerName my-lb -AutoScalingGroupName my-asg
```
+  For API details, see [AttachLoadBalancers](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Complete-ASLifecycleAction`
<a name="auto-scaling_CompleteLifecycleAction_powershell_5_topic"></a>

The following code example shows how to use `Complete-ASLifecycleAction`.

**Tools for PowerShell V5**
**Example 1: This example completes the specified lifecycle action.**

```
Complete-ASLifecycleAction -LifecycleHookName myLifecycleHook -AutoScalingGroupName my-asg -LifecycleActionResult CONTINUE -LifecycleActionToken bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635
```
+  For API details, see [CompleteLifecycleAction](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Disable-ASMetricsCollection`
<a name="auto-scaling_DisableMetricsCollection_powershell_5_topic"></a>

The following code example shows how to use `Disable-ASMetricsCollection`.

**Tools for PowerShell V5**
**Example 1: This example disables monitoring of the specified metrics for the specified Auto Scaling group.**

```
Disable-ASMetricsCollection -AutoScalingGroupName my-asg -Metric @("GroupMinSize", "GroupMaxSize")
```
**Example 2: This example disables monitoring of all metrics for the specified Auto Scaling group.**

```
Disable-ASMetricsCollection -AutoScalingGroupName my-asg
```
+  For API details, see [DisableMetricsCollection](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Dismount-ASInstance`
<a name="auto-scaling_DetachInstances_powershell_5_topic"></a>

The following code example shows how to use `Dismount-ASInstance`.

**Tools for PowerShell V5**
**Example 1: This example detaches the specified instance from the specified Auto Scaling group and decreases the desired capacity so that Auto Scaling does not launch a replacement instance.**

```
Dismount-ASInstance -InstanceId i-93633f9b -AutoScalingGroupName my-asg -ShouldDecrementDesiredCapacity $true
```
**Output:**

```
ActivityId           : 06733445-ce94-4039-be1b-b9f1866e276e
AutoScalingGroupName : my-asg
Cause                : At 2015-11-20T22:34:59Z instance i-93633f9b was detached in response to a user request, shrinking
                       the capacity from 2 to 1.
Description          : Detaching EC2 instance: i-93633f9b
Details              : {"Availability Zone":"us-west-2b","Subnet ID":"subnet-5264e837"}
EndTime              :
Progress             : 50
StartTime            : 11/20/2015 2:34:59 PM
StatusCode           : InProgress
StatusMessage        :
```
**Example 2: This example detaches the specified instance from the specified Auto Scaling group without decreasing the desired capacity. Auto Scaling launches a replacement instance.**

```
Dismount-ASInstance -InstanceId i-7bf746a2 -AutoScalingGroupName my-asg -ShouldDecrementDesiredCapacity $false
```
**Output:**

```
ActivityId           : f43a3cd4-d38c-4af7-9fe0-d76ec2307b6d
AutoScalingGroupName : my-asg
Cause                : At 2015-11-20T22:34:59Z instance i-7bf746a2 was detached in response to a user request.
Description          : Detaching EC2 instance: i-7bf746a2
Details              : {"Availability Zone":"us-west-2b","Subnet ID":"subnet-5264e837"}
EndTime              :
Progress             : 50
StartTime            : 11/20/2015 2:34:59 PM
StatusCode           : InProgress
StatusMessage        :
```
+  For API details, see [DetachInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Dismount-ASLoadBalancer`
<a name="auto-scaling_DetachLoadBalancers_powershell_5_topic"></a>

The following code example shows how to use `Dismount-ASLoadBalancer`.

**Tools for PowerShell V5**
**Example 1: This example detaches the specified load balancer from the specified Auto Scaling group.**

```
Dismount-ASLoadBalancer -LoadBalancerName my-lb -AutoScalingGroupName my-asg
```
+  For API details, see [DetachLoadBalancers](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Enable-ASMetricsCollection`
<a name="auto-scaling_EnableMetricsCollection_powershell_5_topic"></a>

The following code example shows how to use `Enable-ASMetricsCollection`.

**Tools for PowerShell V5**
**Example 1: This example enables monitoring of the specified metrics for the specified Auto Scaling group.**

```
Enable-ASMetricsCollection  -Metric @("GroupMinSize", "GroupMaxSize") -AutoScalingGroupName my-asg -Granularity 1Minute
```
**Example 2: This example enables monitoring of all metrics for the specified Auto Scaling group.**

```
Enable-ASMetricsCollection -AutoScalingGroupName my-asg -Granularity 1Minute
```
+  For API details, see [EnableMetricsCollection](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Enter-ASStandby`
<a name="auto-scaling_EnterStandby_powershell_5_topic"></a>

The following code example shows how to use `Enter-ASStandby`.

**Tools for PowerShell V5**
**Example 1: This example puts the specified instance into standby mode and decreases the desired capacity so that Auto Scaling does not launch a replacement instance.**

```
Enter-ASStandby -InstanceId i-93633f9b -AutoScalingGroupName my-asg -ShouldDecrementDesiredCapacity $true
```
**Output:**

```
ActivityId           : e36a5a54-ced6-4df8-bd19-708e2a59a649
AutoScalingGroupName : my-asg
Cause                : At 2015-11-22T15:48:06Z instance i-95b8484f was moved to standby in response to a user request,
                       shrinking the capacity from 2 to 1.
Description          : Moving EC2 instance to Standby: i-95b8484f
Details              : {"Availability Zone":"us-west-2b","Subnet ID":"subnet-5264e837"}
EndTime              :
Progress             : 50
StartTime            : 11/22/2015 7:48:06 AM
StatusCode           : InProgress
StatusMessage        :
```
**Example 2: This example puts the specified instance into standby mode without decreasing the desired capacity. Auto Scaling launches a replacement instance.**

```
Enter-ASStandby -InstanceId i-93633f9b -AutoScalingGroupName my-asg -ShouldDecrementDesiredCapacity $false
```
**Output:**

```
ActivityId           : e36a5a54-ced6-4df8-bd19-708e2a59a649
AutoScalingGroupName : my-asg
Cause                : At 2015-11-22T15:48:06Z instance i-95b8484f was moved to standby in response to a user request.
Description          : Moving EC2 instance to Standby: i-95b8484f
Details              : {"Availability Zone":"us-west-2b","Subnet ID":"subnet-5264e837"}
EndTime              :
Progress             : 50
StartTime            : 11/22/2015 7:48:06 AM
StatusCode           : InProgress
StatusMessage        :
```
+  For API details, see [EnterStandby](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Exit-ASStandby`
<a name="auto-scaling_ExitStandby_powershell_5_topic"></a>

The following code example shows how to use `Exit-ASStandby`.

**Tools for PowerShell V5**
**Example 1: This example moves the specified instance out of standby mode.**

```
Exit-ASStandby -InstanceId i-93633f9b -AutoScalingGroupName my-asg
```
**Output:**

```
ActivityId           : 1833d3e8-e32f-454e-b731-0670ad4c6934
AutoScalingGroupName : my-asg
Cause                : At 2015-11-22T15:51:21Z instance i-95b8484f was moved out of standby in response to a user
                       request, increasing the capacity from 1 to 2.
Description          : Moving EC2 instance out of Standby: i-95b8484f
Details              : {"Availability Zone":"us-west-2b","Subnet ID":"subnet-5264e837"}
EndTime              :
Progress             : 30
StartTime            : 11/22/2015 7:51:21 AM
StatusCode           : PreInService
StatusMessage        :
```
+  For API details, see [ExitStandby](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASAccountLimit`
<a name="auto-scaling_DescribeAccountLimits_powershell_5_topic"></a>

The following code example shows how to use `Get-ASAccountLimit`.

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

### `Get-ASAdjustmentType`
<a name="auto-scaling_DescribeAdjustmentTypes_powershell_5_topic"></a>

The following code example shows how to use `Get-ASAdjustmentType`.

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

### `Get-ASAutoScalingGroup`
<a name="auto-scaling_DescribeAutoScalingGroups_powershell_5_topic"></a>

The following code example shows how to use `Get-ASAutoScalingGroup`.

**Tools for PowerShell V5**
**Example 1: This example lists the names of your Auto Scaling groups.**

```
Get-ASAutoScalingGroup | format-table -property AutoScalingGroupName
```
**Output:**

```
AutoScalingGroupName
--------------------
my-asg-1
my-asg-2
my-asg-3
my-asg-4
my-asg-5
my-asg-6
```
**Example 2: This example describes the specified Auto Scaling group.**

```
Get-ASAutoScalingGroup -AutoScalingGroupName my-asg-1
```
**Output:**

```
AutoScalingGroupARN     : arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:930d940e-891e-4781-a11a-7b0acd480
                          f03:autoScalingGroupName/my-asg-1
AutoScalingGroupName    : my-asg-1
AvailabilityZones       : {us-west-2b, us-west-2a}
CreatedTime             : 3/1/2015 9:05:31 AM
DefaultCooldown         : 300
DesiredCapacity         : 2
EnabledMetrics          : {}
HealthCheckGracePeriod  : 300
HealthCheckType         : EC2
Instances               : {my-lc}
LaunchConfigurationName : my-lc
LoadBalancerNames       : {}
MaxSize                 : 0
MinSize                 : 0
PlacementGroup          :
Status                  :
SuspendedProcesses      : {}
Tags                    : {}
TerminationPolicies     : {Default}
VPCZoneIdentifier       : subnet-e4f33493,subnet-5264e837
```
**Example 3: This example describes the specified two Auto Scaling groups.**

```
Get-ASAutoScalingGroup -AutoScalingGroupName @("my-asg-1", "my-asg-2")
```
**Example 4: This example describes the Auto Scaling instances for the specified Auto Scaling group.**

```
(Get-ASAutoScalingGroup -AutoScalingGroupName my-asg-1).Instances
```
**Example 5: This example describes all your Auto Scaling groups.**

```
Get-ASAutoScalingGroup
```
**Example 6: This example describes LaunchTemplate for the specified Auto Scaling group. This example assumes that the "Instance purchase options" is set to "Adhere to launch template". In case this option is set to "Combine purchase options and instance types", LaunchTemplate could be accessed using "MixedInstancesPolicy.LaunchTemplate" property.**

```
(Get-ASAutoScalingGroup -AutoScalingGroupName my-ag-1).LaunchTemplate
```
**Output:**

```
LaunchTemplateId     LaunchTemplateName   Version
----------------     ------------------   -------
lt-06095fd619cb40371 test-launch-template $Default
```
+  For API details, see [DescribeAutoScalingGroups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASAutoScalingInstance`
<a name="auto-scaling_DescribeAutoScalingInstances_powershell_5_topic"></a>

The following code example shows how to use `Get-ASAutoScalingInstance`.

**Tools for PowerShell V5**
**Example 1: This example lists the IDs of your Auto Scaling instances.**

```
Get-ASAutoScalingInstance | format-table -property InstanceId
```
**Output:**

```
InstanceId
----------
i-12345678
i-87654321
i-abcd1234
```
**Example 2: This example describes the specified Auto Scaling instance.**

```
Get-ASAutoScalingInstance -InstanceId i-12345678
```
**Output:**

```
AutoScalingGroupName    : my-asg
AvailabilityZone        : us-west-2b
HealthStatus            : HEALTHY
InstanceId              : i-12345678
LaunchConfigurationName : my-lc
LifecycleState          : InService
```
**Example 3: This example describes the specified two Auto Scaling instances.**

```
Get-ASAutoScalingInstance -InstanceId @("i-12345678", "i-87654321")
```
**Example 4: This example describes the Auto Scaling instances for the specified Auto Scaling group.**

```
(Get-ASAutoScalingGroup -AutoScalingGroupName my-asg).Instances | Get-ASAutoScalingInstance
```
**Example 5: This example describes all your Auto Scaling instances.**

```
Get-ASAutoScalingInstance
```
+  For API details, see [DescribeAutoScalingInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASAutoScalingNotificationType`
<a name="auto-scaling_DescribeAutoScalingNotificationTypes_powershell_5_topic"></a>

The following code example shows how to use `Get-ASAutoScalingNotificationType`.

**Tools for PowerShell V5**
**Example 1: This example lists the notification types that are supported by Auto Scaling.**

```
Get-ASAutoScalingNotificationType
```
**Output:**

```
autoscaling:EC2_INSTANCE_LAUNCH
autoscaling:EC2_INSTANCE_LAUNCH_ERROR
autoscaling:EC2_INSTANCE_TERMINATE
autoscaling:EC2_INSTANCE_TERMINATE_ERROR
autoscaling:TEST_NOTIFICATION
```
+  For API details, see [DescribeAutoScalingNotificationTypes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASLaunchConfiguration`
<a name="auto-scaling_DescribeLaunchConfigurations_powershell_5_topic"></a>

The following code example shows how to use `Get-ASLaunchConfiguration`.

**Tools for PowerShell V5**
**Example 1: This example lists the names of your launch configurations.**

```
Get-ASLaunchConfiguration | format-table -property LaunchConfigurationName
```
**Output:**

```
LaunchConfigurationName
-----------------------
my-lc-1
my-lc-2
my-lc-3
my-lc-4
my-lc-5
```
**Example 2: This example describes the specified launch configuration.**

```
Get-ASLaunchConfiguration -LaunchConfigurationName my-lc-1
```
**Output:**

```
AssociatePublicIpAddress     : True
BlockDeviceMappings          : {/dev/xvda}
ClassicLinkVPCId             :
ClassicLinkVPCSecurityGroups : {}
CreatedTime                  : 12/12/2014 3:22:08 PM
EbsOptimized                 : False
IamInstanceProfile           :
ImageId                      : ami-043a5034
InstanceMonitoring           : Amazon.AutoScaling.Model.InstanceMonitoring
InstanceType                 : t2.micro
KernelId                     :
KeyName                      :
LaunchConfigurationARN       : arn:aws:autoscaling:us-west-2:123456789012:launchConfiguration:7e5f31e4-693b-4604-9322-
                               e6f68d7fafad:launchConfigurationName/my-lc-1
LaunchConfigurationName      : my-lc-1
PlacementTenancy             :
RamdiskId                    :
SecurityGroups               : {sg-67ef0308}
SpotPrice                    :
UserData                     :
```
**Example 3: This example describes the specified two launch configurations.**

```
Get-ASLaunchConfiguration -LaunchConfigurationName @("my-lc-1", "my-lc-2")
```
**Example 4: This example describes all your launch configurations.**

```
Get-ASLaunchConfiguration
```
+  For API details, see [DescribeLaunchConfigurations](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASLifecycleHook`
<a name="auto-scaling_DescribeLifecycleHooks_powershell_5_topic"></a>

The following code example shows how to use `Get-ASLifecycleHook`.

**Tools for PowerShell V5**
**Example 1: This example describes the specified lifecycle hook.**

```
Get-ASLifecycleHook -AutoScalingGroupName my-asg -LifecycleHookName myLifecycleHook
```
**Output:**

```
AutoScalingGroupName  : my-asg
DefaultResult         : ABANDON
GlobalTimeout         : 172800
HeartbeatTimeout      : 3600
LifecycleHookName     : myLifecycleHook
LifecycleTransition   : auto-scaling:EC2_INSTANCE_LAUNCHING
NotificationMetadata  :
NotificationTargetARN : arn:aws:sns:us-west-2:123456789012:my-topic
RoleARN               : arn:aws:iam::123456789012:role/my-iam-role
```
**Example 2: This example describes all lifecycle hooks for the specified Auto Scaling group.**

```
Get-ASLifecycleHook -AutoScalingGroupName my-asg
```
**Example 3: This example describes all lifecycle hooks for all your Auto Scaling groups.**

```
Get-ASLifecycleHook
```
+  For API details, see [DescribeLifecycleHooks](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASLifecycleHookType`
<a name="auto-scaling_DescribeLifecycleHookTypes_powershell_5_topic"></a>

The following code example shows how to use `Get-ASLifecycleHookType`.

**Tools for PowerShell V5**
**Example 1: This example lists the lifecycle hook types supported by Auto Scaling.**

```
Get-ASLifecycleHookType
```
**Output:**

```
autoscaling:EC2_INSTANCE_LAUNCHING
auto-scaling:EC2_INSTANCE_TERMINATING
```
+  For API details, see [DescribeLifecycleHookTypes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASLoadBalancer`
<a name="auto-scaling_DescribeLoadBalancers_powershell_5_topic"></a>

The following code example shows how to use `Get-ASLoadBalancer`.

**Tools for PowerShell V5**
**Example 1: This example describes the load balancers for the specified Auto Scaling group.**

```
Get-ASLoadBalancer -AutoScalingGroupName my-asg
```
**Output:**

```
LoadBalancerName    State
----------------    -----
my-lb               Added
```
+  For API details, see [DescribeLoadBalancers](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASMetricCollectionType`
<a name="auto-scaling_DescribeMetricCollectionTypes_powershell_5_topic"></a>

The following code example shows how to use `Get-ASMetricCollectionType`.

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

### `Get-ASNotificationConfiguration`
<a name="auto-scaling_DescribeNotificationConfigurations_powershell_5_topic"></a>

The following code example shows how to use `Get-ASNotificationConfiguration`.

**Tools for PowerShell V5**
**Example 1: This example describes the notification actions associated with the specified Auto Scaling group.**

```
Get-ASNotificationConfiguration -AutoScalingGroupName my-asg | format-list
```
**Output:**

```
AutoScalingGroupName : my-asg
NotificationType     : auto-scaling:EC2_INSTANCE_LAUNCH
TopicARN             : arn:aws:sns:us-west-2:123456789012:my-topic

AutoScalingGroupName : my-asg
NotificationType     : auto-scaling:EC2_INSTANCE_TERMINATE
TopicARN             : arn:aws:sns:us-west-2:123456789012:my-topic
```
**Example 2: This example describes the notification actions associated with all your Auto Scaling groups.**

```
Get-ASNotificationConfiguration
```
+  For API details, see [DescribeNotificationConfigurations](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASPolicy`
<a name="auto-scaling_DescribePolicies_powershell_5_topic"></a>

The following code example shows how to use `Get-ASPolicy`.

**Tools for PowerShell V5**
**Example 1: This example describes all policies for the specified Auto Scaling group.**

```
Get-ASPolicy -AutoScalingGroupName my-asg
```
**Output:**

```
AdjustmentType          : ChangeInCapacity
Alarms                  : {}
AutoScalingGroupName    : my-asg
Cooldown                : 0
EstimatedInstanceWarmup : 0
MetricAggregationType   :
MinAdjustmentMagnitude  : 0
MinAdjustmentStep       : 0
PolicyARN               : arn:aws:auto-scaling:us-west-2:123456789012:scalingPolicy:aa3836ab-5462-42c7-adab-e1d769fc24ef
                          :autoScalingGroupName/my-asg:policyName/myScaleInPolicy
PolicyName              : myScaleInPolicy
PolicyType              : SimpleScaling
ScalingAdjustment       : -1
StepAdjustments         : {}
```
**Example 2: This example describes the specified policies for the specified Auto Scaling group.**

```
Get-ASPolicy -AutoScalingGroupName my-asg -PolicyName @("myScaleOutPolicy", "myScaleInPolicy")
```
**Example 3: This example describes all policies for all your Auto Scaling groups.**

```
Get-ASPolicy
```
+  For API details, see [DescribePolicies](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASScalingActivity`
<a name="auto-scaling_DescribeScalingActivities_powershell_5_topic"></a>

The following code example shows how to use `Get-ASScalingActivity`.

**Tools for PowerShell V5**
**Example 1: This example describes the scaling activities for the last six weeks for the specified Auto Scaling group.**

```
Get-ASScalingActivity -AutoScalingGroupName my-asg
```
**Output:**

```
ActivityId           : 063308ae-aa22-4a9b-94f4-9fae4EXAMPLE
AutoScalingGroupName : my-asg
Cause                : At 2015-11-22T15:45:16Z a user request explicitly set group desired capacity changing the desired
                       capacity from 1 to 2.  At 2015-11-22T15:45:34Z an instance was started in response to a difference
                       between desired and actual capacity, increasing the capacity from 1 to 2.
Description          : Launching a new EC2 instance: i-26e715fc
Details              : {"Availability Zone":"us-west-2b","Subnet ID":"subnet-5264e837"}
EndTime              : 11/22/2015 7:46:09 AM
Progress             : 100
StartTime            : 11/22/2015 7:45:35 AM
StatusCode           : Successful
StatusMessage        :

ActivityId           : ce719997-086d-4c73-a2f1-ab703EXAMPLE
AutoScalingGroupName : my-asg
Cause                : At 2015-11-20T22:57:53Z a user request created an AutoScalingGroup changing the desired capacity
                        from 0 to 1.  At 2015-11-20T22:57:58Z an instance was started in response to a difference betwe
                       en desired and actual capacity, increasing the capacity from 0 to 1.
Description          : Launching a new EC2 instance: i-93633f9b
Details              : {"Availability Zone":"us-west-2b","Subnet ID":"subnet-5264e837"}
EndTime              : 11/20/2015 2:58:32 PM
Progress             : 100
StartTime            : 11/20/2015 2:57:59 PM
StatusCode           : Successful
StatusMessage        :
```
**Example 2: This example describes the specified scaling activity.**

```
Get-ASScalingActivity -ActivityId "063308ae-aa22-4a9b-94f4-9fae4EXAMPLE"
```
**Example 3: This example describes the scaling activities for the last six weeks for all your Auto Scaling groups.**

```
Get-ASScalingActivity
```
+  For API details, see [DescribeScalingActivities](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASScalingProcessType`
<a name="auto-scaling_DescribeScalingProcessTypes_powershell_5_topic"></a>

The following code example shows how to use `Get-ASScalingProcessType`.

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

### `Get-ASScheduledAction`
<a name="auto-scaling_DescribeScheduledActions_powershell_5_topic"></a>

The following code example shows how to use `Get-ASScheduledAction`.

**Tools for PowerShell V5**
**Example 1: This example describes the scheduled scaling actions for the specified Auto Scaling group.**

```
Get-ASScheduledAction -AutoScalingGroupName my-asg
```
**Output:**

```
AutoScalingGroupName : my-asg
DesiredCapacity      : 10
EndTime              :
MaxSize              :
MinSize              :
Recurrence           :
ScheduledActionARN   : arn:aws:autoscaling:us-west-2:123456789012:scheduledUpdateGroupAction:8a4c5f24-6ec6-4306-a2dd-f7
                       2c3af3a4d6:autoScalingGroupName/my-asg:scheduledActionName/myScheduledAction
ScheduledActionName  : myScheduledAction
StartTime            : 11/30/2015 8:00:00 AM
Time                 : 11/30/2015 8:00:00 AM
```
**Example 2: This example describes the specified scheduled scaling actions.**

```
Get-ASScheduledAction -ScheduledActionName @("myScheduledScaleOut", "myScheduledScaleIn")
```
**Example 3: This example describes the scheduled scaling actions that start by the specified time.**

```
Get-ASScheduledAction -StartTime "2015-12-01T08:00:00Z"
```
**Example 4: This example describes the scheduled scaling actions that end by the specified time.**

```
Get-ASScheduledAction -EndTime "2015-12-30T08:00:00Z"
```
**Example 5: This example describes the scheduled scaling actions for all your Auto Scaling groups.**

```
Get-ASScheduledAction
```
+  For API details, see [DescribeScheduledActions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASTag`
<a name="auto-scaling_DescribeTags_powershell_5_topic"></a>

The following code example shows how to use `Get-ASTag`.

**Tools for PowerShell V5**
**Example 1: This example describes the tags with a key value of either 'myTag' or 'myTag2'. The possible values for the filter name are 'auto-scaling-group', 'key', 'value', and 'propagate-at-launch'. The syntax used by this example requires PowerShell version 3 or later.**

```
Get-ASTag -Filter @( @{ Name="key"; Values=@("myTag", "myTag2") } )
```
**Output:**

```
Key               : myTag2
PropagateAtLaunch : True
ResourceId        : my-asg
ResourceType      : auto-scaling-group
Value             : myTagValue2

Key               : myTag
PropagateAtLaunch : True
ResourceId        : my-asg
ResourceType      : auto-scaling-group
Value             : myTagValue
```
**Example 2: With PowerShell version 2, you must use New-Object to create the filter for the Filter parameter.**

```
$keys = New-Object string[] 2
$keys[0] = "myTag"
$keys[1] = "myTag2"
$filter = New-Object Amazon.AutoScaling.Model.Filter
$filter.Name = "key"
$filter.Values = $keys
Get-ASTag -Filter @( $filter )
```
**Example 3: This example describes all tags for all your Auto Scaling groups.**

```
Get-ASTag
```
+  For API details, see [DescribeTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASTerminationPolicyType`
<a name="auto-scaling_DescribeTerminationPolicyTypes_powershell_5_topic"></a>

The following code example shows how to use `Get-ASTerminationPolicyType`.

**Tools for PowerShell V5**
**Example 1: This example lists the termination policies that are supported by Auto Scaling.**

```
Get-ASTerminationPolicyType
```
**Output:**

```
ClosestToNextInstanceHour
Default
NewestInstance
OldestInstance
OldestLaunchConfiguration
```
+  For API details, see [DescribeTerminationPolicyTypes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Mount-ASInstance`
<a name="auto-scaling_AttachInstances_powershell_5_topic"></a>

The following code example shows how to use `Mount-ASInstance`.

**Tools for PowerShell V5**
**Example 1: This example attaches the specified instance to the specified Auto Scaling group. Auto Scaling automatically increases the desired capacity of the Auto Scaling group.**

```
Mount-ASInstance -InstanceId i-93633f9b -AutoScalingGroupName my-asg
```
+  For API details, see [AttachInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-ASAutoScalingGroup`
<a name="auto-scaling_CreateAutoScalingGroup_powershell_5_topic"></a>

The following code example shows how to use `New-ASAutoScalingGroup`.

**Tools for PowerShell V5**
**Example 1: This example creates an Auto Scaling group with the specified name and attributes. The default desired capacity is the minimum size. Therefore, this Auto Scaling group launches two instances, one in each of the specified two Availability Zones.**

```
New-ASAutoScalingGroup -AutoScalingGroupName my-asg -LaunchConfigurationName my-lc -MinSize 2 -MaxSize 6 -AvailabilityZone @("us-west-2a", "us-west-2b")
```
+  For API details, see [CreateAutoScalingGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-ASLaunchConfiguration`
<a name="auto-scaling_CreateLaunchConfiguration_powershell_5_topic"></a>

The following code example shows how to use `New-ASLaunchConfiguration`.

**Tools for PowerShell V5**
**Example 1: This example creates a launch configuration named 'my-lc'. The EC2 instances launched by Auto Scaling groups that use this launch configuration use specified instance type, AMI, security group, and IAM role.**

```
New-ASLaunchConfiguration -LaunchConfigurationName my-lc -InstanceType "m3.medium" -ImageId "ami-12345678" -SecurityGroup "sg-12345678" -IamInstanceProfile "myIamRole"
```
+  For API details, see [CreateLaunchConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ASAutoScalingGroup`
<a name="auto-scaling_DeleteAutoScalingGroup_powershell_5_topic"></a>

The following code example shows how to use `Remove-ASAutoScalingGroup`.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified Auto Scaling group if it has no running instances. You are prompted for confirmation before the operation proceeds.**

```
Remove-ASAutoScalingGroup -AutoScalingGroupName my-asg
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ASAutoScalingGroup (DeleteAutoScalingGroup)" on Target "my-asg".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASAutoScalingGroup -AutoScalingGroupName my-asg -Force
```
**Example 3: This example deletes the specified Auto Scaling group and terminates any running instances that it contains.**

```
Remove-ASAutoScalingGroup -AutoScalingGroupName my-asg -ForceDelete $true -Force
```
+  For API details, see [DeleteAutoScalingGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ASLaunchConfiguration`
<a name="auto-scaling_DeleteLaunchConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Remove-ASLaunchConfiguration`.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified launch configuration if it is not attached to an Auto Scaling group. You are prompted for confirmation before the operation proceeds.**

```
Remove-ASLaunchConfiguration -LaunchConfigurationName my-lc
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ASLaunchConfiguration (DeleteLaunchConfiguration)" on Target "my-lc".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASLaunchConfiguration -LaunchConfigurationName my-lc -Force
```
+  For API details, see [DeleteLaunchConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ASLifecycleHook`
<a name="auto-scaling_DeleteLifecycleHook_powershell_5_topic"></a>

The following code example shows how to use `Remove-ASLifecycleHook`.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified lifecycle hook for the specified Auto Scaling group. You are prompted for confirmation before the operation proceeds.**

```
Remove-ASLifecycleHook -AutoScalingGroupName my-asg -LifecycleHookName myLifecycleHook
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ASLifecycleHook (DeleteLifecycleHook)" on Target "myLifecycleHook".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASLifecycleHook -AutoScalingGroupName my-asg -LifecycleHookName myLifecycleHook -Force
```
+  For API details, see [DeleteLifecycleHook](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ASNotificationConfiguration`
<a name="auto-scaling_DeleteNotificationConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Remove-ASNotificationConfiguration`.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified notification action. You are prompted for confirmation before the operation proceeds.**

```
Remove-ASNotificationConfiguration -AutoScalingGroupName my-asg -TopicARN "arn:aws:sns:us-west-2:123456789012:my-topic"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ASNotificationConfiguration (DeleteNotificationConfiguration)" on Target
"arn:aws:sns:us-west-2:123456789012:my-topic".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASNotificationConfiguration -AutoScalingGroupName my-asg -TopicARN "arn:aws:sns:us-west-2:123456789012:my-topic" -Force
```
+  For API details, see [DeleteNotificationConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ASPolicy`
<a name="auto-scaling_DeletePolicy_powershell_5_topic"></a>

The following code example shows how to use `Remove-ASPolicy`.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified policy for the specified Auto Scaling group. You are prompted for confirmation before the operation proceeds.**

```
Remove-ASPolicy -AutoScalingGroupName my-asg -PolicyName myScaleInPolicy
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ASPolicy (DeletePolicy)" on Target "myScaleInPolicy".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASPolicy -AutoScalingGroupName my-asg -PolicyName myScaleInPolicy -Force
```
+  For API details, see [DeletePolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ASScheduledAction`
<a name="auto-scaling_DeleteScheduledAction_powershell_5_topic"></a>

The following code example shows how to use `Remove-ASScheduledAction`.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified scheduled action for the specified Auto Scaling group. You are prompted for confirmation before the operation proceeds.**

```
Remove-ASScheduledAction -AutoScalingGroupName my-asg -ScheduledAction "myScheduledAction"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ASScheduledAction (DeleteScheduledAction)" on Target "myScheduledAction".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASScheduledAction -AutoScalingGroupName my-asg -ScheduledAction "myScheduledAction" -Force
```
+  For API details, see [DeleteScheduledAction](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ASTag`
<a name="auto-scaling_DeleteTags_powershell_5_topic"></a>

The following code example shows how to use `Remove-ASTag`.

**Tools for PowerShell V5**
**Example 1: This example removes the specified tag from the specified Auto Scaling group. You are prompted for confirmation before the operation proceeds. The syntax used by this example requires PowerShell version 3 or later.**

```
Remove-ASTag -Tag @( @{ResourceType="auto-scaling-group"; ResourceId="my-asg"; Key="myTag" } )
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-ASTag (DeleteTags)" on target "Amazon.AutoScaling.Model.Tag".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASTag -Tag @( @{ResourceType="auto-scaling-group"; ResourceId="my-asg"; Key="myTag" } ) -Force
```
**Example 3: With Powershell version 2, you must use New-Object to create the tag for the Tag parameter.**

```
$tag = New-Object Amazon.AutoScaling.Model.Tag
$tag.ResourceType = "auto-scaling-group"
$tag.ResourceId = "my-asg"
$tag.Key = "myTag"
Remove-ASTag -Tag $tag -Force
```
+  For API details, see [DeleteTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Resume-ASProcess`
<a name="auto-scaling_ResumeProcesses_powershell_5_topic"></a>

The following code example shows how to use `Resume-ASProcess`.

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

### `Set-ASDesiredCapacity`
<a name="auto-scaling_SetDesiredCapacity_powershell_5_topic"></a>

The following code example shows how to use `Set-ASDesiredCapacity`.

**Tools for PowerShell V5**
**Example 1: This example sets the size of the specified Auto Scaling group.**

```
Set-ASDesiredCapacity -AutoScalingGroupName my-asg -DesiredCapacity 2
```
**Example 2: This example sets the size of the specified Auto Scaling group and waits for the cooldown period to complete before scaling to the new size.**

```
Set-ASDesiredCapacity -AutoScalingGroupName my-asg -DesiredCapacity 2 -HonorCooldown $true
```
+  For API details, see [SetDesiredCapacity](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Set-ASInstanceHealth`
<a name="auto-scaling_SetInstanceHealth_powershell_5_topic"></a>

The following code example shows how to use `Set-ASInstanceHealth`.

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

### `Set-ASInstanceProtection`
<a name="auto-scaling_SetInstanceProtection_powershell_5_topic"></a>

The following code example shows how to use `Set-ASInstanceProtection`.

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

### `Set-ASTag`
<a name="auto-scaling_CreateOrUpdateTags_powershell_5_topic"></a>

The following code example shows how to use `Set-ASTag`.

**Tools for PowerShell V5**
**Example 1: This example adds a single tag to the specified Auto Scaling group. The tag key is 'myTag' and the tag value is 'myTagValue'. Auto Scaling propagates this tag to the subsequent EC2 instances launched by the Auto Scaling group. The syntax used by this example requires PowerShell version 3 or later.**

```
Set-ASTag -Tag @( @{ResourceType="auto-scaling-group"; ResourceId="my-asg"; Key="myTag"; Value="myTagValue"; PropagateAtLaunch=$true} )
```
**Example 2: With PowerShell version 2, you must use New-Object to create the tag for the Tag parameter.**

```
$tag = New-Object Amazon.AutoScaling.Model.Tag
$tag.ResourceType = "auto-scaling-group"
$tag.ResourceId = "my-asg"
$tag.Key = "myTag"
$tag.Value = "myTagValue"
$tag.PropagateAtLaunch = $true
Set-ASTag -Tag $tag
```
+  For API details, see [CreateOrUpdateTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Start-ASPolicy`
<a name="auto-scaling_ExecutePolicy_powershell_5_topic"></a>

The following code example shows how to use `Start-ASPolicy`.

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

### `Stop-ASInstanceInAutoScalingGroup`
<a name="auto-scaling_TerminateInstanceInAutoScalingGroup_powershell_5_topic"></a>

The following code example shows how to use `Stop-ASInstanceInAutoScalingGroup`.

**Tools for PowerShell V5**
**Example 1: This example terminates the specified instance and decreases the desired capacity of its Auto Scaling group so that Auto Scaling does not launch a replacement instance.**

```
Stop-ASInstanceInAutoScalingGroup -InstanceId i-93633f9b -ShouldDecrementDesiredCapacity $true
```
**Output:**

```
ActivityId           : 2e40d9bd-1902-444c-abf3-6ea0002efdc5
AutoScalingGroupName :
Cause                : At 2015-11-22T16:09:03Z instance i-93633f9b was taken out of service in response to a user
                       request, shrinking the capacity from 2 to 1.
Description          : Terminating EC2 instance: i-93633f9b
Details              : {"Availability Zone":"us-west-2b","Subnet ID":"subnet-5264e837"}
EndTime              :
Progress             : 0
StartTime            : 11/22/2015 8:09:03 AM
StatusCode           : InProgress
StatusMessage        :
```
**Example 2: This example terminates the specified instance without decreasing the desired capacity of its Auto Scaling group. Auto Scaling launches a replacement instance.**

```
Stop-ASInstanceInAutoScalingGroup -InstanceId i-93633f9b -ShouldDecrementDesiredCapacity $false
```
**Output:**

```
ActivityId           : 2e40d9bd-1902-444c-abf3-6ea0002efdc5
AutoScalingGroupName :
Cause                : At 2015-11-22T16:09:03Z instance i-93633f9b was taken out of service in response to a user
                       request.
Description          : Terminating EC2 instance: i-93633f9b
Details              : {"Availability Zone":"us-west-2b","Subnet ID":"subnet-5264e837"}
EndTime              :
Progress             : 0
StartTime            : 11/22/2015 8:09:03 AM
StatusCode           : InProgress
StatusMessage        :
```
+  For API details, see [TerminateInstanceInAutoScalingGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Suspend-ASProcess`
<a name="auto-scaling_SuspendProcesses_powershell_5_topic"></a>

The following code example shows how to use `Suspend-ASProcess`.

**Tools for PowerShell V5**
**Example 1: This example suspends the specified Auto Scaling process for the specified Auto Scaling group.**

```
Suspend-ASProcess -AutoScalingGroupName my-asg -ScalingProcess "AlarmNotification"
```
**Example 2: This example suspends all Auto Scaling processes for the specified Auto Scaling group.**

```
Suspend-ASProcess -AutoScalingGroupName my-asg
```
+  For API details, see [SuspendProcesses](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-ASAutoScalingGroup`
<a name="auto-scaling_UpdateAutoScalingGroup_powershell_5_topic"></a>

The following code example shows how to use `Update-ASAutoScalingGroup`.

**Tools for PowerShell V5**
**Example 1: This example updates the minimum and maximum size of the specified Auto Scaling group.**

```
Update-ASAutoScalingGroup -AutoScalingGroupName my-asg -MaxSize 5 -MinSize 1
```
**Example 2: This example updates the default cooldown period of the specified Auto Scaling group.**

```
Update-ASAutoScalingGroup -AutoScalingGroupName my-asg -DefaultCooldown 10
```
**Example 3: This example updates the Availability Zones of the specified Auto Scaling group.**

```
Update-ASAutoScalingGroup -AutoScalingGroupName my-asg -AvailabilityZone @("us-west-2a", "us-west-2b")
```
**Example 4: This example updates the specified Auto Scaling group to use Elastic Load Balancing health checks.**

```
Update-ASAutoScalingGroup -AutoScalingGroupName my-asg -HealthCheckType ELB -HealthCheckGracePeriod 60
```
+  For API details, see [UpdateAutoScalingGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-ASLifecycleActionHeartbeat`
<a name="auto-scaling_RecordLifecycleActionHeartbeat_powershell_5_topic"></a>

The following code example shows how to use `Write-ASLifecycleActionHeartbeat`.

**Tools for PowerShell V5**
**Example 1: This example records a heartbeat for the specified lifecycle action. This keeps the instance in a pending state until you complete the custom action.**

```
Write-ASLifecycleActionHeartbeat -AutoScalingGroupName my-asg -LifecycleHookName myLifecycleHook -LifecycleActionToken bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635
```
+  For API details, see [RecordLifecycleActionHeartbeat](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-ASLifecycleHook`
<a name="auto-scaling_PutLifecycleHook_powershell_5_topic"></a>

The following code example shows how to use `Write-ASLifecycleHook`.

**Tools for PowerShell V5**
**Example 1: This example adds the specified lifecycle hook to the specified Auto Scaling group.**

```
Write-ASLifecycleHook -AutoScalingGroupName my-asg -LifecycleHookName "myLifecycleHook" -LifecycleTransition "autoscaling:EC2_INSTANCE_LAUNCHING" -NotificationTargetARN "arn:aws:sns:us-west-2:123456789012:my-sns-topic" -RoleARN "arn:aws:iam::123456789012:role/my-iam-role"
```
+  For API details, see [PutLifecycleHook](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-ASNotificationConfiguration`
<a name="auto-scaling_PutNotificationConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Write-ASNotificationConfiguration`.

**Tools for PowerShell V5**
**Example 1: This example configures the specified Auto Scaling group to send a notification to the specified SNS topic when it launches EC2 instances.**

```
Write-ASNotificationConfiguration -AutoScalingGroupName my-asg -NotificationType "autoscaling:EC2_INSTANCE_LAUNCH" -TopicARN "arn:aws:sns:us-west-2:123456789012:my-topic"
```
**Example 2: This example configures the specified Auto Scaling group to send a notification to the specified SNS topic when it launches or terminates EC2 instances.**

```
Write-ASNotificationConfiguration -AutoScalingGroupName my-asg -NotificationType @("autoscaling:EC2_INSTANCE_LAUNCH", "autoscaling:EC2_INSTANCE_TERMINATE") -TopicARN "arn:aws:sns:us-west-2:123456789012:my-topic"
```
+  For API details, see [PutNotificationConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-ASScalingPolicy`
<a name="auto-scaling_PutScalingPolicy_powershell_5_topic"></a>

The following code example shows how to use `Write-ASScalingPolicy`.

**Tools for PowerShell V5**
**Example 1: This example adds the specified policy to the specified Auto Scaling group. The specified adjustment type determines how to interpret the ScalingAdjustment parameter. With 'ChangeInCapacity', a positive value increases the capacity by the specified number of instances and a negative value decreases the capacity by the specified number of instances.**

```
Write-ASScalingPolicy -AutoScalingGroupName my-asg -AdjustmentType "ChangeInCapacity" -PolicyName "myScaleInPolicy" -ScalingAdjustment -1
```
**Output:**

```
arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:aa3836ab-5462-42c7-adab-e1d769fc24ef:autoScalingGroupName/my-asg
:policyName/myScaleInPolicy
```
+  For API details, see [PutScalingPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-ASScheduledUpdateGroupAction`
<a name="auto-scaling_PutScheduledUpdateGroupAction_powershell_5_topic"></a>

The following code example shows how to use `Write-ASScheduledUpdateGroupAction`.

**Tools for PowerShell V5**
**Example 1: This example creates or updates a one-time scheduled action to change the desired capacity at the specified start time.**

```
Write-ASScheduledUpdateGroupAction -AutoScalingGroupName my-asg -ScheduledActionName "myScheduledAction" -StartTime "2015-12-01T00:00:00Z" -DesiredCapacity 10
```
+  For API details, see [PutScheduledUpdateGroupAction](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
