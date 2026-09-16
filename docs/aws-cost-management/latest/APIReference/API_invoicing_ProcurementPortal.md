---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ProcurementPortal.html
---

# ProcurementPortal
<a name="API_invoicing_ProcurementPortal"></a>

Contains metadata for a procurement portal, including the portal identifier, name, and default feature configurations.

## Contents
<a name="API_invoicing_ProcurementPortal_Contents"></a>

 ** PortalIdentifier **   <a name="awscostmanagement-Type-invoicing_ProcurementPortal-PortalIdentifier"></a>
The unique identifier of the procurement portal.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** PortalName **   <a name="awscostmanagement-Type-invoicing_ProcurementPortal-PortalName"></a>
The name of the procurement portal.
Type: String
Valid Values: `SAP_BUSINESS_NETWORK | COUPA`
Required: Yes

 ** DefaultFeatureConfigurations **   <a name="awscostmanagement-Type-invoicing_ProcurementPortal-DefaultFeatureConfigurations"></a>
The default feature configurations for the procurement portal.
Type: [FeatureConfigurations](API_invoicing_FeatureConfigurations.md) object
Required: No

 ** PortalDisplayName **   <a name="awscostmanagement-Type-invoicing_ProcurementPortal-PortalDisplayName"></a>
The display name of the procurement portal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_invoicing_ProcurementPortal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/ProcurementPortal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/ProcurementPortal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/ProcurementPortal)
