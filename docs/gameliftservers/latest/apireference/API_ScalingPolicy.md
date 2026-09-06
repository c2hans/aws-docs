---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ScalingPolicy.html
---

# ScalingPolicy
<a name="API_ScalingPolicy"></a>

Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.

## Contents
<a name="API_ScalingPolicy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ComparisonOperator **   <a name="gameliftservers-Type-ScalingPolicy-ComparisonOperator"></a>
Comparison operator to use when measuring a metric against the threshold value.
Type: String
Valid Values: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold`
Required: No

 ** EvaluationPeriods **   <a name="gameliftservers-Type-ScalingPolicy-EvaluationPeriods"></a>
Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** FleetArn **   <a name="gameliftservers-Type-ScalingPolicy-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** FleetId **   <a name="gameliftservers-Type-ScalingPolicy-FleetId"></a>
A unique identifier for the fleet that is associated with this scaling policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`
Required: No

 ** Location **   <a name="gameliftservers-Type-ScalingPolicy-Location"></a>
 The fleet location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** MetricName **   <a name="gameliftservers-Type-ScalingPolicy-MetricName"></a>
Name of the Amazon GameLift Servers-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see [Monitor Amazon GameLift Servers with Amazon CloudWatch](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html).
+  **ActivatingGameSessions** -- Game sessions in the process of being created.
+  **ActiveGameSessions** -- Game sessions that are currently running.
+  **ActiveInstances** -- Fleet instances that are currently running at least one game session.
+  **AvailableGameSessions** -- Additional game sessions that fleet could host simultaneously, given current capacity.
+  **AvailablePlayerSessions** -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.
+  **CurrentPlayerSessions** -- Player slots in active game sessions that are being used by a player or are reserved for a player.
+  **IdleInstances** -- Active instances that are currently hosting zero game sessions.
+  **PercentAvailableGameSessions** -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.
+  **PercentIdleInstances** -- Percentage of the total number of active instances that are hosting zero game sessions.
+  **QueueDepth** -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
+  **WaitTime** -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
Type: String
Valid Values: `ActivatingGameSessions | ActiveGameSessions | ActiveInstances | AvailableGameSessions | AvailablePlayerSessions | CurrentPlayerSessions | IdleInstances | PercentAvailableGameSessions | PercentIdleInstances | QueueDepth | WaitTime | ConcurrentActivatableGameSessions`
Required: No

 ** Name **   <a name="gameliftservers-Type-ScalingPolicy-Name"></a>
A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** PolicyType **   <a name="gameliftservers-Type-ScalingPolicy-PolicyType"></a>
The type of scaling policy to create. For a target-based policy, set the parameter *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration*. For a rule-based policy set the following parameters: *MetricName*, *ComparisonOperator*, *Threshold*, *EvaluationPeriods*, *ScalingAdjustmentType*, and *ScalingAdjustment*.
Type: String
Valid Values: `RuleBased | TargetBased`
Required: No

 ** ScalingAdjustment **   <a name="gameliftservers-Type-ScalingPolicy-ScalingAdjustment"></a>
Amount of adjustment to make, based on the scaling adjustment type.
Type: Integer
Required: No

 ** ScalingAdjustmentType **   <a name="gameliftservers-Type-ScalingPolicy-ScalingAdjustmentType"></a>
The type of adjustment to make to a fleet's instance count.
+  **ChangeInCapacity** -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
+  **ExactCapacity** -- set the instance count to the scaling adjustment value.
+  **PercentChangeInCapacity** -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down.
Type: String
Valid Values: `ChangeInCapacity | ExactCapacity | PercentChangeInCapacity`
Required: No

 ** Status **   <a name="gameliftservers-Type-ScalingPolicy-Status"></a>
Current status of the scaling policy. The scaling policy can be in force only when in an `ACTIVE` status. Scaling policies can be suspended for individual fleets. If the policy is suspended for a fleet, the policy status does not change.
+  **ACTIVE** -- The scaling policy can be used for auto-scaling a fleet.
+  **UPDATE\_REQUESTED** -- A request to update the scaling policy has been received.
+  **UPDATING** -- A change is being made to the scaling policy.
+  **DELETE\_REQUESTED** -- A request to delete the scaling policy has been received.
+  **DELETING** -- The scaling policy is being deleted.
+  **DELETED** -- The scaling policy has been deleted.
+  **ERROR** -- An error occurred in creating the policy. It should be removed and recreated.
Type: String
Valid Values: `ACTIVE | UPDATE_REQUESTED | UPDATING | DELETE_REQUESTED | DELETING | DELETED | ERROR`
Required: No

 ** TargetConfiguration **   <a name="gameliftservers-Type-ScalingPolicy-TargetConfiguration"></a>
An object that contains settings for a target-based scaling policy.
Type: [TargetConfiguration](API_TargetConfiguration.md) object
Required: No

 ** Threshold **   <a name="gameliftservers-Type-ScalingPolicy-Threshold"></a>
Metric value used to trigger a scaling event.
Type: Double
Required: No

 ** UpdateStatus **   <a name="gameliftservers-Type-ScalingPolicy-UpdateStatus"></a>
The current status of the fleet's scaling policies in a requested fleet location. The status `PENDING_UPDATE` indicates that an update was requested for the fleet but has not yet been completed for the location.
Type: String
Valid Values: `PENDING_UPDATE`
Required: No

## See Also
<a name="API_ScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ScalingPolicy)
