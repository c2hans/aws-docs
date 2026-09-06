---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-scheduler-schedule-flexibletimewindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::Schedule FlexibleTimeWindow
<a name="aws-properties-scheduler-schedule-flexibletimewindow"></a>

Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.

## Syntax
<a name="aws-properties-scheduler-schedule-flexibletimewindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-scheduler-schedule-flexibletimewindow-syntax.json"></a>

```
{
  "[MaximumWindowInMinutes](#cfn-scheduler-schedule-flexibletimewindow-maximumwindowinminutes)" : {{Number}},
  "[Mode](#cfn-scheduler-schedule-flexibletimewindow-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-scheduler-schedule-flexibletimewindow-syntax.yaml"></a>

```
  [MaximumWindowInMinutes](#cfn-scheduler-schedule-flexibletimewindow-maximumwindowinminutes): {{Number}}
  [Mode](#cfn-scheduler-schedule-flexibletimewindow-mode): {{String}}
```

## Properties
<a name="aws-properties-scheduler-schedule-flexibletimewindow-properties"></a>

`MaximumWindowInMinutes`  <a name="cfn-scheduler-schedule-flexibletimewindow-maximumwindowinminutes"></a>
The maximum time window during which a schedule can be invoked.
*Minimum*: `1`
*Maximum*: `1440`
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `1440`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-scheduler-schedule-flexibletimewindow-mode"></a>
Determines whether the schedule is invoked within a flexible time window. You must use quotation marks when you specify this value in your JSON or YAML template.
*Allowed Values*: `"OFF"` \| `"FLEXIBLE"`
*Required*: Yes
*Type*: String
*Allowed values*: `OFF | FLEXIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
