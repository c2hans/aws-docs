---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_ParameterMapping.html
---

# ParameterMapping
<a name="API_query_ParameterMapping"></a>

Mapping for named parameters.

## Contents
<a name="API_query_ParameterMapping_Contents"></a>

 ** Name **   <a name="timestream-Type-query_ParameterMapping-Name"></a>
Parameter name.
Type: String
Required: Yes

 ** Type **   <a name="timestream-Type-query_ParameterMapping-Type"></a>
Contains the data type of a column in a query result set. The data type can be scalar or complex. The supported scalar data types are integers, Boolean, string, double, timestamp, date, time, and intervals. The supported complex data types are arrays, rows, and timeseries.
Type: [Type](API_query_Type.md) object
Required: Yes

## See Also
<a name="API_query_ParameterMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/ParameterMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/ParameterMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/ParameterMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
