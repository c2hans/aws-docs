---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_PricingCurrencyAmount.html
---

# PricingCurrencyAmount
<a name="API_marketplace-agreements_PricingCurrencyAmount"></a>

Monetary amounts associated with an invoice line item group.

## Contents
<a name="API_marketplace-agreements_PricingCurrencyAmount_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** amount **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PricingCurrencyAmount-amount"></a>
The monetary amount before tax.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** currencyCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PricingCurrencyAmount-currencyCode"></a>
The 3-letter ISO 4217 currency code (e.g., `USD`, `EUR`, `JPY`).
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`
Required: No

 ** maxAdjustmentAmount **   <a name="AWSMarketplaceService-Type-marketplace-agreements_PricingCurrencyAmount-maxAdjustmentAmount"></a>
The maximum refundable amount as a string representation of a decimal number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

## See Also
<a name="API_marketplace-agreements_PricingCurrencyAmount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/PricingCurrencyAmount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/PricingCurrencyAmount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/PricingCurrencyAmount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
