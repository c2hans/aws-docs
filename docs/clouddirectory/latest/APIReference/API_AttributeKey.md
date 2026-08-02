---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_AttributeKey.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# AttributeKey
<a name="API_AttributeKey"></a>

A unique identifier for an attribute.

## Contents
<a name="API_AttributeKey_Contents"></a>

 ** FacetName **   <a name="amazoncds-Type-AttributeKey-FacetName"></a>
The name of the facet that the attribute exists within.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: Yes

 ** Name **   <a name="amazoncds-Type-AttributeKey-Name"></a>
The name of the attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 230.
Pattern: `^[a-zA-Z0-9._:-]*$`
Required: Yes

 ** SchemaArn **   <a name="amazoncds-Type-AttributeKey-SchemaArn"></a>
The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
Type: String
Required: Yes

## See Also
<a name="API_AttributeKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/AttributeKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/AttributeKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/AttributeKey)
