---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AgreementInvoiceLineItemGroupSummary.html
---

# AgreementInvoiceLineItemGroupSummary
<a name="API_marketplace-agreements_AgreementInvoiceLineItemGroupSummary"></a>

A summary of grouped billing data for an agreement invoice line item.

## Contents
<a name="API_marketplace-agreements_AgreementInvoiceLineItemGroupSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** agreementId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementInvoiceLineItemGroupSummary-agreementId"></a>
The unique identifier of the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** invoiceBillingPeriod **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementInvoiceLineItemGroupSummary-invoiceBillingPeriod"></a>
The billing period associated with this group.
Type: [InvoiceBillingPeriod](API_marketplace-agreements_InvoiceBillingPeriod.md) object
Required: No

 ** invoiceId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementInvoiceLineItemGroupSummary-invoiceId"></a>
The identifier of the invoice for this group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** invoiceType **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementInvoiceLineItemGroupSummary-invoiceType"></a>
The type of invoice. Valid values are `INVOICE` and `CREDIT_MEMO`.
Type: String
Valid Values: `INVOICE | CREDIT_MEMO`
Required: No

 ** invoicingEntity **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementInvoiceLineItemGroupSummary-invoicingEntity"></a>
The entity that issues the invoice.
Type: [InvoicingEntity](API_marketplace-agreements_InvoicingEntity.md) object
Required: No

 ** issuedTime **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementInvoiceLineItemGroupSummary-issuedTime"></a>
The timestamp when the invoice containing this group was created.
Type: Timestamp
Required: No

 ** pricingCurrencyAmount **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AgreementInvoiceLineItemGroupSummary-pricingCurrencyAmount"></a>
Monetary amounts for this invoice group.
Type: [PricingCurrencyAmount](API_marketplace-agreements_PricingCurrencyAmount.md) object
Required: No

## See Also
<a name="API_marketplace-agreements_AgreementInvoiceLineItemGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AgreementInvoiceLineItemGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AgreementInvoiceLineItemGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AgreementInvoiceLineItemGroupSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
