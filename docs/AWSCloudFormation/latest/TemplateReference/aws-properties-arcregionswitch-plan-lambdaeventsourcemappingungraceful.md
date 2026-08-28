---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-lambdaeventsourcemappingungraceful.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan LambdaEventSourceMappingUngraceful
<a name="aws-properties-arcregionswitch-plan-lambdaeventsourcemappingungraceful"></a>

Specifies whether to skip enabling or disabling an event source mapping during an ungraceful execution.

## Syntax
<a name="aws-properties-arcregionswitch-plan-lambdaeventsourcemappingungraceful-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-lambdaeventsourcemappingungraceful-syntax.json"></a>

```
{
  "[Behavior](#cfn-arcregionswitch-plan-lambdaeventsourcemappingungraceful-behavior)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-lambdaeventsourcemappingungraceful-syntax.yaml"></a>

```
  [Behavior](#cfn-arcregionswitch-plan-lambdaeventsourcemappingungraceful-behavior): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-lambdaeventsourcemappingungraceful-properties"></a>

`Behavior`  <a name="cfn-arcregionswitch-plan-lambdaeventsourcemappingungraceful-behavior"></a>
Set to `skip` to skip executing this event source mapping step during an ungraceful execution.
*Required*: No
*Type*: String
*Allowed values*: `skip`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
