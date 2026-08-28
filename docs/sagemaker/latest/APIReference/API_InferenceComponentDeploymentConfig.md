---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentDeploymentConfig.html
---

# InferenceComponentDeploymentConfig
<a name="API_InferenceComponentDeploymentConfig"></a>

The deployment configuration for an endpoint that hosts inference components. The configuration includes the desired deployment strategy and rollback settings.

## Contents
<a name="API_InferenceComponentDeploymentConfig_Contents"></a>

 ** RollingUpdatePolicy **   <a name="sagemaker-Type-InferenceComponentDeploymentConfig-RollingUpdatePolicy"></a>
Specifies a rolling deployment strategy for updating a SageMaker AI endpoint.
Type: [InferenceComponentRollingUpdatePolicy](API_InferenceComponentRollingUpdatePolicy.md) object
Required: Yes

 ** AutoRollbackConfiguration **   <a name="sagemaker-Type-InferenceComponentDeploymentConfig-AutoRollbackConfiguration"></a>
Automatic rollback configuration for handling endpoint deployment failures and recovery.
Type: [AutoRollbackConfig](API_AutoRollbackConfig.md) object
Required: No

## See Also
<a name="API_InferenceComponentDeploymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentDeploymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentDeploymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentDeploymentConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
