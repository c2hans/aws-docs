---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-eventbusv2systemmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber EventBusV2SystemMetadata
<a name="aws-properties-eventsv2-subscriber-eventbusv2systemmetadata"></a>

Customer-controllable system metadata attached to each forwarded event.

## Syntax
<a name="aws-properties-eventsv2-subscriber-eventbusv2systemmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-eventbusv2systemmetadata-syntax.json"></a>

```
{
  "[DeduplicationId](#cfn-eventsv2-subscriber-eventbusv2systemmetadata-deduplicationid)" : {{String}},
  "[EventGroupId](#cfn-eventsv2-subscriber-eventbusv2systemmetadata-eventgroupid)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-eventbusv2systemmetadata-syntax.yaml"></a>

```
  [DeduplicationId](#cfn-eventsv2-subscriber-eventbusv2systemmetadata-deduplicationid): {{String}}
  [EventGroupId](#cfn-eventsv2-subscriber-eventbusv2systemmetadata-eventgroupid): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-eventbusv2systemmetadata-properties"></a>

`DeduplicationId`  <a name="cfn-eventsv2-subscriber-eventbusv2systemmetadata-deduplicationid"></a>
The deduplication ID for FIFO deduplication on the downstream event bus. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventGroupId`  <a name="cfn-eventsv2-subscriber-eventbusv2systemmetadata-eventgroupid"></a>
The event group ID for FIFO ordering on the downstream event bus. Accepts a literal value or a JSONata expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
