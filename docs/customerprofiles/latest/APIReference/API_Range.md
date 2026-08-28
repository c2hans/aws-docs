---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_Range.html
---

# Range
<a name="API_connect-customer-profiles_Range"></a>

The relative time period over which data is included in the aggregation.

## Contents
<a name="API_connect-customer-profiles_Range_Contents"></a>

 ** TimestampFormat **   <a name="connect-Type-connect-customer-profiles_Range-TimestampFormat"></a>
The format the timestamp field in your JSON object is specified. This value should be one of EPOCHMILLI (for Unix epoch timestamps with second/millisecond level precision) or ISO\_8601 (following ISO\_8601 format with second/millisecond level precision, with an optional offset of Z or in the format HH:MM or HHMM.). E.g. if your object type is MyType and source JSON is {"generatedAt": {"timestamp": "2001-07-04T12:08:56.235-0700"}}, then TimestampFormat should be "ISO\_8601".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** TimestampSource **   <a name="connect-Type-connect-customer-profiles_Range-TimestampSource"></a>
An expression specifying the field in your JSON object from which the date should be parsed. The expression should follow the structure of \\"{ObjectTypeName.<Location of timestamp field in JSON pointer format>}\\". E.g. if your object type is MyType and source JSON is {"generatedAt": {"timestamp": "1737587945945"}}, then TimestampSource should be "{MyType.generatedAt.timestamp}".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Unit **   <a name="connect-Type-connect-customer-profiles_Range-Unit"></a>
The unit of time.
Type: String
Valid Values: `DAYS`
Required: No

 ** Value **   <a name="connect-Type-connect-customer-profiles_Range-Value"></a>
The amount of time of the specified unit.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** ValueRange **   <a name="connect-Type-connect-customer-profiles_Range-ValueRange"></a>
A structure letting customers specify a relative time window over which over which data is included in the Calculated Attribute. Use positive numbers to indicate that the endpoint is in the past, and negative numbers to indicate it is in the future. ValueRange overrides Value.
Type: [ValueRange](API_connect-customer-profiles_ValueRange.md) object
Required: No

## See Also
<a name="API_connect-customer-profiles_Range_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/Range)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/Range)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/Range)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
