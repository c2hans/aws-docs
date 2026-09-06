---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_KmsGrantConstraints.html
---

# KmsGrantConstraints
<a name="API_KmsGrantConstraints"></a>

Use this structure to propose allowing [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) in the grant only when the operation request includes the specified [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context). You can specify only one type of encryption context. An empty map is treated as not specified. For more information, see [GrantConstraints](https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html).

## Contents
<a name="API_KmsGrantConstraints_Contents"></a>

 ** encryptionContextEquals **   <a name="accessanalyzer-Type-KmsGrantConstraints-encryptionContextEquals"></a>
A list of key-value pairs that must match the encryption context in the [cryptographic operation](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) request. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint.
Type: String to string map
Required: No

 ** encryptionContextSubset **   <a name="accessanalyzer-Type-KmsGrantConstraints-encryptionContextSubset"></a>
A list of key-value pairs that must be included in the encryption context of the [cryptographic operation](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) request. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs.
Type: String to string map
Required: No

## See Also
<a name="API_KmsGrantConstraints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/KmsGrantConstraints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/KmsGrantConstraints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/KmsGrantConstraints)
