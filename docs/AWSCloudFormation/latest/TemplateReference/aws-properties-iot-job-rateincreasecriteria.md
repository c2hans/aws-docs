---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-job-rateincreasecriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Job RateIncreaseCriteria
<a name="aws-properties-iot-job-rateincreasecriteria"></a>

Allows you to define a criteria to initiate the increase in rate of rollout for a job.

## Syntax
<a name="aws-properties-iot-job-rateincreasecriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-job-rateincreasecriteria-syntax.json"></a>

```
{
  "[NumberOfNotifiedThings](#cfn-iot-job-rateincreasecriteria-numberofnotifiedthings)" : {{Integer}},
  "[NumberOfSucceededThings](#cfn-iot-job-rateincreasecriteria-numberofsucceededthings)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-iot-job-rateincreasecriteria-syntax.yaml"></a>

```
  [NumberOfNotifiedThings](#cfn-iot-job-rateincreasecriteria-numberofnotifiedthings): {{Integer}}
  [NumberOfSucceededThings](#cfn-iot-job-rateincreasecriteria-numberofsucceededthings): {{Integer}}
```

## Properties
<a name="aws-properties-iot-job-rateincreasecriteria-properties"></a>

`NumberOfNotifiedThings`  <a name="cfn-iot-job-rateincreasecriteria-numberofnotifiedthings"></a>
The threshold for number of notified things that will initiate the increase in rate of rollout.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberOfSucceededThings`  <a name="cfn-iot-job-rateincreasecriteria-numberofsucceededthings"></a>
The threshold for number of succeeded things that will initiate the increase in rate of rollout.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
