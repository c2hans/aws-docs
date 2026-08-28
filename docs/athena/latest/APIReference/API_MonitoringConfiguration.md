---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_MonitoringConfiguration.html
---

# MonitoringConfiguration
<a name="API_MonitoringConfiguration"></a>

Contains the configuration settings for managed log persistence, delivering logs to Amazon S3 buckets, Amazon CloudWatch log groups etc.

## Contents
<a name="API_MonitoringConfiguration_Contents"></a>

 ** CloudWatchLoggingConfiguration **   <a name="athena-Type-MonitoringConfiguration-CloudWatchLoggingConfiguration"></a>
Configuration settings for delivering logs to Amazon CloudWatch log groups.
Type: [CloudWatchLoggingConfiguration](API_CloudWatchLoggingConfiguration.md) object
Required: No

 ** ManagedLoggingConfiguration **   <a name="athena-Type-MonitoringConfiguration-ManagedLoggingConfiguration"></a>
Configuration settings for managed log persistence.
Type: [ManagedLoggingConfiguration](API_ManagedLoggingConfiguration.md) object
Required: No

 ** S3LoggingConfiguration **   <a name="athena-Type-MonitoringConfiguration-S3LoggingConfiguration"></a>
Configuration settings for delivering logs to Amazon S3 buckets.
Type: [S3LoggingConfiguration](API_S3LoggingConfiguration.md) object
Required: No

## See Also
<a name="API_MonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/MonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/MonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/MonitoringConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
