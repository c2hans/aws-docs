---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteRequest.html
---

# DeleteRequest
<a name="API_DeleteRequest"></a>

Represents a request to perform a `DeleteItem` operation on an item.

## Contents
<a name="API_DeleteRequest_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="DDB-Type-DeleteRequest-Key"></a>
A map of attribute name to attribute values, representing the primary key of the item to delete. All of the table's primary key attributes must be specified, and their data types must match those of the table's key schema.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: Yes

## See Also
<a name="API_DeleteRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DeleteRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DeleteRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DeleteRequest)
