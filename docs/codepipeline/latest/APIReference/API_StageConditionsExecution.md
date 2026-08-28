---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StageConditionsExecution.html
---

# StageConditionsExecution
<a name="API_StageConditionsExecution"></a>

Represents information about the run of a condition for a stage.

## Contents
<a name="API_StageConditionsExecution_Contents"></a>

 ** status **   <a name="CodePipeline-Type-StageConditionsExecution-status"></a>
The status of a run of a condition for a stage.
Type: String
Valid Values: `InProgress | Failed | Errored | Succeeded | Cancelled | Abandoned | Overridden`
Required: No

 ** summary **   <a name="CodePipeline-Type-StageConditionsExecution-summary"></a>
A summary of the run of the condition for a stage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_StageConditionsExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/StageConditionsExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/StageConditionsExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/StageConditionsExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
