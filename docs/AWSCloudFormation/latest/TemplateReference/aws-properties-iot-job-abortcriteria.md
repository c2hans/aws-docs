---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-job-abortcriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Job AbortCriteria
<a name="aws-properties-iot-job-abortcriteria"></a>

The criteria that determine when and how a job abort takes place.

## Syntax
<a name="aws-properties-iot-job-abortcriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-job-abortcriteria-syntax.json"></a>

```
{
  "[Action](#cfn-iot-job-abortcriteria-action)" : {{String}},
  "[FailureType](#cfn-iot-job-abortcriteria-failuretype)" : {{String}},
  "[MinNumberOfExecutedThings](#cfn-iot-job-abortcriteria-minnumberofexecutedthings)" : {{Integer}},
  "[ThresholdPercentage](#cfn-iot-job-abortcriteria-thresholdpercentage)" : {{Number}}
}
```

### YAML
<a name="aws-properties-iot-job-abortcriteria-syntax.yaml"></a>

```
  [Action](#cfn-iot-job-abortcriteria-action): {{String}}
  [FailureType](#cfn-iot-job-abortcriteria-failuretype): {{String}}
  [MinNumberOfExecutedThings](#cfn-iot-job-abortcriteria-minnumberofexecutedthings): {{Integer}}
  [ThresholdPercentage](#cfn-iot-job-abortcriteria-thresholdpercentage): {{Number}}
```

## Properties
<a name="aws-properties-iot-job-abortcriteria-properties"></a>

`Action`  <a name="cfn-iot-job-abortcriteria-action"></a>
The type of job action to take to initiate the job abort.
*Required*: Yes
*Type*: String
*Allowed values*: `CANCEL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FailureType`  <a name="cfn-iot-job-abortcriteria-failuretype"></a>
The type of job execution failures that can initiate a job abort.
*Required*: Yes
*Type*: String
*Allowed values*: `FAILED | REJECTED | TIMED_OUT | ALL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinNumberOfExecutedThings`  <a name="cfn-iot-job-abortcriteria-minnumberofexecutedthings"></a>
The minimum number of things which must receive job execution notifications before the job can be aborted.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThresholdPercentage`  <a name="cfn-iot-job-abortcriteria-thresholdpercentage"></a>
The minimum percentage of job execution failures that must occur to initiate the job abort.
AWS IoT Core supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).
*Required*: Yes
*Type*: Number
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
