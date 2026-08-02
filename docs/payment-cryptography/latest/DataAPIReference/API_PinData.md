---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_PinData.html
---

# PinData
<a name="API_PinData"></a>

Parameters that are required to generate, translate, or verify PIN data.

## Contents
<a name="API_PinData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** PinOffset **   <a name="paymentcryptographydata-Type-PinData-PinOffset"></a>
The PIN offset value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 12.
Pattern: `[0-9]+`
Required: No

 ** VerificationValue **   <a name="paymentcryptographydata-Type-PinData-VerificationValue"></a>
The unique data to identify a cardholder. In most cases, this is the same as cardholder's Primary Account Number (PAN). If a value is not provided, it defaults to PAN.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 12.
Pattern: `[0-9]+`
Required: No

## See Also
<a name="API_PinData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/PinData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/PinData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/PinData)
