---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_RuleExecutionInput.html
---

# RuleExecutionInput
<a name="API_RuleExecutionInput"></a>

Input information used for a rule execution.

## Contents
<a name="API_RuleExecutionInput_Contents"></a>

 ** configuration **   <a name="CodePipeline-Type-RuleExecutionInput-configuration"></a>
Configuration data for a rule execution, such as the resolved values for that run.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Value Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

 ** inputArtifacts **   <a name="CodePipeline-Type-RuleExecutionInput-inputArtifacts"></a>
Details of input artifacts of the rule that correspond to the rule execution.
Type: Array of [ArtifactDetail](API_ArtifactDetail.md) objects
Required: No

 ** region **   <a name="CodePipeline-Type-RuleExecutionInput-region"></a>
The AWS Region for the rule, such as us-east-1.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 30.
Required: No

 ** resolvedConfiguration **   <a name="CodePipeline-Type-RuleExecutionInput-resolvedConfiguration"></a>
Configuration data for a rule execution with all variable references replaced with their real values for the execution.
Type: String to string map
Required: No

 ** roleArn **   <a name="CodePipeline-Type-RuleExecutionInput-roleArn"></a>
The ARN of the IAM service role that performs the declared rule. This is assumed through the roleArn for the pipeline.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `arn:aws(-[\w]+)*:iam::[0-9]{12}:role/.*`
Required: No

 ** ruleTypeId **   <a name="CodePipeline-Type-RuleExecutionInput-ruleTypeId"></a>
The ID for the rule type, which is made up of the combined values for category, owner, provider, and version. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html). For more information about rules, see the [AWS CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html).
Type: [RuleTypeId](API_RuleTypeId.md) object
Required: No

## See Also
<a name="API_RuleExecutionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RuleExecutionInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RuleExecutionInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RuleExecutionInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
