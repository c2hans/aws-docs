---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelQualityBaselineConfig.html
---

# ModelQualityBaselineConfig
<a name="API_ModelQualityBaselineConfig"></a>

Configuration for monitoring constraints and monitoring statistics. These baseline resources are compared against the results of the current job from the series of jobs scheduled to collect data periodically.

## Contents
<a name="API_ModelQualityBaselineConfig_Contents"></a>

 ** BaseliningJobName **   <a name="sagemaker-Type-ModelQualityBaselineConfig-BaseliningJobName"></a>
The name of the job that performs baselining for the monitoring job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ConstraintsResource **   <a name="sagemaker-Type-ModelQualityBaselineConfig-ConstraintsResource"></a>
The constraints resource for a monitoring job.
Type: [MonitoringConstraintsResource](API_MonitoringConstraintsResource.md) object
Required: No

## See Also
<a name="API_ModelQualityBaselineConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelQualityBaselineConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelQualityBaselineConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelQualityBaselineConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
