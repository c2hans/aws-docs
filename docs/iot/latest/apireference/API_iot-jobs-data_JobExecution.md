---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_JobExecution.html
---

# JobExecution
<a name="API_iot-jobs-data_JobExecution"></a>

Contains data about a job execution.

## Contents
<a name="API_iot-jobs-data_JobExecution_Contents"></a>

 ** approximateSecondsBeforeTimedOut **   <a name="iot-Type-iot-jobs-data_JobExecution-approximateSecondsBeforeTimedOut"></a>
The estimated number of seconds that remain before the job execution status will be changed to `TIMED_OUT`. The actual job execution timeout can occur up to 60 seconds later than the estimated duration.
Type: Long
Required: No

 ** executionNumber **   <a name="iot-Type-iot-jobs-data_JobExecution-executionNumber"></a>
A number that identifies a particular job execution on a particular device. It can be used later in commands that return or update job execution information.
Type: Long
Required: No

 ** jobDocument **   <a name="iot-Type-iot-jobs-data_JobExecution-jobDocument"></a>
The content of the job document.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** jobId **   <a name="iot-Type-iot-jobs-data_JobExecution-jobId"></a>
The unique identifier you assigned to this job when it was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** lastUpdatedAt **   <a name="iot-Type-iot-jobs-data_JobExecution-lastUpdatedAt"></a>
The time, in seconds since the epoch, when the job execution was last updated.
Type: Long
Required: No

 ** queuedAt **   <a name="iot-Type-iot-jobs-data_JobExecution-queuedAt"></a>
The time, in seconds since the epoch, when the job execution was enqueued.
Type: Long
Required: No

 ** startedAt **   <a name="iot-Type-iot-jobs-data_JobExecution-startedAt"></a>
The time, in seconds since the epoch, when the job execution was started.
Type: Long
Required: No

 ** status **   <a name="iot-Type-iot-jobs-data_JobExecution-status"></a>
The status of the job execution. Can be one of: "QUEUED", "IN\_PROGRESS", "FAILED", "SUCCESS", "CANCELED", "TIMED\_OUT", "REJECTED", or "REMOVED".
Type: String
Valid Values: `QUEUED | IN_PROGRESS | SUCCEEDED | FAILED | TIMED_OUT | REJECTED | REMOVED | CANCELED`
Required: No

 ** statusDetails **   <a name="iot-Type-iot-jobs-data_JobExecution-statusDetails"></a>
A collection of name/value pairs that describe the status of the job execution.
The maximum length of the value in the name/value pair is 1,024 characters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9:_-]+`
Value Length Constraints: Minimum length of 1.
Value Pattern: `[^\p{C}]+`
Required: No

 ** thingName **   <a name="iot-Type-iot-jobs-data_JobExecution-thingName"></a>
The name of the thing that is executing the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** versionNumber **   <a name="iot-Type-iot-jobs-data_JobExecution-versionNumber"></a>
The version of the job execution. Job execution versions are incremented each time they are updated by a device.
Type: Long
Required: No

## See Also
<a name="API_iot-jobs-data_JobExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-jobs-data-2017-09-29/JobExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-jobs-data-2017-09-29/JobExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-jobs-data-2017-09-29/JobExecution)
