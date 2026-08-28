---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-scheduler-schedule-kinesisparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::Schedule KinesisParameters
<a name="aws-properties-scheduler-schedule-kinesisparameters"></a>

The templated target type for the Amazon Kinesis [`PutRecord`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) API operation.

## Syntax
<a name="aws-properties-scheduler-schedule-kinesisparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-scheduler-schedule-kinesisparameters-syntax.json"></a>

```
{
  "[PartitionKey](#cfn-scheduler-schedule-kinesisparameters-partitionkey)" : {{String}}
}
```

### YAML
<a name="aws-properties-scheduler-schedule-kinesisparameters-syntax.yaml"></a>

```
  [PartitionKey](#cfn-scheduler-schedule-kinesisparameters-partitionkey): {{String}}
```

## Properties
<a name="aws-properties-scheduler-schedule-kinesisparameters-properties"></a>

`PartitionKey`  <a name="cfn-scheduler-schedule-kinesisparameters-partitionkey"></a>
Specifies the shard to which EventBridge Scheduler sends the event. For more information, see [Amazon Kinesis Data Streams terminology and concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html) in the *Amazon Kinesis Streams Developer Guide*.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
