---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolClientSecret.html
---

# DeleteUserPoolClientSecret
<a name="API_DeleteUserPoolClientSecret"></a>

Deletes a specific client secret from a user pool app client. You cannot delete the last remaining secret for an app client.

## Request Syntax
<a name="API_DeleteUserPoolClientSecret_RequestSyntax"></a>

```
{
   "ClientId": "{{string}}",
   "ClientSecretId": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteUserPoolClientSecret_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientId](#API_DeleteUserPoolClientSecret_RequestSyntax) **   <a name="CognitoUserPools-DeleteUserPoolClientSecret-request-ClientId"></a>
The ID of the app client from which you want to delete the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: Yes

 ** [ClientSecretId](#API_DeleteUserPoolClientSecret_RequestSyntax) **   <a name="CognitoUserPools-DeleteUserPoolClientSecret-request-ClientSecretId"></a>
The unique identifier of the client secret you want to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [UserPoolId](#API_DeleteUserPoolClientSecret_RequestSyntax) **   <a name="CognitoUserPools-DeleteUserPoolClientSecret-request-UserPoolId"></a>
The ID of the user pool that contains the app client.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Elements
<a name="API_DeleteUserPoolClientSecret_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteUserPoolClientSecret_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This exception is thrown when Amazon Cognito encounters an internal server error.
HTTP Status Code: 500

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** LimitExceededException **
This exception is thrown when a user exceeds the limit for a requested AWS resource.
 ** message **
The message returned when Amazon Cognito throws a limit exceeded exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteUserPoolClientSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/DeleteUserPoolClientSecret)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/DeleteUserPoolClientSecret)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DeleteUserPoolClientSecret)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/DeleteUserPoolClientSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/DeleteUserPoolClientSecret)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/DeleteUserPoolClientSecret)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/DeleteUserPoolClientSecret)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/DeleteUserPoolClientSecret)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/DeleteUserPoolClientSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/DeleteUserPoolClientSecret)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
