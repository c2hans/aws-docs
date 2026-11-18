---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RoutingTargetAsyncInferenceClientConfig.html
---

# RoutingTargetAsyncInferenceClientConfig
<a name="API_RoutingTargetAsyncInferenceClientConfig"></a>

How the inference router submits asynchronous requests to the destinations of a routing target.

## Contents
<a name="API_RoutingTargetAsyncInferenceClientConfig_Contents"></a>

 ** MaxTimeInBacklogSeconds **   <a name="sagemaker-Type-RoutingTargetAsyncInferenceClientConfig-MaxTimeInBacklogSeconds"></a>
The maximum time, in seconds, that a request can wait at a destination before the inference router moves it to another destination. The default is 900 seconds.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 21600.
Required: No

## See Also
<a name="API_RoutingTargetAsyncInferenceClientConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RoutingTargetAsyncInferenceClientConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RoutingTargetAsyncInferenceClientConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RoutingTargetAsyncInferenceClientConfig)
