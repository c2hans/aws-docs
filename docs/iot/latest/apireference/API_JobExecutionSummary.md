---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_JobExecutionSummary.html
---

# JobExecutionSummary
<a name="API_JobExecutionSummary"></a>

The job execution summary.

## Contents
<a name="API_JobExecutionSummary_Contents"></a>

 ** executionNumber **   <a name="iot-Type-JobExecutionSummary-executionNumber"></a>
A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used later in commands which return or update job execution information.
Type: Long
Required: No

 ** lastUpdatedAt **   <a name="iot-Type-JobExecutionSummary-lastUpdatedAt"></a>
The time, in seconds since the epoch, when the job execution was last updated.
Type: Timestamp
Required: No

 ** queuedAt **   <a name="iot-Type-JobExecutionSummary-queuedAt"></a>
The time, in seconds since the epoch, when the job execution was queued.
Type: Timestamp
Required: No

 ** retryAttempt **   <a name="iot-Type-JobExecutionSummary-retryAttempt"></a>
The number that indicates how many retry attempts have been completed for this job on this device.
Type: Integer
Required: No

 ** startedAt **   <a name="iot-Type-JobExecutionSummary-startedAt"></a>
The time, in seconds since the epoch, when the job execution started.
Type: Timestamp
Required: No

 ** status **   <a name="iot-Type-JobExecutionSummary-status"></a>
The status of the job execution.
Type: String
Valid Values: `QUEUED | IN_PROGRESS | SUCCEEDED | FAILED | TIMED_OUT | REJECTED | REMOVED | CANCELED`
Required: No

## See Also
<a name="API_JobExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/JobExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/JobExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/JobExecutionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
