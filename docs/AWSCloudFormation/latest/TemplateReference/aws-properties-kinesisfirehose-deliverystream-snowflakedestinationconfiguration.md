---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream SnowflakeDestinationConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration"></a>

Configure Snowflake destination

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-syntax.json"></a>

```
{
  "[AccountUrl](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-accounturl)" : {{String}},
  "[BufferingHints](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-bufferinghints)" : {{SnowflakeBufferingHints}},
  "[CloudWatchLoggingOptions](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-cloudwatchloggingoptions)" : {{CloudWatchLoggingOptions}},
  "[ContentColumnName](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-contentcolumnname)" : {{String}},
  "[Database](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-database)" : {{String}},
  "[DataLoadingOption](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-dataloadingoption)" : {{String}},
  "[KeyPassphrase](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-keypassphrase)" : {{String}},
  "[MetaDataColumnName](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-metadatacolumnname)" : {{String}},
  "[PrivateKey](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-privatekey)" : {{String}},
  "[ProcessingConfiguration](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-processingconfiguration)" : {{ProcessingConfiguration}},
  "[RetryOptions](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-retryoptions)" : {{SnowflakeRetryOptions}},
  "[RoleARN](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-rolearn)" : {{String}},
  "[S3BackupMode](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-s3backupmode)" : {{String}},
  "[S3Configuration](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-s3configuration)" : {{S3DestinationConfiguration}},
  "[Schema](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-schema)" : {{String}},
  "[SecretsManagerConfiguration](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-secretsmanagerconfiguration)" : {{SecretsManagerConfiguration}},
  "[SnowflakeRoleConfiguration](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-snowflakeroleconfiguration)" : {{SnowflakeRoleConfiguration}},
  "[SnowflakeVpcConfiguration](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-snowflakevpcconfiguration)" : {{SnowflakeVpcConfiguration}},
  "[Table](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-table)" : {{String}},
  "[User](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-user)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-syntax.yaml"></a>

```
  [AccountUrl](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-accounturl): {{String}}
  [BufferingHints](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-bufferinghints): {{
    SnowflakeBufferingHints}}
  [CloudWatchLoggingOptions](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-cloudwatchloggingoptions): {{
    CloudWatchLoggingOptions}}
  [ContentColumnName](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-contentcolumnname): {{String}}
  [Database](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-database): {{String}}
  [DataLoadingOption](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-dataloadingoption): {{String}}
  [KeyPassphrase](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-keypassphrase): {{String}}
  [MetaDataColumnName](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-metadatacolumnname): {{String}}
  [PrivateKey](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-privatekey): {{String}}
  [ProcessingConfiguration](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-processingconfiguration): {{
    ProcessingConfiguration}}
  [RetryOptions](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-retryoptions): {{
    SnowflakeRetryOptions}}
  [RoleARN](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-rolearn): {{String}}
  [S3BackupMode](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-s3backupmode): {{String}}
  [S3Configuration](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-s3configuration): {{
    S3DestinationConfiguration}}
  [Schema](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-schema): {{String}}
  [SecretsManagerConfiguration](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-secretsmanagerconfiguration): {{
    SecretsManagerConfiguration}}
  [SnowflakeRoleConfiguration](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-snowflakeroleconfiguration): {{
    SnowflakeRoleConfiguration}}
  [SnowflakeVpcConfiguration](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-snowflakevpcconfiguration): {{
    SnowflakeVpcConfiguration}}
  [Table](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-table): {{String}}
  [User](#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-user): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-properties"></a>

`AccountUrl`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-accounturl"></a>
URL for accessing your Snowflake account. This URL must include your [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier). Note that the protocol (https://) and port number are optional.
*Required*: Yes
*Type*: String
*Pattern*: `.+?\.snowflakecomputing\.com`
*Minimum*: `24`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BufferingHints`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-bufferinghints"></a>
 Describes the buffering to perform before delivering data to the Snowflake destination. If you do not specify any value, Firehose uses the default values.
*Required*: No
*Type*: [SnowflakeBufferingHints](aws-properties-kinesisfirehose-deliverystream-snowflakebufferinghints.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CloudWatchLoggingOptions`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-cloudwatchloggingoptions"></a>
Property description not available.
*Required*: No
*Type*: [CloudWatchLoggingOptions](aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentColumnName`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-contentcolumnname"></a>
The name of the record content column.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Database`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-database"></a>
All data in Snowflake is maintained in databases.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataLoadingOption`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-dataloadingoption"></a>
Choose to load JSON keys mapped to table column names or choose to split the JSON payload where content is mapped to a record content column and source metadata is mapped to a record metadata column.
*Required*: No
*Type*: String
*Allowed values*: `JSON_MAPPING | VARIANT_CONTENT_MAPPING | VARIANT_CONTENT_AND_METADATA_MAPPING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyPassphrase`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-keypassphrase"></a>
Passphrase to decrypt the private key when the key is encrypted. For information, see [Using Key Pair Authentication & Key Rotation](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation).
*Required*: No
*Type*: String
*Minimum*: `7`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetaDataColumnName`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-metadatacolumnname"></a>
Specify a column name in the table, where the metadata information has to be loaded. When you enable this field, you will see the following column in the snowflake table, which differs based on the source type.
For Direct PUT as source
 `{ "firehoseDeliveryStreamName" : "streamname", "IngestionTime" : "timestamp" }`
For Kinesis Data Stream as source
 ` "kinesisStreamName" : "streamname", "kinesisShardId" : "Id", "kinesisPartitionKey" : "key", "kinesisSequenceNumber" : "1234", "subsequenceNumber" : "2334", "IngestionTime" : "timestamp" }`
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateKey`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-privatekey"></a>
The private key used to encrypt your Snowflake client. For information, see [Using Key Pair Authentication & Key Rotation](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation).
*Required*: No
*Type*: String
*Pattern*: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`
*Minimum*: `256`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcessingConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-processingconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [ProcessingConfiguration](aws-properties-kinesisfirehose-deliverystream-processingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryOptions`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-retryoptions"></a>
The time period where Firehose will retry sending data to the chosen HTTP endpoint.
*Required*: No
*Type*: [SnowflakeRetryOptions](aws-properties-kinesisfirehose-deliverystream-snowflakeretryoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleARN`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-rolearn"></a>
The Amazon Resource Name (ARN) of the Snowflake role
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BackupMode`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-s3backupmode"></a>
Choose an S3 backup mode
*Required*: No
*Type*: String
*Allowed values*: `FailedDataOnly | AllData`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Configuration`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-s3configuration"></a>
Property description not available.
*Required*: Yes
*Type*: [S3DestinationConfiguration](aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schema`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-schema"></a>
Each database consists of one or more schemas, which are logical groupings of database objects, such as tables and views
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManagerConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-secretsmanagerconfiguration"></a>
 The configuration that defines how you access secrets for Snowflake.
*Required*: No
*Type*: [SecretsManagerConfiguration](aws-properties-kinesisfirehose-deliverystream-secretsmanagerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnowflakeRoleConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-snowflakeroleconfiguration"></a>
Optionally configure a Snowflake role. Otherwise the default user role will be used.
*Required*: No
*Type*: [SnowflakeRoleConfiguration](aws-properties-kinesisfirehose-deliverystream-snowflakeroleconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnowflakeVpcConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-snowflakevpcconfiguration"></a>
The VPCE ID for Firehose to privately connect with Snowflake. The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see [Amazon PrivateLink & Snowflake](https://docs.snowflake.com/en/user-guide/admin-security-privatelink)
*Required*: No
*Type*: [SnowflakeVpcConfiguration](aws-properties-kinesisfirehose-deliverystream-snowflakevpcconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Table`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-table"></a>
All data in Snowflake is stored in database tables, logically structured as collections of columns and rows.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`User`  <a name="cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-user"></a>
User login name for the Snowflake account.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
