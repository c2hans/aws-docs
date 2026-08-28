---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PipelineContext.html
---

# PipelineContext
<a name="API_PipelineContext"></a>

Represents information about a pipeline to a job worker.

**Note**
PipelineContext contains `pipelineArn` and `pipelineExecutionId` for custom action jobs. The `pipelineArn` and `pipelineExecutionId` fields are not populated for ThirdParty action jobs.

## Contents
<a name="API_PipelineContext_Contents"></a>

 ** action **   <a name="CodePipeline-Type-PipelineContext-action"></a>
The context of an action to a job worker in the stage of a pipeline.
Type: [ActionContext](API_ActionContext.md) object
Required: No

 ** pipelineArn **   <a name="CodePipeline-Type-PipelineContext-pipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline.
Type: String
Pattern: `arn:aws(-[\w]+)*:codepipeline:.+:[0-9]{12}:.+`
Required: No

 ** pipelineExecutionId **   <a name="CodePipeline-Type-PipelineContext-pipelineExecutionId"></a>
The execution ID of the pipeline.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** pipelineName **   <a name="CodePipeline-Type-PipelineContext-pipelineName"></a>
The name of the pipeline. This is a user-specified value. Pipeline names must be unique across all pipeline names under an AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9.@\-_]+`
Required: No

 ** stage **   <a name="CodePipeline-Type-PipelineContext-stage"></a>
The stage of the pipeline.
Type: [StageContext](API_StageContext.md) object
Required: No

## See Also
<a name="API_PipelineContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PipelineContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PipelineContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PipelineContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
