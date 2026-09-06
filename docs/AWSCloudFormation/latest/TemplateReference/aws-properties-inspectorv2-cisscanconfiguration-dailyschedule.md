---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-cisscanconfiguration-dailyschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CisScanConfiguration DailySchedule
<a name="aws-properties-inspectorv2-cisscanconfiguration-dailyschedule"></a>

A daily schedule.

## Syntax
<a name="aws-properties-inspectorv2-cisscanconfiguration-dailyschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-cisscanconfiguration-dailyschedule-syntax.json"></a>

```
{
  "[StartTime](#cfn-inspectorv2-cisscanconfiguration-dailyschedule-starttime)" : {{Time}}
}
```

### YAML
<a name="aws-properties-inspectorv2-cisscanconfiguration-dailyschedule-syntax.yaml"></a>

```
  [StartTime](#cfn-inspectorv2-cisscanconfiguration-dailyschedule-starttime): {{
    Time}}
```

## Properties
<a name="aws-properties-inspectorv2-cisscanconfiguration-dailyschedule-properties"></a>

`StartTime`  <a name="cfn-inspectorv2-cisscanconfiguration-dailyschedule-starttime"></a>
The schedule start time.
*Required*: Yes
*Type*: [Time](aws-properties-inspectorv2-cisscanconfiguration-time.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
