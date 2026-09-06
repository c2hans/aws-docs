---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrialComponentMetricSummary.html
---

# TrialComponentMetricSummary
<a name="API_TrialComponentMetricSummary"></a>

A summary of the metrics of a trial component.

## Contents
<a name="API_TrialComponentMetricSummary_Contents"></a>

 ** Avg **   <a name="sagemaker-Type-TrialComponentMetricSummary-Avg"></a>
The average value of the metric.
Type: Double
Required: No

 ** Count **   <a name="sagemaker-Type-TrialComponentMetricSummary-Count"></a>
The number of samples used to generate the metric.
Type: Integer
Required: No

 ** Last **   <a name="sagemaker-Type-TrialComponentMetricSummary-Last"></a>
The most recent value of the metric.
Type: Double
Required: No

 ** Max **   <a name="sagemaker-Type-TrialComponentMetricSummary-Max"></a>
The maximum value of the metric.
Type: Double
Required: No

 ** MetricName **   <a name="sagemaker-Type-TrialComponentMetricSummary-MetricName"></a>
The name of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: No

 ** Min **   <a name="sagemaker-Type-TrialComponentMetricSummary-Min"></a>
The minimum value of the metric.
Type: Double
Required: No

 ** SourceArn **   <a name="sagemaker-Type-TrialComponentMetricSummary-SourceArn"></a>
The Amazon Resource Name (ARN) of the source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:.*`
Required: No

 ** StdDev **   <a name="sagemaker-Type-TrialComponentMetricSummary-StdDev"></a>
The standard deviation of the metric.
Type: Double
Required: No

 ** TimeStamp **   <a name="sagemaker-Type-TrialComponentMetricSummary-TimeStamp"></a>
When the metric was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_TrialComponentMetricSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrialComponentMetricSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrialComponentMetricSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrialComponentMetricSummary)
