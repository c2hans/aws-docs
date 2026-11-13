---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserPoolClientSessionConfiguration.html
---

# SetUserPoolClientSessionConfiguration
<a name="API_SetUserPoolClientSessionConfiguration"></a>

Sets the session configuration for a user pool app client. The configurable client-level setting is the maximum validity period for silent reuse of an SSO session. This operation performs a full replacement of the client-level session configuration; every request parameter is required, and session tracking must be enabled for the user pool. The user pool must be in the Essentials or Plus tier. Otherwise, this operation returns a `FeatureUnavailableInTierException`.

## Request Syntax
<a name="API_SetUserPoolClientSessionConfiguration_RequestSyntax"></a>

```
{
   "ClientId": "{{string}}",
   "SSOSession": {
      "MaxValidityMinutes": {{number}}
   },
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_SetUserPoolClientSessionConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientId](#API_SetUserPoolClientSessionConfiguration_RequestSyntax) **   <a name="CognitoUserPools-SetUserPoolClientSessionConfiguration-request-ClientId"></a>
The ID of the app client that you want to configure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: Yes

 ** [SSOSession](#API_SetUserPoolClientSessionConfiguration_RequestSyntax) **   <a name="CognitoUserPools-SetUserPoolClientSessionConfiguration-request-SSOSession"></a>
The SSO session settings for the app client.
Type: [ClientSSOSessionConfigType](API_ClientSSOSessionConfigType.md) object
Required: Yes

 ** [UserPoolId](#API_SetUserPoolClientSessionConfiguration_RequestSyntax) **   <a name="CognitoUserPools-SetUserPoolClientSessionConfiguration-request-UserPoolId"></a>
The ID of the user pool that contains the app client.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_SetUserPoolClientSessionConfiguration_ResponseSyntax"></a>

```
{
   "ClientId": "string",
   "SSOSession": {
      "MaxValidityMinutes": number
   },
   "UserPoolId": "string"
}
```

## Response Elements
<a name="API_SetUserPoolClientSessionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClientId](#API_SetUserPoolClientSessionConfiguration_ResponseSyntax) **   <a name="CognitoUserPools-SetUserPoolClientSessionConfiguration-response-ClientId"></a>
The ID of the app client that the session configuration was applied to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`

 ** [SSOSession](#API_SetUserPoolClientSessionConfiguration_ResponseSyntax) **   <a name="CognitoUserPools-SetUserPoolClientSessionConfiguration-response-SSOSession"></a>
The SSO session settings that were applied to the app client.
Type: [ClientSSOSessionConfigType](API_ClientSSOSessionConfigType.md) object

 ** [UserPoolId](#API_SetUserPoolClientSessionConfiguration_ResponseSyntax) **   <a name="CognitoUserPools-SetUserPoolClientSessionConfiguration-response-UserPoolId"></a>
The ID of the user pool that contains the app client.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`

## Errors
<a name="API_SetUserPoolClientSessionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
This exception is thrown if two or more modifications are happening concurrently.
 ** message **
The message provided when the concurrent exception is thrown.
HTTP Status Code: 400

 ** FeatureUnavailableInTierException **
This exception is thrown when a feature that you attempted to use or configure isn't included in your user pool's current feature plan. This can occur when:
+ You configure a feature that your feature plan doesn't support.
+ You make a request that uses a feature that requires a higher feature plan.
To resolve this issue, upgrade your user pool to a feature plan that includes the feature.
HTTP Status Code: 400

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.
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
<a name="API_SetUserPoolClientSessionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/SetUserPoolClientSessionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/SetUserPoolClientSessionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SetUserPoolClientSessionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/SetUserPoolClientSessionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SetUserPoolClientSessionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/SetUserPoolClientSessionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/SetUserPoolClientSessionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/SetUserPoolClientSessionConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/SetUserPoolClientSessionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SetUserPoolClientSessionConfiguration)
