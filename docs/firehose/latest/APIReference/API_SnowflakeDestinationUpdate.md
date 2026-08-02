---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_SnowflakeDestinationUpdate.html
---

# SnowflakeDestinationUpdate
<a name="API_SnowflakeDestinationUpdate"></a>

Update to configuration settings

## Contents
<a name="API_SnowflakeDestinationUpdate_Contents"></a>

 ** AccountUrl **   <a name="Firehose-Type-SnowflakeDestinationUpdate-AccountUrl"></a>
URL for accessing your Snowflake account. This URL must include your [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier). Note that the protocol (https://) and port number are optional.
Type: String
Length Constraints: Minimum length of 24. Maximum length of 2048.
Pattern: `.+?\.snowflakecomputing\.com`
Required: No

 ** BufferingHints **   <a name="Firehose-Type-SnowflakeDestinationUpdate-BufferingHints"></a>
 Describes the buffering to perform before delivering data to the Snowflake destination.
Type: [SnowflakeBufferingHints](API_SnowflakeBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-SnowflakeDestinationUpdate-CloudWatchLoggingOptions"></a>
Describes the Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** ContentColumnName **   <a name="Firehose-Type-SnowflakeDestinationUpdate-ContentColumnName"></a>
The name of the content metadata column
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Database **   <a name="Firehose-Type-SnowflakeDestinationUpdate-Database"></a>
All data in Snowflake is maintained in databases.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** DataLoadingOption **   <a name="Firehose-Type-SnowflakeDestinationUpdate-DataLoadingOption"></a>
 JSON keys mapped to table column names or choose to split the JSON payload where content is mapped to a record content column and source metadata is mapped to a record metadata column.
Type: String
Valid Values: `JSON_MAPPING | VARIANT_CONTENT_MAPPING | VARIANT_CONTENT_AND_METADATA_MAPPING`
Required: No

 ** KeyPassphrase **   <a name="Firehose-Type-SnowflakeDestinationUpdate-KeyPassphrase"></a>
Passphrase to decrypt the private key when the key is encrypted. For information, see [Using Key Pair Authentication & Key Rotation](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation).
Type: String
Length Constraints: Minimum length of 7. Maximum length of 255.
Required: No

 ** MetaDataColumnName **   <a name="Firehose-Type-SnowflakeDestinationUpdate-MetaDataColumnName"></a>
The name of the record metadata column
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** PrivateKey **   <a name="Firehose-Type-SnowflakeDestinationUpdate-PrivateKey"></a>
The private key used to encrypt your Snowflake client. For information, see [Using Key Pair Authentication & Key Rotation](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation).
Type: String
Length Constraints: Minimum length of 256. Maximum length of 4096.
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-SnowflakeDestinationUpdate-ProcessingConfiguration"></a>
Describes a data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-SnowflakeDestinationUpdate-RetryOptions"></a>
Specify how long Firehose retries sending data to the New Relic HTTP endpoint. After sending data, Firehose first waits for an acknowledgment from the HTTP endpoint. If an error occurs or the acknowledgment doesn’t arrive within the acknowledgment timeout period, Firehose starts the retry duration counter. It keeps retrying until the retry duration expires. After that, Firehose considers it a data delivery failure and backs up the data to your Amazon S3 bucket. Every time that Firehose sends data to the HTTP endpoint (either the initial attempt or a retry), it restarts the acknowledgement timeout counter and waits for an acknowledgement from the HTTP endpoint. Even if the retry duration expires, Firehose still waits for the acknowledgment until it receives it or the acknowledgement timeout period is reached. If the acknowledgment times out, Firehose determines whether there's time left in the retry counter. If there is time left, it retries again and repeats the logic until it receives an acknowledgment or determines that the retry time has expired. If you don't want Firehose to retry sending data, set this value to 0.
Type: [SnowflakeRetryOptions](API_SnowflakeRetryOptions.md) object
Required: No

 ** RoleARN **   <a name="Firehose-Type-SnowflakeDestinationUpdate-RoleARN"></a>
The Amazon Resource Name (ARN) of the Snowflake role
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-SnowflakeDestinationUpdate-S3BackupMode"></a>
Choose an S3 backup mode. Once you set the mode as `AllData`, you can not change it to `FailedDataOnly`.
Type: String
Valid Values: `FailedDataOnly | AllData`
Required: No

 ** S3Update **   <a name="Firehose-Type-SnowflakeDestinationUpdate-S3Update"></a>
Describes an update for a destination in Amazon S3.
Type: [S3DestinationUpdate](API_S3DestinationUpdate.md) object
Required: No

 ** Schema **   <a name="Firehose-Type-SnowflakeDestinationUpdate-Schema"></a>
Each database consists of one or more schemas, which are logical groupings of database objects, such as tables and views
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** SecretsManagerConfiguration **   <a name="Firehose-Type-SnowflakeDestinationUpdate-SecretsManagerConfiguration"></a>
 Describes the Secrets Manager configuration in Snowflake.
Type: [SecretsManagerConfiguration](API_SecretsManagerConfiguration.md) object
Required: No

 ** SnowflakeRoleConfiguration **   <a name="Firehose-Type-SnowflakeDestinationUpdate-SnowflakeRoleConfiguration"></a>
Optionally configure a Snowflake role. Otherwise the default user role will be used.
Type: [SnowflakeRoleConfiguration](API_SnowflakeRoleConfiguration.md) object
Required: No

 ** Table **   <a name="Firehose-Type-SnowflakeDestinationUpdate-Table"></a>
All data in Snowflake is stored in database tables, logically structured as collections of columns and rows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** User **   <a name="Firehose-Type-SnowflakeDestinationUpdate-User"></a>
User login name for the Snowflake account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_SnowflakeDestinationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/SnowflakeDestinationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/SnowflakeDestinationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/SnowflakeDestinationUpdate)
