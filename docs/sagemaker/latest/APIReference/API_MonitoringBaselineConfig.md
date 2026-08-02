---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringBaselineConfig.html
---

# MonitoringBaselineConfig
<a name="API_MonitoringBaselineConfig"></a>

Configuration for monitoring constraints and monitoring statistics. These baseline resources are compared against the results of the current job from the series of jobs scheduled to collect data periodically.

## Contents
<a name="API_MonitoringBaselineConfig_Contents"></a>

 ** BaseliningJobName **   <a name="sagemaker-Type-MonitoringBaselineConfig-BaseliningJobName"></a>
The name of the job that performs baselining for the monitoring job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ConstraintsResource **   <a name="sagemaker-Type-MonitoringBaselineConfig-ConstraintsResource"></a>
The baseline constraint file in Amazon S3 that the current monitoring job should validated against.
Type: [MonitoringConstraintsResource](API_MonitoringConstraintsResource.md) object
Required: No

 ** StatisticsResource **   <a name="sagemaker-Type-MonitoringBaselineConfig-StatisticsResource"></a>
The baseline statistics file in Amazon S3 that the current monitoring job should be validated against.
Type: [MonitoringStatisticsResource](API_MonitoringStatisticsResource.md) object
Required: No

## See Also
<a name="API_MonitoringBaselineConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringBaselineConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringBaselineConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringBaselineConfig)
