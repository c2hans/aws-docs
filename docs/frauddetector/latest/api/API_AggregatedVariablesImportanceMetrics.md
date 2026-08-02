---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_AggregatedVariablesImportanceMetrics.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# AggregatedVariablesImportanceMetrics
<a name="API_AggregatedVariablesImportanceMetrics"></a>

The details of the relative importance of the aggregated variables.

Account Takeover Insights (ATI) model uses event variables from the login data you provide to continuously calculate a set of variables (aggregated variables) based on historical events. For example, your ATI model might calculate the number of times an user has logged in using the same IP address. In this case, event variables used to derive the aggregated variables are `IP address` and `user`.

## Contents
<a name="API_AggregatedVariablesImportanceMetrics_Contents"></a>

 ** logOddsMetrics **   <a name="FraudDetector-Type-AggregatedVariablesImportanceMetrics-logOddsMetrics"></a>
 List of variables' metrics.
Type: Array of [AggregatedLogOddsMetric](API_AggregatedLogOddsMetric.md) objects
Required: No

## See Also
<a name="API_AggregatedVariablesImportanceMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/AggregatedVariablesImportanceMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/AggregatedVariablesImportanceMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/AggregatedVariablesImportanceMetrics)
