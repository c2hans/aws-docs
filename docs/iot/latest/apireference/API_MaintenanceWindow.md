---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_MaintenanceWindow.html
---

# MaintenanceWindow
<a name="API_MaintenanceWindow"></a>

An optional configuration within the `SchedulingConfig` to setup a recurring maintenance window with a predetermined start time and duration for the rollout of a job document to all devices in a target group for a job.

## Contents
<a name="API_MaintenanceWindow_Contents"></a>

 ** durationInMinutes **   <a name="iot-Type-MaintenanceWindow-durationInMinutes"></a>
Displays the duration of the next maintenance window.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1430.
Required: Yes

 ** startTime **   <a name="iot-Type-MaintenanceWindow-startTime"></a>
Displays the start time of the next maintenance window.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_MaintenanceWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/MaintenanceWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/MaintenanceWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/MaintenanceWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
