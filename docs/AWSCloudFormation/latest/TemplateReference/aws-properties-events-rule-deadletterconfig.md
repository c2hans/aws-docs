---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-rule-deadletterconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Rule DeadLetterConfig
<a name="aws-properties-events-rule-deadletterconfig"></a>

Configuration details of the Amazon SQS queue for EventBridge to use as a dead-letter queue (DLQ).

For more information, see [Using dead-letter queues to process undelivered events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-event-delivery.html#eb-rule-dlq) in the *EventBridge User Guide*.

## Syntax
<a name="aws-properties-events-rule-deadletterconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-rule-deadletterconfig-syntax.json"></a>

```
{
  "[Arn](#cfn-events-rule-deadletterconfig-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-rule-deadletterconfig-syntax.yaml"></a>

```
  [Arn](#cfn-events-rule-deadletterconfig-arn): {{String}}
```

## Properties
<a name="aws-properties-events-rule-deadletterconfig-properties"></a>

`Arn`  <a name="cfn-events-rule-deadletterconfig-arn"></a>
The ARN of the SQS queue specified as the target for the dead-letter queue.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-events-rule-deadletterconfig--examples"></a>

### Set the DeadLetterConfig parameter
<a name="aws-properties-events-rule-deadletterconfig--examples--Set_the_DeadLetterConfig_parameter"></a>

The following example sets the `DeadLetterConfig` parameter to set up arn:aws:sqs:us-west-2:081035103721:demoDLQ as a dead-letter queue.

#### JSON
<a name="aws-properties-events-rule-deadletterconfig--examples--Set_the_DeadLetterConfig_parameter--json"></a>

```
"DeadLetterConfig": {
  "Arn": "arn:aws:sqs:us-west-2:081035103721:demoDLQ"
}
```

#### YAML
<a name="aws-properties-events-rule-deadletterconfig--examples--Set_the_DeadLetterConfig_parameter--yaml"></a>

```
DeadLetterConfig:
  Arn: 'arn:aws:sqs:us-west-2:081035103721:demoDLQ'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
