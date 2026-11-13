---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListUserSessions.html
---

# AdminListUserSessions
<a name="API_AdminListUserSessions"></a>

Lists the active sessions for a specified user as an administrator. The response includes both token sessions and SSO sessions. Only active sessions are returned; revoked and expired sessions aren't included. Amazon Cognito returns all of a user's sessions in a single page of up to 125 sessions. The results are eventually consistent, and new sessions are typically included within a few seconds.

## Request Syntax
<a name="API_AdminListUserSessions_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "Username": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AdminListUserSessions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NextToken](#API_AdminListUserSessions_RequestSyntax) **   <a name="CognitoUserPools-AdminListUserSessions-request-NextToken"></a>
A pagination token that Amazon Cognito returned in a previous response. Use this value to retrieve the next page of results if a `NextToken` was included in a prior response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\S]+`
Required: No

 ** [Username](#API_AdminListUserSessions_RequestSyntax) **   <a name="CognitoUserPools-AdminListUserSessions-request-Username"></a>
The username of the user whose sessions you want to list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** [UserPoolId](#API_AdminListUserSessions_RequestSyntax) **   <a name="CognitoUserPools-AdminListUserSessions-request-UserPoolId"></a>
The ID of the user pool that contains the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_AdminListUserSessions_ResponseSyntax"></a>

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
<a name="API_AdminListUserSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_AdminListUserSessions_ResponseSyntax) **   <a name="CognitoUserPools-AdminListUserSessions-response-NextToken"></a>
The pagination token to use in a subsequent request to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\S]+`

 ** [Sessions](#API_AdminListUserSessions_ResponseSyntax) **   <a name="CognitoUserPools-AdminListUserSessions-response-Sessions"></a>
A list of the user's active sessions. Each element describes one token session or SSO session.
Type: Array of [SessionDescriptionType](API_SessionDescriptionType.md) objects
Array Members: Minimum number of 0 items. Maximum number of 125 items.

## Errors
<a name="API_AdminListUserSessions_Errors"></a>

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

 ** UserNotFoundException **
This exception is thrown when a user isn't found.
 ** message **
The message returned when a user isn't found.
HTTP Status Code: 400

## See Also
<a name="API_AdminListUserSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AdminListUserSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AdminListUserSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminListUserSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AdminListUserSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminListUserSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AdminListUserSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AdminListUserSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AdminListUserSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AdminListUserSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminListUserSessions)
