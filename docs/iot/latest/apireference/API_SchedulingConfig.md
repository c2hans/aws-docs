---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_SchedulingConfig.html
---

# SchedulingConfig
<a name="API_SchedulingConfig"></a>

Specifies the date and time that a job will begin the rollout of the job document to all devices in the target group. Additionally, you can specify the end behavior for each job execution when it reaches the scheduled end time.

## Contents
<a name="API_SchedulingConfig_Contents"></a>

 ** endBehavior **   <a name="iot-Type-SchedulingConfig-endBehavior"></a>
Specifies the end behavior for all job executions after a job reaches the selected `endTime`. If `endTime` is not selected when creating the job, then `endBehavior` does not apply.
Type: String
Valid Values: `STOP_ROLLOUT | CANCEL | FORCE_CANCEL`
Required: No

 ** endTime **   <a name="iot-Type-SchedulingConfig-endTime"></a>
The time a job will stop rollout of the job document to all devices in the target group for a job. The `endTime` must take place no later than two years from the current time and be scheduled a minimum of thirty minutes from the current time. The minimum duration between `startTime` and `endTime` is thirty minutes. The maximum duration between `startTime` and `endTime` is two years. The date and time format for the `endTime` is YYYY-MM-DD for the date and HH:MM for the time.
For more information on the syntax for `endTime` when using an API command or the AWS Command Line Interface, see [Timestamp](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** maintenanceWindows **   <a name="iot-Type-SchedulingConfig-maintenanceWindows"></a>
An optional configuration within the `SchedulingConfig` to setup a recurring maintenance window with a predetermined start time and duration for the rollout of a job document to all devices in a target group for a job.
Type: Array of [MaintenanceWindow](API_MaintenanceWindow.md) objects
Required: No

 ** startTime **   <a name="iot-Type-SchedulingConfig-startTime"></a>
The time a job will begin rollout of the job document to all devices in the target group for a job. The `startTime` can be scheduled up to a year in advance and must be scheduled a minimum of thirty minutes from the current time. The date and time format for the `startTime` is YYYY-MM-DD for the date and HH:MM for the time.
For more information on the syntax for `startTime` when using an API command or the AWS Command Line Interface, see [Timestamp](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_SchedulingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/SchedulingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/SchedulingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/SchedulingConfig)
