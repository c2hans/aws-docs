---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ActionExecutionFilter.html
---

# ActionExecutionFilter
<a name="API_ActionExecutionFilter"></a>

Filter values for the action execution.

## Contents
<a name="API_ActionExecutionFilter_Contents"></a>

 ** latestInPipelineExecution **   <a name="CodePipeline-Type-ActionExecutionFilter-latestInPipelineExecution"></a>
The latest execution in the pipeline.
Filtering on the latest execution is available for executions run on or after February 08, 2024.
Type: [LatestInPipelineExecutionFilter](API_LatestInPipelineExecutionFilter.md) object
Required: No

 ** pipelineExecutionId **   <a name="CodePipeline-Type-ActionExecutionFilter-pipelineExecutionId"></a>
The pipeline execution ID used to filter action execution history.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_ActionExecutionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionExecutionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionExecutionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionExecutionFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
