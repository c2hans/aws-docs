---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber Filter
<a name="aws-properties-eventsv2-subscriber-filter"></a>

A single filter entry: an event pattern and the scope of the event it is evaluated against.

## Syntax
<a name="aws-properties-eventsv2-subscriber-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-filter-syntax.json"></a>

```
{
  "[Pattern](#cfn-eventsv2-subscriber-filter-pattern)" : {{String}},
  "[Scope](#cfn-eventsv2-subscriber-filter-scope)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-filter-syntax.yaml"></a>

```
  [Pattern](#cfn-eventsv2-subscriber-filter-pattern): {{String}}
  [Scope](#cfn-eventsv2-subscriber-filter-scope): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-filter-properties"></a>

`Pattern`  <a name="cfn-eventsv2-subscriber-filter-pattern"></a>
The event pattern, as a JSON string.
*Required*: Yes
*Type*: String
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-eventsv2-subscriber-filter-scope"></a>
Which part of the event the pattern is evaluated against: DATA (the event payload), METADATA (event metadata), or SYSTEM\_METADATA (service-generated metadata).
*Required*: Yes
*Type*: String
*Allowed values*: `DATA | METADATA | SYSTEM_METADATA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
