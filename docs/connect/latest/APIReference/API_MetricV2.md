---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MetricV2.html
---

# MetricV2
<a name="API_MetricV2"></a>

Contains information about the metric.

**Important**
Only one of either the Name or MetricId is required.

## Contents
<a name="API_MetricV2_Contents"></a>

 ** MetricFilters **   <a name="connect-Type-MetricV2-MetricFilters"></a>
Contains the filters to be used when returning data.
Type: Array of [MetricFilterV2](API_MetricFilterV2.md) objects
Array Members: Maximum number of 2 items.
Required: No

 ** MetricId **   <a name="connect-Type-MetricV2-MetricId"></a>
Historical metrics or custom metrics can be referenced via this field. This field is a valid Connect Customer Arn or a UUID
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: No

 ** Name **   <a name="connect-Type-MetricV2-Name"></a>
The name of the metric.
Type: String
Required: No

 ** Threshold **   <a name="connect-Type-MetricV2-Threshold"></a>
Contains information about the threshold for service level metrics.
Type: Array of [ThresholdV2](API_ThresholdV2.md) objects
Array Members: Maximum number of 1 item.
Required: No

## See Also
<a name="API_MetricV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MetricV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MetricV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MetricV2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
