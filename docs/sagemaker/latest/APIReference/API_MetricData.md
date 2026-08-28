---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricData.html
---

# MetricData
<a name="API_MetricData"></a>

The name, value, and date and time of a metric that was emitted to Amazon CloudWatch.

## Contents
<a name="API_MetricData_Contents"></a>

 ** MetricName **   <a name="sagemaker-Type-MetricData-MetricName"></a>
The name of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: No

 ** Timestamp **   <a name="sagemaker-Type-MetricData-Timestamp"></a>
The date and time that the algorithm emitted the metric.
Type: Timestamp
Required: No

 ** Value **   <a name="sagemaker-Type-MetricData-Value"></a>
The value of the metric.
Type: Float
Required: No

## See Also
<a name="API_MetricData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MetricData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MetricData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MetricData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
