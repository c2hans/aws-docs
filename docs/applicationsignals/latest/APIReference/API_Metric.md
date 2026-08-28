---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Metric.html
---

# Metric
<a name="API_Metric"></a>

This structure defines the metric used for a service level indicator, including the metric name, namespace, and dimensions

## Contents
<a name="API_Metric_Contents"></a>

 ** Dimensions **   <a name="applicationsignals-Type-Metric-Dimensions"></a>
An array of one or more dimensions to use to define the metric that you want to use. For more information, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension).
Type: Array of [Dimension](API_Dimension.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

 ** MetricName **   <a name="applicationsignals-Type-Metric-MetricName"></a>
The name of the metric to use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Namespace **   <a name="applicationsignals-Type-Metric-Namespace"></a>
The namespace of the metric. For more information, see [Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*[^:].*`
Required: No

## See Also
<a name="API_Metric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/Metric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/Metric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/Metric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
