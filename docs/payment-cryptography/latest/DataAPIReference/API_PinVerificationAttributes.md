---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_PinVerificationAttributes.html
---

# PinVerificationAttributes
<a name="API_PinVerificationAttributes"></a>

Parameters that are required for PIN data verification.

## Contents
<a name="API_PinVerificationAttributes_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Ibm3624Pin **   <a name="paymentcryptographydata-Type-PinVerificationAttributes-Ibm3624Pin"></a>
Parameters that are required to generate or verify Ibm3624 PIN.
Type: [Ibm3624PinVerification](API_Ibm3624PinVerification.md) object
Required: No

 ** VisaPin **   <a name="paymentcryptographydata-Type-PinVerificationAttributes-VisaPin"></a>
Parameters that are required to generate or verify Visa PIN.
Type: [VisaPinVerification](API_VisaPinVerification.md) object
Required: No

## See Also
<a name="API_PinVerificationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/PinVerificationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/PinVerificationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/PinVerificationAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
