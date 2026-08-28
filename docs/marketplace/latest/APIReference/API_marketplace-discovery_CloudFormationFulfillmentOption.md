---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_CloudFormationFulfillmentOption.html
---

# CloudFormationFulfillmentOption
<a name="API_marketplace-discovery_CloudFormationFulfillmentOption"></a>

Describes an AWS CloudFormation template fulfillment option for infrastructure deployment.

## Contents
<a name="API_marketplace-discovery_CloudFormationFulfillmentOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** fulfillmentOptionDisplayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CloudFormationFulfillmentOption-fulfillmentOptionDisplayName"></a>
A human-readable name for the fulfillment option type.
Type: String
Required: Yes

 ** fulfillmentOptionId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CloudFormationFulfillmentOption-fulfillmentOptionId"></a>
The unique identifier of the fulfillment option.
Type: String
Required: Yes

 ** fulfillmentOptionName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CloudFormationFulfillmentOption-fulfillmentOptionName"></a>
The display name of the fulfillment option version.
Type: String
Required: Yes

 ** fulfillmentOptionType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CloudFormationFulfillmentOption-fulfillmentOptionType"></a>
The category of the fulfillment option.
Type: String
Valid Values: `AMAZON_MACHINE_IMAGE | API | CLOUDFORMATION_TEMPLATE | CONTAINER | HELM | EKS_ADD_ON | EC2_IMAGE_BUILDER_COMPONENT | DATA_EXCHANGE | PROFESSIONAL_SERVICES | SAAS | SAGEMAKER_ALGORITHM | SAGEMAKER_MODEL`
Required: Yes

 ** fulfillmentOptionVersion **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CloudFormationFulfillmentOption-fulfillmentOptionVersion"></a>
The version identifier of the fulfillment option.
Type: String
Required: No

 ** releaseNotes **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CloudFormationFulfillmentOption-releaseNotes"></a>
Release notes describing changes in this version of the fulfillment option.
Type: String
Required: No

 ** usageInstructions **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CloudFormationFulfillmentOption-usageInstructions"></a>
Instructions on how to deploy and use this CloudFormation template.
Type: String
Required: No

## See Also
<a name="API_marketplace-discovery_CloudFormationFulfillmentOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/CloudFormationFulfillmentOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/CloudFormationFulfillmentOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/CloudFormationFulfillmentOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
