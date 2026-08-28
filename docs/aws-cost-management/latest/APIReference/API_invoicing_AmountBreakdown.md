---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_AmountBreakdown.html
---

# AmountBreakdown
<a name="API_invoicing_AmountBreakdown"></a>

Details about how the total amount was calculated and categorized.

## Contents
<a name="API_invoicing_AmountBreakdown_Contents"></a>

 ** Discounts **   <a name="awscostmanagement-Type-invoicing_AmountBreakdown-Discounts"></a>
 The discounted amount.
Type: [DiscountsBreakdown](API_invoicing_DiscountsBreakdown.md) object
Required: No

 ** Fees **   <a name="awscostmanagement-Type-invoicing_AmountBreakdown-Fees"></a>
 The fee amount.
Type: [FeesBreakdown](API_invoicing_FeesBreakdown.md) object
Required: No

 ** SubTotalAmount **   <a name="awscostmanagement-Type-invoicing_AmountBreakdown-SubTotalAmount"></a>
 The total of a set of the breakdown.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** Taxes **   <a name="awscostmanagement-Type-invoicing_AmountBreakdown-Taxes"></a>
 The tax amount.
Type: [TaxesBreakdown](API_invoicing_TaxesBreakdown.md) object
Required: No

## See Also
<a name="API_invoicing_AmountBreakdown_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/AmountBreakdown)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/AmountBreakdown)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/AmountBreakdown)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
