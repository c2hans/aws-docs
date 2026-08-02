---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SegmentAttributeValue.html
---

# SegmentAttributeValue
<a name="API_SegmentAttributeValue"></a>

A value for a segment attribute. This is structured as a map where the key is `valueString` and the value is a string.

## Contents
<a name="API_SegmentAttributeValue_Contents"></a>

 ** ValueArn **   <a name="connect-Type-SegmentAttributeValue-ValueArn"></a>
The value of a segment attribute that has to be a valid ARN. This is only supported for system-defined attributes, not for user-defined attributes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ValueInteger **   <a name="connect-Type-SegmentAttributeValue-ValueInteger"></a>
The value of a segment attribute.
Type: Integer
Required: No

 ** ValueList **   <a name="connect-Type-SegmentAttributeValue-ValueList"></a>
The value of a segment attribute. This is only supported for system-defined attributes, not for user-defined attributes.
Type: Array of [SegmentAttributeValue](#API_SegmentAttributeValue) objects
Required: No

 ** ValueMap **   <a name="connect-Type-SegmentAttributeValue-ValueMap"></a>
The value of a segment attribute.
Type: String to [SegmentAttributeValue](#API_SegmentAttributeValue) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** ValueString **   <a name="connect-Type-SegmentAttributeValue-ValueString"></a>
The value of a segment attribute.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_SegmentAttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SegmentAttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SegmentAttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SegmentAttributeValue)
