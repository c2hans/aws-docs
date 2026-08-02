---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchCreateObject.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchCreateObject
<a name="API_BatchCreateObject"></a>

Represents the output of a [CreateObject](API_CreateObject.md) operation.

## Contents
<a name="API_BatchCreateObject_Contents"></a>

 ** ObjectAttributeList **   <a name="amazoncds-Type-BatchCreateObject-ObjectAttributeList"></a>
An attribute map, which contains an attribute ARN as the key and attribute value as the map value.
Type: Array of [AttributeKeyAndValue](API_AttributeKeyAndValue.md) objects
Required: Yes

 ** SchemaFacet **   <a name="amazoncds-Type-BatchCreateObject-SchemaFacet"></a>
A list of `FacetArns` that will be associated with the object. For more information, see [Arn Examples](arns.md).
Type: Array of [SchemaFacet](API_SchemaFacet.md) objects
Required: Yes

 ** BatchReferenceName **   <a name="amazoncds-Type-BatchCreateObject-BatchReferenceName"></a>
The batch reference name. See [Transaction Support](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html) for more information.
Type: String
Required: No

 ** LinkName **   <a name="amazoncds-Type-BatchCreateObject-LinkName"></a>
The name of the link.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\/\[\]\(\):\{\}#@!?\s\\;]+`
Required: No

 ** ParentReference **   <a name="amazoncds-Type-BatchCreateObject-ParentReference"></a>
If specified, the parent reference to which this object will be attached.
Type: [ObjectReference](API_ObjectReference.md) object
Required: No

## See Also
<a name="API_BatchCreateObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchCreateObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchCreateObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchCreateObject)
