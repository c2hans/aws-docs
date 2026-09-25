---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventsource-onfailureconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventSource OnFailureConfiguration
<a name="aws-properties-eventsv2-eventsource-onfailureconfiguration"></a>

The destination for events that could not be forwarded by the managed forwarding target or, for partner event sources, the managed partner event bus. Arn is optional. An empty object removes a configured destination on update.

## Syntax
<a name="aws-properties-eventsv2-eventsource-onfailureconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventsource-onfailureconfiguration-syntax.json"></a>

```
{
  "[Arn](#cfn-eventsv2-eventsource-onfailureconfiguration-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventsource-onfailureconfiguration-syntax.yaml"></a>

```
  [Arn](#cfn-eventsv2-eventsource-onfailureconfiguration-arn): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-eventsource-onfailureconfiguration-properties"></a>

`Arn`  <a name="cfn-eventsv2-eventsource-onfailureconfiguration-arn"></a>
The ARN of the Amazon SQS standard queue that receives events that could not be forwarded. FIFO queues are not supported.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[a-z0-9]+)*:sqs:[a-z][a-z0-9]*(-[a-z0-9]+)*:[0-9]{12}:[A-Za-z0-9_-]{1,80}$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
