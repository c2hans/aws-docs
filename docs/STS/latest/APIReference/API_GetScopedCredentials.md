---
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_GetScopedCredentials.html
---

# GetScopedCredentials

Returns a set of temporary security credentials that are scoped down from the caller's existing temporary security credentials. `GetScopedCredentials` preserves the caller's identity while narrowing the permissions and optionally shortening the session lifetime.

For a comparison of `GetScopedCredentials` with the other API operations that produce temporary security credentials, see [Requesting Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) and [Compare AWS STS credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_sts-comparison.html) in the IAM User Guide.

 **Credential requirements**

You can only call `GetScopedCredentials` with temporary security credentials, for example, credentials from an assumed role or a federated session. You cannot call it with IAM user credentials or root credentials. If you want to scope down IAM user credentials, first call `GetSessionToken` to get temporary security credentials, and then call `GetScopedCredentials` with those credentials.

**Note**
The `GetScopedCredentials` API is not available on the AWS STS Global endpoint.

## Request Parameters
<a name="API_GetScopedCredentials_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DurationSeconds **
The duration, in seconds, of the resulting scoped down credentials. The value can range from 1 second to 129,600 seconds (36 hours).
If you do not specify this value, the scoped down credentials will inherit the calling session's expiration time.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 129600.
Required: No

 ** MinimumSessionTokenSize **
The minimum size, in bytes, of the session token that STS issues for the request. STS increases the session token to at least this size, regardless of its actual content. The value must not exceed 4,096 bytes. When set to 0 or not specified, the session token size is unchanged.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 4096.
Required: No

 ** Policy **
An IAM policy in JSON format that you want to use as a scope down policy.
A request must provide at least one of `Policy` or `DurationSeconds`. Both parameters are optional individually, but you must specify at least one of them.
The resulting session's permissions are the intersection of the calling session's existing permissions and this scope down policy. You cannot use this scope down policy to grant more permissions than the calling session already has.
The plaintext of the scope down policy cannot exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (\\u0020 through \\u00FF). It can also include the tab (\\u0009), linefeed (\\u000A), and carriage return (\\u000D) characters.
An internal conversion compresses the inline scope down policy into a packed binary format that has a separate limit. If the packed policy exceeds this limit, the request fails with `PackedPolicyTooLarge`.
If the document is not valid IAM policy JSON, the request fails with `MalformedPolicyDocument`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** ScopedSessionDescription **
A caller-supplied description of the scoped session. The value cannot exceed 256 characters. This description is logged to AWS CloudTrail for the request, so you can use it to record the purpose of the scoped session.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: No

## Response Elements
<a name="API_GetScopedCredentials_ResponseElements"></a>

The following elements are returned by the service.

 ** Credentials **
The temporary security credentials for the scoped down session, which include an access key ID, a secret access key, and a security token.
The size of the security token that AWS STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.
Type: [Credentials](API_Credentials.md) object

 ** ScopedPoliciesCount **
 `GetScopedCredentials` can be called recursively and `ScopedPoliciesCount` specifies the number of scope down policies applied to the session. Each recursive call adds another scope down policy layer. A maximum of 3 scope down policy layers are allowed per session. If a session already has 3 `GetScopedCredentials` scope-down policies, a subsequent `GetScopedCredentials` call that supplies a `Policy` (attempting to append a fourth scope-down policy) is denied.
Type: Integer
Valid Range: Minimum value of 0.

 ** SessionInfo **
Metadata about the resulting scoped session, including its identifier and ARN. Because the identity does not change, the identifiers reflect the same principal and session name as the calling session.
Type: [ScopedSession](API_ScopedSession.md) object

 ** SessionTokenSize **
The size, in bytes, of the session token returned in the Credentials for this response.
Type: Integer
Valid Range: Minimum value of 0.

 ** SessionTokenUtilization **
The percentage (0-100) of the maximum allowed session token size that the returned session token consumes.
Type: Integer
Valid Range: Minimum value of 0.

 ** SourceIdentity **
The source identity of the calling session, carried forward unchanged. This operation never sets or modifies the source identity; it reflects the value established when the source identity was first set. For more information, see [Monitor and control actions taken with assumed roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html) in the IAM User Guide.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[\w+=,.@-]*`

## Errors
<a name="API_GetScopedCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientSessionLifetime **
The request was rejected because the requested `DurationSeconds` is greater than the remaining lifetime of the calling session. `GetScopedCredentials` cannot extend a session beyond its original expiration. Request a duration that is less than or equal to the calling session's remaining lifetime, or omit `DurationSeconds` to inherit it.
HTTP Status Code: 400

 ** InvalidSubjectCredentials **
The request was rejected because the session used to call `GetScopedCredentials` is not a valid session. The calling session's credentials could not be validated or resolved.
HTTP Status Code: 400

 ** MalformedPolicyDocument **
The request was rejected because the policy document was malformed. The error message describes the specific error.
HTTP Status Code: 400

 ** PackedPolicyTooLarge **
The request was rejected because the session token exceeded the maximum allowed size. The error message reports the session token size and the maximum allowed size, both in bytes. Session policies and session tags add to the session token size. For more information, see [Passing Session Tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html) in the *IAM User Guide*.
You might receive this error even though you meet the individual session policy and session tag limits. Monitor `SessionTokenUtilization` to track how close the session token is to the maximum allowed size. For more information, see [IAM and AWS STS Entity Character Limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-limits-entity-length) in the *IAM User Guide*.
HTTP Status Code: 400

## Examples
<a name="API_GetScopedCredentials_Examples"></a>

### Example
<a name="API_GetScopedCredentials_Example_1"></a>

This example illustrates one usage of GetScopedCredentials.

#### Sample Request
<a name="API_GetScopedCredentials_Example_1_Request"></a>

```
https://sts.us-east-1.amazonaws.com/
?Version=2011-06-15
&Action=GetScopedCredentials
&DurationSeconds=3600
&Policy=JSON-IAM-POLICY
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetScopedCredentials_Example_1_Response"></a>

```
<GetScopedCredentialsResponse xmlns="https://sts.amazonaws.com/doc/2011-06-15/">
  <GetScopedCredentialsResult>
    <Credentials>
      <AccessKeyId>ASIAIOSFODNN7EXAMPLE</AccessKeyId>
      <SecretAccessKey>wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY</SecretAccessKey>
      <SessionToken>
       AQoDYXdzEPT//////////wEXAMPLEtc764bNrC9SAPBSM22wDOk4x4HIZ8j4FZTwdQW
       LWsKWHGBuFqwAeMicRXmxfpSPfIeoIYRqTflfKD8YUuwthAx7mSEI/qkPpKPi/kMcGd
       QrmGdeehM4IC1NtBmUpp2wUE8phUZampKsburEDy0KPkyQDYwT7WZ0wq5VSXDvp75YU
       9HFvlRd8Tx6q6fE8YQcHNVXAkiY9q6d+xo0rKwT38xVqr7ZD0u0iPPkUL64lIZbqBAz
       +scqKmlzm8FDrypNC9Yjc8fPOLn9FX9KSYvKTr4rvx3iSIlTJabIQwj2ICCR/oLxBA==
      </SessionToken>
      <Expiration>2019-11-09T13:34:41Z</Expiration>
    </Credentials>
    <ScopedPoliciesCount>1</ScopedPoliciesCount>
    <SessionInfo>
      <ScopedSessionId>AROAEXAMPLEID:example-session</ScopedSessionId>
      <Arn>arn:aws:sts::123456789012:assumed-role/example-role/example-session</Arn>
    </SessionInfo>
    <SourceIdentity>example-source-identity</SourceIdentity>
  </GetScopedCredentialsResult>
  <ResponseMetadata>
    <RequestId>c6104cbe-af31-11e0-8154-cbc7ccf896c7</RequestId>
  </ResponseMetadata>
</GetScopedCredentialsResponse>
```

## See Also
<a name="API_GetScopedCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sts-2011-06-15/GetScopedCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sts-2011-06-15/GetScopedCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/GetScopedCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sts-2011-06-15/GetScopedCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/GetScopedCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sts-2011-06-15/GetScopedCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sts-2011-06-15/GetScopedCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sts-2011-06-15/GetScopedCredentials)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sts-2011-06-15/GetScopedCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/GetScopedCredentials)
