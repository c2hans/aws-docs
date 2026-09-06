---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-scheduler-schedulegroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::ScheduleGroup Tag
<a name="aws-properties-scheduler-schedulegroup-tag"></a>

Tag to associate with a schedule group.

## Syntax
<a name="aws-properties-scheduler-schedulegroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-scheduler-schedulegroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-scheduler-schedulegroup-tag-key)" : {{String}},
  "[Value](#cfn-scheduler-schedulegroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-scheduler-schedulegroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-scheduler-schedulegroup-tag-key): {{String}}
  [Value](#cfn-scheduler-schedulegroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-scheduler-schedulegroup-tag-properties"></a>

`Key`  <a name="cfn-scheduler-schedulegroup-tag-key"></a>
The key for the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-scheduler-schedulegroup-tag-value"></a>
The value for the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
