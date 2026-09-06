---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_LocalSecondaryIndex.html
---

# LocalSecondaryIndex
<a name="API_LocalSecondaryIndex"></a>

Represents the properties of a local secondary index.

## Contents
<a name="API_LocalSecondaryIndex_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IndexName **   <a name="DDB-Type-LocalSecondaryIndex-IndexName"></a>
The name of the local secondary index. The name must be unique among all other indexes on this table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** KeySchema **   <a name="DDB-Type-LocalSecondaryIndex-KeySchema"></a>
The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:
+  `HASH` - partition key
+  `RANGE` - sort key
The partition key of an item is also known as its *hash attribute*. The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its *range attribute*. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.
Type: Array of [KeySchemaElement](API_KeySchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** Projection **   <a name="DDB-Type-LocalSecondaryIndex-Projection"></a>
Represents attributes that are copied (projected) from the table into the local secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.
Type: [Projection](API_Projection.md) object
Required: Yes

## See Also
<a name="API_LocalSecondaryIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/LocalSecondaryIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/LocalSecondaryIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/LocalSecondaryIndex)
