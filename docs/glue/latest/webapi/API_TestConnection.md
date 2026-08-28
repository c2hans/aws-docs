---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TestConnection.html
---

# TestConnection
<a name="API_TestConnection"></a>

Tests a connection to a service to validate the service credentials that you provide.

You can either provide an existing connection name or a `TestConnectionInput` for testing a non-existing connection input. Providing both at the same time will cause an error.

If the action is successful, the service sends back an HTTP 200 response.

## Request Syntax
<a name="API_TestConnection_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "ConnectionName": "{{string}}",
   "TestConnectionInput": {
      "AuthenticationConfiguration": {
         "AuthenticationType": "{{string}}",
         "BasicAuthenticationCredentials": {
            "Password": "{{string}}",
            "Username": "{{string}}"
         },
         "CustomAuthenticationCredentials": {
            "{{string}}" : "{{string}}"
         },
         "KmsKeyArn": "{{string}}",
         "OAuth2Properties": {
            "AuthorizationCodeProperties": {
               "AuthorizationCode": "{{string}}",
               "RedirectUri": "{{string}}"
            },
            "OAuth2ClientApplication": {
               "AWSManagedClientApplicationReference": "{{string}}",
               "UserManagedClientApplicationClientId": "{{string}}"
            },
            "OAuth2Credentials": {
               "AccessToken": "{{string}}",
               "JwtToken": "{{string}}",
               "RefreshToken": "{{string}}",
               "UserManagedClientApplicationClientSecret": "{{string}}"
            },
            "OAuth2GrantType": "{{string}}",
            "TokenUrl": "{{string}}",
            "TokenUrlParametersMap": {
               "{{string}}" : "{{string}}"
            }
         },
         "SecretArn": "{{string}}"
      },
      "ConnectionProperties": {
         "{{string}}" : "{{string}}"
      },
      "ConnectionType": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_TestConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_TestConnection_RequestSyntax) **   <a name="Glue-TestConnection-request-CatalogId"></a>
The catalog ID where the connection resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [ConnectionName](#API_TestConnection_RequestSyntax) **   <a name="Glue-TestConnection-request-ConnectionName"></a>
Optional. The name of the connection to test. If only name is provided, the operation will get the connection and use that for testing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [TestConnectionInput](#API_TestConnection_RequestSyntax) **   <a name="Glue-TestConnection-request-TestConnectionInput"></a>
A structure that is used to specify testing a connection to a service.
Type: [TestConnectionInput](API_TestConnectionInput.md) object
Required: No

## Response Elements
<a name="API_TestConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TestConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConflictException **
The `CreatePartitions` API was called on a table that has indexes enabled.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** FederationSourceException **
A federation source failed.
 ** FederationSourceErrorCode **
The error code of the problem.
 ** Message **
The message describing the problem.
HTTP Status Code: 400

 ** GlueEncryptionException **
An encryption operation failed.
 ** Message **
The message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_TestConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/TestConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/TestConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TestConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/TestConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TestConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/TestConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/TestConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/TestConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/TestConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TestConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
