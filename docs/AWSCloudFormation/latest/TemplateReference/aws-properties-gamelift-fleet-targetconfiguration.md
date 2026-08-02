---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-fleet-targetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::Fleet TargetConfiguration
<a name="aws-properties-gamelift-fleet-targetconfiguration"></a>

Settings for a target-based scaling policy. A target-based policy tracks a particular fleet metric specifies a target value for the metric. As player usage changes, the policy triggers Amazon GameLift Servers to adjust capacity so that the metric returns to the target value. The target configuration specifies settings as needed for the target based policy, including the target value.

## Syntax
<a name="aws-properties-gamelift-fleet-targetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-fleet-targetconfiguration-syntax.json"></a>

```
{
  "[TargetValue](#cfn-gamelift-fleet-targetconfiguration-targetvalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-gamelift-fleet-targetconfiguration-syntax.yaml"></a>

```
  [TargetValue](#cfn-gamelift-fleet-targetconfiguration-targetvalue): {{Number}}
```

## Properties
<a name="aws-properties-gamelift-fleet-targetconfiguration-properties"></a>

`TargetValue`  <a name="cfn-gamelift-fleet-targetconfiguration-targetvalue"></a>
Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet's buffer (the percent of capacity that should be idle and ready for new game sessions).
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
