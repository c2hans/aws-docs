---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeploymentStage.html
---

# DeploymentStage
<a name="API_DeploymentStage"></a>

Contains information about a stage in an edge deployment plan.

## Contents
<a name="API_DeploymentStage_Contents"></a>

 ** DeviceSelectionConfig **   <a name="sagemaker-Type-DeploymentStage-DeviceSelectionConfig"></a>
Configuration of the devices in the stage.
Type: [DeviceSelectionConfig](API_DeviceSelectionConfig.md) object
Required: Yes

 ** StageName **   <a name="sagemaker-Type-DeploymentStage-StageName"></a>
The name of the stage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** DeploymentConfig **   <a name="sagemaker-Type-DeploymentStage-DeploymentConfig"></a>
Configuration of the deployment details.
Type: [EdgeDeploymentConfig](API_EdgeDeploymentConfig.md) object
Required: No

## See Also
<a name="API_DeploymentStage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeploymentStage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeploymentStage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeploymentStage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
