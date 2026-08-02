---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_KekValidationRequest.html
---

# KekValidationRequest
<a name="API_KekValidationRequest"></a>

Parameter information for generating a KEK validation request during node-to-node initialization.

## Contents
<a name="API_KekValidationRequest_Contents"></a>

 ** DeriveKeyAlgorithm **   <a name="paymentcryptographydata-Type-KekValidationRequest-DeriveKeyAlgorithm"></a>
The key derivation algorithm to use for generating a KEK validation request.
Type: String
Valid Values: `TDES_2KEY | TDES_3KEY | AES_128 | AES_192 | AES_256 | HMAC_SHA256 | HMAC_SHA384 | HMAC_SHA512 | HMAC_SHA224`
Required: Yes

 ** RandomKeyMaxLength **   <a name="paymentcryptographydata-Type-KekValidationRequest-RandomKeyMaxLength"></a>
The maximum length of the random key to generate for a KEK validation request.
Type: String
Valid Values: `BYTES_8 | BYTES_16 | BYTES_24`
Required: No

## See Also
<a name="API_KekValidationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/KekValidationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/KekValidationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/KekValidationRequest)
