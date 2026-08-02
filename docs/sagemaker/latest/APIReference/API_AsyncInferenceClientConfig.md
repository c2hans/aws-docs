---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AsyncInferenceClientConfig.html
---

# AsyncInferenceClientConfig
<a name="API_AsyncInferenceClientConfig"></a>

Configures the behavior of the client used by SageMaker to interact with the model container during asynchronous inference.

## Contents
<a name="API_AsyncInferenceClientConfig_Contents"></a>

 ** MaxConcurrentInvocationsPerInstance **   <a name="sagemaker-Type-AsyncInferenceClientConfig-MaxConcurrentInvocationsPerInstance"></a>
The maximum number of concurrent requests sent by the SageMaker client to the model container. If no value is provided, SageMaker chooses an optimal value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

## See Also
<a name="API_AsyncInferenceClientConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AsyncInferenceClientConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AsyncInferenceClientConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AsyncInferenceClientConfig)
