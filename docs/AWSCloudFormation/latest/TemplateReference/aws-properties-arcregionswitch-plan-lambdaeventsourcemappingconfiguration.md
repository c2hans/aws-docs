---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-lambdaeventsourcemappingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan LambdaEventSourceMappingConfiguration
<a name="aws-properties-arcregionswitch-plan-lambdaeventsourcemappingconfiguration"></a>

Configuration for AWS Lambda event source mappings used in a Region switch plan.

## Syntax
<a name="aws-properties-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-syntax.json"></a>

```
{
  "[Action](#cfn-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-action)" : {{String}},
  "[RegionEventSourceMappings](#cfn-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-regioneventsourcemappings)" : {{{{{Key}}: {{Value}}, ...}}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-timeoutminutes)" : {{Number}},
  "[Ungraceful](#cfn-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-ungraceful)" : {{LambdaEventSourceMappingUngraceful}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-syntax.yaml"></a>

```
  [Action](#cfn-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-action): {{String}}
  [RegionEventSourceMappings](#cfn-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-regioneventsourcemappings): {{
    {{Key}}: {{Value}}}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-timeoutminutes): {{Number}}
  [Ungraceful](#cfn-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-ungraceful): {{
    LambdaEventSourceMappingUngraceful}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-properties"></a>

`Action`  <a name="cfn-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-action"></a>
The action to take - whether to `enable` or `disable` an event source mapping.
*Required*: Yes
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionEventSourceMappings`  <a name="cfn-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-regioneventsourcemappings"></a>
Per-region configuration for which Lambda event source mapping to enable or disable when activating or deactivating a region.
*Required*: Yes
*Type*: Object of [EventSourceMapping](aws-properties-arcregionswitch-plan-eventsourcemapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ungraceful`  <a name="cfn-arcregionswitch-plan-lambdaeventsourcemappingconfiguration-ungraceful"></a>
The settings for ungraceful execution.
*Required*: No
*Type*: [LambdaEventSourceMappingUngraceful](aws-properties-arcregionswitch-plan-lambdaeventsourcemappingungraceful.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
