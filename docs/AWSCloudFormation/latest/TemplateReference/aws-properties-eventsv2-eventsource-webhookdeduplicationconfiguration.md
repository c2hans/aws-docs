---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventsource-webhookdeduplicationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventSource WebhookDeduplicationConfiguration

Deduplication settings for a webhook event source's events.

## Syntax
<a name="aws-properties-eventsv2-eventsource-webhookdeduplicationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventsource-webhookdeduplicationconfiguration-syntax.json"></a>

```json
{
  "[DeduplicationType](#cfn-eventsv2-eventsource-webhookdeduplicationconfiguration-deduplicationtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventsource-webhookdeduplicationconfiguration-syntax.yaml"></a>

```yaml
  [DeduplicationType](#cfn-eventsv2-eventsource-webhookdeduplicationconfiguration-deduplicationtype): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-eventsource-webhookdeduplicationconfiguration-properties"></a>

`DeduplicationType`  <a name="cfn-eventsv2-eventsource-webhookdeduplicationconfiguration-deduplicationtype"></a>
How EventBridge detects duplicate events.
Valid values: - CONTENT\_BASED - Detects duplicates by a hash of the event content.
*Required*: Yes
*Type*: String
*Allowed values*: `CONTENT_BASED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
