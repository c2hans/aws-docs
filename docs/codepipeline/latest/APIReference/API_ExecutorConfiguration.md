---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ExecutorConfiguration.html
---

# ExecutorConfiguration
<a name="API_ExecutorConfiguration"></a>

The action engine, or executor, related to the supported integration model used to create and update the action type. The available executor types are `Lambda` and `JobWorker`.

## Contents
<a name="API_ExecutorConfiguration_Contents"></a>

 ** jobWorkerExecutorConfiguration **   <a name="CodePipeline-Type-ExecutorConfiguration-jobWorkerExecutorConfiguration"></a>
Details about the `JobWorker` executor of the action type.
Type: [JobWorkerExecutorConfiguration](API_JobWorkerExecutorConfiguration.md) object
Required: No

 ** lambdaExecutorConfiguration **   <a name="CodePipeline-Type-ExecutorConfiguration-lambdaExecutorConfiguration"></a>
Details about the `Lambda` executor of the action type.
Type: [LambdaExecutorConfiguration](API_LambdaExecutorConfiguration.md) object
Required: No

## See Also
<a name="API_ExecutorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ExecutorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ExecutorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ExecutorConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
