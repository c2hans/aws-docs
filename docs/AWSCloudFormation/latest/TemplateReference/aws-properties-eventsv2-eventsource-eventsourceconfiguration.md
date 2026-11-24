---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventsource-eventsourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventSource EventSourceConfiguration

Event source configuration. Exactly one of the three variants must be set.

## Syntax
<a name="aws-properties-eventsv2-eventsource-eventsourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventsource-eventsourceconfiguration-syntax.json"></a>

```json
{
  "[AwsServiceEventsConfiguration](#cfn-eventsv2-eventsource-eventsourceconfiguration-awsserviceeventsconfiguration)" : {{AwsServiceEventsConfiguration}},
  "[PartnerEventsConfiguration](#cfn-eventsv2-eventsource-eventsourceconfiguration-partnereventsconfiguration)" : {{PartnerEventsConfiguration}},
  "[WebhookEventsConfiguration](#cfn-eventsv2-eventsource-eventsourceconfiguration-webhookeventsconfiguration)" : {{WebhookEventsConfiguration}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventsource-eventsourceconfiguration-syntax.yaml"></a>

```yaml
  [AwsServiceEventsConfiguration](#cfn-eventsv2-eventsource-eventsourceconfiguration-awsserviceeventsconfiguration): {{
    AwsServiceEventsConfiguration}}
  [PartnerEventsConfiguration](#cfn-eventsv2-eventsource-eventsourceconfiguration-partnereventsconfiguration): {{
    PartnerEventsConfiguration}}
  [WebhookEventsConfiguration](#cfn-eventsv2-eventsource-eventsourceconfiguration-webhookeventsconfiguration): {{
    WebhookEventsConfiguration}}
```

## Properties
<a name="aws-properties-eventsv2-eventsource-eventsourceconfiguration-properties"></a>

`AwsServiceEventsConfiguration`  <a name="cfn-eventsv2-eventsource-eventsourceconfiguration-awsserviceeventsconfiguration"></a>
Configuration for forwarding a single AWS service's events.
*Required*: No
*Type*: [AwsServiceEventsConfiguration](aws-properties-eventsv2-eventsource-awsserviceeventsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartnerEventsConfiguration`  <a name="cfn-eventsv2-eventsource-eventsourceconfiguration-partnereventsconfiguration"></a>
Configuration for forwarding a partner event source's events.
*Required*: No
*Type*: [PartnerEventsConfiguration](aws-properties-eventsv2-eventsource-partnereventsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebhookEventsConfiguration`  <a name="cfn-eventsv2-eventsource-eventsourceconfiguration-webhookeventsconfiguration"></a>
Configuration for receiving events that an external provider sends to a webhook URL.
*Required*: No
*Type*: [WebhookEventsConfiguration](aws-properties-eventsv2-eventsource-webhookeventsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
