---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_TestEnvPreference.html
---

# TestEnvPreference
<a name="API_invoicing_TestEnvPreference"></a>

Contains configuration settings for testing the procurement portal integration in a non-production environment.

## Contents
<a name="API_invoicing_TestEnvPreference_Contents"></a>

 ** BuyerDomain **   <a name="awscostmanagement-Type-invoicing_TestEnvPreference-BuyerDomain"></a>
The domain identifier for the buyer in the test environment of the procurement portal.
Type: String
Valid Values: `NetworkID`
Required: Yes

 ** BuyerIdentifier **   <a name="awscostmanagement-Type-invoicing_TestEnvPreference-BuyerIdentifier"></a>
The unique identifier for the buyer in the test environment of the procurement portal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: Yes

 ** SupplierDomain **   <a name="awscostmanagement-Type-invoicing_TestEnvPreference-SupplierDomain"></a>
The domain identifier for the supplier in the test environment of the procurement portal.
Type: String
Valid Values: `NetworkID`
Required: Yes

 ** SupplierIdentifier **   <a name="awscostmanagement-Type-invoicing_TestEnvPreference-SupplierIdentifier"></a>
The unique identifier for the supplier in the test environment of the procurement portal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: Yes

 ** ProcurementPortalInstanceEndpoint **   <a name="awscostmanagement-Type-invoicing_TestEnvPreference-ProcurementPortalInstanceEndpoint"></a>
The endpoint URL where e-invoices are delivered in the test environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** ProcurementPortalSharedSecret **   <a name="awscostmanagement-Type-invoicing_TestEnvPreference-ProcurementPortalSharedSecret"></a>
The shared secret or authentication credential used for secure communication with the test environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** PurchaseOrderRetrievalEndpoint **   <a name="awscostmanagement-Type-invoicing_TestEnvPreference-PurchaseOrderRetrievalEndpoint"></a>
The endpoint URL used for retrieving purchase orders in the test environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

## See Also
<a name="API_invoicing_TestEnvPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/TestEnvPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/TestEnvPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/TestEnvPreference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
