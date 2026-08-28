---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-ecsungraceful.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan EcsUngraceful
<a name="aws-properties-arcregionswitch-plan-ecsungraceful"></a>

The settings for ungraceful execution.

## Syntax
<a name="aws-properties-arcregionswitch-plan-ecsungraceful-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-ecsungraceful-syntax.json"></a>

```
{
  "[MinimumSuccessPercentage](#cfn-arcregionswitch-plan-ecsungraceful-minimumsuccesspercentage)" : {{Number}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-ecsungraceful-syntax.yaml"></a>

```
  [MinimumSuccessPercentage](#cfn-arcregionswitch-plan-ecsungraceful-minimumsuccesspercentage): {{Number}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-ecsungraceful-properties"></a>

`MinimumSuccessPercentage`  <a name="cfn-arcregionswitch-plan-ecsungraceful-minimumsuccesspercentage"></a>
The minimum success percentage specified for the configuration.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `99`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
