---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_Dimension.html
---

# Dimension
<a name="API_Dimension"></a>

Represents the metadata attributes of the time series. For example, the name and Availability Zone of an EC2 instance or the name of the manufacturer of a wind turbine are dimensions.

## Contents
<a name="API_Dimension_Contents"></a>

 ** Name **   <a name="timestream-Type-Dimension-Name"></a>
 Dimension represents the metadata attributes of the time series. For example, the name and Availability Zone of an EC2 instance or the name of the manufacturer of a wind turbine are dimensions.
For constraints on dimension names, see [Naming Constraints](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html#limits.naming).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Required: Yes

 ** Value **   <a name="timestream-Type-Dimension-Value"></a>
The value of the dimension.
Type: String
Required: Yes

 ** DimensionValueType **   <a name="timestream-Type-Dimension-DimensionValueType"></a>
The data type of the dimension for the time-series data point.
Type: String
Valid Values: `VARCHAR`
Required: No

## See Also
<a name="API_Dimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/Dimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/Dimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/Dimension)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
