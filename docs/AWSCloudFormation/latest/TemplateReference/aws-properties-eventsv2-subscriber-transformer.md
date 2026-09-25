---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-transformer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber Transformer
<a name="aws-properties-eventsv2-subscriber-transformer"></a>

Configuration for transforming events before delivery: the raw payload, the payload with its metadata envelope, or the output of a JSONata expression.

## Syntax
<a name="aws-properties-eventsv2-subscriber-transformer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-transformer-syntax.json"></a>

```
{
  "[JsonataConfiguration](#cfn-eventsv2-subscriber-transformer-jsonataconfiguration)" : {{JsonataConfiguration}},
  "[Type](#cfn-eventsv2-subscriber-transformer-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-transformer-syntax.yaml"></a>

```
  [JsonataConfiguration](#cfn-eventsv2-subscriber-transformer-jsonataconfiguration): {{
    JsonataConfiguration}}
  [Type](#cfn-eventsv2-subscriber-transformer-type): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-transformer-properties"></a>

`JsonataConfiguration`  <a name="cfn-eventsv2-subscriber-transformer-jsonataconfiguration"></a>
The JSONata expression configuration. Required when Type is JSONATA.
*Required*: No
*Type*: [JsonataConfiguration](aws-properties-eventsv2-subscriber-jsonataconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-eventsv2-subscriber-transformer-type"></a>
The transform type: RAW delivers the event payload only; WITH\_METADATA delivers the event with its metadata envelope; JSONATA delivers the output of the JSONata expression in JsonataConfiguration.
*Required*: No
*Type*: String
*Allowed values*: `RAW | WITH_METADATA | JSONATA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
