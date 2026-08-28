---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_NotebookInstanceLifecycleConfigSummary.html
---

# NotebookInstanceLifecycleConfigSummary
<a name="API_NotebookInstanceLifecycleConfigSummary"></a>

Provides a summary of a notebook instance lifecycle configuration.

## Contents
<a name="API_NotebookInstanceLifecycleConfigSummary_Contents"></a>

 ** NotebookInstanceLifecycleConfigArn **   <a name="sagemaker-Type-NotebookInstanceLifecycleConfigSummary-NotebookInstanceLifecycleConfigArn"></a>
The Amazon Resource Name (ARN) of the lifecycle configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** NotebookInstanceLifecycleConfigName **   <a name="sagemaker-Type-NotebookInstanceLifecycleConfigSummary-NotebookInstanceLifecycleConfigName"></a>
The name of the lifecycle configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** CreationTime **   <a name="sagemaker-Type-NotebookInstanceLifecycleConfigSummary-CreationTime"></a>
A timestamp that tells when the lifecycle configuration was created.
Type: Timestamp
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-NotebookInstanceLifecycleConfigSummary-LastModifiedTime"></a>
A timestamp that tells when the lifecycle configuration was last modified.
Type: Timestamp
Required: No

## See Also
<a name="API_NotebookInstanceLifecycleConfigSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/NotebookInstanceLifecycleConfigSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/NotebookInstanceLifecycleConfigSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/NotebookInstanceLifecycleConfigSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
