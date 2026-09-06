---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_TypedLinkAttributeRange.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# TypedLinkAttributeRange
<a name="API_TypedLinkAttributeRange"></a>

Identifies the range of attributes that are used by a specified filter.

## Contents
<a name="API_TypedLinkAttributeRange_Contents"></a>

 ** Range **   <a name="amazoncds-Type-TypedLinkAttributeRange-Range"></a>
The range of attribute values that are being selected.
Type: [TypedAttributeValueRange](API_TypedAttributeValueRange.md) object
Required: Yes

 ** AttributeName **   <a name="amazoncds-Type-TypedLinkAttributeRange-AttributeName"></a>
The unique name of the typed link attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 230.
Pattern: `^[a-zA-Z0-9._:-]*$`
Required: No

## See Also
<a name="API_TypedLinkAttributeRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/TypedLinkAttributeRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/TypedLinkAttributeRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/TypedLinkAttributeRange)
