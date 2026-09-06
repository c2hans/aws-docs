---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VariantProperty.html
---

# VariantProperty
<a name="API_VariantProperty"></a>

Specifies a production variant property type for an Endpoint.

If you are updating an endpoint with the `RetainAllVariantProperties` option of [UpdateEndpointInput](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) set to `true`, the `VariantProperty` objects listed in the `ExcludeRetainedVariantProperties` parameter of [UpdateEndpointInput](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) override the existing variant properties of the endpoint.

## Contents
<a name="API_VariantProperty_Contents"></a>

 ** VariantPropertyType **   <a name="sagemaker-Type-VariantProperty-VariantPropertyType"></a>
The type of variant property. The supported values are:
+  `DesiredInstanceCount`: Overrides the existing variant instance counts using the `InitialInstanceCount` values in the `ProductionVariants` of [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html).
+  `DesiredWeight`: Overrides the existing variant weights using the `InitialVariantWeight` values in the `ProductionVariants` of [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html).
+  `DataCaptureConfig`: (Not currently supported.)
Type: String
Valid Values: `DesiredInstanceCount | DesiredWeight | DataCaptureConfig`
Required: Yes

## See Also
<a name="API_VariantProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/VariantProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/VariantProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/VariantProperty)
