---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StageExecution.html
---

# StageExecution
<a name="API_StageExecution"></a>

Represents information about the run of a stage.

## Contents
<a name="API_StageExecution_Contents"></a>

 ** pipelineExecutionId **   <a name="CodePipeline-Type-StageExecution-pipelineExecutionId"></a>
The ID of the pipeline execution associated with the stage.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** status **   <a name="CodePipeline-Type-StageExecution-status"></a>
The status of the stage, or for a completed stage, the last status of the stage.
A status of cancelled means that the pipeline’s definition was updated before the stage execution could be completed.
Type: String
Valid Values: `Cancelled | InProgress | Failed | Stopped | Stopping | Succeeded | Skipped`
Required: Yes

 ** type **   <a name="CodePipeline-Type-StageExecution-type"></a>
The type of pipeline execution for the stage, such as a rollback pipeline execution.
Type: String
Valid Values: `STANDARD | ROLLBACK`
Required: No

## See Also
<a name="API_StageExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/StageExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/StageExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/StageExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
