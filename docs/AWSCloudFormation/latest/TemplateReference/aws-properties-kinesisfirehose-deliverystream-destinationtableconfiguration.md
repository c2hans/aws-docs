---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-destinationtableconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream DestinationTableConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-destinationtableconfiguration"></a>

 Describes the configuration of a destination in Apache Iceberg Tables. This section is only needed for tables where you want to update or delete data.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-destinationtableconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-destinationtableconfiguration-syntax.json"></a>

```
{
  "[DestinationDatabaseName](#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-destinationdatabasename)" : {{String}},
  "[DestinationTableName](#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-destinationtablename)" : {{String}},
  "[PartitionSpec](#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-partitionspec)" : {{PartitionSpec}},
  "[S3ErrorOutputPrefix](#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-s3erroroutputprefix)" : {{String}},
  "[UniqueKeys](#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-uniquekeys)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-destinationtableconfiguration-syntax.yaml"></a>

```
  [DestinationDatabaseName](#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-destinationdatabasename): {{String}}
  [DestinationTableName](#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-destinationtablename): {{String}}
  [PartitionSpec](#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-partitionspec): {{
    PartitionSpec}}
  [S3ErrorOutputPrefix](#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-s3erroroutputprefix): {{String}}
  [UniqueKeys](#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-uniquekeys): {{
    - String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-destinationtableconfiguration-properties"></a>

`DestinationDatabaseName`  <a name="cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-destinationdatabasename"></a>
 The name of the Apache Iceberg database.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationTableName`  <a name="cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-destinationtablename"></a>
 Specifies the name of the Apache Iceberg Table.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartitionSpec`  <a name="cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-partitionspec"></a>
The partition spec configuration for a table that is used by automatic table creation.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: No
*Type*: [PartitionSpec](aws-properties-kinesisfirehose-deliverystream-partitionspec.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3ErrorOutputPrefix`  <a name="cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-s3erroroutputprefix"></a>
 The table specific S3 error output prefix. All the errors that occurred while delivering to this table will be prefixed with this value in S3 destination.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UniqueKeys`  <a name="cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-uniquekeys"></a>
 A list of unique keys for a given Apache Iceberg table. Firehose will use these for running Create, Update, or Delete operations on the given Iceberg table.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
