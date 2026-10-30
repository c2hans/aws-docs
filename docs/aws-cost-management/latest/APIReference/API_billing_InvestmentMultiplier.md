---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_InvestmentMultiplier.html
---

# InvestmentMultiplier
<a name="API_billing_InvestmentMultiplier"></a>

A multiplier used to convert attestation input into an investment value.

## Contents
<a name="API_billing_InvestmentMultiplier_Contents"></a>

 ** investmentAttestationInputUnit **   <a name="awscostmanagement-Type-billing_InvestmentMultiplier-investmentAttestationInputUnit"></a>
The unit of the attestation input that the multiplier applies to, such as `workloads migrated`. This value is 1–1000 characters. The terms of the contract define this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** multiplierType **   <a name="awscostmanagement-Type-billing_InvestmentMultiplier-multiplierType"></a>
The type of the multiplier. A value of `PERCENTAGE` applies a percentage of a value. A value of `CURRENCY_AMOUNT` applies a currency amount per unit of attestation input. The terms of the contract define this value.
Type: String
Valid Values: `PERCENTAGE | CURRENCY_AMOUNT`
Required: Yes

 ** value **   <a name="awscostmanagement-Type-billing_InvestmentMultiplier-value"></a>
The multiplier value, expressed as a decimal string to preserve precision. The value is digits with an optional decimal point and is 1–1000 characters. The terms of the contract define this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[0-9]+(\.[0-9]+)?`
Required: Yes

## See Also
<a name="API_billing_InvestmentMultiplier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/InvestmentMultiplier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/InvestmentMultiplier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/InvestmentMultiplier)
