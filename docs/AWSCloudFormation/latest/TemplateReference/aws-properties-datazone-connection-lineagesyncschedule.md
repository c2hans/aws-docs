---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-lineagesyncschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection LineageSyncSchedule
<a name="aws-properties-datazone-connection-lineagesyncschedule"></a>

The lineage sync schedule.

## Syntax
<a name="aws-properties-datazone-connection-lineagesyncschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-lineagesyncschedule-syntax.json"></a>

```
{
  "[Schedule](#cfn-datazone-connection-lineagesyncschedule-schedule)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-lineagesyncschedule-syntax.yaml"></a>

```
  [Schedule](#cfn-datazone-connection-lineagesyncschedule-schedule): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-lineagesyncschedule-properties"></a>

`Schedule`  <a name="cfn-datazone-connection-lineagesyncschedule-schedule"></a>
The lineage sync schedule.
*Required*: No
*Type*: String
*Pattern*: `^cron\((\b[0-5]?[0-9]\b) (\b2[0-3]\b|\b[0-1]?[0-9]\b) ([-?*,/\dLW]){1,83} ([-*,/\d]|[a-zA-Z]{3}){1,23} ([-?#*,/\dL]|[a-zA-Z]{3}){1,13} ([^\)]+)\)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
