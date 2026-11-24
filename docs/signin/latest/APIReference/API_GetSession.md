---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_GetSession.html
---

# GetSession

Retrieves the details of a single sign-in session.

## Request Syntax
<a name="API_GetSession_RequestSyntax"></a>

```
{
   "principalArn": "{{string}}",
   "sessionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [principalArn](#API_GetSession_RequestSyntax) **   <a name="signin-GetSession-request-principalArn"></a>
The ARN of the identity that owns the session. If not provided, the caller's identity is used.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]+)*:((iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]{1,64})|(iam::[0-9]{12}:user/[a-zA-Z0-9_+=,.@-]{1,64})|(sts::[0-9]{12}:federated-user/[a-zA-Z0-9_+=,.@-]{2,193})|(iam::[0-9]{12}:root)|(iam::[0-9]{12}:[*]))`
Required: No

 ** [sessionArn](#API_GetSession_RequestSyntax) **   <a name="signin-GetSession-request-sessionArn"></a>
The ARN of the session to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_GetSession_ResponseSyntax"></a>

```
{
   "clientId": "string",
   "clientType": "string",
   "expiresAt": number,
   "issuedAt": number,
   "issuedInRegion": "string",
   "lastUsedAt": number,
   "originSessionArn": "string",
   "principalArn": "string",
   "resource": "string",
   "role": "string",
   "sessionArn": "string",
   "status": "string",
   "userAgent": "string"
}
```

## Response Elements
<a name="API_GetSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientId](#API_GetSession_ResponseSyntax) **   <a name="signin-GetSession-response-clientId"></a>
The identifier of the OAuth client that created the session.
Type: String

 ** [clientType](#API_GetSession_ResponseSyntax) **   <a name="signin-GetSession-response-clientType"></a>
The type of OAuth client that created the session, either `CLI` or `MCP`.
Type: String
Valid Values: `CLI | MCP`

 ** [expiresAt](#API_GetSession_ResponseSyntax) **   <a name="signin-GetSession-response-expiresAt"></a>
The time the session expires, as a NumericDate (epoch seconds). Setting, changing, or removing `MaxSignInSessionDuration` does not affect refresh tokens issued for standard sessions. An extended session uses the principal's current `MaxSignInSessionDuration` when it refreshes. Reducing the value can shorten or end the session, removing the value prevents refresh, and increasing the value cannot extend the session beyond its original expiration.
Type: Long

 ** [issuedAt](#API_GetSession_ResponseSyntax) **   <a name="signin-GetSession-response-issuedAt"></a>
The time the session was created, as a NumericDate (epoch seconds).
Type: Long

 ** [issuedInRegion](#API_GetSession_ResponseSyntax) **   <a name="signin-GetSession-response-issuedInRegion"></a>
The AWS Region where the session was created.
Type: String

 ** [lastUsedAt](#API_GetSession_ResponseSyntax) **   <a name="signin-GetSession-response-lastUsedAt"></a>
The time the session was last refreshed, as a NumericDate (epoch seconds).
Type: Long

 ** [originSessionArn](#API_GetSession_ResponseSyntax) **   <a name="signin-GetSession-response-originSessionArn"></a>
The ARN of the session that this session originated from.
Type: String

 ** [principalArn](#API_GetSession_ResponseSyntax) **   <a name="signin-GetSession-response-principalArn"></a>
The ARN of the identity that owns the session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]+)*:((iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]{1,64})|(iam::[0-9]{12}:user/[a-zA-Z0-9_+=,.@-]{1,64})|(sts::[0-9]{12}:federated-user/[a-zA-Z0-9_+=,.@-]{2,193})|(iam::[0-9]{12}:root))`

 ** [resource](#API_GetSession_ResponseSyntax) **   <a name="signin-GetSession-response-resource"></a>
The resource that the session's tokens are bound to.
Type: String

 ** [role](#API_GetSession_ResponseSyntax) **   <a name="signin-GetSession-response-role"></a>
The ARN of the IAM role for the session, if the identity is a role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]+)*:((iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]{1,64})|(iam::[0-9]{12}:user/[a-zA-Z0-9_+=,.@-]{1,64})|(sts::[0-9]{12}:federated-user/[a-zA-Z0-9_+=,.@-]{2,193})|(iam::[0-9]{12}:root))`

 ** [sessionArn](#API_GetSession_ResponseSyntax) **   <a name="signin-GetSession-response-sessionArn"></a>
The ARN of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [status](#API_GetSession_ResponseSyntax) **   <a name="signin-GetSession-response-status"></a>
The status of the session, either `ACTIVE` or `REVOKED`.
Type: String
Valid Values: `ACTIVE | REVOKED`

 ** [userAgent](#API_GetSession_ResponseSyntax) **   <a name="signin-GetSession-response-userAgent"></a>
The user agent of the client that created or last refreshed the session.
Type: String

## Errors
<a name="API_GetSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 400

 ** InternalServerException **
An internal error occurred while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A resource specified in the request could not be found.
HTTP Status Code: 400

 ** ThrottlingException **
Your request was throttled because you exceeded the allowed request rate.
HTTP Status Code: 400

 ** ValidationException **
The request contains invalid or incorrectly formatted input.
HTTP Status Code: 400

## See Also
<a name="API_GetSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signincontrolplane-2022-07-26/GetSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signincontrolplane-2022-07-26/GetSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/GetSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signincontrolplane-2022-07-26/GetSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/GetSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signincontrolplane-2022-07-26/GetSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signincontrolplane-2022-07-26/GetSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signincontrolplane-2022-07-26/GetSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/signincontrolplane-2022-07-26/GetSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/GetSession)
