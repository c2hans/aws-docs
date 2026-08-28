---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_ATITrainingMetricsValue.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# ATITrainingMetricsValue
<a name="API_ATITrainingMetricsValue"></a>

 The Account Takeover Insights (ATI) model training metric details.

## Contents
<a name="API_ATITrainingMetricsValue_Contents"></a>

 ** metricDataPoints **   <a name="FraudDetector-Type-ATITrainingMetricsValue-metricDataPoints"></a>
 The model's performance metrics data points.
Type: Array of [ATIMetricDataPoint](API_ATIMetricDataPoint.md) objects
Required: No

 ** modelPerformance **   <a name="FraudDetector-Type-ATITrainingMetricsValue-modelPerformance"></a>
 The model's overall performance scores.
Type: [ATIModelPerformance](API_ATIModelPerformance.md) object
Required: No

## See Also
<a name="API_ATITrainingMetricsValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/ATITrainingMetricsValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/ATITrainingMetricsValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/ATITrainingMetricsValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
