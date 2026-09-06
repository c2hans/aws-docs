---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportAttributes.html
---

# ExportAttributes
<a name="API_ExportAttributes"></a>

The attributes for IPEK generation during export.

## Contents
<a name="API_ExportAttributes_Contents"></a>

 ** ExportDukptInitialKey **   <a name="paymentcryptography-Type-ExportAttributes-ExportDukptInitialKey"></a>
Parameter information for IPEK export.
Type: [ExportDukptInitialKey](API_ExportDukptInitialKey.md) object
Required: No

 ** KeyCheckValueAlgorithm **   <a name="paymentcryptography-Type-ExportAttributes-KeyCheckValueAlgorithm"></a>
The algorithm that AWS Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity. Specify KCV for IPEK export only.
For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.
Type: String
Valid Values: `CMAC | ANSI_X9_24 | HMAC | SHA_1`
Required: No

## See Also
<a name="API_ExportAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ExportAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ExportAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ExportAttributes)
