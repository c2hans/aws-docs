---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_NumberPreferenceItem.html
---

# NumberPreferenceItem
<a name="API_NumberPreferenceItem"></a>

A single number preference that specifies how to match available phone numbers. Each preference pairs a match type with one or more filter values.

## Contents
<a name="API_NumberPreferenceItem_Contents"></a>

 ** Filter **   <a name="pinpoint-Type-NumberPreferenceItem-Filter"></a>
The digit pattern values to match against available phone numbers, using the specified preference type.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 2. Maximum length of 16.
Pattern: `\+?[0-9]{1,15}`
Required: Yes

 ** PreferenceType **   <a name="pinpoint-Type-NumberPreferenceItem-PreferenceType"></a>
The type of match to apply to the filter values.
+  `StartsWith`: Returns numbers that begin with the filter value.
+  `EndsWith`: Returns numbers that end with the filter value.
+  `Contains`: Returns numbers that contain the filter value.
+  `ExactMatch`: Returns the number that exactly matches the filter value.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `StartsWith | EndsWith | Contains | ExactMatch`
Required: Yes

## See Also
<a name="API_NumberPreferenceItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/NumberPreferenceItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/NumberPreferenceItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/NumberPreferenceItem)
