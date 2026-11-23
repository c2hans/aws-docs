---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunitySearchFilterValue.html
---

# OpportunitySearchFilterValue

Contains the value that a search predicate compares against. Specify exactly one member. The member you choose must match the field type and the comparison operator of the predicate.

## Contents
<a name="API_OpportunitySearchFilterValue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** DateValue **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilterValue-DateValue"></a>
A date-time value in RFC 3339 format, used by the range comparisons on date fields.
Type: Timestamp
Required: No

 ** DoubleValue **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilterValue-DoubleValue"></a>
A fractional numeric value, used by the range comparisons on numeric amount fields such as `EstimatedMrr`.
Type: Double
Required: No

 ** LongValue **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilterValue-LongValue"></a>
An integral numeric value, used by the range comparisons on integral numeric fields.
Type: Long
Required: No

 ** StringListValue **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilterValue-StringListValue"></a>
A list of string values. Used by `ContainsAny` or `ContainsAll` to match against multiple values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** StringValue **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilterValue-StringValue"></a>
A single string value. Used by `EqualsTo`, and by `ContainsAny` or `ContainsAll` for a single-value match.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_OpportunitySearchFilterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunitySearchFilterValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunitySearchFilterValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunitySearchFilterValue)
