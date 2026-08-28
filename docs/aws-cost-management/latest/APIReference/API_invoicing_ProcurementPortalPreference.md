---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ProcurementPortalPreference.html
---

# ProcurementPortalPreference
<a name="API_invoicing_ProcurementPortalPreference"></a>

Represents the full configuration of a procurement portal preference, including settings for e-invoice delivery and purchase order retrieval.

## Contents
<a name="API_invoicing_ProcurementPortalPreference_Contents"></a>

 ** AwsAccountId **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-AwsAccountId"></a>
The AWS account ID associated with this procurement portal preference.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** BuyerDomain **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-BuyerDomain"></a>
The domain identifier for the buyer in the procurement portal.
Type: String
Valid Values: `NetworkID`
Required: Yes

 ** BuyerIdentifier **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-BuyerIdentifier"></a>
The unique identifier for the buyer in the procurement portal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: Yes

 ** CreateDate **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-CreateDate"></a>
The date and time when the procurement portal preference was created.
Type: Timestamp
Required: Yes

 ** EinvoiceDeliveryEnabled **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-EinvoiceDeliveryEnabled"></a>
Indicates whether e-invoice delivery is enabled for this procurement portal preference.
Type: Boolean
Required: Yes

 ** LastUpdateDate **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-LastUpdateDate"></a>
The date and time when the procurement portal preference was last updated.
Type: Timestamp
Required: Yes

 ** ProcurementPortalName **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-ProcurementPortalName"></a>
The name of the procurement portal.
Type: String
Valid Values: `SAP_BUSINESS_NETWORK | COUPA`
Required: Yes

 ** ProcurementPortalPreferenceArn **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-ProcurementPortalPreferenceArn"></a>
The Amazon Resource Name (ARN) of the procurement portal preference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws:invoicing::[0-9]{12}:procurement-portal-preference/[-a-zA-Z0-9]+`
Required: Yes

 ** PurchaseOrderRetrievalEnabled **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-PurchaseOrderRetrievalEnabled"></a>
Indicates whether purchase order retrieval is enabled for this procurement portal preference.
Type: Boolean
Required: Yes

 ** SupplierDomain **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-SupplierDomain"></a>
The domain identifier for the supplier in the procurement portal.
Type: String
Valid Values: `NetworkID`
Required: Yes

 ** SupplierIdentifier **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-SupplierIdentifier"></a>
The unique identifier for the supplier in the procurement portal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: Yes

 ** Version **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-Version"></a>
The version number of the procurement portal preference configuration.
Type: Long
Required: Yes

 ** Contacts **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-Contacts"></a>
List of contact information for portal administrators and technical contacts.
Type: Array of [Contact](API_invoicing_Contact.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** EinvoiceDeliveryPreference **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-EinvoiceDeliveryPreference"></a>
The configuration settings that specify how e-invoices are delivered to the procurement portal.
Type: [EinvoiceDeliveryPreference](API_invoicing_EinvoiceDeliveryPreference.md) object
Required: No

 ** EinvoiceDeliveryPreferenceStatus **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-EinvoiceDeliveryPreferenceStatus"></a>
The current status of the e-invoice delivery preference.
Type: String
Valid Values: `PENDING_VERIFICATION | VALIDATED | TEST_INITIALIZED | TEST_INITIALIZATION_FAILED | TEST_FAILED | ACTIVE | SUSPENDED`
Required: No

 ** EinvoiceDeliveryPreferenceStatusReason **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-EinvoiceDeliveryPreferenceStatusReason"></a>
The reason for the current e-invoice delivery preference status.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** ProcurementPortalInstanceEndpoint **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-ProcurementPortalInstanceEndpoint"></a>
The endpoint URL where e-invoices are delivered to the procurement portal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** ProcurementPortalSharedSecret **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-ProcurementPortalSharedSecret"></a>
The shared secret or authentication credential used for secure communication with the procurement portal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** PurchaseOrderRetrievalEndpoint **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-PurchaseOrderRetrievalEndpoint"></a>
The endpoint URL used for retrieving purchase orders from the procurement portal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** PurchaseOrderRetrievalPreferenceStatus **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-PurchaseOrderRetrievalPreferenceStatus"></a>
The current status of the purchase order retrieval preference.
Type: String
Valid Values: `PENDING_VERIFICATION | VALIDATED | TEST_INITIALIZED | TEST_INITIALIZATION_FAILED | TEST_FAILED | ACTIVE | SUSPENDED`
Required: No

 ** PurchaseOrderRetrievalPreferenceStatusReason **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-PurchaseOrderRetrievalPreferenceStatusReason"></a>
The reason for the current purchase order retrieval preference status.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** Selector **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-Selector"></a>
Specifies criteria for selecting which invoices should be processed using a particular procurement portal preference.
Type: [ProcurementPortalPreferenceSelector](API_invoicing_ProcurementPortalPreferenceSelector.md) object
Required: No

 ** TestEnvPreference **   <a name="awscostmanagement-Type-invoicing_ProcurementPortalPreference-TestEnvPreference"></a>
Configuration on settings for the test environment of the procurement portal.
Type: [TestEnvPreference](API_invoicing_TestEnvPreference.md) object
Required: No

## See Also
<a name="API_invoicing_ProcurementPortalPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/ProcurementPortalPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/ProcurementPortalPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/ProcurementPortalPreference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
