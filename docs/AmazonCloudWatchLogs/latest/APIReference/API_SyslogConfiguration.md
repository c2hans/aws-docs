---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_SyslogConfiguration.html
---

# SyslogConfiguration
<a name="API_SyslogConfiguration"></a>

Contains information about a syslog configuration associated with a log group.

## Contents
<a name="API_SyslogConfiguration_Contents"></a>

 ** createdAt **   <a name="CWL-Type-SyslogConfiguration-createdAt"></a>
The time when the syslog configuration was created, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** logGroupArn **   <a name="CWL-Type-SyslogConfiguration-logGroupArn"></a>
The ARN of the log group associated with this syslog configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: No

 ** sourceType **   <a name="CWL-Type-SyslogConfiguration-sourceType"></a>
The source type for the syslog configuration.
Type: String
Valid Values: `VPCE`
Required: No

 ** vpcEndpointId **   <a name="CWL-Type-SyslogConfiguration-vpcEndpointId"></a>
The ID of the VPC endpoint used for syslog ingestion.
Type: String
Pattern: `^vpce-[0-9a-f]{1,64}$`
Required: No

## See Also
<a name="API_SyslogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/SyslogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/SyslogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/SyslogConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
