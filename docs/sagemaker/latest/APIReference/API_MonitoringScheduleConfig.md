---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringScheduleConfig.html
---

# MonitoringScheduleConfig
<a name="API_MonitoringScheduleConfig"></a>

Configures the monitoring schedule and defines the monitoring job.

## Contents
<a name="API_MonitoringScheduleConfig_Contents"></a>

 ** MonitoringJobDefinition **   <a name="sagemaker-Type-MonitoringScheduleConfig-MonitoringJobDefinition"></a>
Defines the monitoring job.
Type: [MonitoringJobDefinition](API_MonitoringJobDefinition.md) object
Required: No

 ** MonitoringJobDefinitionName **   <a name="sagemaker-Type-MonitoringScheduleConfig-MonitoringJobDefinitionName"></a>
The name of the monitoring job definition to schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** MonitoringType **   <a name="sagemaker-Type-MonitoringScheduleConfig-MonitoringType"></a>
The type of the monitoring job definition to schedule.
Type: String
Valid Values: `DataQuality | ModelQuality | ModelBias | ModelExplainability`
Required: No

 ** ScheduleConfig **   <a name="sagemaker-Type-MonitoringScheduleConfig-ScheduleConfig"></a>
Configures the monitoring schedule.
Type: [ScheduleConfig](API_ScheduleConfig.md) object
Required: No

## See Also
<a name="API_MonitoringScheduleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringScheduleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringScheduleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringScheduleConfig)
