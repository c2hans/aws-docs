---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_LogConfiguration.html
---

# LogConfiguration
<a name="API_LogConfiguration"></a>

Defines where AWS Elemental MediaTailor sends logs for the playback configuration.

## Contents
<a name="API_LogConfiguration_Contents"></a>

 ** EnabledLoggingStrategies **   <a name="mediatailor-Type-LogConfiguration-EnabledLoggingStrategies"></a>
The method used for collecting logs from AWS Elemental MediaTailor. `LEGACY_CLOUDWATCH` indicates that MediaTailor is sending logs directly to Amazon CloudWatch Logs. `VENDED_LOGS` indicates that MediaTailor is sending logs to CloudWatch, which then vends the logs to your destination of choice. Supported destinations are CloudWatch Logs log group, Amazon S3 bucket, and Amazon Data Firehose stream.
Type: Array of strings
Valid Values: `VENDED_LOGS | LEGACY_CLOUDWATCH`
Required: Yes

 ** PercentEnabled **   <a name="mediatailor-Type-LogConfiguration-PercentEnabled"></a>
The percentage of session logs that MediaTailor sends to your configured log destination. For example, if your playback configuration has 1000 sessions and `percentEnabled` is set to `60`, MediaTailor sends logs for 600 of the sessions to CloudWatch Logs. MediaTailor decides at random which of the playback configuration sessions to send logs for. If you want to view logs for a specific session, you can use the [debug log mode](https://docs.aws.amazon.com/mediatailor/latest/ug/debug-log-mode.html).
Valid values: `0` - `100`
Type: Integer
Required: Yes

 ** AdsInteractionLog **   <a name="mediatailor-Type-LogConfiguration-AdsInteractionLog"></a>
Settings for customizing what events are included in logs for interactions with the ad decision server (ADS).
Type: [AdsInteractionLog](API_AdsInteractionLog.md) object
Required: No

 ** ManifestServiceInteractionLog **   <a name="mediatailor-Type-LogConfiguration-ManifestServiceInteractionLog"></a>
Settings for customizing what events are included in logs for interactions with the origin server.
Type: [ManifestServiceInteractionLog](API_ManifestServiceInteractionLog.md) object
Required: No

## See Also
<a name="API_LogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/LogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/LogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/LogConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
