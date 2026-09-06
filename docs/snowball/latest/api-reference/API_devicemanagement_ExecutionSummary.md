---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_ExecutionSummary.html
---

# ExecutionSummary
<a name="API_devicemanagement_ExecutionSummary"></a>

The summary of a task execution on a specified device.

## Contents
<a name="API_devicemanagement_ExecutionSummary_Contents"></a>

 ** executionId **   <a name="Snowball-Type-devicemanagement_ExecutionSummary-executionId"></a>
The ID of the execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** managedDeviceId **   <a name="Snowball-Type-devicemanagement_ExecutionSummary-managedDeviceId"></a>
The ID of the managed device that the task is being executed on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** state **   <a name="Snowball-Type-devicemanagement_ExecutionSummary-state"></a>
The state of the execution.
Type: String
Valid Values: `QUEUED | IN_PROGRESS | CANCELED | FAILED | SUCCEEDED | REJECTED | TIMED_OUT`
Required: No

 ** taskId **   <a name="Snowball-Type-devicemanagement_ExecutionSummary-taskId"></a>
The ID of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_devicemanagement_ExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/ExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/ExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/ExecutionSummary)
