---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsApiGatewayCanarySettings.html
---

# AwsApiGatewayCanarySettings
<a name="API_AwsApiGatewayCanarySettings"></a>

Contains information about settings for canary deployment in the stage.

## Contents
<a name="API_AwsApiGatewayCanarySettings_Contents"></a>

 ** DeploymentId **   <a name="securityhub-Type-AwsApiGatewayCanarySettings-DeploymentId"></a>
The deployment identifier for the canary deployment.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PercentTraffic **   <a name="securityhub-Type-AwsApiGatewayCanarySettings-PercentTraffic"></a>
The percentage of traffic that is diverted to a canary deployment.
Type: Double
Required: No

 ** StageVariableOverrides **   <a name="securityhub-Type-AwsApiGatewayCanarySettings-StageVariableOverrides"></a>
Stage variables that are overridden in the canary release deployment. The variables include new stage variables that are introduced in the canary.
Each variable is represented as a string-to-string map between the stage variable name and the variable value.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

 ** UseStageCache **   <a name="securityhub-Type-AwsApiGatewayCanarySettings-UseStageCache"></a>
Indicates whether the canary deployment uses the stage cache.
Type: Boolean
Required: No

## See Also
<a name="API_AwsApiGatewayCanarySettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsApiGatewayCanarySettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsApiGatewayCanarySettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsApiGatewayCanarySettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
