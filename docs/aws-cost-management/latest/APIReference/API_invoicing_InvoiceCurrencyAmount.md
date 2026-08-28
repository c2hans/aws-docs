---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceCurrencyAmount.html
---

# InvoiceCurrencyAmount
<a name="API_invoicing_InvoiceCurrencyAmount"></a>

 The amount charged after taxes, in the preferred currency.

## Contents
<a name="API_invoicing_InvoiceCurrencyAmount_Contents"></a>

 ** AmountBreakdown **   <a name="awscostmanagement-Type-invoicing_InvoiceCurrencyAmount-AmountBreakdown"></a>
 Details about the invoice currency amount.
Type: [AmountBreakdown](API_invoicing_AmountBreakdown.md) object
Required: No

 ** CurrencyCode **   <a name="awscostmanagement-Type-invoicing_InvoiceCurrencyAmount-CurrencyCode"></a>
The currency dominion of the invoice document.
Type: String
Length Constraints: Fixed length of 3.
Required: No

 ** CurrencyExchangeDetails **   <a name="awscostmanagement-Type-invoicing_InvoiceCurrencyAmount-CurrencyExchangeDetails"></a>
 The details of currency exchange.
Type: [CurrencyExchangeDetails](API_invoicing_CurrencyExchangeDetails.md) object
Required: No

 ** TotalAmount **   <a name="awscostmanagement-Type-invoicing_InvoiceCurrencyAmount-TotalAmount"></a>
 The invoice currency amount.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** TotalAmountBeforeTax **   <a name="awscostmanagement-Type-invoicing_InvoiceCurrencyAmount-TotalAmountBeforeTax"></a>
 Details about the invoice total amount before tax.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_invoicing_InvoiceCurrencyAmount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/InvoiceCurrencyAmount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/InvoiceCurrencyAmount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/InvoiceCurrencyAmount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
