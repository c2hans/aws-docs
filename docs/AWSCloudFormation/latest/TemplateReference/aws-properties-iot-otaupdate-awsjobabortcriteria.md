---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-awsjobabortcriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate AwsJobAbortCriteria
<a name="aws-properties-iot-otaupdate-awsjobabortcriteria"></a>

The criteria that determine when and how a job abort takes place.

## Syntax
<a name="aws-properties-iot-otaupdate-awsjobabortcriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-awsjobabortcriteria-syntax.json"></a>

```
{
  "[Action](#cfn-iot-otaupdate-awsjobabortcriteria-action)" : {{String}},
  "[FailureType](#cfn-iot-otaupdate-awsjobabortcriteria-failuretype)" : {{String}},
  "[MinNumberOfExecutedThings](#cfn-iot-otaupdate-awsjobabortcriteria-minnumberofexecutedthings)" : {{Integer}},
  "[ThresholdPercentage](#cfn-iot-otaupdate-awsjobabortcriteria-thresholdpercentage)" : {{Number}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-awsjobabortcriteria-syntax.yaml"></a>

```
  [Action](#cfn-iot-otaupdate-awsjobabortcriteria-action): {{String}}
  [FailureType](#cfn-iot-otaupdate-awsjobabortcriteria-failuretype): {{String}}
  [MinNumberOfExecutedThings](#cfn-iot-otaupdate-awsjobabortcriteria-minnumberofexecutedthings): {{Integer}}
  [ThresholdPercentage](#cfn-iot-otaupdate-awsjobabortcriteria-thresholdpercentage): {{Number}}
```

## Properties
<a name="aws-properties-iot-otaupdate-awsjobabortcriteria-properties"></a>

`Action`  <a name="cfn-iot-otaupdate-awsjobabortcriteria-action"></a>
The type of job action to take to initiate the job abort.
*Required*: Yes
*Type*: String
*Allowed values*: `CANCEL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FailureType`  <a name="cfn-iot-otaupdate-awsjobabortcriteria-failuretype"></a>
The type of job execution failures that can initiate a job abort.
*Required*: Yes
*Type*: String
*Allowed values*: `FAILED | REJECTED | TIMED_OUT | ALL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinNumberOfExecutedThings`  <a name="cfn-iot-otaupdate-awsjobabortcriteria-minnumberofexecutedthings"></a>
The minimum number of things which must receive job execution notifications before the job can be aborted.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ThresholdPercentage`  <a name="cfn-iot-otaupdate-awsjobabortcriteria-thresholdpercentage"></a>
The minimum percentage of job execution failures that must occur to initiate the job abort.
AWS IoT Core supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).
*Required*: Yes
*Type*: Number
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
