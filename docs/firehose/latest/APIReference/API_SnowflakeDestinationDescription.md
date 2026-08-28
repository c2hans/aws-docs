---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_SnowflakeDestinationDescription.html
---

# SnowflakeDestinationDescription
<a name="API_SnowflakeDestinationDescription"></a>

Optional Snowflake destination description

## Contents
<a name="API_SnowflakeDestinationDescription_Contents"></a>

 ** AccountUrl **   <a name="Firehose-Type-SnowflakeDestinationDescription-AccountUrl"></a>
URL for accessing your Snowflake account. This URL must include your [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier). Note that the protocol (https://) and port number are optional.
Type: String
Length Constraints: Minimum length of 24. Maximum length of 2048.
Pattern: `.+?\.snowflakecomputing\.com`
Required: No

 ** BufferingHints **   <a name="Firehose-Type-SnowflakeDestinationDescription-BufferingHints"></a>
 Describes the buffering to perform before delivering data to the Snowflake destination. If you do not specify any value, Firehose uses the default values.
Type: [SnowflakeBufferingHints](API_SnowflakeBufferingHints.md) object
Required: No

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-SnowflakeDestinationDescription-CloudWatchLoggingOptions"></a>
Describes the Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** ContentColumnName **   <a name="Firehose-Type-SnowflakeDestinationDescription-ContentColumnName"></a>
The name of the record content column
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Database **   <a name="Firehose-Type-SnowflakeDestinationDescription-Database"></a>
All data in Snowflake is maintained in databases.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** DataLoadingOption **   <a name="Firehose-Type-SnowflakeDestinationDescription-DataLoadingOption"></a>
Choose to load JSON keys mapped to table column names or choose to split the JSON payload where content is mapped to a record content column and source metadata is mapped to a record metadata column.
Type: String
Valid Values: `JSON_MAPPING | VARIANT_CONTENT_MAPPING | VARIANT_CONTENT_AND_METADATA_MAPPING`
Required: No

 ** MetaDataColumnName **   <a name="Firehose-Type-SnowflakeDestinationDescription-MetaDataColumnName"></a>
The name of the record metadata column
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-SnowflakeDestinationDescription-ProcessingConfiguration"></a>
Describes a data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-SnowflakeDestinationDescription-RetryOptions"></a>
The time period where Firehose will retry sending data to the chosen HTTP endpoint.
Type: [SnowflakeRetryOptions](API_SnowflakeRetryOptions.md) object
Required: No

 ** RoleARN **   <a name="Firehose-Type-SnowflakeDestinationDescription-RoleARN"></a>
The Amazon Resource Name (ARN) of the Snowflake role
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-SnowflakeDestinationDescription-S3BackupMode"></a>
Choose an S3 backup mode
Type: String
Valid Values: `FailedDataOnly | AllData`
Required: No

 ** S3DestinationDescription **   <a name="Firehose-Type-SnowflakeDestinationDescription-S3DestinationDescription"></a>
Describes a destination in Amazon S3.
Type: [S3DestinationDescription](API_S3DestinationDescription.md) object
Required: No

 ** Schema **   <a name="Firehose-Type-SnowflakeDestinationDescription-Schema"></a>
Each database consists of one or more schemas, which are logical groupings of database objects, such as tables and views
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** SecretsManagerConfiguration **   <a name="Firehose-Type-SnowflakeDestinationDescription-SecretsManagerConfiguration"></a>
 The configuration that defines how you access secrets for Snowflake.
Type: [SecretsManagerConfiguration](API_SecretsManagerConfiguration.md) object
Required: No

 ** SnowflakeRoleConfiguration **   <a name="Firehose-Type-SnowflakeDestinationDescription-SnowflakeRoleConfiguration"></a>
Optionally configure a Snowflake role. Otherwise the default user role will be used.
Type: [SnowflakeRoleConfiguration](API_SnowflakeRoleConfiguration.md) object
Required: No

 ** SnowflakeVpcConfiguration **   <a name="Firehose-Type-SnowflakeDestinationDescription-SnowflakeVpcConfiguration"></a>
The VPCE ID for Firehose to privately connect with Snowflake. The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see [Amazon PrivateLink & Snowflake](https://docs.snowflake.com/en/user-guide/admin-security-privatelink)
Type: [SnowflakeVpcConfiguration](API_SnowflakeVpcConfiguration.md) object
Required: No

 ** Table **   <a name="Firehose-Type-SnowflakeDestinationDescription-Table"></a>
All data in Snowflake is stored in database tables, logically structured as collections of columns and rows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** User **   <a name="Firehose-Type-SnowflakeDestinationDescription-User"></a>
User login name for the Snowflake account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_SnowflakeDestinationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/SnowflakeDestinationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/SnowflakeDestinationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/SnowflakeDestinationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
