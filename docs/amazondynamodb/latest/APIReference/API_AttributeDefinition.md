---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AttributeDefinition.html
---

# AttributeDefinition
<a name="API_AttributeDefinition"></a>

Represents an attribute for describing the schema for the table and indexes.

## Contents
<a name="API_AttributeDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AttributeName **   <a name="DDB-Type-AttributeDefinition-AttributeName"></a>
A name for the attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** AttributeType **   <a name="DDB-Type-AttributeDefinition-AttributeType"></a>
The data type for the attribute, where:
+  `S` - the attribute is of type String
+  `N` - the attribute is of type Number
+  `B` - the attribute is of type Binary
Type: String
Valid Values: `S | N | B`
Required: Yes

## See Also
<a name="API_AttributeDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/AttributeDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/AttributeDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/AttributeDefinition)
