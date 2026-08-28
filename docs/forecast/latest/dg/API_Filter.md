---
source_url: https://docs.aws.amazon.com/forecast/latest/dg/API_Filter.html
---

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# Filter
<a name="API_Filter"></a>

Describes a filter for choosing a subset of objects. Each filter consists of a condition and a match statement. The condition is either `IS` or `IS_NOT`, which specifies whether to include or exclude the objects that match the statement, respectively. The match statement consists of a key and a value.

## Contents
<a name="API_Filter_Contents"></a>

 ** Condition **   <a name="forecast-Type-Filter-Condition"></a>
The condition to apply. To include the objects that match the statement, specify `IS`. To exclude matching objects, specify `IS_NOT`.
Type: String
Valid Values: `IS | IS_NOT`
Required: Yes

 ** Key **   <a name="forecast-Type-Filter-Key"></a>
The name of the parameter to filter on.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[a-zA-Z0-9\_]+$`
Required: Yes

 ** Value **   <a name="forecast-Type-Filter-Value"></a>
The value to match.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Forecast. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query forecast` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
