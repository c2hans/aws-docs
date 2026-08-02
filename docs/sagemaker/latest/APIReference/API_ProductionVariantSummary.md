---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantSummary.html
---

# ProductionVariantSummary
<a name="API_ProductionVariantSummary"></a>

Describes weight and capacities for a production variant associated with an endpoint. If you sent a request to the `UpdateEndpointWeightsAndCapacities` API and the endpoint status is `Updating`, you get different desired and current values.

## Contents
<a name="API_ProductionVariantSummary_Contents"></a>

 ** VariantName **   <a name="sagemaker-Type-ProductionVariantSummary-VariantName"></a>
The name of the variant.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** CapacityReservationConfig **   <a name="sagemaker-Type-ProductionVariantSummary-CapacityReservationConfig"></a>
Settings for the capacity reservation for the compute instances that SageMaker AI reserves for an endpoint.
Type: [ProductionVariantCapacityReservationSummary](API_ProductionVariantCapacityReservationSummary.md) object
Required: No

 ** CurrentInstanceCount **   <a name="sagemaker-Type-ProductionVariantSummary-CurrentInstanceCount"></a>
The number of instances associated with the variant.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** CurrentServerlessConfig **   <a name="sagemaker-Type-ProductionVariantSummary-CurrentServerlessConfig"></a>
The serverless configuration for the endpoint.
Type: [ProductionVariantServerlessConfig](API_ProductionVariantServerlessConfig.md) object
Required: No

 ** CurrentWeight **   <a name="sagemaker-Type-ProductionVariantSummary-CurrentWeight"></a>
The weight associated with the variant.
Type: Float
Valid Range: Minimum value of 0.
Required: No

 ** DeployedImages **   <a name="sagemaker-Type-ProductionVariantSummary-DeployedImages"></a>
An array of `DeployedImage` objects that specify the Amazon EC2 Container Registry paths of the inference images deployed on instances of this `ProductionVariant`.
Type: Array of [DeployedImage](API_DeployedImage.md) objects
Required: No

 ** DesiredInstanceCount **   <a name="sagemaker-Type-ProductionVariantSummary-DesiredInstanceCount"></a>
The number of instances requested in the `UpdateEndpointWeightsAndCapacities` request.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** DesiredServerlessConfig **   <a name="sagemaker-Type-ProductionVariantSummary-DesiredServerlessConfig"></a>
The serverless configuration requested for the endpoint update.
Type: [ProductionVariantServerlessConfig](API_ProductionVariantServerlessConfig.md) object
Required: No

 ** DesiredWeight **   <a name="sagemaker-Type-ProductionVariantSummary-DesiredWeight"></a>
The requested weight, as specified in the `UpdateEndpointWeightsAndCapacities` request.
Type: Float
Valid Range: Minimum value of 0.
Required: No

 ** InstancePools **   <a name="sagemaker-Type-ProductionVariantSummary-InstancePools"></a>
A list of instance pools for the production variant. Each pool indicates the instance type and the current number of instances of that type.
Type: Array of [InstancePoolSummary](API_InstancePoolSummary.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** ManagedInstanceScaling **   <a name="sagemaker-Type-ProductionVariantSummary-ManagedInstanceScaling"></a>
Settings that control the range in the number of instances that the endpoint provisions as it scales up or down to accommodate traffic.
Type: [ProductionVariantManagedInstanceScaling](API_ProductionVariantManagedInstanceScaling.md) object
Required: No

 ** RoutingConfig **   <a name="sagemaker-Type-ProductionVariantSummary-RoutingConfig"></a>
Settings that control how the endpoint routes incoming traffic to the instances that the endpoint hosts.
Type: [ProductionVariantRoutingConfig](API_ProductionVariantRoutingConfig.md) object
Required: No

 ** VariantStatus **   <a name="sagemaker-Type-ProductionVariantSummary-VariantStatus"></a>
The endpoint variant status which describes the current deployment stage status or operational status.
Type: Array of [ProductionVariantStatus](API_ProductionVariantStatus.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## See Also
<a name="API_ProductionVariantSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProductionVariantSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProductionVariantSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProductionVariantSummary)
