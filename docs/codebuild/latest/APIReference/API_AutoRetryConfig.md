---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_AutoRetryConfig.html
---

# AutoRetryConfig
<a name="API_AutoRetryConfig"></a>

Information about the auto-retry configuration for the build.

## Contents
<a name="API_AutoRetryConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** autoRetryLimit **   <a name="CodeBuild-Type-AutoRetryConfig-autoRetryLimit"></a>
The maximum number of additional automatic retries after a failed build. For example, if the auto-retry limit is set to 2, CodeBuild will call the `RetryBuild` API to automatically retry your build for up to 2 additional times.
Type: Integer
Required: No

 ** autoRetryNumber **   <a name="CodeBuild-Type-AutoRetryConfig-autoRetryNumber"></a>
The number of times that the build has been retried. The initial build will have an auto-retry number of 0.
Type: Integer
Required: No

 ** nextAutoRetry **   <a name="CodeBuild-Type-AutoRetryConfig-nextAutoRetry"></a>
The build ARN of the auto-retried build triggered by the current build. The next auto-retry will be `null` for builds that don't trigger an auto-retry.
Type: String
Required: No

 ** previousAutoRetry **   <a name="CodeBuild-Type-AutoRetryConfig-previousAutoRetry"></a>
The build ARN of the build that triggered the current auto-retry build. The previous auto-retry will be `null` for the initial build.
Type: String
Required: No

## See Also
<a name="API_AutoRetryConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/AutoRetryConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/AutoRetryConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/AutoRetryConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
