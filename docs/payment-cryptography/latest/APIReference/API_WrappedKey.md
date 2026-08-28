---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_WrappedKey.html
---

# WrappedKey
<a name="API_WrappedKey"></a>

Parameter information for generating a WrappedKeyBlock for key exchange.

## Contents
<a name="API_WrappedKey_Contents"></a>

 ** KeyMaterial **   <a name="paymentcryptography-Type-WrappedKey-KeyMaterial"></a>
Parameter information for generating a wrapped key using TR-31 or TR-34 skey exchange method.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 16384.
Required: Yes

 ** WrappedKeyMaterialFormat **   <a name="paymentcryptography-Type-WrappedKey-WrappedKeyMaterialFormat"></a>
The key block format of a wrapped key.
Type: String
Valid Values: `KEY_CRYPTOGRAM | TR31_KEY_BLOCK | TR34_KEY_BLOCK`
Required: Yes

 ** WrappingKeyArn **   <a name="paymentcryptography-Type-WrappedKey-WrappingKeyArn"></a>
The `KeyARN` of the wrapped key.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`
Required: Yes

 ** KeyCheckValue **   <a name="paymentcryptography-Type-WrappedKey-KeyCheckValue"></a>
The key check value (KCV) is used to check if all parties holding a given key have the same key or to detect that a key has changed.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`
Required: No

 ** KeyCheckValueAlgorithm **   <a name="paymentcryptography-Type-WrappedKey-KeyCheckValueAlgorithm"></a>
The algorithm that AWS Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.
For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.
Type: String
Valid Values: `CMAC | ANSI_X9_24 | HMAC | SHA_1`
Required: No

## See Also
<a name="API_WrappedKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/WrappedKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/WrappedKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/WrappedKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
