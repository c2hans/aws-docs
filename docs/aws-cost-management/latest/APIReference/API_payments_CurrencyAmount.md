---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_CurrencyAmount.html
---

# CurrencyAmount

A monetary amount expressed as a decimal string in the currency's standard unit.

## Contents
<a name="API_payments_CurrencyAmount_Contents"></a>

 ** currency **   <a name="awscostmanagement-Type-payments_CurrencyAmount-currency"></a>
The ISO 4217 currency code for the amount (for example, `USD`).
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]{3}`
Required: Yes

 ** value **   <a name="awscostmanagement-Type-payments_CurrencyAmount-value"></a>
The amount, as a decimal string, such as `10.99`. The number of decimal places can differ between amounts, for example `0.0` and `1000.24`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `-?((0|[1-9]\d*)(\.\d+)?)`
Required: Yes

## See Also
<a name="API_payments_CurrencyAmount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/CurrencyAmount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/CurrencyAmount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/CurrencyAmount)
