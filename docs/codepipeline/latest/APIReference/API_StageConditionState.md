---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StageConditionState.html
---

# StageConditionState
<a name="API_StageConditionState"></a>

The state of a run of a condition for a stage.

## Contents
<a name="API_StageConditionState_Contents"></a>

 ** conditionStates **   <a name="CodePipeline-Type-StageConditionState-conditionStates"></a>
The states of the conditions for a run of a condition for a stage.
Type: Array of [ConditionState](API_ConditionState.md) objects
Required: No

 ** latestExecution **   <a name="CodePipeline-Type-StageConditionState-latestExecution"></a>
Represents information about the latest run of a condition for a stage.
Type: [StageConditionsExecution](API_StageConditionsExecution.md) object
Required: No

## See Also
<a name="API_StageConditionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/StageConditionState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/StageConditionState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/StageConditionState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
