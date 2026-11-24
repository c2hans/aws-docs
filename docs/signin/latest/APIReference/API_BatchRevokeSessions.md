---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_BatchRevokeSessions.html
---

# BatchRevokeSessions

Revokes one or more AWS Sign-In Sessions. You can revoke up to five sessions in a single request. Revocation prevents these sessions from renewing OAuth access tokens. OAuth access tokens issued before revocation remain valid until they expire, which can take up to one hour.

## Request Syntax
<a name="API_BatchRevokeSessions_RequestSyntax"></a>

```
{
   "principalArn": "{{string}}",
   "reason": "{{string}}",
   "sessionArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchRevokeSessions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [principalArn](#API_BatchRevokeSessions_RequestSyntax) **   <a name="signin-BatchRevokeSessions-request-principalArn"></a>
The ARN of the principal whose Sign-In Sessions you want to revoke. If you omit this parameter, the caller's identity is used. Specify a supported principal ARN to revoke sessions for that principal, or an account wildcard such as `arn:aws:iam::123456789012:*` to revoke sessions across your account. The principal or account wildcard must be in the caller's AWS account. Revoking sessions associated with another principal requires appropriate IAM permissions.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]+)*:((iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]{1,64})|(iam::[0-9]{12}:user/[a-zA-Z0-9_+=,.@-]{1,64})|(sts::[0-9]{12}:federated-user/[a-zA-Z0-9_+=,.@-]{2,193})|(iam::[0-9]{12}:root)|(iam::[0-9]{12}:[*]))`
Required: No

 ** [reason](#API_BatchRevokeSessions_RequestSyntax) **   <a name="signin-BatchRevokeSessions-request-reason"></a>
An optional reason for revoking the specified Sign-In Sessions. When the operation changes a session from `ACTIVE` to `REVOKED`, the reason is recorded on that session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [sessionArns](#API_BatchRevokeSessions_RequestSyntax) **   <a name="signin-BatchRevokeSessions-request-sessionArns"></a>
The ARNs of the Sign-In Sessions to revoke. Specify between one and five session ARNs in a single request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_BatchRevokeSessions_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "code": "string",
         "message": "string",
         "sessionArn": "string"
      }
   ],
   "revokedSessions": [
      {
         "sessionArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchRevokeSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchRevokeSessions_ResponseSyntax) **   <a name="signin-BatchRevokeSessions-response-errors"></a>
A list of session-specific revocation failures. Each entry identifies the session ARN and includes an error code and message. An HTTP 200 response can include both successful and failed session results.
Type: Array of [BatchRevokeSessionError](API_BatchRevokeSessionError.md) objects

 ** [revokedSessions](#API_BatchRevokeSessions_ResponseSyntax) **   <a name="signin-BatchRevokeSessions-response-revokedSessions"></a>
A list of session ARNs for which the revocation request succeeded. This list can include sessions that were already revoked.
Type: Array of [RevokedSession](API_RevokedSession.md) objects

## Errors
<a name="API_BatchRevokeSessions_Errors"></a>

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
<a name="API_BatchRevokeSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signincontrolplane-2022-07-26/BatchRevokeSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signincontrolplane-2022-07-26/BatchRevokeSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/BatchRevokeSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signincontrolplane-2022-07-26/BatchRevokeSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/BatchRevokeSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signincontrolplane-2022-07-26/BatchRevokeSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signincontrolplane-2022-07-26/BatchRevokeSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signincontrolplane-2022-07-26/BatchRevokeSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/signincontrolplane-2022-07-26/BatchRevokeSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/BatchRevokeSessions)
