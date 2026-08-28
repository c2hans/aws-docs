---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-firehoselogdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe FirehoseLogDestination
<a name="aws-properties-pipes-pipe-firehoselogdestination"></a>

Represents the Amazon Data Firehose logging configuration settings for the pipe.

## Syntax
<a name="aws-properties-pipes-pipe-firehoselogdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-firehoselogdestination-syntax.json"></a>

```
{
  "[DeliveryStreamArn](#cfn-pipes-pipe-firehoselogdestination-deliverystreamarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-firehoselogdestination-syntax.yaml"></a>

```
  [DeliveryStreamArn](#cfn-pipes-pipe-firehoselogdestination-deliverystreamarn): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-firehoselogdestination-properties"></a>

`DeliveryStreamArn`  <a name="cfn-pipes-pipe-firehoselogdestination-deliverystreamarn"></a>
The Amazon Resource Name (ARN) of the Firehose delivery stream to which EventBridge delivers the pipe log records.
*Required*: No
*Type*: String
*Pattern*: `^(^arn:aws([a-z]|\-)*:firehose:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}):(\d{12}):deliverystream/.+)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
