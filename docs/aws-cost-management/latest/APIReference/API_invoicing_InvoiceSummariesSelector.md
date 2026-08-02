---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceSummariesSelector.html
---

# InvoiceSummariesSelector
<a name="API_invoicing_InvoiceSummariesSelector"></a>

Specifies the invoice summary.

## Contents
<a name="API_invoicing_InvoiceSummariesSelector_Contents"></a>

 ** ResourceType **   <a name="awscostmanagement-Type-invoicing_InvoiceSummariesSelector-ResourceType"></a>
The query identifier type (`INVOICE_ID` or `ACCOUNT_ID`).
Type: String
Valid Values: `ACCOUNT_ID | INVOICE_ID`
Required: Yes

 ** Value **   <a name="awscostmanagement-Type-invoicing_InvoiceSummariesSelector-Value"></a>
The value of the query identifier.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_invoicing_InvoiceSummariesSelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/InvoiceSummariesSelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/InvoiceSummariesSelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/InvoiceSummariesSelector)
