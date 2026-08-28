---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_NotebookInstanceLifecycleHook.html
---

# NotebookInstanceLifecycleHook
<a name="API_NotebookInstanceLifecycleHook"></a>

Contains the notebook instance lifecycle configuration script.

Each lifecycle configuration script has a limit of 16384 characters.

The value of the `$PATH` environment variable that is available to both scripts is `/sbin:bin:/usr/sbin:/usr/bin`.

View Amazon CloudWatch Logs for notebook instance lifecycle configurations in log group `/aws/sagemaker/NotebookInstances` in log stream `[notebook-instance-name]/[LifecycleConfigHook]`.

Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.

For information about notebook instance lifestyle configurations, see [Step 2.1: (Optional) Customize a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html).

## Contents
<a name="API_NotebookInstanceLifecycleHook_Contents"></a>

 ** Content **   <a name="sagemaker-Type-NotebookInstanceLifecycleHook-Content"></a>
A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Pattern: `[\S\s]+`
Required: No

## See Also
<a name="API_NotebookInstanceLifecycleHook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/NotebookInstanceLifecycleHook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/NotebookInstanceLifecycleHook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/NotebookInstanceLifecycleHook)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
