---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRevokeUserSession.html
---

# AdminRevokeUserSession
<a name="API_AdminRevokeUserSession"></a>

Revokes a specific user session as an administrator. Amazon Cognito revokes all refresh and access tokens that are associated with the session and deletes the session record. You can revoke either a token session or an SSO session, and you can optionally cascade the revocation to linked sessions.

## Request Syntax
<a name="API_AdminRevokeUserSession_RequestSyntax"></a>

```
{
   "RevokeAssociatedSessions": "{{string}}",
   "SessionId": "{{string}}",
   "Username": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AdminRevokeUserSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RevokeAssociatedSessions](#API_AdminRevokeUserSession_RequestSyntax) **   <a name="CognitoUserPools-AdminRevokeUserSession-request-RevokeAssociatedSessions"></a>
Specifies whether to also revoke the sessions that are linked to the targeted session. `NONE`, the default, revokes only the targeted session. `LINKED` also revokes the directly linked session or sessions, interpreted relative to the type of the targeted session: revoking a token session also revokes the parent SSO session it came through, and revoking an SSO session also revokes the token sessions that came through it. The set of linked sessions is eventually consistent, so associated sessions are typically revoked within a few seconds.
Type: String
Valid Values: `NONE | LINKED`
Required: No

 ** [SessionId](#API_AdminRevokeUserSession_RequestSyntax) **   <a name="CognitoUserPools-AdminRevokeUserSession-request-SessionId"></a>
The ID of the session to revoke. This is a 28-character string of lowercase letters and digits, prefixed with `tkn` for a token session or `sso` for an SSO session.
Type: String
Length Constraints: Fixed length of 28.
Pattern: `^(tkn|sso)[a-z0-9]{25}$`
Required: Yes

 ** [Username](#API_AdminRevokeUserSession_RequestSyntax) **   <a name="CognitoUserPools-AdminRevokeUserSession-request-Username"></a>
The username of the user who owns the session. The username must match the user associated with the `SessionId`, to confirm they are the intended target user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** [UserPoolId](#API_AdminRevokeUserSession_RequestSyntax) **   <a name="CognitoUserPools-AdminRevokeUserSession-request-UserPoolId"></a>
The ID of the user pool that contains the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Elements
<a name="API_AdminRevokeUserSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AdminRevokeUserSession_Errors"></a>

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
<a name="API_AdminRevokeUserSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AdminRevokeUserSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AdminRevokeUserSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminRevokeUserSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AdminRevokeUserSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminRevokeUserSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AdminRevokeUserSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AdminRevokeUserSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AdminRevokeUserSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AdminRevokeUserSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminRevokeUserSession)
