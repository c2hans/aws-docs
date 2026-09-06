---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-hoursofoperation-hoursofoperationoverrideconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::HoursOfOperation HoursOfOperationOverrideConfig
<a name="aws-properties-connect-hoursofoperation-hoursofoperationoverrideconfig"></a>

Information about the hours of operation override config: day, start time, and end time.

## Syntax
<a name="aws-properties-connect-hoursofoperation-hoursofoperationoverrideconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-hoursofoperation-hoursofoperationoverrideconfig-syntax.json"></a>

```
{
  "[Day](#cfn-connect-hoursofoperation-hoursofoperationoverrideconfig-day)" : {{String}},
  "[EndTime](#cfn-connect-hoursofoperation-hoursofoperationoverrideconfig-endtime)" : {{OverrideTimeSlice}},
  "[StartTime](#cfn-connect-hoursofoperation-hoursofoperationoverrideconfig-starttime)" : {{OverrideTimeSlice}}
}
```

### YAML
<a name="aws-properties-connect-hoursofoperation-hoursofoperationoverrideconfig-syntax.yaml"></a>

```
  [Day](#cfn-connect-hoursofoperation-hoursofoperationoverrideconfig-day): {{String}}
  [EndTime](#cfn-connect-hoursofoperation-hoursofoperationoverrideconfig-endtime): {{
    OverrideTimeSlice}}
  [StartTime](#cfn-connect-hoursofoperation-hoursofoperationoverrideconfig-starttime): {{
    OverrideTimeSlice}}
```

## Properties
<a name="aws-properties-connect-hoursofoperation-hoursofoperationoverrideconfig-properties"></a>

`Day`  <a name="cfn-connect-hoursofoperation-hoursofoperationoverrideconfig-day"></a>
The day that the hours of operation override applies to.
*Required*: Yes
*Type*: String
*Allowed values*: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndTime`  <a name="cfn-connect-hoursofoperation-hoursofoperationoverrideconfig-endtime"></a>
The end time that your contact center closes if overrides are applied.
*Required*: Yes
*Type*: [OverrideTimeSlice](aws-properties-connect-hoursofoperation-overridetimeslice.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTime`  <a name="cfn-connect-hoursofoperation-hoursofoperationoverrideconfig-starttime"></a>
The start time when your contact center opens if overrides are applied.
*Required*: Yes
*Type*: [OverrideTimeSlice](aws-properties-connect-hoursofoperation-overridetimeslice.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
