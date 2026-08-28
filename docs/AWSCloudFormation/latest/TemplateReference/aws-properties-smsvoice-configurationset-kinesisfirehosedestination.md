---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-configurationset-kinesisfirehosedestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::ConfigurationSet KinesisFirehoseDestination
<a name="aws-properties-smsvoice-configurationset-kinesisfirehosedestination"></a>

Contains the delivery stream Amazon Resource Name (ARN), and the ARN of the AWS Identity and Access Management (IAM) role associated with a Firehose event destination.

Event destinations, such as Firehose, are associated with configuration sets, which enable you to publish message sending events.

## Syntax
<a name="aws-properties-smsvoice-configurationset-kinesisfirehosedestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-configurationset-kinesisfirehosedestination-syntax.json"></a>

```
{
  "[DeliveryStreamArn](#cfn-smsvoice-configurationset-kinesisfirehosedestination-deliverystreamarn)" : {{String}},
  "[IamRoleArn](#cfn-smsvoice-configurationset-kinesisfirehosedestination-iamrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-smsvoice-configurationset-kinesisfirehosedestination-syntax.yaml"></a>

```
  [DeliveryStreamArn](#cfn-smsvoice-configurationset-kinesisfirehosedestination-deliverystreamarn): {{String}}
  [IamRoleArn](#cfn-smsvoice-configurationset-kinesisfirehosedestination-iamrolearn): {{String}}
```

## Properties
<a name="aws-properties-smsvoice-configurationset-kinesisfirehosedestination-properties"></a>

`DeliveryStreamArn`  <a name="cfn-smsvoice-configurationset-kinesisfirehosedestination-deliverystreamarn"></a>
The Amazon Resource Name (ARN) of the delivery stream.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:\S+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamRoleArn`  <a name="cfn-smsvoice-configurationset-kinesisfirehosedestination-iamrolearn"></a>
The ARN of an AWS Identity and Access Management role that is able to write event data to an Amazon Data Firehose destination.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:\S+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
