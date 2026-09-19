---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormMetricConfiguration.html
---

# EvaluationFormMetricConfiguration
<a name="API_EvaluationFormMetricConfiguration"></a>

Information about the metric configuration for an evaluation form question. Use this to associate a business outcome metric with a question.

## Contents
<a name="API_EvaluationFormMetricConfiguration_Contents"></a>

 ** MetricName **   <a name="connect-Type-EvaluationFormMetricConfiguration-MetricName"></a>
The name of the metric. Valid values are:
+  `SALE_SUCCESS` – Sale success.
+  `CSAT` – Customer satisfaction.
+  `CHURN_PROPENSITY` – Churn propensity.
+  `SELF_SERVICE_SUCCESS` – Self-service success.
+  `PARTIAL_SELF_SERVICE_SUCCESS` – Partial self-service success.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[^\p{C}]*$`
Required: Yes

 ** MetricType **   <a name="connect-Type-EvaluationFormMetricConfiguration-MetricType"></a>
The type of metric. Currently, only `BUSINESS_OUTCOME` is supported.
Type: String
Valid Values: `BUSINESS_OUTCOME`
Required: Yes

## See Also
<a name="API_EvaluationFormMetricConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormMetricConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormMetricConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormMetricConfiguration)
