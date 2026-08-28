---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ResponseResourceMetric.html
---

# ResponseResourceMetric
<a name="API_ResponseResourceMetric"></a>

An object that contains the full name, description, and unit of a metric.

## Contents
<a name="API_ResponseResourceMetric_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Description **   <a name="performanceinsights-Type-ResponseResourceMetric-Description"></a>
The description of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Metric **   <a name="performanceinsights-Type-ResponseResourceMetric-Metric"></a>
The full name of the metric.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** Unit **   <a name="performanceinsights-Type-ResponseResourceMetric-Unit"></a>
The unit of the metric.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ResponseResourceMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/ResponseResourceMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/ResponseResourceMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/ResponseResourceMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Performance Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query performance-insights` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
