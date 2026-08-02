---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ProcurementPortalPreferenceSelector.html
---

# ProcurementPortalPreferenceSelector
<a name="API_invoicing_ProcurementPortalPreferenceSelector"></a>

Specifies criteria for selecting which invoices should be processed using a particular procurement portal preference.

## Contents
<a name="API_invoicing_ProcurementPortalPreferenceSelector_Contents"></a>

 ** InvoiceUnitArns **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSelector-InvoiceUnitArns"></a>
 The Amazon Resource Name (ARN) of invoice unit identifiers to which this preference applies.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: No

 ** SellerOfRecords **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSelector-SellerOfRecords"></a>
 The list of seller of record IDs to which this preference applies.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

## See Also
<a name="API_invoicing_ProcurementPortalPreferenceSelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/ProcurementPortalPreferenceSelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/ProcurementPortalPreferenceSelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/ProcurementPortalPreferenceSelector)
