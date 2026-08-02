---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_HelmFulfillmentOption.html
---

# HelmFulfillmentOption
<a name="API_marketplace-discovery_HelmFulfillmentOption"></a>

Describes a Helm chart fulfillment option for Kubernetes deployment.

## Contents
<a name="API_marketplace-discovery_HelmFulfillmentOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** fulfillmentOptionDisplayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_HelmFulfillmentOption-fulfillmentOptionDisplayName"></a>
A human-readable name for the fulfillment option type.
Type: String
Required: Yes

 ** fulfillmentOptionId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_HelmFulfillmentOption-fulfillmentOptionId"></a>
The unique identifier of the fulfillment option.
Type: String
Required: Yes

 ** fulfillmentOptionName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_HelmFulfillmentOption-fulfillmentOptionName"></a>
The display name of the fulfillment option version.
Type: String
Required: Yes

 ** fulfillmentOptionType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_HelmFulfillmentOption-fulfillmentOptionType"></a>
The category of the fulfillment option.
Type: String
Valid Values: `AMAZON_MACHINE_IMAGE | API | CLOUDFORMATION_TEMPLATE | CONTAINER | HELM | EKS_ADD_ON | EC2_IMAGE_BUILDER_COMPONENT | DATA_EXCHANGE | PROFESSIONAL_SERVICES | SAAS | SAGEMAKER_ALGORITHM | SAGEMAKER_MODEL`
Required: Yes

 ** awsSupportedServices **   <a name="AWSMarketplaceService-Type-marketplace-discovery_HelmFulfillmentOption-awsSupportedServices"></a>
The AWS services supported by this Helm chart deployment.
Type: Array of [AwsSupportedService](API_marketplace-discovery_AwsSupportedService.md) objects
Required: No

 ** fulfillmentOptionVersion **   <a name="AWSMarketplaceService-Type-marketplace-discovery_HelmFulfillmentOption-fulfillmentOptionVersion"></a>
The version identifier of the fulfillment option.
Type: String
Required: No

 ** operatingSystems **   <a name="AWSMarketplaceService-Type-marketplace-discovery_HelmFulfillmentOption-operatingSystems"></a>
The operating systems supported by this Helm chart.
Type: Array of [HelmOperatingSystem](API_marketplace-discovery_HelmOperatingSystem.md) objects
Required: No

 ** releaseNotes **   <a name="AWSMarketplaceService-Type-marketplace-discovery_HelmFulfillmentOption-releaseNotes"></a>
Release notes describing changes in this version of the fulfillment option.
Type: String
Required: No

 ** usageInstructions **   <a name="AWSMarketplaceService-Type-marketplace-discovery_HelmFulfillmentOption-usageInstructions"></a>
Instructions on how to deploy and use this Helm chart.
Type: String
Required: No

## See Also
<a name="API_marketplace-discovery_HelmFulfillmentOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/HelmFulfillmentOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/HelmFulfillmentOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/HelmFulfillmentOption)
