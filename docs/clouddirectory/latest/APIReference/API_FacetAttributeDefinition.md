---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_FacetAttributeDefinition.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# FacetAttributeDefinition
<a name="API_FacetAttributeDefinition"></a>

A facet attribute definition. See [Attribute References](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html) for more information.

## Contents
<a name="API_FacetAttributeDefinition_Contents"></a>

 ** Type **   <a name="amazoncds-Type-FacetAttributeDefinition-Type"></a>
The type of the attribute.
Type: String
Valid Values: `STRING | BINARY | BOOLEAN | NUMBER | DATETIME | VARIANT`
Required: Yes

 ** DefaultValue **   <a name="amazoncds-Type-FacetAttributeDefinition-DefaultValue"></a>
The default value of the attribute (if configured).
Type: [TypedAttributeValue](API_TypedAttributeValue.md) object
Required: No

 ** IsImmutable **   <a name="amazoncds-Type-FacetAttributeDefinition-IsImmutable"></a>
Whether the attribute is mutable or not.
Type: Boolean
Required: No

 ** Rules **   <a name="amazoncds-Type-FacetAttributeDefinition-Rules"></a>
Validation rules attached to the attribute definition.
Type: String to [Rule](API_Rule.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9._-]*$`
Required: No

## See Also
<a name="API_FacetAttributeDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/FacetAttributeDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/FacetAttributeDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/FacetAttributeDefinition)
