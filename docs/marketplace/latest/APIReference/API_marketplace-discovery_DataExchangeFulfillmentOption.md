---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_DataExchangeFulfillmentOption.html
---

# DataExchangeFulfillmentOption
<a name="API_marketplace-discovery_DataExchangeFulfillmentOption"></a>

Describes an AWS Data Exchange fulfillment option for data set delivery.

## Contents
<a name="API_marketplace-discovery_DataExchangeFulfillmentOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** fulfillmentOptionDisplayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_DataExchangeFulfillmentOption-fulfillmentOptionDisplayName"></a>
A human-readable name for the fulfillment option type.
Type: String
Required: Yes

 ** fulfillmentOptionId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_DataExchangeFulfillmentOption-fulfillmentOptionId"></a>
The unique identifier of the fulfillment option.
Type: String
Required: Yes

 ** fulfillmentOptionType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_DataExchangeFulfillmentOption-fulfillmentOptionType"></a>
The category of the fulfillment option.
Type: String
Valid Values: `AMAZON_MACHINE_IMAGE | API | CLOUDFORMATION_TEMPLATE | CONTAINER | HELM | EKS_ADD_ON | EC2_IMAGE_BUILDER_COMPONENT | DATA_EXCHANGE | PROFESSIONAL_SERVICES | SAAS | SAGEMAKER_ALGORITHM | SAGEMAKER_MODEL`
Required: Yes

 ** dataArtifacts **   <a name="AWSMarketplaceService-Type-marketplace-discovery_DataExchangeFulfillmentOption-dataArtifacts"></a>
The data artifacts included in this Data Exchange fulfillment option.
Type: Array of [DataArtifact](API_marketplace-discovery_DataArtifact.md) objects
Required: No

## See Also
<a name="API_marketplace-discovery_DataExchangeFulfillmentOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/DataExchangeFulfillmentOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/DataExchangeFulfillmentOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/DataExchangeFulfillmentOption)
