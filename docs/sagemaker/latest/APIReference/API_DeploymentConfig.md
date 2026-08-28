---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeploymentConfig.html
---

# DeploymentConfig
<a name="API_DeploymentConfig"></a>

The deployment configuration for an endpoint, which contains the desired deployment strategy and rollback configurations.

## Contents
<a name="API_DeploymentConfig_Contents"></a>

 ** AutoRollbackConfiguration **   <a name="sagemaker-Type-DeploymentConfig-AutoRollbackConfiguration"></a>
Automatic rollback configuration for handling endpoint deployment failures and recovery.
Type: [AutoRollbackConfig](API_AutoRollbackConfig.md) object
Required: No

 ** BlueGreenUpdatePolicy **   <a name="sagemaker-Type-DeploymentConfig-BlueGreenUpdatePolicy"></a>
Update policy for a blue/green deployment. If this update policy is specified, SageMaker creates a new fleet during the deployment while maintaining the old fleet. SageMaker flips traffic to the new fleet according to the specified traffic routing configuration. Only one update policy should be used in the deployment configuration. If no update policy is specified, SageMaker uses a blue/green deployment strategy with all at once traffic shifting by default.
Type: [BlueGreenUpdatePolicy](API_BlueGreenUpdatePolicy.md) object
Required: No

 ** RollingUpdatePolicy **   <a name="sagemaker-Type-DeploymentConfig-RollingUpdatePolicy"></a>
Specifies a rolling deployment strategy for updating a SageMaker endpoint.
Type: [RollingUpdatePolicy](API_RollingUpdatePolicy.md) object
Required: No

## See Also
<a name="API_DeploymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeploymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeploymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeploymentConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
