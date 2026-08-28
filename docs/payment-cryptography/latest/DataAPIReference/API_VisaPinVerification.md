---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VisaPinVerification.html
---

# VisaPinVerification
<a name="API_VisaPinVerification"></a>

Parameters that are required to generate or verify Visa PIN.

## Contents
<a name="API_VisaPinVerification_Contents"></a>

 ** PinVerificationKeyIndex **   <a name="paymentcryptographydata-Type-VisaPinVerification-PinVerificationKeyIndex"></a>
The value for PIN verification index. It is used in the Visa PIN algorithm to calculate the PVV (PIN Verification Value).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6.
Required: Yes

 ** VerificationValue **   <a name="paymentcryptographydata-Type-VisaPinVerification-VerificationValue"></a>
Parameters that are required to generate or verify Visa PVV (PIN Verification Value).
Type: String
Length Constraints: Minimum length of 4. Maximum length of 12.
Pattern: `[0-9]+`
Required: Yes

## See Also
<a name="API_VisaPinVerification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/VisaPinVerification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/VisaPinVerification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/VisaPinVerification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
