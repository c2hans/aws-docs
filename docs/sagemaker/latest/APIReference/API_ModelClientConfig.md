---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelClientConfig.html
---

# ModelClientConfig
<a name="API_ModelClientConfig"></a>

Configures the timeout and maximum number of retries for processing a transform job invocation.

## Contents
<a name="API_ModelClientConfig_Contents"></a>

 ** InvocationsMaxRetries **   <a name="sagemaker-Type-ModelClientConfig-InvocationsMaxRetries"></a>
The maximum number of retries when invocation requests are failing. The default value is 3.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3.
Required: No

 ** InvocationsTimeoutInSeconds **   <a name="sagemaker-Type-ModelClientConfig-InvocationsTimeoutInSeconds"></a>
The timeout value in seconds for an invocation request. The default value is 600.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3600.
Required: No

## See Also
<a name="API_ModelClientConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelClientConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelClientConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelClientConfig)
