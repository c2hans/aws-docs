---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_TypedAttributeValueRange.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
