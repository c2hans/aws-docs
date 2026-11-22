---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_SAMLKeyHashEntry.html
---

# SAMLKeyHashEntry

Contains the key hashes that are associated with a SAML identity provider issuer.

This data type is used as a response element in the [GetSAMLProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetSAMLProvider.html) operation.

## Contents
<a name="API_SAMLKeyHashEntry_Contents"></a>

 ** IssuerURL **
The issuer URL of the SAML identity provider that the key hashes are associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** KeyHashes.member.N **
The list of key hashes for the SAML identity provider issuer.
Type: Array of strings
Required: No

## See Also
<a name="API_SAMLKeyHashEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/SAMLKeyHashEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/SAMLKeyHashEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/SAMLKeyHashEntry)
