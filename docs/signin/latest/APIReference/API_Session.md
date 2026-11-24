---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_Session.html
---

# Session

Summary information about a sign-in session.

## Contents
<a name="API_Session_Contents"></a>

 ** expiresAt **   <a name="signin-Type-Session-expiresAt"></a>
The time the session expires, as a NumericDate (epoch seconds). Setting, changing, or removing `MaxSignInSessionDuration` does not affect refresh tokens issued for standard sessions. An extended session uses the principal's current `MaxSignInSessionDuration` when it refreshes. Reducing the value can shorten or end the session, removing the value prevents refresh, and increasing the value cannot extend the session beyond its original expiration.
Type: Long
Required: Yes

 ** issuedAt **   <a name="signin-Type-Session-issuedAt"></a>
The time the session was created, as a NumericDate (epoch seconds).
Type: Long
Required: Yes

 ** principalArn **   <a name="signin-Type-Session-principalArn"></a>
The ARN of the identity that owns the session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]+)*:((iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]{1,64})|(iam::[0-9]{12}:user/[a-zA-Z0-9_+=,.@-]{1,64})|(sts::[0-9]{12}:federated-user/[a-zA-Z0-9_+=,.@-]{2,193})|(iam::[0-9]{12}:root))`
Required: Yes

 ** sessionArn **   <a name="signin-Type-Session-sessionArn"></a>
The ARN of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** clientId **   <a name="signin-Type-Session-clientId"></a>
The identifier of the OAuth client that created the session.
Type: String
Required: No

 ** clientType **   <a name="signin-Type-Session-clientType"></a>
The type of OAuth client that created the session, either `CLI` or `MCP`.
Type: String
Valid Values: `CLI | MCP`
Required: No

 ** resource **   <a name="signin-Type-Session-resource"></a>
The resource that the session's tokens are bound to.
Type: String
Required: No

 ** role **   <a name="signin-Type-Session-role"></a>
The ARN of the IAM role for the session, if the identity is a role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]+)*:((iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]{1,64})|(iam::[0-9]{12}:user/[a-zA-Z0-9_+=,.@-]{1,64})|(sts::[0-9]{12}:federated-user/[a-zA-Z0-9_+=,.@-]{2,193})|(iam::[0-9]{12}:root))`
Required: No

 ** status **   <a name="signin-Type-Session-status"></a>
The status of the session, either `ACTIVE` or `REVOKED`.
Type: String
Valid Values: `ACTIVE | REVOKED`
Required: No

## See Also
<a name="API_Session_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/Session)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/Session)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/Session)
