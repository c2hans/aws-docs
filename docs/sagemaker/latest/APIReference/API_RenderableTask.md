---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RenderableTask.html
---

# RenderableTask
<a name="API_RenderableTask"></a>

Contains input values for a task.

## Contents
<a name="API_RenderableTask_Contents"></a>

 ** Input **   <a name="sagemaker-Type-RenderableTask-Input"></a>
A JSON object that contains values for the variables defined in the template. It is made available to the template under the substitution variable `task.input`. For example, if you define a variable `task.input.text` in your template, you can supply the variable in the JSON object as `"text": "sample text"`.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128000.
Pattern: `[\S\s]+`
Required: Yes

## See Also
<a name="API_RenderableTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RenderableTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RenderableTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RenderableTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
