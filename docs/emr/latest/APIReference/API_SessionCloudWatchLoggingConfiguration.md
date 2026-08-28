---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_SessionCloudWatchLoggingConfiguration.html
---

# SessionCloudWatchLoggingConfiguration
<a name="API_SessionCloudWatchLoggingConfiguration"></a>

The CloudWatch Logs configuration for a session.

## Contents
<a name="API_SessionCloudWatchLoggingConfiguration_Contents"></a>

 ** Enabled **   <a name="EMR-Type-SessionCloudWatchLoggingConfiguration-Enabled"></a>
Whether CloudWatch Logs is enabled for the session.
Type: Boolean
Required: No

 ** EncryptionKeyArn **   <a name="EMR-Type-SessionCloudWatchLoggingConfiguration-EncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the logs published to CloudWatch Logs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LogGroup **   <a name="EMR-Type-SessionCloudWatchLoggingConfiguration-LogGroup"></a>
The name of the log group where session logs are published.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LogStreamNamePrefix **   <a name="EMR-Type-SessionCloudWatchLoggingConfiguration-LogStreamNamePrefix"></a>
The prefix applied to the log stream name where session logs are published.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LogTypes **   <a name="EMR-Type-SessionCloudWatchLoggingConfiguration-LogTypes"></a>
A map of log component names (for example, `SPARK_DRIVER`, `SPARK_EXECUTOR`) to the list of log types to publish for that component (for example, `stdout`, `stderr`).
Type: String to array of strings map
Key Length Constraints: Minimum length of 0. Maximum length of 10280.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Length Constraints: Minimum length of 0. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_SessionCloudWatchLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SessionCloudWatchLoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SessionCloudWatchLoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SessionCloudWatchLoggingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
