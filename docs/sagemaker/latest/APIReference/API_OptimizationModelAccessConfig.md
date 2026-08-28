---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OptimizationModelAccessConfig.html
---

# OptimizationModelAccessConfig
<a name="API_OptimizationModelAccessConfig"></a>

The access configuration settings for the source ML model for an optimization job, where you can accept the model end-user license agreement (EULA).

## Contents
<a name="API_OptimizationModelAccessConfig_Contents"></a>

 ** AcceptEula **   <a name="sagemaker-Type-OptimizationModelAccessConfig-AcceptEula"></a>
Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.
Type: Boolean
Required: Yes

## See Also
<a name="API_OptimizationModelAccessConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OptimizationModelAccessConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OptimizationModelAccessConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OptimizationModelAccessConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
