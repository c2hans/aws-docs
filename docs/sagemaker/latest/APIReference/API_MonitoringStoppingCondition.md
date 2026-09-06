---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringStoppingCondition.html
---

# MonitoringStoppingCondition
<a name="API_MonitoringStoppingCondition"></a>

A time limit for how long the monitoring job is allowed to run before stopping.

## Contents
<a name="API_MonitoringStoppingCondition_Contents"></a>

 ** MaxRuntimeInSeconds **   <a name="sagemaker-Type-MonitoringStoppingCondition-MaxRuntimeInSeconds"></a>
The maximum runtime allowed in seconds.
The `MaxRuntimeInSeconds` cannot exceed the frequency of the job. For data quality and model explainability, this can be up to 3600 seconds for an hourly schedule. For model bias and model quality hourly schedules, this can be up to 1800 seconds.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.
Required: Yes

## See Also
<a name="API_MonitoringStoppingCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringStoppingCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringStoppingCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringStoppingCondition)
