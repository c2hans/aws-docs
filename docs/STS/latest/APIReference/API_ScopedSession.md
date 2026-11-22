---
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_ScopedSession.html
---

# ScopedSession

Identifiers for the scoped session that `GetScopedCredentials` returns. The underlying identity and session name do not change from the caller principal.

## Contents
<a name="API_ScopedSession_Contents"></a>

 ** Arn **
The ARN of the scoped session. For more information about ARNs and how to use them in policies, see [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]+`
Required: Yes

 ** ScopedSessionId **
A unique identifier for the scoped session. Because the identity is preserved, this identifies the same principal as the calling session.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 193.
Pattern: `[\w+=,.@:-]*`
Required: Yes

## See Also
<a name="API_ScopedSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/ScopedSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/ScopedSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/ScopedSession)
