---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ContainerFulfillmentOption.html
---

# ContainerFulfillmentOption
<a name="API_marketplace-discovery_ContainerFulfillmentOption"></a>

Describes a container image fulfillment option for container-based deployment.

## Contents
<a name="API_marketplace-discovery_ContainerFulfillmentOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** fulfillmentOptionDisplayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ContainerFulfillmentOption-fulfillmentOptionDisplayName"></a>
A human-readable name for the fulfillment option type.
Type: String
Required: Yes

 ** fulfillmentOptionId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ContainerFulfillmentOption-fulfillmentOptionId"></a>
The unique identifier of the fulfillment option.
Type: String
Required: Yes

 ** fulfillmentOptionName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ContainerFulfillmentOption-fulfillmentOptionName"></a>
The display name of the fulfillment option version.
Type: String
Required: Yes

 ** fulfillmentOptionType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ContainerFulfillmentOption-fulfillmentOptionType"></a>
The category of the fulfillment option.
Type: String
Valid Values: `AMAZON_MACHINE_IMAGE | API | CLOUDFORMATION_TEMPLATE | CONTAINER | HELM | EKS_ADD_ON | EC2_IMAGE_BUILDER_COMPONENT | DATA_EXCHANGE | PROFESSIONAL_SERVICES | SAAS | SAGEMAKER_ALGORITHM | SAGEMAKER_MODEL`
Required: Yes

 ** awsSupportedServices **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ContainerFulfillmentOption-awsSupportedServices"></a>
The AWS services supported by this container deployment.
Type: Array of [AwsSupportedService](API_marketplace-discovery_AwsSupportedService.md) objects
Required: No

 ** fulfillmentOptionVersion **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ContainerFulfillmentOption-fulfillmentOptionVersion"></a>
The version identifier of the fulfillment option.
Type: String
Required: No

 ** operatingSystems **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ContainerFulfillmentOption-operatingSystems"></a>
The operating systems supported by this container image.
Type: Array of [ContainerOperatingSystem](API_marketplace-discovery_ContainerOperatingSystem.md) objects
Required: No

 ** releaseNotes **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ContainerFulfillmentOption-releaseNotes"></a>
Release notes describing changes in this version of the fulfillment option.
Type: String
Required: No

 ** usageInstructions **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ContainerFulfillmentOption-usageInstructions"></a>
Instructions on how to deploy and use this container image.
Type: String
Required: No

## See Also
<a name="API_marketplace-discovery_ContainerFulfillmentOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ContainerFulfillmentOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ContainerFulfillmentOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ContainerFulfillmentOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
