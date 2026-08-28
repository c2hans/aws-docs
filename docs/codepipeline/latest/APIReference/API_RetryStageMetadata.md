---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_RetryStageMetadata.html
---

# RetryStageMetadata
<a name="API_RetryStageMetadata"></a>

The details of a specific automatic retry on stage failure, including the attempt number and trigger.

## Contents
<a name="API_RetryStageMetadata_Contents"></a>

 ** autoStageRetryAttempt **   <a name="CodePipeline-Type-RetryStageMetadata-autoStageRetryAttempt"></a>
The number of attempts for a specific stage with automatic retry on stage failure. One attempt is allowed for automatic stage retry on failure.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** latestRetryTrigger **   <a name="CodePipeline-Type-RetryStageMetadata-latestRetryTrigger"></a>
The latest trigger for a specific stage where manual or automatic retries have been made upon stage failure.
Type: String
Valid Values: `AutomatedStageRetry | ManualStageRetry`
Required: No

 ** manualStageRetryAttempt **   <a name="CodePipeline-Type-RetryStageMetadata-manualStageRetryAttempt"></a>
The number of attempts for a specific stage where manual retries have been made upon stage failure.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_RetryStageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RetryStageMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RetryStageMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RetryStageMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
