---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CisScanConfiguration MonthlySchedule
<a name="aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule"></a>

A monthly schedule.

## Syntax
<a name="aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule-syntax.json"></a>

```
{
  "[Day](#cfn-inspectorv2-cisscanconfiguration-monthlyschedule-day)" : {{String}},
  "[StartTime](#cfn-inspectorv2-cisscanconfiguration-monthlyschedule-starttime)" : {{Time}}
}
```

### YAML
<a name="aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule-syntax.yaml"></a>

```
  [Day](#cfn-inspectorv2-cisscanconfiguration-monthlyschedule-day): {{String}}
  [StartTime](#cfn-inspectorv2-cisscanconfiguration-monthlyschedule-starttime): {{
    Time}}
```

## Properties
<a name="aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule-properties"></a>

`Day`  <a name="cfn-inspectorv2-cisscanconfiguration-monthlyschedule-day"></a>
The monthly schedule's day.
*Required*: Yes
*Type*: String
*Allowed values*: `MON | TUE | WED | THU | FRI | SAT | SUN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTime`  <a name="cfn-inspectorv2-cisscanconfiguration-monthlyschedule-starttime"></a>
The monthly schedule's start time.
*Required*: Yes
*Type*: [Time](aws-properties-inspectorv2-cisscanconfiguration-time.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
