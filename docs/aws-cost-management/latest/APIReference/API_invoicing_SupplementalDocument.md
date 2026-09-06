---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_SupplementalDocument.html
---

# SupplementalDocument
<a name="API_invoicing_SupplementalDocument"></a>

Supplemental document associated with the invoice.

## Contents
<a name="API_invoicing_SupplementalDocument_Contents"></a>

 ** DocumentId **   <a name="awscostmanagement-Type-invoicing_SupplementalDocument-DocumentId"></a>
The ID of the supplemental document.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** DocumentType **   <a name="awscostmanagement-Type-invoicing_SupplementalDocument-DocumentType"></a>
The type of supplemental document.
Type: String
Valid Values: `GOVERNMENT_INVOICE | TAX_E_INVOICE | PAYMENT_RECEIPT | SUPPLEMENT`
Required: No

 ** DocumentUrl **   <a name="awscostmanagement-Type-invoicing_SupplementalDocument-DocumentUrl"></a>
The pre-signed URL to download invoice supplemental document.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** DocumentUrlExpirationDate **   <a name="awscostmanagement-Type-invoicing_SupplementalDocument-DocumentUrlExpirationDate"></a>
The pre-signed URL expiration date of invoice supplemental document.
Type: Timestamp
Required: No

## See Also
<a name="API_invoicing_SupplementalDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/SupplementalDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/SupplementalDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/SupplementalDocument)
