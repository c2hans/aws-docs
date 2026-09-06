---
source_url: https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_SigningKeyInfo.html
---

# SigningKeyInfo
<a name="API_SigningKeyInfo"></a>

The signing key used to cryptographically sign a support permit.

## Contents
<a name="API_SigningKeyInfo_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** kmsKey **   <a name="supportauthorization-Type-SigningKeyInfo-kmsKey"></a>
The ARN of the AWS KMS key used to sign the permit. The key must have key spec ECC\_NIST\_P384 and key usage SIGN\_VERIFY.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9/:_-]{1,512}`
Required: No

## See Also
<a name="API_SigningKeyInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supportauthz-2026-06-30/SigningKeyInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supportauthz-2026-06-30/SigningKeyInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supportauthz-2026-06-30/SigningKeyInfo)
