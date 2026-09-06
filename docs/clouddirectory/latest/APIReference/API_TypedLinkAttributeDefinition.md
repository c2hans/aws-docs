---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_TypedLinkAttributeDefinition.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# TypedLinkAttributeDefinition
<a name="API_TypedLinkAttributeDefinition"></a>

A typed link attribute definition.

## Contents
<a name="API_TypedLinkAttributeDefinition_Contents"></a>

 ** Name **   <a name="amazoncds-Type-TypedLinkAttributeDefinition-Name"></a>
The unique name of the typed link attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 230.
Pattern: `^[a-zA-Z0-9._:-]*$`
Required: Yes

 ** RequiredBehavior **   <a name="amazoncds-Type-TypedLinkAttributeDefinition-RequiredBehavior"></a>
The required behavior of the `TypedLinkAttributeDefinition`.
Type: String
Valid Values: `REQUIRED_ALWAYS | NOT_REQUIRED`
Required: Yes

 ** Type **   <a name="amazoncds-Type-TypedLinkAttributeDefinition-Type"></a>
The type of the attribute.
Type: String
Valid Values: `STRING | BINARY | BOOLEAN | NUMBER | DATETIME | VARIANT`
Required: Yes

 ** DefaultValue **   <a name="amazoncds-Type-TypedLinkAttributeDefinition-DefaultValue"></a>
The default value of the attribute (if configured).
Type: [TypedAttributeValue](API_TypedAttributeValue.md) object
Required: No

 ** IsImmutable **   <a name="amazoncds-Type-TypedLinkAttributeDefinition-IsImmutable"></a>
Whether the attribute is mutable or not.
Type: Boolean
Required: No

 ** Rules **   <a name="amazoncds-Type-TypedLinkAttributeDefinition-Rules"></a>
Validation rules that are attached to the attribute definition.
Type: String to [Rule](API_Rule.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9._-]*$`
Required: No

## See Also
<a name="API_TypedLinkAttributeDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/TypedLinkAttributeDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/TypedLinkAttributeDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/TypedLinkAttributeDefinition)
