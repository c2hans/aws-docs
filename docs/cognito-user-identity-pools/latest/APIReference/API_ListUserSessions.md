---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserSessions.html
---

# ListUserSessions
<a name="API_ListUserSessions"></a>

Lists the active sessions for the currently signed-in user. Amazon Cognito authorizes this operation with the user's access token and returns all of the user's active sessions across every app client in the user pool, including both token sessions and SSO sessions. The `IsCurrentSession` field identifies the session that the calling access token belongs to. The results are eventually consistent, and new sessions are typically included within a few seconds.

## Request Syntax
<a name="API_ListUserSessions_RequestSyntax"></a>

```
{
   "AccessToken": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListUserSessions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessToken](#API_ListUserSessions_RequestSyntax) **   <a name="CognitoUserPools-ListUserSessions-request-AccessToken"></a>
A valid access token that Amazon Cognito issued to the user whose sessions you want to list. Amazon Cognito derives the user pool and username from this token.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: Yes

 ** [NextToken](#API_ListUserSessions_RequestSyntax) **   <a name="CognitoUserPools-ListUserSessions-request-NextToken"></a>
A pagination token that Amazon Cognito returned in a previous response. Use this value to retrieve the next page of results if a `NextToken` was included in a prior response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\S]+`
Required: No

## Response Syntax
<a name="API_ListUserSessions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Sessions": [
      {
         "ClientId": "string",
         "CreateDate": number,
         "DeviceType": "string",
         "IsCurrentSession": boolean,
         "LastActiveDate": number,
         "LastIPAddress": "string",
         "LastLocation": {
            "City": "string",
            "Country": "string"
         },
         "OriginSessionId": "string",
         "SessionId": "string",
         "SessionType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUserSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListUserSessions_ResponseSyntax) **   <a name="CognitoUserPools-ListUserSessions-response-NextToken"></a>
The pagination token to use in a subsequent request to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\S]+`

 ** [Sessions](#API_ListUserSessions_ResponseSyntax) **   <a name="CognitoUserPools-ListUserSessions-response-Sessions"></a>
A list of the user's active sessions. Each element describes one token session or SSO session.
Type: Array of [SessionDescriptionType](API_SessionDescriptionType.md) objects
Array Members: Minimum number of 0 items. Maximum number of 125 items.

## Errors
<a name="API_ListUserSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ForbiddenException **
This exception is thrown when AWS WAF doesn't allow your request based on a web ACL that's associated with your user pool.
 ** message **
The message returned when AWS WAF doesn't allow your request based on a web ACL that's associated with your user pool.
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

 ** PasswordResetRequiredException **
This exception is thrown when a password reset is required.
 ** message **
The message returned when a password reset is required.
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

 ** UserNotConfirmedException **
This exception is thrown when a user isn't confirmed successfully.
 ** message **
The message returned when a user isn't confirmed successfully.
HTTP Status Code: 400

 ** UserNotFoundException **
This exception is thrown when a user isn't found.
 ** message **
The message returned when a user isn't found.
HTTP Status Code: 400

## See Also
<a name="API_ListUserSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/ListUserSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/ListUserSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ListUserSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/ListUserSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ListUserSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/ListUserSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/ListUserSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/ListUserSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/ListUserSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ListUserSessions)
