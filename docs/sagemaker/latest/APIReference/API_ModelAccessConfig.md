---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelAccessConfig.html
---

# ModelAccessConfig
<a name="API_ModelAccessConfig"></a>

The access configuration file to control access to the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig`.
+ If you are a Jumpstart user, see the [End-user license agreements](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula) section for more details on accepting the EULA.
+ If you are an AutoML user, see the *Optional Parameters* section of *Create an AutoML job to fine-tune text generation models using the API* for details on [How to set the EULA acceptance when fine-tuning a model using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-finetune-llms.html#autopilot-llms-finetuning-api-optional-params).

## Contents
<a name="API_ModelAccessConfig_Contents"></a>

 ** AcceptEula **   <a name="sagemaker-Type-ModelAccessConfig-AcceptEula"></a>
Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.
Type: Boolean
Required: Yes

## See Also
<a name="API_ModelAccessConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelAccessConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelAccessConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelAccessConfig)
