---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_TrainingMetrics.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# TrainingMetrics
<a name="API_TrainingMetrics"></a>

The training metric details.

## Contents
<a name="API_TrainingMetrics_Contents"></a>

 ** auc **   <a name="FraudDetector-Type-TrainingMetrics-auc"></a>
The area under the curve. This summarizes true positive rate (TPR) and false positive rate (FPR) across all possible model score thresholds. A model with no predictive power has an AUC of 0.5, whereas a perfect model has a score of 1.0.
Type: Float
Required: No

 ** metricDataPoints **   <a name="FraudDetector-Type-TrainingMetrics-metricDataPoints"></a>
The data points details.
Type: Array of [MetricDataPoint](API_MetricDataPoint.md) objects
Required: No

## See Also
<a name="API_TrainingMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/TrainingMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/TrainingMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/TrainingMetrics)
