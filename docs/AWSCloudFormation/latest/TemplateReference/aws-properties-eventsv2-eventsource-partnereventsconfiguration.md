---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventsource-partnereventsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventSource PartnerEventsConfiguration
<a name="aws-properties-eventsv2-eventsource-partnereventsconfiguration"></a>

Forward a partner event source's events through a managed partner event bus.

## Syntax
<a name="aws-properties-eventsv2-eventsource-partnereventsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventsource-partnereventsconfiguration-syntax.json"></a>

```
{
  "[OnFailureConfiguration](#cfn-eventsv2-eventsource-partnereventsconfiguration-onfailureconfiguration)" : {{OnFailureConfiguration}},
  "[PartnerBusKmsKeyIdentifier](#cfn-eventsv2-eventsource-partnereventsconfiguration-partnerbuskmskeyidentifier)" : {{String}},
  "[PartnerEventSourceArn](#cfn-eventsv2-eventsource-partnereventsconfiguration-partnereventsourcearn)" : {{String}},
  "[Pattern](#cfn-eventsv2-eventsource-partnereventsconfiguration-pattern)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventsource-partnereventsconfiguration-syntax.yaml"></a>

```
  [OnFailureConfiguration](#cfn-eventsv2-eventsource-partnereventsconfiguration-onfailureconfiguration): {{
    OnFailureConfiguration}}
  [PartnerBusKmsKeyIdentifier](#cfn-eventsv2-eventsource-partnereventsconfiguration-partnerbuskmskeyidentifier): {{String}}
  [PartnerEventSourceArn](#cfn-eventsv2-eventsource-partnereventsconfiguration-partnereventsourcearn): {{String}}
  [Pattern](#cfn-eventsv2-eventsource-partnereventsconfiguration-pattern): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-eventsource-partnereventsconfiguration-properties"></a>

`OnFailureConfiguration`  <a name="cfn-eventsv2-eventsource-partnereventsconfiguration-onfailureconfiguration"></a>
The destination for events that could not be forwarded, covering both the forwarding target and the managed partner event bus.
*Required*: No
*Type*: [OnFailureConfiguration](aws-properties-eventsv2-eventsource-onfailureconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartnerBusKmsKeyIdentifier`  <a name="cfn-eventsv2-eventsource-partnereventsconfiguration-partnerbuskmskeyidentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt events on the managed partner event bus. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN. If you do not specify a customer managed key identifier, EventBridge uses an AWS owned key to encrypt events on the event bus.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-/:]*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartnerEventSourceArn`  <a name="cfn-eventsv2-eventsource-partnereventsconfiguration-partnereventsourcearn"></a>
The ARN of the partner event source to forward. The partner owns the event source, so the ARN's account segment is empty. Changing this property replaces the event source. Because Name and EventBusArn together identify an event source, and the replacement is created before the old resource is deleted, change Name in the same update.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12})?:event-source\/aws\.partner(\/[\.\-_A-Za-z0-9]+){2,}$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Pattern`  <a name="cfn-eventsv2-eventsource-partnereventsconfiguration-pattern"></a>
A filter pattern, as a JSON string, that defines which events from the specified partner event source are forwarded to the event bus. If you do not specify a pattern, all events from the partner event source are forwarded.
*Required*: No
*Type*: String
*Maximum*: `3753`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
