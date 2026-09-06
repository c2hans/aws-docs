---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Amount.html
---

# Amount
<a name="API_billing_Amount"></a>

A monetary amount with a currency code. Used throughout the Billing API to represent credit balances, allocations, and adjustments.

## Contents
<a name="API_billing_Amount_Contents"></a>

 ** currencyAmount **   <a name="awscostmanagement-Type-billing_Amount-currencyAmount"></a>
The amount as a decimal string (for example, `"743.21"`). Negative values represent credits that reduce a bill.
Type: String
Pattern: `[0-9]+(.[0-9]+)`
Required: Yes

 ** currencyCode **   <a name="awscostmanagement-Type-billing_Amount-currencyCode"></a>
The ISO 4217 currency code for the amount (for example, `USD`).
Type: String
Pattern: `[A-Z]{3}`
Required: Yes

## See Also
<a name="API_billing_Amount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/Amount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/Amount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/Amount)
