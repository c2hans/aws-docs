---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_OtaTaskSchedulingConfig.html
---

# OtaTaskSchedulingConfig
<a name="API_OtaTaskSchedulingConfig"></a>

Over-the-air (OTA) task scheduling config.

## Contents
<a name="API_OtaTaskSchedulingConfig_Contents"></a>

 ** EndBehavior **   <a name="managedintegrations-Type-OtaTaskSchedulingConfig-EndBehavior"></a>
Specifies the end behavior for all task executions after a task reaches the selected `endTime`. If `endTime` is not selected when creating the task, then `endBehavior` does not apply.
Type: String
Valid Values: `STOP_ROLLOUT | CANCEL | FORCE_CANCEL`
Required: No

 ** EndTime **   <a name="managedintegrations-Type-OtaTaskSchedulingConfig-EndTime"></a>
The time an over-the-air (OTA) task will stop.
Type: String
Required: No

 ** MaintenanceWindows **   <a name="managedintegrations-Type-OtaTaskSchedulingConfig-MaintenanceWindows"></a>
Maintenance window list for over-the-air (OTA) task scheduling config.
Type: Array of [ScheduleMaintenanceWindow](API_ScheduleMaintenanceWindow.md) objects
Required: No

 ** StartTime **   <a name="managedintegrations-Type-OtaTaskSchedulingConfig-StartTime"></a>
The time an over-the-air (OTA) task will start.
Type: String
Required: No

## See Also
<a name="API_OtaTaskSchedulingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/OtaTaskSchedulingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/OtaTaskSchedulingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/OtaTaskSchedulingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
