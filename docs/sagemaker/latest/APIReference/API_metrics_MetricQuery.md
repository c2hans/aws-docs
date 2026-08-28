---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_metrics_MetricQuery.html
---

# MetricQuery
<a name="API_metrics_MetricQuery"></a>

Specifies a query to retrieve training metrics from SageMaker.

## Contents
<a name="API_metrics_MetricQuery_Contents"></a>

 ** MetricName **   <a name="sagemaker-Type-metrics_MetricQuery-MetricName"></a>
The name of the metric to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

 ** MetricStat **   <a name="sagemaker-Type-metrics_MetricQuery-MetricStat"></a>
The metrics stat type of metrics to retrieve.
Type: String
Valid Values: `Min | Max | Avg | Count | StdDev | Last`
Required: Yes

 ** Period **   <a name="sagemaker-Type-metrics_MetricQuery-Period"></a>
The time period of metrics to retrieve.
Type: String
Valid Values: `OneMinute | FiveMinute | OneHour | IterationNumber`
Required: Yes

 ** ResourceArn **   <a name="sagemaker-Type-metrics_MetricQuery-ResourceArn"></a>
The ARN of the SageMaker resource to retrieve metrics for.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-].*/.*`
Required: Yes

 ** XAxisType **   <a name="sagemaker-Type-metrics_MetricQuery-XAxisType"></a>
The x-axis type of metrics to retrieve.
Type: String
Valid Values: `IterationNumber | Timestamp`
Required: Yes

 ** End **   <a name="sagemaker-Type-metrics_MetricQuery-End"></a>
The end time of metrics to retrieve.
Type: Long
Required: No

 ** Start **   <a name="sagemaker-Type-metrics_MetricQuery-Start"></a>
The start time of metrics to retrieve.
Type: Long
Required: No

## See Also
<a name="API_metrics_MetricQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-metrics-2022-09-30/MetricQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-metrics-2022-09-30/MetricQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-metrics-2022-09-30/MetricQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
