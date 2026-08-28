---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SageMakerModelFulfillmentOption.html
---

# SageMakerModelFulfillmentOption
<a name="API_marketplace-discovery_SageMakerModelFulfillmentOption"></a>

Describes an Amazon SageMaker model fulfillment option, including version details and recommended instance types.

## Contents
<a name="API_marketplace-discovery_SageMakerModelFulfillmentOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** fulfillmentOptionDisplayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SageMakerModelFulfillmentOption-fulfillmentOptionDisplayName"></a>
A human-readable name for the fulfillment option type.
Type: String
Required: Yes

 ** fulfillmentOptionId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SageMakerModelFulfillmentOption-fulfillmentOptionId"></a>
The unique identifier of the fulfillment option.
Type: String
Required: Yes

 ** fulfillmentOptionType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SageMakerModelFulfillmentOption-fulfillmentOptionType"></a>
The category of the fulfillment option.
Type: String
Valid Values: `AMAZON_MACHINE_IMAGE | API | CLOUDFORMATION_TEMPLATE | CONTAINER | HELM | EKS_ADD_ON | EC2_IMAGE_BUILDER_COMPONENT | DATA_EXCHANGE | PROFESSIONAL_SERVICES | SAAS | SAGEMAKER_ALGORITHM | SAGEMAKER_MODEL`
Required: Yes

 ** fulfillmentOptionVersion **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SageMakerModelFulfillmentOption-fulfillmentOptionVersion"></a>
The version identifier of the fulfillment option.
Type: String
Required: No

 ** recommendation **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SageMakerModelFulfillmentOption-recommendation"></a>
Recommended instance types for inference with this model.
Type: [SageMakerModelRecommendation](API_marketplace-discovery_SageMakerModelRecommendation.md) object
Required: No

 ** releaseNotes **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SageMakerModelFulfillmentOption-releaseNotes"></a>
Release notes describing changes in this version of the fulfillment option.
Type: String
Required: No

 ** usageInstructions **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SageMakerModelFulfillmentOption-usageInstructions"></a>
Instructions on how to use this SageMaker model.
Type: String
Required: No

## See Also
<a name="API_marketplace-discovery_SageMakerModelFulfillmentOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/SageMakerModelFulfillmentOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/SageMakerModelFulfillmentOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SageMakerModelFulfillmentOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
