---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_PutIdentityPolicy.html
---

# PutIdentityPolicy
<a name="API_PutIdentityPolicy"></a>

Adds or updates a sending authorization policy for the specified identity (an email address or a domain).

**Note**
This operation is for the identity owner only. If you have not verified the identity, it returns an error.

Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html).

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_PutIdentityPolicy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Identity **
The identity to which that the policy applies. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: `user@example.com`, `example.com`, `arn:aws:ses:us-east-1:123456789012:identity/example.com`.
To successfully call this operation, you must own the identity.
Type: String
Required: Yes

 ** Policy **
The text of the policy in JSON format. The policy cannot exceed 4 KB.
For information about the syntax of sending authorization policies, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-policies.html).
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** PolicyName **
The name of the policy.
The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Errors
<a name="API_PutIdentityPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidPolicy **
Indicates that the provided policy is invalid. Check the error stack for more information about what caused the error.
HTTP Status Code: 400

## See Also
<a name="API_PutIdentityPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/PutIdentityPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/PutIdentityPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/PutIdentityPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/PutIdentityPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/PutIdentityPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/PutIdentityPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/PutIdentityPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/PutIdentityPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/PutIdentityPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/PutIdentityPolicy)
