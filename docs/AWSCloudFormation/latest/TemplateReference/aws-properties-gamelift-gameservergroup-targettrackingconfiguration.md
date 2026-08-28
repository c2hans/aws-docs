---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-gameservergroup-targettrackingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::GameServerGroup TargetTrackingConfiguration
<a name="aws-properties-gamelift-gameservergroup-targettrackingconfiguration"></a>

 **This data type is used with the Amazon GameLift FleetIQ and game server groups.**

Settings for a target-based scaling policy as part of a `GameServerGroupAutoScalingPolicy`. These settings are used to create a target-based policy that tracks the GameLift FleetIQ metric `"PercentUtilizedGameServers"` and specifies a target value for the metric. As player usage changes, the policy triggers to adjust the game server group capacity so that the metric returns to the target value.

## Syntax
<a name="aws-properties-gamelift-gameservergroup-targettrackingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-gameservergroup-targettrackingconfiguration-syntax.json"></a>

```
{
  "[TargetValue](#cfn-gamelift-gameservergroup-targettrackingconfiguration-targetvalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-gamelift-gameservergroup-targettrackingconfiguration-syntax.yaml"></a>

```
  [TargetValue](#cfn-gamelift-gameservergroup-targettrackingconfiguration-targetvalue): {{Number}}
```

## Properties
<a name="aws-properties-gamelift-gameservergroup-targettrackingconfiguration-properties"></a>

`TargetValue`  <a name="cfn-gamelift-gameservergroup-targettrackingconfiguration-targetvalue"></a>
Desired value to use with a game server group target-based scaling policy.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
