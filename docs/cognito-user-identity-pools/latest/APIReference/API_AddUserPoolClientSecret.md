---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AddUserPoolClientSecret.html
---

# AddUserPoolClientSecret
<a name="API_AddUserPoolClientSecret"></a>

Creates a new client secret for an existing confidential user pool app client. Supports up to 2 active secrets per app client for zero-downtime credential rotation workflows.

## Request Syntax
<a name="API_AddUserPoolClientSecret_RequestSyntax"></a>

```
{
   "ClientId": "{{string}}",
   "ClientSecret": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AddUserPoolClientSecret_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientId](#API_AddUserPoolClientSecret_RequestSyntax) **   <a name="CognitoUserPools-AddUserPoolClientSecret-request-ClientId"></a>
The ID of the app client for which you want to create a new secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: Yes

 ** [ClientSecret](#API_AddUserPoolClientSecret_RequestSyntax) **   <a name="CognitoUserPools-AddUserPoolClientSecret-request-ClientSecret"></a>
The client secret value you want to use. If you don't provide this parameter, Amazon Cognito generates a secure secret for you.
Type: String
Length Constraints: Minimum length of 24. Maximum length of 64.
Pattern: `[\w+]+`
Required: No

 ** [UserPoolId](#API_AddUserPoolClientSecret_RequestSyntax) **   <a name="CognitoUserPools-AddUserPoolClientSecret-request-UserPoolId"></a>
The ID of the user pool that contains the app client.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_AddUserPoolClientSecret_ResponseSyntax"></a>

```
{
   "ClientSecretDescriptor": {
      "ClientSecretCreateDate": number,
      "ClientSecretId": "string",
      "ClientSecretValue": "string"
   }
}
```

## Response Elements
<a name="API_AddUserPoolClientSecret_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClientSecretDescriptor](#API_AddUserPoolClientSecret_ResponseSyntax) **   <a name="CognitoUserPools-AddUserPoolClientSecret-response-ClientSecretDescriptor"></a>
The details of the newly created client secret, including its unique identifier and creation timestamp. The ClientSecretValue is only returned when Amazon Cognito generates the secret. For custom secrets that you provide, the ClientSecretValue is not included in the response.
Type: [ClientSecretDescriptorType](API_ClientSecretDescriptorType.md) object

## Errors
<a name="API_AddUserPoolClientSecret_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This exception is thrown when you don't have sufficient permissions to perform the requested operation.
HTTP Status Code: 400

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
<a name="API_AddUserPoolClientSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AddUserPoolClientSecret)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AddUserPoolClientSecret)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AddUserPoolClientSecret)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AddUserPoolClientSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AddUserPoolClientSecret)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AddUserPoolClientSecret)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AddUserPoolClientSecret)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AddUserPoolClientSecret)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AddUserPoolClientSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AddUserPoolClientSecret)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
