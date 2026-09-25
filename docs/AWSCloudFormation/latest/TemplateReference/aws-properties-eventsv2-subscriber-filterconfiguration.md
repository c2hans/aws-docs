---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-filterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber FilterConfiguration
<a name="aws-properties-eventsv2-subscriber-filterconfiguration"></a>

Configuration for filtering which events are delivered to the target. An event must match every filter to be delivered.

## Syntax
<a name="aws-properties-eventsv2-subscriber-filterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-filterconfiguration-syntax.json"></a>

```
{
  "[Filters](#cfn-eventsv2-subscriber-filterconfiguration-filters)" : {{[ Filter, ... ]}},
  "[Language](#cfn-eventsv2-subscriber-filterconfiguration-language)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-filterconfiguration-syntax.yaml"></a>

```
  [Filters](#cfn-eventsv2-subscriber-filterconfiguration-filters): {{
    - Filter}}
  [Language](#cfn-eventsv2-subscriber-filterconfiguration-language): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-filterconfiguration-properties"></a>

`Filters`  <a name="cfn-eventsv2-subscriber-filterconfiguration-filters"></a>
The list of filters, 1-50 entries. An event must match every filter to be delivered.
*Required*: Yes
*Type*: Array of [Filter](aws-properties-eventsv2-subscriber-filter.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Language`  <a name="cfn-eventsv2-subscriber-filterconfiguration-language"></a>
The filter language. The default is EVENT\_BRIDGE\_PATTERN.
*Required*: No
*Type*: String
*Allowed values*: `EVENT_BRIDGE_PATTERN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
