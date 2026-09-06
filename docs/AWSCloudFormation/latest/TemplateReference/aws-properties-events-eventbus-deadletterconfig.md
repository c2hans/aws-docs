---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-eventbus-deadletterconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::EventBus DeadLetterConfig
<a name="aws-properties-events-eventbus-deadletterconfig"></a>

Configuration details of the Amazon SQS queue for EventBridge to use as a dead-letter queue (DLQ).

For more information, see [Using dead-letter queues to process undelivered events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-event-delivery.html#eb-rule-dlq) in the *EventBridge User Guide*.

## Syntax
<a name="aws-properties-events-eventbus-deadletterconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-eventbus-deadletterconfig-syntax.json"></a>

```
{
  "[Arn](#cfn-events-eventbus-deadletterconfig-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-eventbus-deadletterconfig-syntax.yaml"></a>

```
  [Arn](#cfn-events-eventbus-deadletterconfig-arn): {{String}}
```

## Properties
<a name="aws-properties-events-eventbus-deadletterconfig-properties"></a>

`Arn`  <a name="cfn-events-eventbus-deadletterconfig-arn"></a>
The ARN of the SQS queue specified as the target for the dead-letter queue.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
