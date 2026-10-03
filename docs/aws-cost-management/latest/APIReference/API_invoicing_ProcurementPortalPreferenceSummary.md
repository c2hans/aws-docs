---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ProcurementPortalPreferenceSummary.html
---

# ProcurementPortalPreferenceSummary
<a name="API_invoicing_ProcurementPortalPreferenceSummary"></a>

Provides a summary of a procurement portal preference, including key identifiers and status information.

## Contents
<a name="API_invoicing_ProcurementPortalPreferenceSummary_Contents"></a>

 ** AwsAccountId **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-AwsAccountId"></a>
The AWS account ID associated with this procurement portal preference summary.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** BuyerDomain **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-BuyerDomain"></a>
The domain identifier for the buyer in the procurement portal.
Type: String
Valid Values: `NetworkID`
Required: Yes

 ** BuyerIdentifier **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-BuyerIdentifier"></a>
The unique identifier for the buyer in the procurement portal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: Yes

 ** CreateDate **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-CreateDate"></a>
The date and time when the procurement portal preference was created.
Type: Timestamp
Required: Yes

 ** EinvoiceDeliveryEnabled **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-EinvoiceDeliveryEnabled"></a>
Indicates whether e-invoice delivery is enabled for this procurement portal preference.
Type: Boolean
Required: Yes

 ** LastUpdateDate **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-LastUpdateDate"></a>
The date and time when the procurement portal preference was last updated.
Type: Timestamp
Required: Yes

 ** ProcurementPortalName **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-ProcurementPortalName"></a>
The name of the procurement portal.
Type: String
Valid Values: `SAP_BUSINESS_NETWORK | COUPA`
Required: Yes

 ** ProcurementPortalPreferenceArn **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-ProcurementPortalPreferenceArn"></a>
The Amazon Resource Name (ARN) of the procurement portal preference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws:invoicing::[0-9]{12}:procurement-portal-preference/[-a-zA-Z0-9]+`
Required: Yes

 ** PurchaseOrderRetrievalEnabled **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-PurchaseOrderRetrievalEnabled"></a>
Indicates whether purchase order retrieval is enabled for this procurement portal preference.
Type: Boolean
Required: Yes

 ** SupplierDomain **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-SupplierDomain"></a>
The domain identifier for the supplier in the procurement portal.
Type: String
Valid Values: `NetworkID`
Required: Yes

 ** SupplierIdentifier **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-SupplierIdentifier"></a>
The unique identifier for the supplier in the procurement portal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: Yes

 ** Version **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-Version"></a>
The version number of the procurement portal preference configuration in this summary.
Type: Long
Required: Yes

 ** EinvoiceDeliveryPreferenceStatus **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-EinvoiceDeliveryPreferenceStatus"></a>
The current status of the e-invoice delivery preference in this summary.
Type: String
Valid Values: `PENDING_VERIFICATION | VALIDATED | TEST_INITIALIZED | TEST_INITIALIZATION_FAILED | TEST_FAILED | ACTIVE | SUSPENDED`
Required: No

 ** EinvoiceDeliveryPreferenceStatusReason **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-EinvoiceDeliveryPreferenceStatusReason"></a>
The reason for the current e-invoice delivery preference status in this summary.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** MarketplacePunchOutEnabled **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-MarketplacePunchOutEnabled"></a>
Indicates whether Marketplace PunchOut is enabled for this procurement portal preference. Defaults to `false`.
Type: Boolean
Required: No

 ** PurchaseOrderRetrievalPreferenceStatus **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-PurchaseOrderRetrievalPreferenceStatus"></a>
The current status of the purchase order retrieval preference in this summary.
Type: String
Valid Values: `PENDING_VERIFICATION | VALIDATED | TEST_INITIALIZED | TEST_INITIALIZATION_FAILED | TEST_FAILED | ACTIVE | SUSPENDED`
Required: No

 ** PurchaseOrderRetrievalPreferenceStatusReason **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-PurchaseOrderRetrievalPreferenceStatusReason"></a>
The reason for the current purchase order retrieval preference status in this summary.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** Selector **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreferenceSummary-Selector"></a>
Specifies criteria for selecting which invoices should be processed using a particular procurement portal preference.
Type: [ProcurementPortalPreferenceSelector](API_invoicing_ProcurementPortalPreferenceSelector.md) object
Required: No

## See Also
<a name="API_invoicing_ProcurementPortalPreferenceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/ProcurementPortalPreferenceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/ProcurementPortalPreferenceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/ProcurementPortalPreferenceSummary)
