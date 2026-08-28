---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PipelineVariable.html
---

# PipelineVariable
<a name="API_PipelineVariable"></a>

A pipeline-level variable used for a pipeline execution.

## Contents
<a name="API_PipelineVariable_Contents"></a>

 ** name **   <a name="CodePipeline-Type-PipelineVariable-name"></a>
The name of a pipeline-level variable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9@\-_]+`
Required: Yes

 ** value **   <a name="CodePipeline-Type-PipelineVariable-value"></a>
The value of a pipeline-level variable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_PipelineVariable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PipelineVariable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PipelineVariable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PipelineVariable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
