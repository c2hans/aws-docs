---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_PinGenerationAttributes.html
---

# PinGenerationAttributes
<a name="API_PinGenerationAttributes"></a>

Parameters that are required for PIN data generation.

## Contents
<a name="API_PinGenerationAttributes_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Ibm3624NaturalPin **   <a name="paymentcryptographydata-Type-PinGenerationAttributes-Ibm3624NaturalPin"></a>
Parameters that are required to generate or verify Ibm3624 natural PIN.
Type: [Ibm3624NaturalPin](API_Ibm3624NaturalPin.md) object
Required: No

 ** Ibm3624PinFromOffset **   <a name="paymentcryptographydata-Type-PinGenerationAttributes-Ibm3624PinFromOffset"></a>
Parameters that are required to generate or verify Ibm3624 PIN from offset PIN.
Type: [Ibm3624PinFromOffset](API_Ibm3624PinFromOffset.md) object
Required: No

 ** Ibm3624PinOffset **   <a name="paymentcryptographydata-Type-PinGenerationAttributes-Ibm3624PinOffset"></a>
Parameters that are required to generate or verify Ibm3624 PIN offset PIN.
Type: [Ibm3624PinOffset](API_Ibm3624PinOffset.md) object
Required: No

 ** Ibm3624RandomPin **   <a name="paymentcryptographydata-Type-PinGenerationAttributes-Ibm3624RandomPin"></a>
Parameters that are required to generate or verify Ibm3624 random PIN.
Type: [Ibm3624RandomPin](API_Ibm3624RandomPin.md) object
Required: No

 ** VisaPin **   <a name="paymentcryptographydata-Type-PinGenerationAttributes-VisaPin"></a>
Parameters that are required to generate or verify Visa PIN.
Type: [VisaPin](API_VisaPin.md) object
Required: No

 ** VisaPinVerificationValue **   <a name="paymentcryptographydata-Type-PinGenerationAttributes-VisaPinVerificationValue"></a>
Parameters that are required to generate or verify Visa PIN Verification Value (PVV).
Type: [VisaPinVerificationValue](API_VisaPinVerificationValue.md) object
Required: No

## See Also
<a name="API_PinGenerationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/PinGenerationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/PinGenerationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/PinGenerationAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
