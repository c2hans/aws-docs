---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-onfailureconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber OnFailureConfiguration
<a name="aws-properties-eventsv2-subscriber-onfailureconfiguration"></a>

The destination for events that could not be delivered.

## Syntax
<a name="aws-properties-eventsv2-subscriber-onfailureconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-onfailureconfiguration-syntax.json"></a>

```
{
  "[Arn](#cfn-eventsv2-subscriber-onfailureconfiguration-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-onfailureconfiguration-syntax.yaml"></a>

```
  [Arn](#cfn-eventsv2-subscriber-onfailureconfiguration-arn): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-onfailureconfiguration-properties"></a>

`Arn`  <a name="cfn-eventsv2-subscriber-onfailureconfiguration-arn"></a>
The ARN of the destination that receives events that could not be delivered. An Amazon SQS queue is the supported destination.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[a-z0-9]+)*:sqs:[a-z][a-z0-9]*(-[a-z0-9]+)*:[0-9]{12}:([A-Za-z0-9_-]{1,80}|[A-Za-z0-9_-]{1,75}\.fifo)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
