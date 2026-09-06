---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_MacAlgorithmDukpt.html
---

# MacAlgorithmDukpt
<a name="API_MacAlgorithmDukpt"></a>

Parameters required for DUKPT MAC generation and verification.

## Contents
<a name="API_MacAlgorithmDukpt_Contents"></a>

 ** DukptKeyVariant **   <a name="paymentcryptographydata-Type-MacAlgorithmDukpt-DukptKeyVariant"></a>
The type of use of DUKPT, which can be MAC generation, MAC verification, or both.
Type: String
Valid Values: `BIDIRECTIONAL | REQUEST | RESPONSE`
Required: Yes

 ** KeySerialNumber **   <a name="paymentcryptographydata-Type-MacAlgorithmDukpt-KeySerialNumber"></a>
The unique identifier known as Key Serial Number (KSN) that comes from an encrypting device using DUKPT encryption method. The KSN is derived from the encrypting device unique identifier and an internal transaction counter.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 24.
Pattern: `(?:[0-9a-fA-F]{16}|[0-9a-fA-F]{20}|[0-9a-fA-F]{24})`
Required: Yes

 ** DukptDerivationType **   <a name="paymentcryptographydata-Type-MacAlgorithmDukpt-DukptDerivationType"></a>
The key type derived using DUKPT from a Base Derivation Key (BDK) and Key Serial Number (KSN). This must be less than or equal to the strength of the BDK. For example, you can't use `AES_128` as a derivation type for a BDK of `AES_128` or `TDES_2KEY`.
Type: String
Valid Values: `TDES_2KEY | TDES_3KEY | AES_128 | AES_192 | AES_256`
Required: No

## See Also
<a name="API_MacAlgorithmDukpt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/MacAlgorithmDukpt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/MacAlgorithmDukpt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/MacAlgorithmDukpt)
