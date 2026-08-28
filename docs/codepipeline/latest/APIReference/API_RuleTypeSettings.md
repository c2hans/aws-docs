---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_RuleTypeSettings.html
---

# RuleTypeSettings
<a name="API_RuleTypeSettings"></a>

Returns information about the settings for a rule type.

## Contents
<a name="API_RuleTypeSettings_Contents"></a>

 ** entityUrlTemplate **   <a name="CodePipeline-Type-RuleTypeSettings-entityUrlTemplate"></a>
The URL returned to the CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for a CodeDeploy deployment group. This link is provided as part of the action display in the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** executionUrlTemplate **   <a name="CodePipeline-Type-RuleTypeSettings-executionUrlTemplate"></a>
The URL returned to the CodePipeline console that contains a link to the top-level landing page for the external system, such as the console page for CodeDeploy. This link is shown on the pipeline view page in the CodePipeline console and provides a link to the execution entity of the external action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** revisionUrlTemplate **   <a name="CodePipeline-Type-RuleTypeSettings-revisionUrlTemplate"></a>
The URL returned to the CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** thirdPartyConfigurationUrl **   <a name="CodePipeline-Type-RuleTypeSettings-thirdPartyConfigurationUrl"></a>
The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_RuleTypeSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RuleTypeSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RuleTypeSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RuleTypeSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
