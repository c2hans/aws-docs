---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivschat-loggingconfiguration-firehosedestinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVSChat::LoggingConfiguration FirehoseDestinationConfiguration
<a name="aws-properties-ivschat-loggingconfiguration-firehosedestinationconfiguration"></a>

The FirehoseDestinationConfiguration property type specifies a Kinesis Firehose location where chat logs will be stored.

## Syntax
<a name="aws-properties-ivschat-loggingconfiguration-firehosedestinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivschat-loggingconfiguration-firehosedestinationconfiguration-syntax.json"></a>

```
{
  "[DeliveryStreamName](#cfn-ivschat-loggingconfiguration-firehosedestinationconfiguration-deliverystreamname)" : {{String}}
}
```

### YAML
<a name="aws-properties-ivschat-loggingconfiguration-firehosedestinationconfiguration-syntax.yaml"></a>

```
  [DeliveryStreamName](#cfn-ivschat-loggingconfiguration-firehosedestinationconfiguration-deliverystreamname): {{String}}
```

## Properties
<a name="aws-properties-ivschat-loggingconfiguration-firehosedestinationconfiguration-properties"></a>

`DeliveryStreamName`  <a name="cfn-ivschat-loggingconfiguration-firehosedestinationconfiguration-deliverystreamname"></a>
Name of the Amazon Kinesis Firehose delivery stream where chat activity will be logged.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
