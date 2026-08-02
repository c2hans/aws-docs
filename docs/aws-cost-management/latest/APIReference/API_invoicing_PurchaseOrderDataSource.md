---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_PurchaseOrderDataSource.html
---

# PurchaseOrderDataSource
<a name="API_invoicing_PurchaseOrderDataSource"></a>

Specifies the source configuration for retrieving purchase order data.

## Contents
<a name="API_invoicing_PurchaseOrderDataSource_Contents"></a>

 ** EinvoiceDeliveryDocumentType **   <a name="awscostmanagement-Type-invoicing_PurchaseOrderDataSource-EinvoiceDeliveryDocumentType"></a>
The type of e-invoice document that requires purchase order data.
Type: String
Valid Values: `AWS_CLOUD_INVOICE | AWS_CLOUD_CREDIT_MEMO | AWS_MARKETPLACE_INVOICE | AWS_MARKETPLACE_CREDIT_MEMO | AWS_REQUEST_FOR_PAYMENT`
Required: No

 ** PurchaseOrderDataSourceType **   <a name="awscostmanagement-Type-invoicing_PurchaseOrderDataSource-PurchaseOrderDataSourceType"></a>
The type of source for purchase order data.
Type: String
Valid Values: `ASSOCIATED_PURCHASE_ORDER_REQUIRED | PURCHASE_ORDER_NOT_REQUIRED`
Required: No

## See Also
<a name="API_invoicing_PurchaseOrderDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/PurchaseOrderDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/PurchaseOrderDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/PurchaseOrderDataSource)
