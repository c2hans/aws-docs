---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_FilterValue.html
---

# FilterValue

Specifies the value that a filter compares a field against. This structure holds a single comparison value. Set the member that matches the type of the field you're filtering on.

## Contents
<a name="API_FilterValue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** DateValue **   <a name="AWSPartnerCentral-Type-FilterValue-DateValue"></a>
A date and time value, used by the range comparisons on date fields.
Type: Timestamp
Required: No

 ** LongValue **   <a name="AWSPartnerCentral-Type-FilterValue-LongValue"></a>
Reserved for future use.
Type: Long
Required: No

 ** StringListValue **   <a name="AWSPartnerCentral-Type-FilterValue-StringListValue"></a>
A list of 1 to 20 string values, used by `ContainsAny` and `ContainsAll`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** StringValue **   <a name="AWSPartnerCentral-Type-FilterValue-StringValue"></a>
A single string value, used by `EqualsTo`.
Type: String
Required: No

## See Also
<a name="API_FilterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/FilterValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/FilterValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/FilterValue)
