---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ProcurementPortalSupplier.html
---

# ProcurementPortalSupplier
<a name="API_invoicing_ProcurementPortalSupplier"></a>

Contains metadata for a supplier configured within a procurement portal.

## Contents
<a name="API_invoicing_ProcurementPortalSupplier_Contents"></a>

 ** SupplierIdentifier **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalSupplier-SupplierIdentifier"></a>
The unique identifier of the supplier within the procurement portal.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** CountryCode **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalSupplier-CountryCode"></a>
The two-letter ISO 3166-1 alpha-2 country code associated with the supplier.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: No

 ** Environment **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalSupplier-Environment"></a>
The environment identifier for the supplier in the procurement portal. PROD for production env, or TEST for sandbox/test env.
Type: String
Valid Values: `PROD | TEST`
Required: No

 ** SellerOfRecord **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalSupplier-SellerOfRecord"></a>
The AWS seller of record associated with the supplier—the AWS legal entity that issues invoices for the account (for example, `AWS_INC` or `AWS_EUROPE`).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

## See Also
<a name="API_invoicing_ProcurementPortalSupplier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/ProcurementPortalSupplier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/ProcurementPortalSupplier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/ProcurementPortalSupplier)
