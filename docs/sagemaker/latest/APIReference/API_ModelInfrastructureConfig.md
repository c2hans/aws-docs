---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelInfrastructureConfig.html
---

# ModelInfrastructureConfig
<a name="API_ModelInfrastructureConfig"></a>

The configuration for the infrastructure that the model will be deployed to.

## Contents
<a name="API_ModelInfrastructureConfig_Contents"></a>

 ** InfrastructureType **   <a name="sagemaker-Type-ModelInfrastructureConfig-InfrastructureType"></a>
The inference option to which to deploy your model. Possible values are the following:
+  `RealTime`: Deploy to real-time inference.
Type: String
Valid Values: `RealTimeInference`
Required: Yes

 ** RealTimeInferenceConfig **   <a name="sagemaker-Type-ModelInfrastructureConfig-RealTimeInferenceConfig"></a>
The infrastructure configuration for deploying the model to real-time inference.
Type: [RealTimeInferenceConfig](API_RealTimeInferenceConfig.md) object
Required: Yes

## See Also
<a name="API_ModelInfrastructureConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelInfrastructureConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelInfrastructureConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelInfrastructureConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
