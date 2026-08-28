---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AggregationType.html
---

# AggregationType
<a name="API_AggregationType"></a>

The type of aggregation queries.

## Contents
<a name="API_AggregationType_Contents"></a>

 ** name **   <a name="iot-Type-AggregationType-name"></a>
The name of the aggregation type.
Type: String
Valid Values: `Statistics | Percentiles | Cardinality`
Required: Yes

 ** values **   <a name="iot-Type-AggregationType-values"></a>
A list of the values of aggregation types.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[a-zA-Z0-9]+`
Required: No

## See Also
<a name="API_AggregationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AggregationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AggregationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AggregationType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
