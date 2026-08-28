---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_MetricDimension.html
---

# MetricDimension
<a name="API_MetricDimension"></a>

The dimension of a metric.

## Contents
<a name="API_MetricDimension_Contents"></a>

 ** dimensionName **   <a name="iot-Type-MetricDimension-dimensionName"></a>
A unique identifier for the dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

 ** operator **   <a name="iot-Type-MetricDimension-operator"></a>
Defines how the `dimensionValues` of a dimension are interpreted. For example, for dimension type TOPIC\_FILTER, the `IN` operator, a message will be counted only if its topic matches one of the topic filters. With `NOT_IN` operator, a message will be counted only if it doesn't match any of the topic filters. The operator is optional: if it's not provided (is `null`), it will be interpreted as `IN`.
Type: String
Valid Values: `IN | NOT_IN`
Required: No

## See Also
<a name="API_MetricDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/MetricDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/MetricDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/MetricDimension)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
