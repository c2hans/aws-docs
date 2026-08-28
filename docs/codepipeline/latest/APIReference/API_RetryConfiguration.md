---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_RetryConfiguration.html
---

# RetryConfiguration
<a name="API_RetryConfiguration"></a>

The retry configuration specifies automatic retry for a failed stage, along with the configured retry mode.

## Contents
<a name="API_RetryConfiguration_Contents"></a>

 ** retryMode **   <a name="CodePipeline-Type-RetryConfiguration-retryMode"></a>
The method that you want to configure for automatic stage retry on stage failure. You can specify to retry only failed action in the stage or all actions in the stage.
Type: String
Valid Values: `FAILED_ACTIONS | ALL_ACTIONS`
Required: No

## See Also
<a name="API_RetryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RetryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RetryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RetryConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
