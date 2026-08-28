---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ConfigureLogsForPlaybackConfiguration.html
---

# ConfigureLogsForPlaybackConfiguration
<a name="API_ConfigureLogsForPlaybackConfiguration"></a>

Defines where AWS Elemental MediaTailor sends logs for the playback configuration.

## Request Syntax
<a name="API_ConfigureLogsForPlaybackConfiguration_RequestSyntax"></a>

```
PUT /configureLogs/playbackConfiguration HTTP/1.1
Content-type: application/json

{
   "AdsInteractionLog": {
      "ExcludeEventTypes": [ "{{string}}" ],
      "PublishOptInEventTypes": [ "{{string}}" ]
   },
   "EnabledLoggingStrategies": [ "{{string}}" ],
   "ManifestServiceInteractionLog": {
      "ExcludeEventTypes": [ "{{string}}" ],
      "PublishOptInEventTypes": [ "{{string}}" ]
   },
   "PercentEnabled": {{number}},
   "PlaybackConfigurationName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ConfigureLogsForPlaybackConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ConfigureLogsForPlaybackConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdsInteractionLog](#API_ConfigureLogsForPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-ConfigureLogsForPlaybackConfiguration-request-AdsInteractionLog"></a>
The event types that MediaTailor emits in logs for interactions with the ADS.
Type: [AdsInteractionLog](API_AdsInteractionLog.md) object
Required: No

 ** [EnabledLoggingStrategies](#API_ConfigureLogsForPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-ConfigureLogsForPlaybackConfiguration-request-EnabledLoggingStrategies"></a>
The method used for collecting logs from AWS Elemental MediaTailor. To configure MediaTailor to send logs directly to Amazon CloudWatch Logs, choose `LEGACY_CLOUDWATCH`. To configure MediaTailor to send logs to CloudWatch, which then vends the logs to your destination of choice, choose `VENDED_LOGS`. Supported destinations are CloudWatch Logs log group, Amazon S3 bucket, and Amazon Data Firehose stream.
To use vended logs, you must configure the delivery destination in Amazon CloudWatch, as described in [Enable logging from AWS services, Logging that requires additional permissions [V2]](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-vended-logs-permissions-V2).
Type: Array of strings
Valid Values: `VENDED_LOGS | LEGACY_CLOUDWATCH`
Required: No

 ** [ManifestServiceInteractionLog](#API_ConfigureLogsForPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-ConfigureLogsForPlaybackConfiguration-request-ManifestServiceInteractionLog"></a>
The event types that MediaTailor emits in logs for interactions with the origin server.
Type: [ManifestServiceInteractionLog](API_ManifestServiceInteractionLog.md) object
Required: No

 ** [PercentEnabled](#API_ConfigureLogsForPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-ConfigureLogsForPlaybackConfiguration-request-PercentEnabled"></a>
The percentage of session logs that MediaTailor sends to your CloudWatch Logs account. For example, if your playback configuration has 1000 sessions and percentEnabled is set to `60`, MediaTailor sends logs for 600 of the sessions to CloudWatch Logs. MediaTailor decides at random which of the playback configuration sessions to send logs for. If you want to view logs for a specific session, you can use the [debug log mode](https://docs.aws.amazon.com/mediatailor/latest/ug/debug-log-mode.html).
Valid values: `0` - `100`
Type: Integer
Required: Yes

 ** [PlaybackConfigurationName](#API_ConfigureLogsForPlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-ConfigureLogsForPlaybackConfiguration-request-PlaybackConfigurationName"></a>
The name of the playback configuration.
Type: String
Required: Yes

## Response Syntax
<a name="API_ConfigureLogsForPlaybackConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AdsInteractionLog": {
      "ExcludeEventTypes": [ "string" ],
      "PublishOptInEventTypes": [ "string" ]
   },
   "EnabledLoggingStrategies": [ "string" ],
   "ManifestServiceInteractionLog": {
      "ExcludeEventTypes": [ "string" ],
      "PublishOptInEventTypes": [ "string" ]
   },
   "PercentEnabled": number,
   "PlaybackConfigurationName": "string"
}
```

## Response Elements
<a name="API_ConfigureLogsForPlaybackConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdsInteractionLog](#API_ConfigureLogsForPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-ConfigureLogsForPlaybackConfiguration-response-AdsInteractionLog"></a>
The event types that MediaTailor emits in logs for interactions with the ADS.
Type: [AdsInteractionLog](API_AdsInteractionLog.md) object

 ** [EnabledLoggingStrategies](#API_ConfigureLogsForPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-ConfigureLogsForPlaybackConfiguration-response-EnabledLoggingStrategies"></a>
The method used for collecting logs from AWS Elemental MediaTailor. `LEGACY_CLOUDWATCH` indicates that MediaTailor is sending logs directly to Amazon CloudWatch Logs. `VENDED_LOGS` indicates that MediaTailor is sending logs to CloudWatch, which then vends the logs to your destination of choice. Supported destinations are CloudWatch Logs log group, Amazon S3 bucket, and Amazon Data Firehose stream.
Type: Array of strings
Valid Values: `VENDED_LOGS | LEGACY_CLOUDWATCH`

 ** [ManifestServiceInteractionLog](#API_ConfigureLogsForPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-ConfigureLogsForPlaybackConfiguration-response-ManifestServiceInteractionLog"></a>
The event types that MediaTailor emits in logs for interactions with the origin server.
Type: [ManifestServiceInteractionLog](API_ManifestServiceInteractionLog.md) object

 ** [PercentEnabled](#API_ConfigureLogsForPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-ConfigureLogsForPlaybackConfiguration-response-PercentEnabled"></a>
The percentage of session logs that MediaTailor sends to your Cloudwatch Logs account.
Type: Integer

 ** [PlaybackConfigurationName](#API_ConfigureLogsForPlaybackConfiguration_ResponseSyntax) **   <a name="mediatailor-ConfigureLogsForPlaybackConfiguration-response-PlaybackConfigurationName"></a>
The name of the playback configuration.
Type: String

## Errors
<a name="API_ConfigureLogsForPlaybackConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ConfigureLogsForPlaybackConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/ConfigureLogsForPlaybackConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/ConfigureLogsForPlaybackConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ConfigureLogsForPlaybackConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/ConfigureLogsForPlaybackConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ConfigureLogsForPlaybackConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/ConfigureLogsForPlaybackConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/ConfigureLogsForPlaybackConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/ConfigureLogsForPlaybackConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/ConfigureLogsForPlaybackConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ConfigureLogsForPlaybackConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
