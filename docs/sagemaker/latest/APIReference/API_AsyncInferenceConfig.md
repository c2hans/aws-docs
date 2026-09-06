---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AsyncInferenceConfig.html
---

# AsyncInferenceConfig
<a name="API_AsyncInferenceConfig"></a>

Specifies configuration for how an endpoint performs asynchronous inference.

## Contents
<a name="API_AsyncInferenceConfig_Contents"></a>

 ** OutputConfig **   <a name="sagemaker-Type-AsyncInferenceConfig-OutputConfig"></a>
Specifies the configuration for asynchronous inference invocation outputs.
Type: [AsyncInferenceOutputConfig](API_AsyncInferenceOutputConfig.md) object
Required: Yes

 ** ClientConfig **   <a name="sagemaker-Type-AsyncInferenceConfig-ClientConfig"></a>
Configures the behavior of the client used by SageMaker to interact with the model container during asynchronous inference.
Type: [AsyncInferenceClientConfig](API_AsyncInferenceClientConfig.md) object
Required: No

## See Also
<a name="API_AsyncInferenceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AsyncInferenceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AsyncInferenceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AsyncInferenceConfig)
