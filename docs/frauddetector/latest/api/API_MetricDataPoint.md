---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_MetricDataPoint.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# MetricDataPoint
<a name="API_MetricDataPoint"></a>

Model performance metrics data points.

## Contents
<a name="API_MetricDataPoint_Contents"></a>

 ** fpr **   <a name="FraudDetector-Type-MetricDataPoint-fpr"></a>
The false positive rate. This is the percentage of total legitimate events that are incorrectly predicted as fraud.
Type: Float
Required: No

 ** precision **   <a name="FraudDetector-Type-MetricDataPoint-precision"></a>
The percentage of fraud events correctly predicted as fraudulent as compared to all events predicted as fraudulent.
Type: Float
Required: No

 ** threshold **   <a name="FraudDetector-Type-MetricDataPoint-threshold"></a>
The model threshold that specifies an acceptable fraud capture rate. For example, a threshold of 500 means any model score 500 or above is labeled as fraud.
Type: Float
Required: No

 ** tpr **   <a name="FraudDetector-Type-MetricDataPoint-tpr"></a>
The true positive rate. This is the percentage of total fraud the model detects. Also known as capture rate.
Type: Float
Required: No

## See Also
<a name="API_MetricDataPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/MetricDataPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/MetricDataPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/MetricDataPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
