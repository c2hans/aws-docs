---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-eventbusv2parameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber EventBusV2Parameters
<a name="aws-properties-eventsv2-subscriber-eventbusv2parameters"></a>

Parameters for forwarding events to another EventBridge event bus, used when TargetArn is an event bus ARN of the form arn:{partition}:events:{region}:{account}:event-busv2/{name}/{id}.

## Syntax
<a name="aws-properties-eventsv2-subscriber-eventbusv2parameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-eventbusv2parameters-syntax.json"></a>

```
{
  "[DeduplicationConfiguration](#cfn-eventsv2-subscriber-eventbusv2parameters-deduplicationconfiguration)" : {{DeduplicationConfiguration}},
  "[Metadata](#cfn-eventsv2-subscriber-eventbusv2parameters-metadata)" : {{{{{Key}}: {{Value}}, ...}}},
  "[SystemMetadata](#cfn-eventsv2-subscriber-eventbusv2parameters-systemmetadata)" : {{EventBusV2SystemMetadata}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-eventbusv2parameters-syntax.yaml"></a>

```
  [DeduplicationConfiguration](#cfn-eventsv2-subscriber-eventbusv2parameters-deduplicationconfiguration): {{
    DeduplicationConfiguration}}
  [Metadata](#cfn-eventsv2-subscriber-eventbusv2parameters-metadata): {{
    {{Key}}: {{Value}}}}
  [SystemMetadata](#cfn-eventsv2-subscriber-eventbusv2parameters-systemmetadata): {{
    EventBusV2SystemMetadata}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-eventbusv2parameters-properties"></a>

`DeduplicationConfiguration`  <a name="cfn-eventsv2-subscriber-eventbusv2parameters-deduplicationconfiguration"></a>
Deduplication settings applied to the forwarded events on the downstream event bus.
*Required*: No
*Type*: [DeduplicationConfiguration](aws-properties-eventsv2-subscriber-deduplicationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metadata`  <a name="cfn-eventsv2-subscriber-eventbusv2parameters-metadata"></a>
Metadata forwarded with each event, as key-value string pairs, with at most 100 entries. A key or value may also be a JSONata expression.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\s\S]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SystemMetadata`  <a name="cfn-eventsv2-subscriber-eventbusv2parameters-systemmetadata"></a>
System metadata attached to each forwarded event, controlling FIFO ordering and deduplication on the downstream event bus.
*Required*: No
*Type*: [EventBusV2SystemMetadata](aws-properties-eventsv2-subscriber-eventbusv2systemmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
