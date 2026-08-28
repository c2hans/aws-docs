---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_WrappedKey.html
---

# WrappedKey
<a name="API_WrappedKey"></a>

Parameter information of a WrappedKeyBlock for encryption key exchange.

## Contents
<a name="API_WrappedKey_Contents"></a>

 ** WrappedKeyMaterial **   <a name="paymentcryptographydata-Type-WrappedKey-WrappedKeyMaterial"></a>
Parameter information of a WrappedKeyBlock for encryption key exchange.
Type: [WrappedKeyMaterial](API_WrappedKeyMaterial.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** KeyCheckValueAlgorithm **   <a name="paymentcryptographydata-Type-WrappedKey-KeyCheckValueAlgorithm"></a>
The algorithm that AWS Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.
For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result.
Type: String
Valid Values: `CMAC | ANSI_X9_24 | HMAC | SHA_1`
Required: No

## See Also
<a name="API_WrappedKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/WrappedKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/WrappedKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/WrappedKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
