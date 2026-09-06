---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DiffieHellmanDerivationData.html
---

# DiffieHellmanDerivationData
<a name="API_DiffieHellmanDerivationData"></a>

The shared information used when deriving a key using ECDH.

## Contents
<a name="API_DiffieHellmanDerivationData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** SharedInformation **   <a name="paymentcryptographydata-Type-DiffieHellmanDerivationData-SharedInformation"></a>
A string containing information that binds the ECDH derived key to the two parties involved or to the context of the key.
It may include details like identities of the two parties deriving the key, context of the operation, session IDs, and optionally a nonce. It must not contain zero bytes. It is not recommended to reuse shared information for multiple ECDH key derivations, as it could result in derived key material being the same across different derivations.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 2048.
Pattern: `(?:[0-9a-fA-F][0-9a-fA-F])+`
Required: No

## See Also
<a name="API_DiffieHellmanDerivationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/DiffieHellmanDerivationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/DiffieHellmanDerivationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/DiffieHellmanDerivationData)
