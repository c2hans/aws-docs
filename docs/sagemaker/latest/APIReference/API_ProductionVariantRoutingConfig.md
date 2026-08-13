---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantRoutingConfig.html
---

# ProductionVariantRoutingConfig
<a name="API_ProductionVariantRoutingConfig"></a>

Settings that control how the endpoint routes incoming traffic to the instances that the endpoint hosts.

## Contents
<a name="API_ProductionVariantRoutingConfig_Contents"></a>

 ** RoutingStrategy **   <a name="sagemaker-Type-ProductionVariantRoutingConfig-RoutingStrategy"></a>
Sets how the endpoint routes incoming traffic:
+  `LEAST_OUTSTANDING_REQUESTS`: The endpoint routes requests to the specific instances that have more capacity to process them.
+  `RANDOM`: The endpoint routes each request to a randomly chosen instance.
+  `PREFIX_AWARE`: The endpoint routes requests that share the same prompt prefix to the same instance. When the number of in-flight requests on the selected instance reaches the configured threshold, the endpoint routes the request to an instance with more available capacity.
Type: String
Valid Values: `LEAST_OUTSTANDING_REQUESTS | RANDOM | PREFIX_AWARE`
Required: Yes

 ** PrefixAwareRoutingConfig **   <a name="sagemaker-Type-ProductionVariantRoutingConfig-PrefixAwareRoutingConfig"></a>
The configuration for prefix-aware routing. Specify this parameter only when you set `RoutingStrategy` to `PREFIX_AWARE`.
Type: [PrefixAwareRoutingConfig](API_PrefixAwareRoutingConfig.md) object
Required: No

## See Also
<a name="API_ProductionVariantRoutingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProductionVariantRoutingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProductionVariantRoutingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProductionVariantRoutingConfig)
