---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_DeploymentCanarySettings.html
---

# DeploymentCanarySettings
<a name="API_DeploymentCanarySettings"></a>

The input configuration for a canary deployment.

## Contents
<a name="API_DeploymentCanarySettings_Contents"></a>

 ** percentTraffic **   <a name="apigw-Type-DeploymentCanarySettings-percentTraffic"></a>
The percentage (0.0-100.0) of traffic routed to the canary deployment.
Type: Double
Required: No

 ** stageVariableOverrides **   <a name="apigw-Type-DeploymentCanarySettings-stageVariableOverrides"></a>
A stage variable overrides used for the canary release deployment. They can override existing stage variables or add new stage variables for the canary release deployment. These stage variables are represented as a string-to-string map between stage variable names and their values.
Type: String to string map
Required: No

 ** useStageCache **   <a name="apigw-Type-DeploymentCanarySettings-useStageCache"></a>
A Boolean flag to indicate whether the canary release deployment uses the stage cache or not.
Type: Boolean
Required: No

## See Also
<a name="API_DeploymentCanarySettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/DeploymentCanarySettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/DeploymentCanarySettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/DeploymentCanarySettings)
