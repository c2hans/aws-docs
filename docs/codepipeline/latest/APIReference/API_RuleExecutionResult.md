---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_RuleExecutionResult.html
---

# RuleExecutionResult
<a name="API_RuleExecutionResult"></a>

Execution result information, such as the external execution ID.

## Contents
<a name="API_RuleExecutionResult_Contents"></a>

 ** errorDetails **   <a name="CodePipeline-Type-RuleExecutionResult-errorDetails"></a>
Represents information about an error in CodePipeline.
Type: [ErrorDetails](API_ErrorDetails.md) object
Required: No

 ** externalExecutionId **   <a name="CodePipeline-Type-RuleExecutionResult-externalExecutionId"></a>
The external ID for the rule execution.
Type: String
Required: No

 ** externalExecutionSummary **   <a name="CodePipeline-Type-RuleExecutionResult-externalExecutionSummary"></a>
The external provider summary for the rule execution.
Type: String
Required: No

 ** externalExecutionUrl **   <a name="CodePipeline-Type-RuleExecutionResult-externalExecutionUrl"></a>
The deepest external link to the external resource (for example, a repository URL or deployment endpoint) that is used when running the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_RuleExecutionResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RuleExecutionResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RuleExecutionResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RuleExecutionResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
