---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemon-daemonalarmconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Daemon DaemonAlarmConfiguration
<a name="aws-properties-ecs-daemon-daemonalarmconfiguration"></a>

The CloudWatch alarm configuration for a daemon. When enabled, CloudWatch alarms determine whether a daemon deployment has failed.

## Syntax
<a name="aws-properties-ecs-daemon-daemonalarmconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-daemon-daemonalarmconfiguration-syntax.json"></a>

```
{
  "[AlarmNames](#cfn-ecs-daemon-daemonalarmconfiguration-alarmnames)" : {{[ String, ... ]}},
  "[Enable](#cfn-ecs-daemon-daemonalarmconfiguration-enable)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ecs-daemon-daemonalarmconfiguration-syntax.yaml"></a>

```
  [AlarmNames](#cfn-ecs-daemon-daemonalarmconfiguration-alarmnames): {{
    - String}}
  [Enable](#cfn-ecs-daemon-daemonalarmconfiguration-enable): {{Boolean}}
```

## Properties
<a name="aws-properties-ecs-daemon-daemonalarmconfiguration-properties"></a>

`AlarmNames`  <a name="cfn-ecs-daemon-daemonalarmconfiguration-alarmnames"></a>
The CloudWatch alarm names to monitor during a daemon deployment.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enable`  <a name="cfn-ecs-daemon-daemonalarmconfiguration-enable"></a>
Determines whether to use the CloudWatch alarm option in the daemon deployment process. The default value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
