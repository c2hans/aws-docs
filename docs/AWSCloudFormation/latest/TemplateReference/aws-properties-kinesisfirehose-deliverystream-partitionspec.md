---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-partitionspec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream PartitionSpec
<a name="aws-properties-kinesisfirehose-deliverystream-partitionspec"></a>

Represents how to produce partition data for a table. Partition data is produced by transforming columns in a table. Each column transform is represented by a named `PartitionField`.

Here is an example of the schema in JSON.

 `"partitionSpec": { "identity": [ {"sourceName": "column1"}, {"sourceName": "column2"}, {"sourceName": "column3"} ] }`

Amazon Data Firehose is in preview release and is subject to change.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-partitionspec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-partitionspec-syntax.json"></a>

```
{
  "[Identity](#cfn-kinesisfirehose-deliverystream-partitionspec-identity)" : {{[ PartitionField, ... ]}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-partitionspec-syntax.yaml"></a>

```
  [Identity](#cfn-kinesisfirehose-deliverystream-partitionspec-identity): {{
    - PartitionField}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-partitionspec-properties"></a>

`Identity`  <a name="cfn-kinesisfirehose-deliverystream-partitionspec-identity"></a>
 List of identity [transforms](https://iceberg.apache.org/spec/#partition-transforms) that performs an identity transformation. The transform takes the source value, and does not modify it. Result type is the source type.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: No
*Type*: Array of [PartitionField](aws-properties-kinesisfirehose-deliverystream-partitionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
