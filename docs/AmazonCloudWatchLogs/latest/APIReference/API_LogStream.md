---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogStream.html
---

# LogStream
<a name="API_LogStream"></a>

Represents a log stream, which is a sequence of log events from a single emitter of logs.

## Contents
<a name="API_LogStream_Contents"></a>

 ** arn **   <a name="CWL-Type-LogStream-arn"></a>
The Amazon Resource Name (ARN) of the log stream.
Type: String
Required: No

 ** creationTime **   <a name="CWL-Type-LogStream-creationTime"></a>
The creation time of the stream, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** firstEventTimestamp **   <a name="CWL-Type-LogStream-firstEventTimestamp"></a>
The time of the first event, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** lastEventTimestamp **   <a name="CWL-Type-LogStream-lastEventTimestamp"></a>
The time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`. The `lastEventTime` value updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but in rare situations might take longer.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** lastIngestionTime **   <a name="CWL-Type-LogStream-lastIngestionTime"></a>
The ingestion time, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC` The `lastIngestionTime` value updates on an eventual consistency basis. It typically updates in less than an hour after ingestion, but in rare situations might take longer.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** logStreamName **   <a name="CWL-Type-LogStream-logStreamName"></a>
The name of the log stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** storedBytes **   <a name="CWL-Type-LogStream-storedBytes"></a>
 *This member has been deprecated.*
The number of bytes stored.
 **Important:** As of June 17, 2019, this parameter is no longer supported for log streams, and is always reported as zero. This change applies only to log streams. The `storedBytes` parameter for log groups is not affected.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** uploadSequenceToken **   <a name="CWL-Type-LogStream-uploadSequenceToken"></a>
The sequence token.
The sequence token is now ignored in `PutLogEvents` actions. `PutLogEvents` actions are always accepted regardless of receiving an invalid sequence token. You don't need to obtain `uploadSequenceToken` to use a `PutLogEvents` action.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_LogStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/LogStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/LogStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/LogStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
