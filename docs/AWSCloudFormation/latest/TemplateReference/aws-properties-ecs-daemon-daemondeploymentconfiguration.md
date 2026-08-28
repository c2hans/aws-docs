---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemon-daemondeploymentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Daemon DaemonDeploymentConfiguration
<a name="aws-properties-ecs-daemon-daemondeploymentconfiguration"></a>

Optional deployment parameters that control how a daemon rolls out updates across container instances.

## Syntax
<a name="aws-properties-ecs-daemon-daemondeploymentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-daemon-daemondeploymentconfiguration-syntax.json"></a>

```
{
  "[Alarms](#cfn-ecs-daemon-daemondeploymentconfiguration-alarms)" : {{DaemonAlarmConfiguration}},
  "[BakeTimeInMinutes](#cfn-ecs-daemon-daemondeploymentconfiguration-baketimeinminutes)" : {{Integer}},
  "[DrainPercent](#cfn-ecs-daemon-daemondeploymentconfiguration-drainpercent)" : {{Number}}
}
```

### YAML
<a name="aws-properties-ecs-daemon-daemondeploymentconfiguration-syntax.yaml"></a>

```
  [Alarms](#cfn-ecs-daemon-daemondeploymentconfiguration-alarms): {{
    DaemonAlarmConfiguration}}
  [BakeTimeInMinutes](#cfn-ecs-daemon-daemondeploymentconfiguration-baketimeinminutes): {{Integer}}
  [DrainPercent](#cfn-ecs-daemon-daemondeploymentconfiguration-drainpercent): {{Number}}
```

## Properties
<a name="aws-properties-ecs-daemon-daemondeploymentconfiguration-properties"></a>

`Alarms`  <a name="cfn-ecs-daemon-daemondeploymentconfiguration-alarms"></a>
The CloudWatch alarm configuration for the daemon deployment. When alarms are triggered during a deployment, the deployment can be automatically rolled back.
*Required*: No
*Type*: [DaemonAlarmConfiguration](aws-properties-ecs-daemon-daemonalarmconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BakeTimeInMinutes`  <a name="cfn-ecs-daemon-daemondeploymentconfiguration-baketimeinminutes"></a>
The amount of time (in minutes) to wait after a successful deployment step before proceeding. This allows time to monitor for issues before continuing. The default value is 0.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1440`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DrainPercent`  <a name="cfn-ecs-daemon-daemondeploymentconfiguration-drainpercent"></a>
The percentage of container instances to drain simultaneously during a daemon deployment. Valid values are between 0.0 and 100.0.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
