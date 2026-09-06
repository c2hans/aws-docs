---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_OAuthClientApplicationSummary.html
---

# OAuthClientApplicationSummary
<a name="API_OAuthClientApplicationSummary"></a>

A summary of an OAuthClientApplication.

## Contents
<a name="API_OAuthClientApplicationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-OAuthClientApplicationSummary-Arn"></a>
The Amazon Resource Name (ARN) of the OAuthClientApplication.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-OAuthClientApplicationSummary-CreatedTime"></a>
The time that the OAuthClientApplication was created.
Type: Timestamp
Required: No

 ** DataSourceType **   <a name="QS-Type-OAuthClientApplicationSummary-DataSourceType"></a>
The type of data source that the OAuthClientApplication is used with. Valid values are `SNOWFLAKE`.
Type: String
Valid Values: `ADOBE_ANALYTICS | AMAZON_ELASTICSEARCH | ATHENA | AURORA | AURORA_POSTGRESQL | AWS_IOT_ANALYTICS | GITHUB | JIRA | MARIADB | MYSQL | ORACLE | POSTGRESQL | PRESTO | REDSHIFT | S3 | S3_TABLES | SALESFORCE | SERVICENOW | SNOWFLAKE | SPARK | SQLSERVER | TERADATA | TWITTER | TIMESTREAM | AMAZON_OPENSEARCH | EXASOL | DATABRICKS | STARBURST | TRINO | BIGQUERY | GOOGLESHEETS | GOOGLE_DRIVE | CONFLUENCE | SHAREPOINT | ONE_DRIVE | WEB_CRAWLER | S3_KNOWLEDGE_BASE | QBUSINESS`
Required: No

 ** IdentityProviderVpcConnectionProperties **   <a name="QS-Type-OAuthClientApplicationSummary-IdentityProviderVpcConnectionProperties"></a>
VPC connection properties.
Type: [VpcConnectionProperties](API_VpcConnectionProperties.md) object
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-OAuthClientApplicationSummary-LastUpdatedTime"></a>
The time that the OAuthClientApplication was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-OAuthClientApplicationSummary-Name"></a>
The display name of the OAuthClientApplication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** OAuthClientApplicationId **   <a name="QS-Type-OAuthClientApplicationSummary-OAuthClientApplicationId"></a>
The ID of the OAuthClientApplication. This ID is unique per AWS Region for each AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^/][^\p{Cc}]*`
Required: No

 ** OAuthClientAuthenticationType **   <a name="QS-Type-OAuthClientApplicationSummary-OAuthClientAuthenticationType"></a>
The OAuth client authentication type used by the OAuthClientApplication. Valid values are `TOKEN`.
Type: String
Valid Values: `TOKEN`
Required: No

## See Also
<a name="API_OAuthClientApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/OAuthClientApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/OAuthClientApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/OAuthClientApplicationSummary)
