---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-deduplicationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber DeduplicationConfiguration
<a name="aws-properties-eventsv2-subscriber-deduplicationconfiguration"></a>

Deduplication settings applied to the forwarded events on the downstream bus.

## Syntax
<a name="aws-properties-eventsv2-subscriber-deduplicationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-deduplicationconfiguration-syntax.json"></a>

```
{
  "[DeduplicationType](#cfn-eventsv2-subscriber-deduplicationconfiguration-deduplicationtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-deduplicationconfiguration-syntax.yaml"></a>

```
  [DeduplicationType](#cfn-eventsv2-subscriber-deduplicationconfiguration-deduplicationtype): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-deduplicationconfiguration-properties"></a>

`DeduplicationType`  <a name="cfn-eventsv2-subscriber-deduplicationconfiguration-deduplicationtype"></a>
How duplicate events are detected: CONTENT\_BASED deduplicates by a hash of the event content. To deduplicate by a caller-supplied token instead, omit DeduplicationConfiguration and set SystemMetadata.DeduplicationId.
*Required*: Yes
*Type*: String
*Allowed values*: `CONTENT_BASED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
