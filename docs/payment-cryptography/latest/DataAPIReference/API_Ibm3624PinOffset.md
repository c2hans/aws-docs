---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_Ibm3624PinOffset.html
---

# Ibm3624PinOffset
<a name="API_Ibm3624PinOffset"></a>

Pparameters that are required to generate or verify Ibm3624 PIN offset PIN.

## Contents
<a name="API_Ibm3624PinOffset_Contents"></a>

 ** DecimalizationTable **   <a name="paymentcryptographydata-Type-Ibm3624PinOffset-DecimalizationTable"></a>
The decimalization table to use for IBM 3624 PIN algorithm. The table is used to convert the algorithm intermediate result from hexadecimal characters to decimal.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `[0-9]+`
Required: Yes

 ** EncryptedPinBlock **   <a name="paymentcryptographydata-Type-Ibm3624PinOffset-EncryptedPinBlock"></a>
The encrypted PIN block data. According to ISO 9564 standard, a PIN Block is an encoded representation of a payment card Personal Account Number (PAN) and the cardholder Personal Identification Number (PIN).
Type: String
Length Constraints: Minimum length of 16. Maximum length of 32.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** PinValidationData **   <a name="paymentcryptographydata-Type-Ibm3624PinOffset-PinValidationData"></a>
The unique data for cardholder identification.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9]+`
Required: Yes

 ** PinValidationDataPadCharacter **   <a name="paymentcryptographydata-Type-Ibm3624PinOffset-PinValidationDataPadCharacter"></a>
The padding character for validation data.
Type: String
Length Constraints: Fixed length of 1.
Pattern: `[0-9A-F]+`
Required: Yes

## See Also
<a name="API_Ibm3624PinOffset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/Ibm3624PinOffset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/Ibm3624PinOffset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/Ibm3624PinOffset)
