---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDashboardMonitoringSchedule.html
---

# ModelDashboardMonitoringSchedule
<a name="API_ModelDashboardMonitoringSchedule"></a>

A monitoring schedule for a model displayed in the Amazon SageMaker Model Dashboard.

## Contents
<a name="API_ModelDashboardMonitoringSchedule_Contents"></a>

 ** BatchTransformInput **   <a name="sagemaker-Type-ModelDashboardMonitoringSchedule-BatchTransformInput"></a>
Input object for the batch transform job.
Type: [BatchTransformInput](API_BatchTransformInput.md) object
Required: No

 ** CreationTime **   <a name="sagemaker-Type-ModelDashboardMonitoringSchedule-CreationTime"></a>
A timestamp that indicates when the monitoring schedule was created.
Type: Timestamp
Required: No

 ** EndpointName **   <a name="sagemaker-Type-ModelDashboardMonitoringSchedule-EndpointName"></a>
The endpoint which is monitored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** FailureReason **   <a name="sagemaker-Type-ModelDashboardMonitoringSchedule-FailureReason"></a>
If a monitoring job failed, provides the reason.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-ModelDashboardMonitoringSchedule-LastModifiedTime"></a>
A timestamp that indicates when the monitoring schedule was last updated.
Type: Timestamp
Required: No

 ** LastMonitoringExecutionSummary **   <a name="sagemaker-Type-ModelDashboardMonitoringSchedule-LastMonitoringExecutionSummary"></a>
Summary of information about the last monitoring job to run.
Type: [MonitoringExecutionSummary](API_MonitoringExecutionSummary.md) object
Required: No

 ** MonitoringAlertSummaries **   <a name="sagemaker-Type-ModelDashboardMonitoringSchedule-MonitoringAlertSummaries"></a>
A JSON array where each element is a summary for a monitoring alert.
Type: Array of [MonitoringAlertSummary](API_MonitoringAlertSummary.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** MonitoringScheduleArn **   <a name="sagemaker-Type-ModelDashboardMonitoringSchedule-MonitoringScheduleArn"></a>
The Amazon Resource Name (ARN) of a monitoring schedule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** MonitoringScheduleConfig **   <a name="sagemaker-Type-ModelDashboardMonitoringSchedule-MonitoringScheduleConfig"></a>
Configures the monitoring schedule and defines the monitoring job.
Type: [MonitoringScheduleConfig](API_MonitoringScheduleConfig.md) object
Required: No

 ** MonitoringScheduleName **   <a name="sagemaker-Type-ModelDashboardMonitoringSchedule-MonitoringScheduleName"></a>
The name of a monitoring schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** MonitoringScheduleStatus **   <a name="sagemaker-Type-ModelDashboardMonitoringSchedule-MonitoringScheduleStatus"></a>
The status of the monitoring schedule.
Type: String
Valid Values: `Pending | Failed | Scheduled | Stopped`
Required: No

 ** MonitoringType **   <a name="sagemaker-Type-ModelDashboardMonitoringSchedule-MonitoringType"></a>
The monitor type of a model monitor.
Type: String
Valid Values: `DataQuality | ModelQuality | ModelBias | ModelExplainability`
Required: No

## See Also
<a name="API_ModelDashboardMonitoringSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelDashboardMonitoringSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelDashboardMonitoringSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelDashboardMonitoringSchedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
