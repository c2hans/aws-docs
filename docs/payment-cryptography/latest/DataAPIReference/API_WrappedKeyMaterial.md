---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_WrappedKeyMaterial.html
---

# WrappedKeyMaterial
<a name="API_WrappedKeyMaterial"></a>

Parameter information of a WrappedKeyBlock for encryption key exchange.

## Contents
<a name="API_WrappedKeyMaterial_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** DiffieHellmanSymmetricKey **   <a name="paymentcryptographydata-Type-WrappedKeyMaterial-DiffieHellmanSymmetricKey"></a>
The parameter information for deriving a ECDH shared key.
Type: [EcdhDerivationAttributes](API_EcdhDerivationAttributes.md) object
Required: No

 ** Tr31KeyBlock **   <a name="paymentcryptographydata-Type-WrappedKeyMaterial-Tr31KeyBlock"></a>
The TR-31 wrapped key block.
Type: String
Length Constraints: Minimum length of 56. Maximum length of 9984.
Pattern: `[0-9a-zA-Z]+`
Required: No

## See Also
<a name="API_WrappedKeyMaterial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/WrappedKeyMaterial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/WrappedKeyMaterial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/WrappedKeyMaterial)
