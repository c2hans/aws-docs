---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_TypedAttributeValueRange.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# TypedAttributeValueRange
<a name="API_TypedAttributeValueRange"></a>

A range of attribute values. For more information, see [Range Filters](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_range_filters.html).

## Contents
<a name="API_TypedAttributeValueRange_Contents"></a>

 ** EndMode **   <a name="amazoncds-Type-TypedAttributeValueRange-EndMode"></a>
The inclusive or exclusive range end.
Type: String
Valid Values: `FIRST | LAST | LAST_BEFORE_MISSING_VALUES | INCLUSIVE | EXCLUSIVE`
Required: Yes

 ** StartMode **   <a name="amazoncds-Type-TypedAttributeValueRange-StartMode"></a>
The inclusive or exclusive range start.
Type: String
Valid Values: `FIRST | LAST | LAST_BEFORE_MISSING_VALUES | INCLUSIVE | EXCLUSIVE`
Required: Yes

 ** EndValue **   <a name="amazoncds-Type-TypedAttributeValueRange-EndValue"></a>
The attribute value to terminate the range at.
Type: [TypedAttributeValue](API_TypedAttributeValue.md) object
Required: No

 ** StartValue **   <a name="amazoncds-Type-TypedAttributeValueRange-StartValue"></a>
The value to start the range at.
Type: [TypedAttributeValue](API_TypedAttributeValue.md) object
Required: No

## See Also
<a name="API_TypedAttributeValueRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/TypedAttributeValueRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/TypedAttributeValueRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/TypedAttributeValueRange)
