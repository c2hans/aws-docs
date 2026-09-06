---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_XksProxyAuthenticationCredentialType.html
---

# XksProxyAuthenticationCredentialType
<a name="API_XksProxyAuthenticationCredentialType"></a>

 AWS KMS uses the authentication credential to sign requests that it sends to the external key store proxy (XKS proxy) on your behalf. You establish these credentials on your external key store proxy and report them to AWS KMS.

The `XksProxyAuthenticationCredential` includes two required elements.

## Contents
<a name="API_XksProxyAuthenticationCredentialType_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccessKeyId **   <a name="KMS-Type-XksProxyAuthenticationCredentialType-AccessKeyId"></a>
A unique identifier for the raw secret access key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 30.
Pattern: `^[A-Z2-7]+$`
Required: Yes

 ** RawSecretAccessKey **   <a name="KMS-Type-XksProxyAuthenticationCredentialType-RawSecretAccessKey"></a>
A secret string of 43-64 characters. Valid characters are a-z, A-Z, 0-9, /, \+, and =.
Type: String
Length Constraints: Minimum length of 43. Maximum length of 64.
Pattern: `^[a-zA-Z0-9\/+=]+$`
Required: Yes

## See Also
<a name="API_XksProxyAuthenticationCredentialType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/XksProxyAuthenticationCredentialType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/XksProxyAuthenticationCredentialType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/XksProxyAuthenticationCredentialType)
