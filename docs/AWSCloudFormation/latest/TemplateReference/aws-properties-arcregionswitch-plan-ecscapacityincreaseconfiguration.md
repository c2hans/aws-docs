---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-ecscapacityincreaseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan EcsCapacityIncreaseConfiguration
<a name="aws-properties-arcregionswitch-plan-ecscapacityincreaseconfiguration"></a>

The configuration for an AWS ECS capacity increase.

## Syntax
<a name="aws-properties-arcregionswitch-plan-ecscapacityincreaseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-ecscapacityincreaseconfiguration-syntax.json"></a>

```
{
  "[CapacityMonitoringApproach](#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-capacitymonitoringapproach)" : {{}},
  "[Services](#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-services)" : {{[ Service, ... ]}},
  "[TargetPercent](#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-targetpercent)" : {{Number}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-timeoutminutes)" : {{Number}},
  "[Ungraceful](#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-ungraceful)" : {{EcsUngraceful}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-ecscapacityincreaseconfiguration-syntax.yaml"></a>

```
  [CapacityMonitoringApproach](#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-capacitymonitoringapproach): {{
    }}
  [Services](#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-services): {{
    - Service}}
  [TargetPercent](#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-targetpercent): {{Number}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-timeoutminutes): {{Number}}
  [Ungraceful](#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-ungraceful): {{
    EcsUngraceful}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-ecscapacityincreaseconfiguration-properties"></a>

`CapacityMonitoringApproach`  <a name="cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-capacitymonitoringapproach"></a>
The monitoring approach specified for the configuration, for example, `Most_Recent`.
*Required*: No
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Services`  <a name="cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-services"></a>
The services specified for the configuration.
*Required*: Yes
*Type*: Array of [Service](aws-properties-arcregionswitch-plan-service.md)
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetPercent`  <a name="cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-targetpercent"></a>
The target percentage specified for the configuration. The default is 100.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ungraceful`  <a name="cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-ungraceful"></a>
The settings for ungraceful execution.
*Required*: No
*Type*: [EcsUngraceful](aws-properties-arcregionswitch-plan-ecsungraceful.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
