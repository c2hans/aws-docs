---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream IcebergDestinationConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration"></a>

 Specifies the destination configure settings for Apache Iceberg Table.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration-syntax.json"></a>

```
{
  "[AppendOnly](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-appendonly)" : {{Boolean}},
  "[BufferingHints](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-bufferinghints)" : {{BufferingHints}},
  "[CatalogConfiguration](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-catalogconfiguration)" : {{CatalogConfiguration}},
  "[CloudWatchLoggingOptions](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-cloudwatchloggingoptions)" : {{CloudWatchLoggingOptions}},
  "[DestinationTableConfigurationList](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-destinationtableconfigurationlist)" : {{[ DestinationTableConfiguration, ... ]}},
  "[ProcessingConfiguration](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-processingconfiguration)" : {{ProcessingConfiguration}},
  "[RetryOptions](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-retryoptions)" : {{RetryOptions}},
  "[RoleARN](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-rolearn)" : {{String}},
  "[s3BackupMode](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-s3backupmode)" : {{String}},
  "[S3Configuration](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-s3configuration)" : {{S3DestinationConfiguration}},
  "[SchemaEvolutionConfiguration](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-schemaevolutionconfiguration)" : {{SchemaEvolutionConfiguration}},
  "[TableCreationConfiguration](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-tablecreationconfiguration)" : {{TableCreationConfiguration}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration-syntax.yaml"></a>

```
  [AppendOnly](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-appendonly): {{Boolean}}
  [BufferingHints](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-bufferinghints): {{
    BufferingHints}}
  [CatalogConfiguration](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-catalogconfiguration): {{
    CatalogConfiguration}}
  [CloudWatchLoggingOptions](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-cloudwatchloggingoptions): {{
    CloudWatchLoggingOptions}}
  [DestinationTableConfigurationList](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-destinationtableconfigurationlist): {{
    - DestinationTableConfiguration}}
  [ProcessingConfiguration](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-processingconfiguration): {{
    ProcessingConfiguration}}
  [RetryOptions](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-retryoptions): {{
    RetryOptions}}
  [RoleARN](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-rolearn): {{String}}
  [s3BackupMode](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-s3backupmode): {{String}}
  [S3Configuration](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-s3configuration): {{
    S3DestinationConfiguration}}
  [SchemaEvolutionConfiguration](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-schemaevolutionconfiguration): {{
    SchemaEvolutionConfiguration}}
  [TableCreationConfiguration](#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-tablecreationconfiguration): {{
    TableCreationConfiguration}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration-properties"></a>

`AppendOnly`  <a name="cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-appendonly"></a>
 Describes whether all incoming data for this delivery stream will be append only (inserts only and not for updates and deletes) for Iceberg delivery. This feature is only applicable for Apache Iceberg Tables.
The default value is false. If you set this value to true, Firehose automatically increases the throughput limit of a stream based on the throttling levels of the stream. If you set this parameter to true for a stream with updates and deletes, you will see out of order delivery.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BufferingHints`  <a name="cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-bufferinghints"></a>
Property description not available.
*Required*: No
*Type*: [BufferingHints](aws-properties-kinesisfirehose-deliverystream-bufferinghints.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CatalogConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-catalogconfiguration"></a>
 Configuration describing where the destination Apache Iceberg Tables are persisted.
*Required*: Yes
*Type*: [CatalogConfiguration](aws-properties-kinesisfirehose-deliverystream-catalogconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CloudWatchLoggingOptions`  <a name="cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-cloudwatchloggingoptions"></a>
Property description not available.
*Required*: No
*Type*: [CloudWatchLoggingOptions](aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationTableConfigurationList`  <a name="cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-destinationtableconfigurationlist"></a>
 Provides a list of `DestinationTableConfigurations` which Firehose uses to deliver data to Apache Iceberg Tables. Firehose will write data with insert if table specific configuration is not provided here.
*Required*: No
*Type*: Array of [DestinationTableConfiguration](aws-properties-kinesisfirehose-deliverystream-destinationtableconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcessingConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-processingconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [ProcessingConfiguration](aws-properties-kinesisfirehose-deliverystream-processingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryOptions`  <a name="cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-retryoptions"></a>
Property description not available.
*Required*: No
*Type*: [RetryOptions](aws-properties-kinesisfirehose-deliverystream-retryoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleARN`  <a name="cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-rolearn"></a>
 The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling Apache Iceberg Tables.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`s3BackupMode`  <a name="cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-s3backupmode"></a>
 Describes how Firehose will backup records. Currently,S3 backup only supports `FailedDataOnly`.
*Required*: No
*Type*: String
*Allowed values*: `AllData | FailedDataOnly`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Configuration`  <a name="cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-s3configuration"></a>
Property description not available.
*Required*: Yes
*Type*: [S3DestinationConfiguration](aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaEvolutionConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-schemaevolutionconfiguration"></a>
The configuration to enable automatic schema evolution.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: No
*Type*: [SchemaEvolutionConfiguration](aws-properties-kinesisfirehose-deliverystream-schemaevolutionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableCreationConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-tablecreationconfiguration"></a>
The configuration to enable automatic table creation.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: No
*Type*: [TableCreationConfiguration](aws-properties-kinesisfirehose-deliverystream-tablecreationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
