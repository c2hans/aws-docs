---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EdgeDeploymentModelConfig.html
---

# EdgeDeploymentModelConfig
<a name="API_EdgeDeploymentModelConfig"></a>

Contains information about the configuration of a model in a deployment.

## Contents
<a name="API_EdgeDeploymentModelConfig_Contents"></a>

 ** EdgePackagingJobName **   <a name="sagemaker-Type-EdgeDeploymentModelConfig-EdgePackagingJobName"></a>
The edge packaging job associated with this deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ModelHandle **   <a name="sagemaker-Type-EdgeDeploymentModelConfig-ModelHandle"></a>
The name the device application uses to reference this model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## See Also
<a name="API_EdgeDeploymentModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EdgeDeploymentModelConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EdgeDeploymentModelConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EdgeDeploymentModelConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
