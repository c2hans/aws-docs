---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementSearchFilterValue.html
---

# EngagementSearchFilterValue

The value that a leaf condition compares against. Specify one of the following:
+  `StringValue`: A single string, used with `EqualsTo`, `ContainsAny`, and `ContainsAll`.
+  `StringListValue`: A list of strings, used with `ContainsAny` and `ContainsAll`.
+  `DateValue`: A date and time, used with range comparisons on date fields.
+  `LongValue`: A whole number, used with range comparisons on numeric fields.

## Contents
<a name="API_EngagementSearchFilterValue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** DateValue **   <a name="AWSPartnerCentral-Type-EngagementSearchFilterValue-DateValue"></a>
A date-time value in RFC 3339 format, used by the range comparisons on date fields.
Type: Timestamp
Required: No

 ** LongValue **   <a name="AWSPartnerCentral-Type-EngagementSearchFilterValue-LongValue"></a>
An integral numeric value, used by the range comparisons on numeric fields.
Type: Long
Required: No

 ** StringListValue **   <a name="AWSPartnerCentral-Type-EngagementSearchFilterValue-StringListValue"></a>
A list of 1 to 20 string values, used by `ContainsAny` and `ContainsAll`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** StringValue **   <a name="AWSPartnerCentral-Type-EngagementSearchFilterValue-StringValue"></a>
A single string value, used by `EqualsTo`, `ContainsAny`, and `ContainsAll`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_EngagementSearchFilterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementSearchFilterValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementSearchFilterValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementSearchFilterValue)
