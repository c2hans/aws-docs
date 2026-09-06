---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_SnowflakeDestinationConfiguration.html
---

# SnowflakeDestinationConfiguration
<a name="API_SnowflakeDestinationConfiguration"></a>

Configure Snowflake destination

## Contents
<a name="API_SnowflakeDestinationConfiguration_Contents"></a>

 ** AccountUrl **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-AccountUrl"></a>
URL for accessing your Snowflake account. This URL must include your [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier). Note that the protocol (https://) and port number are optional.
Type: String
Length Constraints: Minimum length of 24. Maximum length of 2048.
Pattern: `.+?\.snowflakecomputing\.com`
Required: Yes

 ** Database **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-Database"></a>
All data in Snowflake is maintained in databases.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** RoleARN **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-RoleARN"></a>
The Amazon Resource Name (ARN) of the Snowflake role
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** S3Configuration **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-S3Configuration"></a>
Describes the configuration of a destination in Amazon S3.
Type: [S3DestinationConfiguration](API_S3DestinationConfiguration.md) object
Required: Yes

 ** Schema **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-Schema"></a>
Each database consists of one or more schemas, which are logical groupings of database objects, such as tables and views
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Table **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-Table"></a>
All data in Snowflake is stored in database tables, logically structured as collections of columns and rows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** BufferingHints **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-BufferingHints"></a>
 Describes the buffering to perform before delivering data to the Snowflake destination. If you do not specify any value, Firehose uses the default values.
Type: [SnowflakeBufferingHints](API_SnowflakeBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-CloudWatchLoggingOptions"></a>
Describes the Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** ContentColumnName **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-ContentColumnName"></a>
The name of the record content column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** DataLoadingOption **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-DataLoadingOption"></a>
Choose to load JSON keys mapped to table column names or choose to split the JSON payload where content is mapped to a record content column and source metadata is mapped to a record metadata column.
Type: String
Valid Values: `JSON_MAPPING | VARIANT_CONTENT_MAPPING | VARIANT_CONTENT_AND_METADATA_MAPPING`
Required: No

 ** KeyPassphrase **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-KeyPassphrase"></a>
Passphrase to decrypt the private key when the key is encrypted. For information, see [Using Key Pair Authentication & Key Rotation](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation).
Type: String
Length Constraints: Minimum length of 7. Maximum length of 255.
Required: No

 ** MetaDataColumnName **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-MetaDataColumnName"></a>
Specify a column name in the table, where the metadata information has to be loaded. When you enable this field, you will see the following column in the snowflake table, which differs based on the source type.
For Direct PUT as source
 `{ "firehoseDeliveryStreamName" : "streamname", "IngestionTime" : "timestamp" }`
For Kinesis Data Stream as source
 ` "kinesisStreamName" : "streamname", "kinesisShardId" : "Id", "kinesisPartitionKey" : "key", "kinesisSequenceNumber" : "1234", "subsequenceNumber" : "2334", "IngestionTime" : "timestamp" }`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** PrivateKey **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-PrivateKey"></a>
The private key used to encrypt your Snowflake client. For information, see [Using Key Pair Authentication & Key Rotation](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation).
Type: String
Length Constraints: Minimum length of 256. Maximum length of 4096.
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-ProcessingConfiguration"></a>
Describes a data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-RetryOptions"></a>
The time period where Firehose will retry sending data to the chosen HTTP endpoint.
Type: [SnowflakeRetryOptions](API_SnowflakeRetryOptions.md) object
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-S3BackupMode"></a>
Choose an S3 backup mode
Type: String
Valid Values: `FailedDataOnly | AllData`
Required: No

 ** SecretsManagerConfiguration **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-SecretsManagerConfiguration"></a>
 The configuration that defines how you access secrets for Snowflake.
Type: [SecretsManagerConfiguration](API_SecretsManagerConfiguration.md) object
Required: No

 ** SnowflakeRoleConfiguration **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-SnowflakeRoleConfiguration"></a>
Optionally configure a Snowflake role. Otherwise the default user role will be used.
Type: [SnowflakeRoleConfiguration](API_SnowflakeRoleConfiguration.md) object
Required: No

 ** SnowflakeVpcConfiguration **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-SnowflakeVpcConfiguration"></a>
The VPCE ID for Firehose to privately connect with Snowflake. The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see [Amazon PrivateLink & Snowflake](https://docs.snowflake.com/en/user-guide/admin-security-privatelink)
Type: [SnowflakeVpcConfiguration](API_SnowflakeVpcConfiguration.md) object
Required: No

 ** User **   <a name="Firehose-Type-SnowflakeDestinationConfiguration-User"></a>
User login name for the Snowflake account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_SnowflakeDestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/SnowflakeDestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/SnowflakeDestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/SnowflakeDestinationConfiguration)
