---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_JobExecutionState.html
---

# JobExecutionState
<a name="API_iot-jobs-data_JobExecutionState"></a>

Contains data about the state of a job execution.

## Contents
<a name="API_iot-jobs-data_JobExecutionState_Contents"></a>

 ** status **   <a name="iot-Type-iot-jobs-data_JobExecutionState-status"></a>
The status of the job execution. Can be one of: "QUEUED", "IN\_PROGRESS", "FAILED", "SUCCESS", "CANCELED", "TIMED\_OUT", "REJECTED", or "REMOVED".
Type: String
Valid Values: `QUEUED | IN_PROGRESS | SUCCEEDED | FAILED | TIMED_OUT | REJECTED | REMOVED | CANCELED`
Required: No

 ** statusDetails **   <a name="iot-Type-iot-jobs-data_JobExecutionState-statusDetails"></a>
A collection of name/value pairs that describe the status of the job execution.
The maximum length of the value in the name/value pair is 1,024 characters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9:_-]+`
Value Length Constraints: Minimum length of 1.
Value Pattern: `[^\p{C}]+`
Required: No

 ** versionNumber **   <a name="iot-Type-iot-jobs-data_JobExecutionState-versionNumber"></a>
The version of the job execution. Job execution versions are incremented each time they are updated by a device.
Type: Long
Required: No

## See Also
<a name="API_iot-jobs-data_JobExecutionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-jobs-data-2017-09-29/JobExecutionState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-jobs-data-2017-09-29/JobExecutionState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-jobs-data-2017-09-29/JobExecutionState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
