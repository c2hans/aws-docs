---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ExecutionTrigger.html
---

# ExecutionTrigger
<a name="API_ExecutionTrigger"></a>

The interaction or event that started a pipeline execution.

## Contents
<a name="API_ExecutionTrigger_Contents"></a>

 ** triggerDetail **   <a name="CodePipeline-Type-ExecutionTrigger-triggerDetail"></a>
Detail related to the event that started a pipeline execution, such as the webhook ARN of the webhook that triggered the pipeline execution or the user ARN for a user-initiated `start-pipeline-execution` CLI command.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** triggerType **   <a name="CodePipeline-Type-ExecutionTrigger-triggerType"></a>
The type of change-detection method, command, or user interaction that started a pipeline execution.
Type: String
Valid Values: `CreatePipeline | StartPipelineExecution | PollForSourceChanges | Webhook | CloudWatchEvent | PutActionRevision | WebhookV2 | ManualRollback | AutomatedRollback`
Required: No

## See Also
<a name="API_ExecutionTrigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ExecutionTrigger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ExecutionTrigger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ExecutionTrigger)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
