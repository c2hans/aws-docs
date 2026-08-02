---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_Ibm3624PinFromOffset.html
---

# Ibm3624PinFromOffset
<a name="API_Ibm3624PinFromOffset"></a>

Parameters that are required to generate or verify Ibm3624 PIN from offset PIN.

## Contents
<a name="API_Ibm3624PinFromOffset_Contents"></a>

 ** DecimalizationTable **   <a name="paymentcryptographydata-Type-Ibm3624PinFromOffset-DecimalizationTable"></a>
The decimalization table to use for IBM 3624 PIN algorithm. The table is used to convert the algorithm intermediate result from hexadecimal characters to decimal.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `[0-9]+`
Required: Yes

 ** PinOffset **   <a name="paymentcryptographydata-Type-Ibm3624PinFromOffset-PinOffset"></a>
The PIN offset value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 12.
Pattern: `[0-9]+`
Required: Yes

 ** PinValidationData **   <a name="paymentcryptographydata-Type-Ibm3624PinFromOffset-PinValidationData"></a>
The unique data for cardholder identification.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9]+`
Required: Yes

 ** PinValidationDataPadCharacter **   <a name="paymentcryptographydata-Type-Ibm3624PinFromOffset-PinValidationDataPadCharacter"></a>
The padding character for validation data.
Type: String
Length Constraints: Fixed length of 1.
Pattern: `[0-9A-F]+`
Required: Yes

## See Also
<a name="API_Ibm3624PinFromOffset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/Ibm3624PinFromOffset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/Ibm3624PinFromOffset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/Ibm3624PinFromOffset)
