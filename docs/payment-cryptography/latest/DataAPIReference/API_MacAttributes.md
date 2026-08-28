---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_MacAttributes.html
---

# MacAttributes
<a name="API_MacAttributes"></a>

Parameters that are required for DUKPT, HMAC, or EMV MAC generation or verification.

## Contents
<a name="API_MacAttributes_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Algorithm **   <a name="paymentcryptographydata-Type-MacAttributes-Algorithm"></a>
The encryption algorithm for MAC generation or verification.
Type: String
Valid Values: `ISO9797_ALGORITHM1 | ISO9797_ALGORITHM3 | CMAC | HMAC | HMAC_SHA224 | HMAC_SHA256 | HMAC_SHA384 | HMAC_SHA512 | AS2805_4_1`
Required: No

 ** DukptCmac **   <a name="paymentcryptographydata-Type-MacAttributes-DukptCmac"></a>
Parameters that are required for MAC generation or verification using DUKPT CMAC algorithm.
Type: [MacAlgorithmDukpt](API_MacAlgorithmDukpt.md) object
Required: No

 ** DukptIso9797Algorithm1 **   <a name="paymentcryptographydata-Type-MacAttributes-DukptIso9797Algorithm1"></a>
Parameters that are required for MAC generation or verification using DUKPT ISO 9797 algorithm1.
Type: [MacAlgorithmDukpt](API_MacAlgorithmDukpt.md) object
Required: No

 ** DukptIso9797Algorithm3 **   <a name="paymentcryptographydata-Type-MacAttributes-DukptIso9797Algorithm3"></a>
Parameters that are required for MAC generation or verification using DUKPT ISO 9797 algorithm3.
Type: [MacAlgorithmDukpt](API_MacAlgorithmDukpt.md) object
Required: No

 ** EmvMac **   <a name="paymentcryptographydata-Type-MacAttributes-EmvMac"></a>
Parameters that are required for MAC generation or verification using EMV MAC algorithm.
Type: [MacAlgorithmEmv](API_MacAlgorithmEmv.md) object
Required: No

## See Also
<a name="API_MacAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/MacAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/MacAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/MacAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
