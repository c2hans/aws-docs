---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_FulfillmentOption.html
---

# FulfillmentOption
<a name="API_marketplace-discovery_FulfillmentOption"></a>

Describes a fulfillment option for a product. Each element contains exactly one fulfillment option type.

## Contents
<a name="API_marketplace-discovery_FulfillmentOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** amazonMachineImageFulfillmentOption **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FulfillmentOption-amazonMachineImageFulfillmentOption"></a>
An Amazon Machine Image (AMI) fulfillment option for EC2 deployment.
Type: [AmazonMachineImageFulfillmentOption](API_marketplace-discovery_AmazonMachineImageFulfillmentOption.md) object
Required: No

 ** apiFulfillmentOption **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FulfillmentOption-apiFulfillmentOption"></a>
An API-based fulfillment option for programmatic integration.
Type: [ApiFulfillmentOption](API_marketplace-discovery_ApiFulfillmentOption.md) object
Required: No

 ** cloudFormationFulfillmentOption **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FulfillmentOption-cloudFormationFulfillmentOption"></a>
An AWS CloudFormation template fulfillment option for infrastructure deployment.
Type: [CloudFormationFulfillmentOption](API_marketplace-discovery_CloudFormationFulfillmentOption.md) object
Required: No

 ** containerFulfillmentOption **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FulfillmentOption-containerFulfillmentOption"></a>
A container image fulfillment option for container-based deployment.
Type: [ContainerFulfillmentOption](API_marketplace-discovery_ContainerFulfillmentOption.md) object
Required: No

 ** dataExchangeFulfillmentOption **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FulfillmentOption-dataExchangeFulfillmentOption"></a>
An AWS Data Exchange fulfillment option for data set delivery.
Type: [DataExchangeFulfillmentOption](API_marketplace-discovery_DataExchangeFulfillmentOption.md) object
Required: No

 ** ec2ImageBuilderComponentFulfillmentOption **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FulfillmentOption-ec2ImageBuilderComponentFulfillmentOption"></a>
An EC2 Image Builder component fulfillment option.
Type: [Ec2ImageBuilderComponentFulfillmentOption](API_marketplace-discovery_Ec2ImageBuilderComponentFulfillmentOption.md) object
Required: No

 ** eksAddOnFulfillmentOption **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FulfillmentOption-eksAddOnFulfillmentOption"></a>
An Amazon EKS add-on fulfillment option.
Type: [EksAddOnFulfillmentOption](API_marketplace-discovery_EksAddOnFulfillmentOption.md) object
Required: No

 ** helmFulfillmentOption **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FulfillmentOption-helmFulfillmentOption"></a>
A Helm chart fulfillment option for Kubernetes deployment.
Type: [HelmFulfillmentOption](API_marketplace-discovery_HelmFulfillmentOption.md) object
Required: No

 ** professionalServicesFulfillmentOption **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FulfillmentOption-professionalServicesFulfillmentOption"></a>
A professional services fulfillment option.
Type: [ProfessionalServicesFulfillmentOption](API_marketplace-discovery_ProfessionalServicesFulfillmentOption.md) object
Required: No

 ** saasFulfillmentOption **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FulfillmentOption-saasFulfillmentOption"></a>
A Software as a Service (SaaS) fulfillment option.
Type: [SaasFulfillmentOption](API_marketplace-discovery_SaasFulfillmentOption.md) object
Required: No

 ** sageMakerAlgorithmFulfillmentOption **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FulfillmentOption-sageMakerAlgorithmFulfillmentOption"></a>
An Amazon SageMaker algorithm fulfillment option.
Type: [SageMakerAlgorithmFulfillmentOption](API_marketplace-discovery_SageMakerAlgorithmFulfillmentOption.md) object
Required: No

 ** sageMakerModelFulfillmentOption **   <a name="AWSMarketplaceService-Type-marketplace-discovery_FulfillmentOption-sageMakerModelFulfillmentOption"></a>
An Amazon SageMaker model fulfillment option.
Type: [SageMakerModelFulfillmentOption](API_marketplace-discovery_SageMakerModelFulfillmentOption.md) object
Required: No

## See Also
<a name="API_marketplace-discovery_FulfillmentOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/FulfillmentOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/FulfillmentOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/FulfillmentOption)
