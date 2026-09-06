---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_OAuthClientApplication.html
---

# OAuthClientApplication
<a name="API_OAuthClientApplication"></a>

An OAuth client application that is used to authenticate connections to a data source through an OAuth identity provider.

## Contents
<a name="API_OAuthClientApplication_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-OAuthClientApplication-Arn"></a>
The Amazon Resource Name (ARN) of the OAuthClientApplication.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-OAuthClientApplication-CreatedTime"></a>
The time that the OAuthClientApplication was created.
Type: Timestamp
Required: No

 ** DataSourceType **   <a name="QS-Type-OAuthClientApplication-DataSourceType"></a>
The type of data source that the OAuthClientApplication is used with. Valid values are `SNOWFLAKE`.
Type: String
Valid Values: `ADOBE_ANALYTICS | AMAZON_ELASTICSEARCH | ATHENA | AURORA | AURORA_POSTGRESQL | AWS_IOT_ANALYTICS | GITHUB | JIRA | MARIADB | MYSQL | ORACLE | POSTGRESQL | PRESTO | REDSHIFT | S3 | S3_TABLES | SALESFORCE | SERVICENOW | SNOWFLAKE | SPARK | SQLSERVER | TERADATA | TWITTER | TIMESTREAM | AMAZON_OPENSEARCH | EXASOL | DATABRICKS | STARBURST | TRINO | BIGQUERY | GOOGLESHEETS | GOOGLE_DRIVE | CONFLUENCE | SHAREPOINT | ONE_DRIVE | WEB_CRAWLER | S3_KNOWLEDGE_BASE | QBUSINESS`
Required: No

 ** IdentityProviderVpcConnectionProperties **   <a name="QS-Type-OAuthClientApplication-IdentityProviderVpcConnectionProperties"></a>
VPC connection properties.
Type: [VpcConnectionProperties](API_VpcConnectionProperties.md) object
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-OAuthClientApplication-LastUpdatedTime"></a>
The time that the OAuthClientApplication was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-OAuthClientApplication-Name"></a>
The display name of the OAuthClientApplication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** OAuthAuthorizationEndpointUrl **   <a name="QS-Type-OAuthClientApplication-OAuthAuthorizationEndpointUrl"></a>
The authorization endpoint URL of the identity provider that is used to obtain authorization codes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^https://[^\p{Cc}]+`
Required: No

 ** OAuthClientApplicationId **   <a name="QS-Type-OAuthClientApplication-OAuthClientApplicationId"></a>
The ID of the OAuthClientApplication. This ID is unique per AWS Region for each AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^/][^\p{Cc}]*`
Required: No

 ** OAuthClientAuthenticationType **   <a name="QS-Type-OAuthClientApplication-OAuthClientAuthenticationType"></a>
The OAuth client authentication type used by the OAuthClientApplication. Valid values are `TOKEN`.
Type: String
Valid Values: `TOKEN`
Required: No

 ** OAuthScopes **   <a name="QS-Type-OAuthClientApplication-OAuthScopes"></a>
The OAuth scopes that are requested when the OAuthClientApplication obtains an access token from the identity provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[^\p{Cc}]+`
Required: No

 ** OAuthTokenEndpointUrl **   <a name="QS-Type-OAuthClientApplication-OAuthTokenEndpointUrl"></a>
The token endpoint URL of the identity provider that is used to obtain access tokens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^https://[^\p{Cc}]+`
Required: No

## See Also
<a name="API_OAuthClientApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/OAuthClientApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/OAuthClientApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/OAuthClientApplication)
