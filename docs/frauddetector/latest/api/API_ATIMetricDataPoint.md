---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_ATIMetricDataPoint.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# ATIMetricDataPoint
<a name="API_ATIMetricDataPoint"></a>

 The Account Takeover Insights (ATI) model performance metrics data points.

## Contents
<a name="API_ATIMetricDataPoint_Contents"></a>

 ** adr **   <a name="FraudDetector-Type-ATIMetricDataPoint-adr"></a>
 The anomaly discovery rate. This metric quantifies the percentage of anomalies that can be detected by the model at the selected score threshold. A lower score threshold increases the percentage of anomalies captured by the model, but would also require challenging a larger percentage of login events, leading to a higher customer friction.
Type: Float
Required: No

 ** atodr **   <a name="FraudDetector-Type-ATIMetricDataPoint-atodr"></a>
 The account takeover discovery rate. This metric quantifies the percentage of account compromise events that can be detected by the model at the selected score threshold. This metric is only available if 50 or more entities with at-least one labeled account takeover event is present in the ingested dataset.
Type: Float
Required: No

 ** cr **   <a name="FraudDetector-Type-ATIMetricDataPoint-cr"></a>
 The challenge rate. This indicates the percentage of login events that the model recommends to challenge such as one-time password, multi-factor authentication, and investigations.
Type: Float
Required: No

 ** threshold **   <a name="FraudDetector-Type-ATIMetricDataPoint-threshold"></a>
 The model's threshold that specifies an acceptable fraud capture rate. For example, a threshold of 500 means any model score 500 or above is labeled as fraud.
Type: Float
Required: No

## See Also
<a name="API_ATIMetricDataPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/ATIMetricDataPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/ATIMetricDataPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/ATIMetricDataPoint)
