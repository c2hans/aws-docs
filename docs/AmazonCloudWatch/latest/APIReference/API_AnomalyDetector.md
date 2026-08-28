---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AnomalyDetector.html
---

# AnomalyDetector
<a name="API_AnomalyDetector"></a>

An anomaly detection model associated with a particular CloudWatch metric, statistic, or metric math expression. You can use the model to display a band of expected, normal values when the metric is graphed.

If you have enabled unified cross-account observability, and this account is a monitoring account, the metric can be in the same account or a source account.

## Contents
<a name="API_AnomalyDetector_Contents"></a>

 ** AnomalyDetectorId **   <a name="ACW-Type-AnomalyDetector-AnomalyDetectorId"></a>
The unique identifier of the anomaly detector.
The identifier does not restrict access to a specific anomaly detector in an IAM policy. Permissions for anomaly detector operations apply to all anomaly detectors in the account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_./:%()+-]+`
Required: No

 ** Configuration **   <a name="ACW-Type-AnomalyDetector-Configuration"></a>
The configuration specifies details about how the anomaly detection model is to be trained, including time ranges to exclude from use for training the model, and the time zone to use for the metric.
Type: [AnomalyDetectorConfiguration](API_AnomalyDetectorConfiguration.md) object
Required: No

 ** Dimensions **   <a name="ACW-Type-AnomalyDetector-Dimensions"></a>
 *This member has been deprecated.*
The metric dimensions associated with the anomaly detection model.
Type: Array of [Dimension](API_Dimension.md) objects
Array Members: Maximum number of 30 items.
Required: No

 ** MetricCharacteristics **   <a name="ACW-Type-AnomalyDetector-MetricCharacteristics"></a>
This object includes parameters that you can use to provide information about your metric to CloudWatch to help it build more accurate anomaly detection models. Currently, it includes the `PeriodicSpikes` parameter.
Type: [MetricCharacteristics](API_MetricCharacteristics.md) object
Required: No

 ** MetricMathAnomalyDetector **   <a name="ACW-Type-AnomalyDetector-MetricMathAnomalyDetector"></a>
The CloudWatch metric math expression for this anomaly detector.
Type: [MetricMathAnomalyDetector](API_MetricMathAnomalyDetector.md) object
Required: No

 ** MetricName **   <a name="ACW-Type-AnomalyDetector-MetricName"></a>
 *This member has been deprecated.*
The name of the metric associated with the anomaly detection model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Namespace **   <a name="ACW-Type-AnomalyDetector-Namespace"></a>
 *This member has been deprecated.*
The namespace of the metric associated with the anomaly detection model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^:].*`
Required: No

 ** SingleMetricAnomalyDetector **   <a name="ACW-Type-AnomalyDetector-SingleMetricAnomalyDetector"></a>
The CloudWatch metric and statistic for this anomaly detector.
Type: [SingleMetricAnomalyDetector](API_SingleMetricAnomalyDetector.md) object
Required: No

 ** Stat **   <a name="ACW-Type-AnomalyDetector-Stat"></a>
 *This member has been deprecated.*
The statistic associated with the anomaly detection model.
Type: String
Length Constraints: Maximum length of 50.
Pattern: `(SampleCount|Average|Sum|Minimum|Maximum|IQM|(p|tc|tm|ts|wm)(\d{1,2}(\.\d{0,10})?|100)|[ou]\d+(\.\d*)?)(_E|_L|_H)?|(TM|TC|TS|WM)\(((((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%)?:((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%|((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%:(((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%)?)\)|(TM|TC|TS|WM|PR)\(((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)):((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))?|((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))?:(\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))\)`
Required: No

 ** StateValue **   <a name="ACW-Type-AnomalyDetector-StateValue"></a>
The current status of the anomaly detector's training.
Type: String
Valid Values: `PENDING_TRAINING | TRAINED_INSUFFICIENT_DATA | TRAINED`
Required: No

## See Also
<a name="API_AnomalyDetector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/AnomalyDetector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/AnomalyDetector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/AnomalyDetector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
