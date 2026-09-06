---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactSearchSummarySegmentAttributeValue.html
---

# ContactSearchSummarySegmentAttributeValue
<a name="API_ContactSearchSummarySegmentAttributeValue"></a>

The value of a segment attribute. This is structured as a map with a single key-value pair. The key 'valueString' indicates that the attribute type is a string, and its corresponding value is the actual string value of the segment attribute.

## Contents
<a name="API_ContactSearchSummarySegmentAttributeValue_Contents"></a>

 ** ValueMap **   <a name="connect-Type-ContactSearchSummarySegmentAttributeValue-ValueMap"></a>
The key and value of a segment attribute.
Type: String to [SegmentAttributeValue](API_SegmentAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** ValueString **   <a name="connect-Type-ContactSearchSummarySegmentAttributeValue-ValueString"></a>
The value of a segment attribute represented as a string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ContactSearchSummarySegmentAttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactSearchSummarySegmentAttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactSearchSummarySegmentAttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactSearchSummarySegmentAttributeValue)
