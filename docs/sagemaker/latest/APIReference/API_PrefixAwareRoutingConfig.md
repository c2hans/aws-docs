---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PrefixAwareRoutingConfig.html
---

# PrefixAwareRoutingConfig
<a name="API_PrefixAwareRoutingConfig"></a>

The configuration for prefix-aware routing on a SageMaker real-time inference endpoint. Specify `PrefixLength` and `ConcurrencyThreshold` to control routing behavior.

## Contents
<a name="API_PrefixAwareRoutingConfig_Contents"></a>

 ** ConcurrencyThreshold **   <a name="sagemaker-Type-PrefixAwareRoutingConfig-ConcurrencyThreshold"></a>
The number of in-flight requests on the selected instance or inference component copy at which the endpoint routes a request to another copy or instance. Required when `RoutingStrategy` is `PREFIX_AWARE`.
On an endpoint without inference components, the endpoint compares this threshold with the number of in-flight requests on the selected instance. When that number reaches the threshold, the endpoint routes the request to another instance.
On an endpoint with inference components, the endpoint compares this threshold with the number of in-flight requests on the selected copy of the invoked inference component. Requests to other inference components on the same instance don't count. When the instance hosts more than one copy of the inference component, the endpoint routes requests that share a prefix to the same copy and, while that copy has reached the threshold, to another copy on the instance that is under the threshold. When every copy on the instance has reached the threshold, the endpoint routes the request to another instance.
The threshold applies to every instance and every copy of every inference component in the production variant, so choose a value that suits the instance or copy that can serve the fewest concurrent requests.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

 ** PrefixLength **   <a name="sagemaker-Type-PrefixAwareRoutingConfig-PrefixLength"></a>
The maximum length of the prefix used for routing decisions. Required when `RoutingStrategy` is `PREFIX_AWARE`.
+ For the SageMaker Runtime `InvokeEndpoint` and `InvokeEndpointWithResponseStream` APIs, this value specifies the number of bytes from the beginning of the request body.
+ For OpenAI-compatible API, this value specifies the number of characters from the text content of the messages array.
The endpoint routes requests that share the same prefix to the same instance and, when that instance hosts more than one copy of the invoked inference component, to the same copy. Set this value to cover shared content (such as system prompts) plus enough unique content to distribute workloads across instances and copies.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65536.
Required: No

## See Also
<a name="API_PrefixAwareRoutingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PrefixAwareRoutingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PrefixAwareRoutingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PrefixAwareRoutingConfig)
