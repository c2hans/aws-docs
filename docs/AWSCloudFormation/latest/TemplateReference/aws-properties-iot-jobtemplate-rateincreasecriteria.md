---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-jobtemplate-rateincreasecriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::JobTemplate RateIncreaseCriteria
<a name="aws-properties-iot-jobtemplate-rateincreasecriteria"></a>

Allows you to define a criteria to initiate the increase in rate of rollout for a job.

## Syntax
<a name="aws-properties-iot-jobtemplate-rateincreasecriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-jobtemplate-rateincreasecriteria-syntax.json"></a>

```
{
  "[NumberOfNotifiedThings](#cfn-iot-jobtemplate-rateincreasecriteria-numberofnotifiedthings)" : {{Integer}},
  "[NumberOfSucceededThings](#cfn-iot-jobtemplate-rateincreasecriteria-numberofsucceededthings)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-iot-jobtemplate-rateincreasecriteria-syntax.yaml"></a>

```
  [NumberOfNotifiedThings](#cfn-iot-jobtemplate-rateincreasecriteria-numberofnotifiedthings): {{Integer}}
  [NumberOfSucceededThings](#cfn-iot-jobtemplate-rateincreasecriteria-numberofsucceededthings): {{Integer}}
```

## Properties
<a name="aws-properties-iot-jobtemplate-rateincreasecriteria-properties"></a>

`NumberOfNotifiedThings`  <a name="cfn-iot-jobtemplate-rateincreasecriteria-numberofnotifiedthings"></a>
The threshold for number of notified things that will initiate the increase in rate of rollout.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NumberOfSucceededThings`  <a name="cfn-iot-jobtemplate-rateincreasecriteria-numberofsucceededthings"></a>
The threshold for number of succeeded things that will initiate the increase in rate of rollout.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
