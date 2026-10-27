---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-awsjobrateincreasecriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate AwsJobRateIncreaseCriteria
<a name="aws-properties-iot-otaupdate-awsjobrateincreasecriteria"></a>

The criteria to initiate the increase in rate of rollout for a job.

## Syntax
<a name="aws-properties-iot-otaupdate-awsjobrateincreasecriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-awsjobrateincreasecriteria-syntax.json"></a>

```
{
  "[NumberOfNotifiedThings](#cfn-iot-otaupdate-awsjobrateincreasecriteria-numberofnotifiedthings)" : {{Integer}},
  "[NumberOfSucceededThings](#cfn-iot-otaupdate-awsjobrateincreasecriteria-numberofsucceededthings)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-awsjobrateincreasecriteria-syntax.yaml"></a>

```
  [NumberOfNotifiedThings](#cfn-iot-otaupdate-awsjobrateincreasecriteria-numberofnotifiedthings): {{Integer}}
  [NumberOfSucceededThings](#cfn-iot-otaupdate-awsjobrateincreasecriteria-numberofsucceededthings): {{Integer}}
```

## Properties
<a name="aws-properties-iot-otaupdate-awsjobrateincreasecriteria-properties"></a>

`NumberOfNotifiedThings`  <a name="cfn-iot-otaupdate-awsjobrateincreasecriteria-numberofnotifiedthings"></a>
When this number of things have been notified, it will initiate an increase in the rollout rate.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NumberOfSucceededThings`  <a name="cfn-iot-otaupdate-awsjobrateincreasecriteria-numberofsucceededthings"></a>
When this number of things have succeeded in their job execution, it will initiate an increase in the rollout rate.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
