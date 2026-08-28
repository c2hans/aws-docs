---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_MeasureValue.html
---

# MeasureValue
<a name="API_MeasureValue"></a>

 Represents the data attribute of the time series. For example, the CPU utilization of an EC2 instance or the RPM of a wind turbine are measures. MeasureValue has both name and value.

 MeasureValue is only allowed for type `MULTI`. Using `MULTI` type, you can pass multiple data attributes associated with the same time series in a single record

## Contents
<a name="API_MeasureValue_Contents"></a>

 ** Name **   <a name="timestream-Type-MeasureValue-Name"></a>
 The name of the MeasureValue.
 For constraints on MeasureValue names, see [ Naming Constraints](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html#limits.naming) in the Amazon Timestream Developer Guide.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** Type **   <a name="timestream-Type-MeasureValue-Type"></a>
Contains the data type of the MeasureValue for the time-series data point.
Type: String
Valid Values: `DOUBLE | BIGINT | VARCHAR | BOOLEAN | TIMESTAMP | MULTI`
Required: Yes

 ** Value **   <a name="timestream-Type-MeasureValue-Value"></a>
 The value for the MeasureValue. For information, see [Data types](https://docs.aws.amazon.com/timestream/latest/developerguide/writes.html#writes.data-types).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_MeasureValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/MeasureValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/MeasureValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/MeasureValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
