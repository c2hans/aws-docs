---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_TrustCenterControl.html
---

# TrustCenterControl

A control that a trust center publishes.

## Contents
<a name="API_marketplace-discovery_TrustCenterControl_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** domains **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterControl-domains"></a>
The trust center domains to which the control applies.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `SECURITY | AI_GOVERNANCE | RESILIENCE`
Required: Yes

 ** name **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterControl-name"></a>
The name of the control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** description **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterControl-description"></a>
A description of the control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_marketplace-discovery_TrustCenterControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/TrustCenterControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/TrustCenterControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/TrustCenterControl)
