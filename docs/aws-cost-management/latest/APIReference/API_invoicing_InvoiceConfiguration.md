---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceConfiguration.html
---

# InvoiceConfiguration
<a name="API_invoicing_InvoiceConfiguration"></a>

Specifies the supported document types and attachment types for invoice delivery to a procurement portal.

## Contents
<a name="API_invoicing_InvoiceConfiguration_Contents"></a>

 ** AttachmentTypes **   <a name="awscostmanagement-Type-invoicing_InvoiceConfiguration-AttachmentTypes"></a>
The attachment types supported by the procurement portal for e-invoice delivery.
Type: Array of strings
Valid Values: `INVOICE_PDF | RFP_PDF`
Required: No

 ** DocumentTypes **   <a name="awscostmanagement-Type-invoicing_InvoiceConfiguration-DocumentTypes"></a>
The e-invoice document types supported by the procurement portal.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `AWS_CLOUD_INVOICE | AWS_CLOUD_CREDIT_MEMO | AWS_MARKETPLACE_INVOICE | AWS_MARKETPLACE_CREDIT_MEMO | AWS_REQUEST_FOR_PAYMENT`
Required: No

## See Also
<a name="API_invoicing_InvoiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/InvoiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/InvoiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/InvoiceConfiguration)
