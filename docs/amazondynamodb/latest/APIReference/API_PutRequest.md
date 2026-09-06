---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutRequest.html
---

# PutRequest
<a name="API_PutRequest"></a>

Represents a request to perform a `PutItem` operation on an item.

## Contents
<a name="API_PutRequest_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Item **   <a name="DDB-Type-PutRequest-Item"></a>
A map of attribute name to attribute values, representing the primary key of an item to be processed by `PutItem`. All of the table's primary key attributes must be specified, and their data types must match those of the table's key schema. If any attributes are present in the item that are part of an index key schema for the table, their types must match the index key schema.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: Yes

## See Also
<a name="API_PutRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/PutRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/PutRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/PutRequest)
