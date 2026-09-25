---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SaasFulfillmentOption.html
---

# SaasFulfillmentOption
<a name="API_marketplace-discovery_SaasFulfillmentOption"></a>

Describes a Software as a Service (SaaS) fulfillment option.

## Contents
<a name="API_marketplace-discovery_SaasFulfillmentOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** fulfillmentOptionDisplayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasFulfillmentOption-fulfillmentOptionDisplayName"></a>
A human-readable name for the fulfillment option type.
Type: String
Required: Yes

 ** fulfillmentOptionId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasFulfillmentOption-fulfillmentOptionId"></a>
The unique identifier of the fulfillment option.
Type: String
Required: Yes

 ** fulfillmentOptionType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasFulfillmentOption-fulfillmentOptionType"></a>
The category of the fulfillment option.
Type: String
Valid Values: `AMAZON_MACHINE_IMAGE | API | CLOUDFORMATION_TEMPLATE | CONTAINER | HELM | EKS_ADD_ON | EC2_IMAGE_BUILDER_COMPONENT | DATA_EXCHANGE | PROFESSIONAL_SERVICES | SAAS | SAGEMAKER_ALGORITHM | SAGEMAKER_MODEL`
Required: Yes

 ** quickLaunch **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasFulfillmentOption-quickLaunch"></a>
Specifies whether the SaaS product supports quick-launch deployment.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** availableFromTime **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasFulfillmentOption-availableFromTime"></a>
The date and time when the SaaS product became available for fulfillment.
Type: Timestamp
Required: No

 ** fulfillmentUrl **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasFulfillmentOption-fulfillmentUrl"></a>
The URL of the seller's software registration landing page.
Type: String
Required: No

 ** launchUrl **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasFulfillmentOption-launchUrl"></a>
The URL that a buyer uses to launch the seller's SaaS product. This URL is distinct from `fulfillmentUrl`, which is the seller's software registration landing page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://.*`
Required: No

 ** usageInstructions **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SaasFulfillmentOption-usageInstructions"></a>
Instructions on how to access and use this SaaS product.
Type: String
Required: No

## See Also
<a name="API_marketplace-discovery_SaasFulfillmentOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/SaasFulfillmentOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/SaasFulfillmentOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SaasFulfillmentOption)
