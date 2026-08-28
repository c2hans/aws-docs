---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_JobExecution.html
---

# JobExecution
<a name="API_JobExecution"></a>

The job execution object represents the execution of a job on a particular device.

## Contents
<a name="API_JobExecution_Contents"></a>

 ** approximateSecondsBeforeTimedOut **   <a name="iot-Type-JobExecution-approximateSecondsBeforeTimedOut"></a>
The estimated number of seconds that remain before the job execution status will be changed to `TIMED_OUT`. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The actual job execution timeout can occur up to 60 seconds later than the estimated duration. This value will not be included if the job execution has reached a terminal status.
Type: Long
Required: No

 ** executionNumber **   <a name="iot-Type-JobExecution-executionNumber"></a>
A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used in commands which return or update job execution information.
Type: Long
Required: No

 ** forceCanceled **   <a name="iot-Type-JobExecution-forceCanceled"></a>
Will be `true` if the job execution was canceled with the optional `force` parameter set to `true`.
Type: Boolean
Required: No

 ** jobId **   <a name="iot-Type-JobExecution-jobId"></a>
The unique identifier you assigned to the job when it was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** lastUpdatedAt **   <a name="iot-Type-JobExecution-lastUpdatedAt"></a>
The time, in seconds since the epoch, when the job execution was last updated.
Type: Timestamp
Required: No

 ** queuedAt **   <a name="iot-Type-JobExecution-queuedAt"></a>
The time, in seconds since the epoch, when the job execution was queued.
Type: Timestamp
Required: No

 ** startedAt **   <a name="iot-Type-JobExecution-startedAt"></a>
The time, in seconds since the epoch, when the job execution started.
Type: Timestamp
Required: No

 ** status **   <a name="iot-Type-JobExecution-status"></a>
The status of the job execution (IN\_PROGRESS, QUEUED, FAILED, SUCCEEDED, TIMED\_OUT, CANCELED, or REJECTED).
Type: String
Valid Values: `QUEUED | IN_PROGRESS | SUCCEEDED | FAILED | TIMED_OUT | REJECTED | REMOVED | CANCELED`
Required: No

 ** statusDetails **   <a name="iot-Type-JobExecution-statusDetails"></a>
A collection of name/value pairs that describe the status of the job execution.
Type: [JobExecutionStatusDetails](API_JobExecutionStatusDetails.md) object
Required: No

 ** thingArn **   <a name="iot-Type-JobExecution-thingArn"></a>
The ARN of the thing on which the job execution is running.
Type: String
Required: No

 ** versionNumber **   <a name="iot-Type-JobExecution-versionNumber"></a>
The version of the job execution. Job execution versions are incremented each time they are updated by a device.
Type: Long
Required: No

## See Also
<a name="API_JobExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/JobExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/JobExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/JobExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
