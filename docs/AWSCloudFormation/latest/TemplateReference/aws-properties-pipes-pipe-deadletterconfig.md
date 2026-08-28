---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-deadletterconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe DeadLetterConfig
<a name="aws-properties-pipes-pipe-deadletterconfig"></a>

A `DeadLetterConfig` object that contains information about a dead-letter queue configuration.

## Syntax
<a name="aws-properties-pipes-pipe-deadletterconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-deadletterconfig-syntax.json"></a>

```
{
  "[Arn](#cfn-pipes-pipe-deadletterconfig-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-deadletterconfig-syntax.yaml"></a>

```
  [Arn](#cfn-pipes-pipe-deadletterconfig-arn): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-deadletterconfig-properties"></a>

`Arn`  <a name="cfn-pipes-pipe-deadletterconfig-arn"></a>
The ARN of the specified target for the dead-letter queue.
For Amazon Kinesis stream and Amazon DynamoDB stream sources, specify either an Amazon SNS topic or Amazon SQS queue ARN.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:(.+)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
