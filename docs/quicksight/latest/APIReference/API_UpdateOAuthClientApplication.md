---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateOAuthClientApplication.html
---

# UpdateOAuthClientApplication
<a name="API_UpdateOAuthClientApplication"></a>

Updates an OAuthClientApplication.

## Request Syntax
<a name="API_UpdateOAuthClientApplication_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/oauth-client-applications/{{OAuthClientApplicationId}} HTTP/1.1
Content-type: application/json

{
   "ClientId": "{{string}}",
   "ClientSecret": "{{string}}",
   "DataSourceType": "{{string}}",
   "IdentityProviderVpcConnectionProperties": {
      "VpcConnectionArn": "{{string}}"
   },
   "Name": "{{string}}",
   "OAuthAuthorizationEndpointUrl": "{{string}}",
   "OAuthScopes": "{{string}}",
   "OAuthTokenEndpointUrl": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateOAuthClientApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateOAuthClientApplication_RequestSyntax) **   <a name="QS-UpdateOAuthClientApplication-request-uri-AwsAccountId"></a>
The AWS account ID.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [OAuthClientApplicationId](#API_UpdateOAuthClientApplication_RequestSyntax) **   <a name="QS-UpdateOAuthClientApplication-request-uri-OAuthClientApplicationId"></a>
The ID of the OAuthClientApplication that you want to update.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^/][^\p{Cc}]*`
Required: Yes

## Request Body
<a name="API_UpdateOAuthClientApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_UpdateOAuthClientApplication_RequestSyntax) **   <a name="QS-UpdateOAuthClientApplication-request-Name"></a>
The display name for the OAuthClientApplication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [ClientId](#API_UpdateOAuthClientApplication_RequestSyntax) **   <a name="QS-UpdateOAuthClientApplication-request-ClientId"></a>
The client ID of the OAuth application that is registered with the identity provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\p{Cc}]+`
Required: No

 ** [ClientSecret](#API_UpdateOAuthClientApplication_RequestSyntax) **   <a name="QS-UpdateOAuthClientApplication-request-ClientSecret"></a>
The client secret of the OAuth application that is registered with the identity provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\p{Cc}]+`
Required: No

 ** [DataSourceType](#API_UpdateOAuthClientApplication_RequestSyntax) **   <a name="QS-UpdateOAuthClientApplication-request-DataSourceType"></a>
The type of data source that the OAuthClientApplication is used with. Valid values are `SNOWFLAKE`.
Type: String
Valid Values: `ADOBE_ANALYTICS | AMAZON_ELASTICSEARCH | ATHENA | AURORA | AURORA_POSTGRESQL | AWS_IOT_ANALYTICS | GITHUB | JIRA | MARIADB | MYSQL | ORACLE | POSTGRESQL | PRESTO | REDSHIFT | S3 | S3_TABLES | SALESFORCE | SERVICENOW | SNOWFLAKE | SPARK | SQLSERVER | TERADATA | TWITTER | TIMESTREAM | AMAZON_OPENSEARCH | EXASOL | DATABRICKS | STARBURST | TRINO | BIGQUERY | GOOGLESHEETS | GOOGLE_DRIVE | CONFLUENCE | SHAREPOINT | ONE_DRIVE | WEB_CRAWLER | S3_KNOWLEDGE_BASE | QBUSINESS`
Required: No

 ** [IdentityProviderVpcConnectionProperties](#API_UpdateOAuthClientApplication_RequestSyntax) **   <a name="QS-UpdateOAuthClientApplication-request-IdentityProviderVpcConnectionProperties"></a>
VPC connection properties.
Type: [VpcConnectionProperties](API_VpcConnectionProperties.md) object
Required: No

 ** [OAuthAuthorizationEndpointUrl](#API_UpdateOAuthClientApplication_RequestSyntax) **   <a name="QS-UpdateOAuthClientApplication-request-OAuthAuthorizationEndpointUrl"></a>
The authorization endpoint URL of the identity provider that is used to obtain authorization codes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^https://[^\p{Cc}]+`
Required: No

 ** [OAuthScopes](#API_UpdateOAuthClientApplication_RequestSyntax) **   <a name="QS-UpdateOAuthClientApplication-request-OAuthScopes"></a>
The OAuth scopes that are requested when the OAuthClientApplication obtains an access token from the identity provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[^\p{Cc}]+`
Required: No

 ** [OAuthTokenEndpointUrl](#API_UpdateOAuthClientApplication_RequestSyntax) **   <a name="QS-UpdateOAuthClientApplication-request-OAuthTokenEndpointUrl"></a>
The token endpoint URL of the identity provider that is used to obtain access tokens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^https://[^\p{Cc}]+`
Required: No

## Response Syntax
<a name="API_UpdateOAuthClientApplication_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "OAuthClientApplicationId": "string",
   "RequestId": "string",
   "UpdateStatus": "string"
}
```

## Response Elements
<a name="API_UpdateOAuthClientApplication_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateOAuthClientApplication_ResponseSyntax) **   <a name="QS-UpdateOAuthClientApplication-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateOAuthClientApplication_ResponseSyntax) **   <a name="QS-UpdateOAuthClientApplication-response-Arn"></a>
The Amazon Resource Name (ARN) of the OAuthClientApplication.
Type: String

 ** [OAuthClientApplicationId](#API_UpdateOAuthClientApplication_ResponseSyntax) **   <a name="QS-UpdateOAuthClientApplication-response-OAuthClientApplicationId"></a>
The ID of the OAuthClientApplication. This ID is unique per AWS Region for each AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^/][^\p{Cc}]*`

 ** [RequestId](#API_UpdateOAuthClientApplication_ResponseSyntax) **   <a name="QS-UpdateOAuthClientApplication-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [UpdateStatus](#API_UpdateOAuthClientApplication_ResponseSyntax) **   <a name="QS-UpdateOAuthClientApplication-response-UpdateStatus"></a>
The status of updating the OAuthClientApplication.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`

## Errors
<a name="API_UpdateOAuthClientApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateOAuthClientApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateOAuthClientApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateOAuthClientApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateOAuthClientApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateOAuthClientApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateOAuthClientApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateOAuthClientApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateOAuthClientApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateOAuthClientApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateOAuthClientApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateOAuthClientApplication)
