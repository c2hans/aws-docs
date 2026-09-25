---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_AmazonMachineImageFulfillmentOption.html
---

# AmazonMachineImageFulfillmentOption
<a name="API_marketplace-discovery_AmazonMachineImageFulfillmentOption"></a>

Describes an Amazon Machine Image (AMI) fulfillment option, including version details, supported operating systems, and recommended instance types.

## Contents
<a name="API_marketplace-discovery_AmazonMachineImageFulfillmentOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** architecture **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-architecture"></a>
The architecture of the AMI, such as `x86_64`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** fulfillmentOptionDisplayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-fulfillmentOptionDisplayName"></a>
A human-readable name for the fulfillment option type.
Type: String
Required: Yes

 ** fulfillmentOptionId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-fulfillmentOptionId"></a>
The unique identifier of the fulfillment option.
Type: String
Required: Yes

 ** fulfillmentOptionName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-fulfillmentOptionName"></a>
The display name of the fulfillment option version.
Type: String
Required: Yes

 ** fulfillmentOptionType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-fulfillmentOptionType"></a>
The category of the fulfillment option.
Type: String
Valid Values: `AMAZON_MACHINE_IMAGE | API | CLOUDFORMATION_TEMPLATE | CONTAINER | HELM | EKS_ADD_ON | EC2_IMAGE_BUILDER_COMPONENT | DATA_EXCHANGE | PROFESSIONAL_SERVICES | SAAS | SAGEMAKER_ALGORITHM | SAGEMAKER_MODEL`
Required: Yes

 ** operatingSystems **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-operatingSystems"></a>
The operating systems supported by this AMI.
Type: Array of [AmazonMachineImageOperatingSystem](API_marketplace-discovery_AmazonMachineImageOperatingSystem.md) objects
Required: Yes

 ** accessUrlTemplate **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-accessUrlTemplate"></a>
The URL pattern for accessing the product when an instance is running.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** amiAlias **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-amiAlias"></a>
The alias of the AMI associated with this fulfillment option.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** availableFromTime **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-availableFromTime"></a>
The date and time when the AMI became available for fulfillment.
Type: Timestamp
Required: No

 ** ebsVolume **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-ebsVolume"></a>
The supported Amazon EBS volume configuration for the AMI.
Type: [AmazonMachineImageEbsVolume](API_marketplace-discovery_AmazonMachineImageEbsVolume.md) object
Required: No

 ** fulfillmentOptionVersion **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-fulfillmentOptionVersion"></a>
The version identifier of the fulfillment option.
Type: String
Required: No

 ** recommendation **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-recommendation"></a>
Recommended instance types for running this AMI.
Type: [AmazonMachineImageRecommendation](API_marketplace-discovery_AmazonMachineImageRecommendation.md) object
Required: No

 ** releaseNotes **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-releaseNotes"></a>
Release notes describing changes in this version of the fulfillment option.
Type: String
Required: No

 ** shortDescription **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-shortDescription"></a>
A short description of the fulfillment option.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** usageInstructions **   <a name="AWSMarketplaceService-Type-marketplace-discovery_AmazonMachineImageFulfillmentOption-usageInstructions"></a>
Instructions on how to deploy and use this fulfillment option.
Type: String
Required: No

## See Also
<a name="API_marketplace-discovery_AmazonMachineImageFulfillmentOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/AmazonMachineImageFulfillmentOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/AmazonMachineImageFulfillmentOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/AmazonMachineImageFulfillmentOption)
