---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_CanarySettings.html
---

# CanarySettings
<a name="API_CanarySettings"></a>

Configuration settings of a canary deployment.

## Contents
<a name="API_CanarySettings_Contents"></a>

 ** deploymentId **   <a name="apigw-Type-CanarySettings-deploymentId"></a>
The ID of the canary deployment.
Type: String
Required: No

 ** percentTraffic **   <a name="apigw-Type-CanarySettings-percentTraffic"></a>
The percent (0-100) of traffic diverted to a canary deployment.
Type: Double
Required: No

 ** stageVariableOverrides **   <a name="apigw-Type-CanarySettings-stageVariableOverrides"></a>
Stage variables overridden for a canary release deployment, including new stage variables introduced in the canary. These stage variables are represented as a string-to-string map between stage variable names and their values.
Type: String to string map
Required: No

 ** useStageCache **   <a name="apigw-Type-CanarySettings-useStageCache"></a>
A Boolean flag to indicate whether the canary deployment uses the stage cache or not.
Type: Boolean
Required: No

## See Also
<a name="API_CanarySettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/CanarySettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/CanarySettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/CanarySettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
