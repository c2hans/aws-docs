---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containerfleet-scalingpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerFleet ScalingPolicy
<a name="aws-properties-gamelift-containerfleet-scalingpolicy"></a>

Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.

## Syntax
<a name="aws-properties-gamelift-containerfleet-scalingpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containerfleet-scalingpolicy-syntax.json"></a>

```
{
  "[ComparisonOperator](#cfn-gamelift-containerfleet-scalingpolicy-comparisonoperator)" : {{String}},
  "[EvaluationPeriods](#cfn-gamelift-containerfleet-scalingpolicy-evaluationperiods)" : {{Integer}},
  "[MetricName](#cfn-gamelift-containerfleet-scalingpolicy-metricname)" : {{String}},
  "[Name](#cfn-gamelift-containerfleet-scalingpolicy-name)" : {{String}},
  "[PolicyType](#cfn-gamelift-containerfleet-scalingpolicy-policytype)" : {{String}},
  "[ScalingAdjustment](#cfn-gamelift-containerfleet-scalingpolicy-scalingadjustment)" : {{Integer}},
  "[ScalingAdjustmentType](#cfn-gamelift-containerfleet-scalingpolicy-scalingadjustmenttype)" : {{String}},
  "[TargetConfiguration](#cfn-gamelift-containerfleet-scalingpolicy-targetconfiguration)" : {{TargetConfiguration}},
  "[Threshold](#cfn-gamelift-containerfleet-scalingpolicy-threshold)" : {{Number}}
}
```

### YAML
<a name="aws-properties-gamelift-containerfleet-scalingpolicy-syntax.yaml"></a>

```
  [ComparisonOperator](#cfn-gamelift-containerfleet-scalingpolicy-comparisonoperator): {{String}}
  [EvaluationPeriods](#cfn-gamelift-containerfleet-scalingpolicy-evaluationperiods): {{Integer}}
  [MetricName](#cfn-gamelift-containerfleet-scalingpolicy-metricname): {{String}}
  [Name](#cfn-gamelift-containerfleet-scalingpolicy-name): {{String}}
  [PolicyType](#cfn-gamelift-containerfleet-scalingpolicy-policytype): {{String}}
  [ScalingAdjustment](#cfn-gamelift-containerfleet-scalingpolicy-scalingadjustment): {{Integer}}
  [ScalingAdjustmentType](#cfn-gamelift-containerfleet-scalingpolicy-scalingadjustmenttype): {{String}}
  [TargetConfiguration](#cfn-gamelift-containerfleet-scalingpolicy-targetconfiguration): {{
    TargetConfiguration}}
  [Threshold](#cfn-gamelift-containerfleet-scalingpolicy-threshold): {{Number}}
```

## Properties
<a name="aws-properties-gamelift-containerfleet-scalingpolicy-properties"></a>

`ComparisonOperator`  <a name="cfn-gamelift-containerfleet-scalingpolicy-comparisonoperator"></a>
Comparison operator to use when measuring a metric against the threshold value.
*Required*: No
*Type*: String
*Allowed values*: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EvaluationPeriods`  <a name="cfn-gamelift-containerfleet-scalingpolicy-evaluationperiods"></a>
Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-gamelift-containerfleet-scalingpolicy-metricname"></a>
Name of the Amazon GameLift Servers-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see [Monitor Amazon GameLift Servers with Amazon CloudWatch](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html).
+ **ActivatingGameSessions** -- Game sessions in the process of being created.
+ **ActiveGameSessions** -- Game sessions that are currently running.
+ **ActiveInstances** -- Fleet instances that are currently running at least one game session.
+ **AvailableGameSessions** -- Additional game sessions that fleet could host simultaneously, given current capacity.
+ **AvailablePlayerSessions** -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.
+ **CurrentPlayerSessions** -- Player slots in active game sessions that are being used by a player or are reserved for a player.
+ **IdleInstances** -- Active instances that are currently hosting zero game sessions.
+ **PercentAvailableGameSessions** -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.
+ **PercentIdleInstances** -- Percentage of the total number of active instances that are hosting zero game sessions.
+ **QueueDepth** -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
+ **WaitTime** -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
*Required*: No
*Type*: String
*Allowed values*: `ActivatingGameSessions | ActiveGameSessions | ActiveInstances | AvailableGameSessions | AvailablePlayerSessions | CurrentPlayerSessions | IdleInstances | PercentAvailableGameSessions | PercentIdleInstances | QueueDepth | WaitTime | ConcurrentActivatableGameSessions`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-gamelift-containerfleet-scalingpolicy-name"></a>
A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyType`  <a name="cfn-gamelift-containerfleet-scalingpolicy-policytype"></a>
The type of scaling policy to create. For a target-based policy, set the parameter *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration*. For a rule-based policy set the following parameters: *MetricName*, *ComparisonOperator*, *Threshold*, *EvaluationPeriods*, *ScalingAdjustmentType*, and *ScalingAdjustment*.
*Required*: No
*Type*: String
*Allowed values*: `RuleBased | TargetBased | ManagedScaling`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingAdjustment`  <a name="cfn-gamelift-containerfleet-scalingpolicy-scalingadjustment"></a>
Amount of adjustment to make, based on the scaling adjustment type.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingAdjustmentType`  <a name="cfn-gamelift-containerfleet-scalingpolicy-scalingadjustmenttype"></a>
The type of adjustment to make to a fleet's instance count.
+ **ChangeInCapacity** -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
+ **ExactCapacity** -- set the instance count to the scaling adjustment value.
+ **PercentChangeInCapacity** -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down.
*Required*: No
*Type*: String
*Allowed values*: `ChangeInCapacity | ExactCapacity | PercentChangeInCapacity`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetConfiguration`  <a name="cfn-gamelift-containerfleet-scalingpolicy-targetconfiguration"></a>
An object that contains settings for a target-based scaling policy.
*Required*: No
*Type*: [TargetConfiguration](aws-properties-gamelift-containerfleet-targetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Threshold`  <a name="cfn-gamelift-containerfleet-scalingpolicy-threshold"></a>
Metric value used to trigger a scaling event.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
