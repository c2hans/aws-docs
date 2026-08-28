---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_SessionMonitoringConfiguration.html
---

# SessionMonitoringConfiguration
<a name="API_SessionMonitoringConfiguration"></a>

The monitoring configuration for a session. Controls where session logs are published.

## Contents
<a name="API_SessionMonitoringConfiguration_Contents"></a>

 ** CloudWatchLoggingConfiguration **   <a name="EMR-Type-SessionMonitoringConfiguration-CloudWatchLoggingConfiguration"></a>
The CloudWatch Logs configuration for the session.
Type: [SessionCloudWatchLoggingConfiguration](API_SessionCloudWatchLoggingConfiguration.md) object
Required: No

 ** ManagedLoggingConfiguration **   <a name="EMR-Type-SessionMonitoringConfiguration-ManagedLoggingConfiguration"></a>
The Amazon EMR-managed logging configuration for the session.
Type: [SessionManagedLoggingConfiguration](API_SessionManagedLoggingConfiguration.md) object
Required: No

 ** S3LoggingConfiguration **   <a name="EMR-Type-SessionMonitoringConfiguration-S3LoggingConfiguration"></a>
The Amazon S3 logging configuration for the session.
Type: [SessionS3LoggingConfiguration](API_SessionS3LoggingConfiguration.md) object
Required: No

## See Also
<a name="API_SessionMonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SessionMonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SessionMonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SessionMonitoringConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
