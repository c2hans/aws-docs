---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceExecutionConfig.html
---

# InferenceExecutionConfig
<a name="API_InferenceExecutionConfig"></a>

Specifies details about how containers in a multi-container endpoint are run.

## Contents
<a name="API_InferenceExecutionConfig_Contents"></a>

 ** Mode **   <a name="sagemaker-Type-InferenceExecutionConfig-Mode"></a>
How containers in a multi-container are run. The following values are valid.
+  `SERIAL` - Containers run as a serial pipeline.
+  `DIRECT` - Only the individual container that you specify is run.
Type: String
Valid Values: `Serial | Direct`
Required: Yes

## See Also
<a name="API_InferenceExecutionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceExecutionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceExecutionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceExecutionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
