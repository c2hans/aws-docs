---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventsource-eventsourcedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventSource EventSourceDetails

Values Amazon EventBridge generated for the event source that depend on its type. Only the member for the event source's type is set.

## Syntax
<a name="aws-properties-eventsv2-eventsource-eventsourcedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventsource-eventsourcedetails-syntax.json"></a>

```json
{
  "[WebhookDetails](#cfn-eventsv2-eventsource-eventsourcedetails-webhookdetails)" : {{WebhookDetails}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventsource-eventsourcedetails-syntax.yaml"></a>

```yaml
  [WebhookDetails](#cfn-eventsv2-eventsource-eventsourcedetails-webhookdetails): {{
    WebhookDetails}}
```

## Properties
<a name="aws-properties-eventsv2-eventsource-eventsourcedetails-properties"></a>

`WebhookDetails`  <a name="cfn-eventsv2-eventsource-eventsourcedetails-webhookdetails"></a>
Values generated for a webhook event source.
*Required*: No
*Type*: [WebhookDetails](aws-properties-eventsv2-eventsource-webhookdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
