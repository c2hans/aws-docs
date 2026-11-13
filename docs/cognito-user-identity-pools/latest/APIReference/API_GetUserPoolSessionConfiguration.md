---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUserPoolSessionConfiguration.html
---

# GetUserPoolSessionConfiguration
<a name="API_GetUserPoolSessionConfiguration"></a>

Retrieves the session tracking configuration for a user pool, including whether session tracking is enabled and the pool-wide maximum number of active token sessions for each user. If you have never called `SetUserPoolSessionConfiguration` for the user pool, this operation returns the default values: `UserSessionTracking` as `DISABLED` and a `MaxPerUser` value of `20`.

## Request Syntax
<a name="API_GetUserPoolSessionConfiguration_RequestSyntax"></a>

```
{
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetUserPoolSessionConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [UserPoolId](#API_GetUserPoolSessionConfiguration_RequestSyntax) **   <a name="CognitoUserPools-GetUserPoolSessionConfiguration-request-UserPoolId"></a>
The ID of the user pool where you want to retrieve the session configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_GetUserPoolSessionConfiguration_ResponseSyntax"></a>

```
{
   "TokenSession": {
      "MaxPerUser": number
   },
   "UserPoolId": "string",
   "UserSessionTracking": "string"
}
```

## Response Elements
<a name="API_GetUserPoolSessionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TokenSession](#API_GetUserPoolSessionConfiguration_ResponseSyntax) **   <a name="CognitoUserPools-GetUserPoolSessionConfiguration-response-TokenSession"></a>
The pool-wide token session settings for the user pool.
Type: [UserPoolTokenSessionConfigType](API_UserPoolTokenSessionConfigType.md) object

 ** [UserPoolId](#API_GetUserPoolSessionConfiguration_ResponseSyntax) **   <a name="CognitoUserPools-GetUserPoolSessionConfiguration-response-UserPoolId"></a>
The ID of the user pool that the session configuration applies to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`

 ** [UserSessionTracking](#API_GetUserPoolSessionConfiguration_ResponseSyntax) **   <a name="CognitoUserPools-GetUserPoolSessionConfiguration-response-UserSessionTracking"></a>
Indicates whether session tracking is enabled for the user pool.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_GetUserPoolSessionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetUserPoolSessionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/GetUserPoolSessionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/GetUserPoolSessionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/GetUserPoolSessionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/GetUserPoolSessionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/GetUserPoolSessionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/GetUserPoolSessionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/GetUserPoolSessionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/GetUserPoolSessionConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/GetUserPoolSessionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/GetUserPoolSessionConfiguration)
