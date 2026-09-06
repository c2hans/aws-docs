---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceSummariesFilter.html
---

# InvoiceSummariesFilter
<a name="API_invoicing_InvoiceSummariesFilter"></a>

 Filters for your invoice summaries.

## Contents
<a name="API_invoicing_InvoiceSummariesFilter_Contents"></a>

 ** BillingPeriod **   <a name="awscostmanagement-Type-invoicing_InvoiceSummariesFilter-BillingPeriod"></a>
The billing period associated with the invoice documents.
Type: [BillingPeriod](API_invoicing_BillingPeriod.md) object
Required: No

 ** InvoicingEntity **   <a name="awscostmanagement-Type-invoicing_InvoiceSummariesFilter-InvoicingEntity"></a>
The name of the entity that issues the AWS invoice.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** ReceiverRole **   <a name="awscostmanagement-Type-invoicing_InvoiceSummariesFilter-ReceiverRole"></a>
The role of the invoice receiver to filter by.
When `ReceiverRole` is specified:
+ Data is available starting `2025-06-01`. Queries for periods before `2025-06-01` return a validation error.
+  `TimeInterval` supports a time interval of up to 5 years. Without `ReceiverRole`, `TimeInterval` is limited to one month.
Type: String
Valid Values: `SELLER | RESELLER | BUYER`
Required: No

 ** TimeInterval **   <a name="awscostmanagement-Type-invoicing_InvoiceSummariesFilter-TimeInterval"></a>
The date range for invoice summary retrieval.
Type: [DateInterval](API_invoicing_DateInterval.md) object
Required: No

## See Also
<a name="API_invoicing_InvoiceSummariesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/InvoiceSummariesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/InvoiceSummariesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/InvoiceSummariesFilter)
