---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_JobExecutionSummary.html
---

# JobExecutionSummary
<a name="API_iot-jobs-data_JobExecutionSummary"></a>

Contains a subset of information about a job execution.

## Contents
<a name="API_iot-jobs-data_JobExecutionSummary_Contents"></a>

 ** executionNumber **   <a name="iot-Type-iot-jobs-data_JobExecutionSummary-executionNumber"></a>
A number that identifies a particular job execution on a particular device.
Type: Long
Required: No

 ** jobId **   <a name="iot-Type-iot-jobs-data_JobExecutionSummary-jobId"></a>
The unique identifier you assigned to this job when it was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** lastUpdatedAt **   <a name="iot-Type-iot-jobs-data_JobExecutionSummary-lastUpdatedAt"></a>
The time, in seconds since the epoch, when the job execution was last updated.
Type: Long
Required: No

 ** queuedAt **   <a name="iot-Type-iot-jobs-data_JobExecutionSummary-queuedAt"></a>
The time, in seconds since the epoch, when the job execution was enqueued.
Type: Long
Required: No

 ** startedAt **   <a name="iot-Type-iot-jobs-data_JobExecutionSummary-startedAt"></a>
The time, in seconds since the epoch, when the job execution started.
Type: Long
Required: No

 ** versionNumber **   <a name="iot-Type-iot-jobs-data_JobExecutionSummary-versionNumber"></a>
The version of the job execution. Job execution versions are incremented each time AWS IoT Jobs receives an update from a device.
Type: Long
Required: No

## See Also
<a name="API_iot-jobs-data_JobExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-jobs-data-2017-09-29/JobExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-jobs-data-2017-09-29/JobExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-jobs-data-2017-09-29/JobExecutionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
