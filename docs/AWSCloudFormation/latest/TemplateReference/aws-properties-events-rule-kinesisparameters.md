---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-rule-kinesisparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Rule KinesisParameters
<a name="aws-properties-events-rule-kinesisparameters"></a>

This object enables you to specify a JSON path to extract from the event and use as the partition key for the Amazon Kinesis data stream, so that you can control the shard to which the event goes. If you do not include this parameter, the default is to use the `eventId` as the partition key.

## Syntax
<a name="aws-properties-events-rule-kinesisparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-rule-kinesisparameters-syntax.json"></a>

```
{
  "[PartitionKeyPath](#cfn-events-rule-kinesisparameters-partitionkeypath)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-rule-kinesisparameters-syntax.yaml"></a>

```
  [PartitionKeyPath](#cfn-events-rule-kinesisparameters-partitionkeypath): {{String}}
```

## Properties
<a name="aws-properties-events-rule-kinesisparameters-properties"></a>

`PartitionKeyPath`  <a name="cfn-events-rule-kinesisparameters-partitionkeypath"></a>
The JSON path to be extracted from the event and used as the partition key. For more information, see [Amazon Kinesis Streams Key Concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key) in the *Amazon Kinesis Streams Developer Guide*.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
