---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_EinvoiceDeliveryPreference.html
---

# EinvoiceDeliveryPreference
<a name="API_invoicing_EinvoiceDeliveryPreference"></a>

Specifies the preferences for e-invoice delivery, including document types, attachment types, and customization settings.

## Contents
<a name="API_invoicing_EinvoiceDeliveryPreference_Contents"></a>

 ** ConnectionTestingMethod **   <a name="awscostmanagement-Type-invoicing_EinvoiceDeliveryPreference-ConnectionTestingMethod"></a>
The method to use for testing the connection to the procurement portal.
Type: String
Valid Values: `PROD_ENV_DOLLAR_TEST | TEST_ENV_REPLAY_TEST`
Required: Yes

 ** EinvoiceDeliveryActivationDate **   <a name="awscostmanagement-Type-invoicing_EinvoiceDeliveryPreference-EinvoiceDeliveryActivationDate"></a>
The date when e-invoice delivery should be activated for this preference.
Type: Timestamp
Required: Yes

 ** EinvoiceDeliveryDocumentTypes **   <a name="awscostmanagement-Type-invoicing_EinvoiceDeliveryPreference-EinvoiceDeliveryDocumentTypes"></a>
The types of e-invoice documents to be delivered.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `AWS_CLOUD_INVOICE | AWS_CLOUD_CREDIT_MEMO | AWS_MARKETPLACE_INVOICE | AWS_MARKETPLACE_CREDIT_MEMO | AWS_REQUEST_FOR_PAYMENT`
Required: Yes

 ** Protocol **   <a name="awscostmanagement-Type-invoicing_EinvoiceDeliveryPreference-Protocol"></a>
The communication protocol to use for e-invoice delivery.
Type: String
Valid Values: `CXML`
Required: Yes

 ** PurchaseOrderDataSources **   <a name="awscostmanagement-Type-invoicing_EinvoiceDeliveryPreference-PurchaseOrderDataSources"></a>
The sources of purchase order data to use for e-invoice generation and delivery.
Type: Array of [PurchaseOrderDataSource](API_invoicing_PurchaseOrderDataSource.md) objects
Required: Yes

 ** EinvoiceDeliveryAttachmentTypes **   <a name="awscostmanagement-Type-invoicing_EinvoiceDeliveryPreference-EinvoiceDeliveryAttachmentTypes"></a>
The types of attachments to include with the e-invoice delivery.
Type: Array of strings
Valid Values: `INVOICE_PDF | RFP_PDF`
Required: No

## See Also
<a name="API_invoicing_EinvoiceDeliveryPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/EinvoiceDeliveryPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/EinvoiceDeliveryPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/EinvoiceDeliveryPreference)
