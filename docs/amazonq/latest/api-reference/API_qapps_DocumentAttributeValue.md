---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DocumentAttributeValue.html
---

# DocumentAttributeValue
<a name="API_qapps_DocumentAttributeValue"></a>

The value of a document attribute. You can only provide one value for a document attribute.

## Contents
<a name="API_qapps_DocumentAttributeValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** dateValue **   <a name="qbusiness-Type-qapps_DocumentAttributeValue-dateValue"></a>
A date expressed as an ISO 8601 string.
It's important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10\+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.
Type: Timestamp
Required: No

 ** longValue **   <a name="qbusiness-Type-qapps_DocumentAttributeValue-longValue"></a>
A long integer value.
Type: Long
Required: No

 ** stringListValue **   <a name="qbusiness-Type-qapps_DocumentAttributeValue-stringListValue"></a>
A list of strings.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** stringValue **   <a name="qbusiness-Type-qapps_DocumentAttributeValue-stringValue"></a>
A string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_qapps_DocumentAttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/DocumentAttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/DocumentAttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/DocumentAttributeValue)
