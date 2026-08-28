---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ActionContext.html
---

# ActionContext
<a name="API_ActionContext"></a>

Represents the context of an action in the stage of a pipeline to a job worker.

## Contents
<a name="API_ActionContext_Contents"></a>

 ** actionExecutionId **   <a name="CodePipeline-Type-ActionContext-actionExecutionId"></a>
The system-generated unique ID that corresponds to an action's execution.
Type: String
Required: No

 ** name **   <a name="CodePipeline-Type-ActionContext-name"></a>
The name of the action in the context of a job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9.@\-_]+`
Required: No

## See Also
<a name="API_ActionContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
