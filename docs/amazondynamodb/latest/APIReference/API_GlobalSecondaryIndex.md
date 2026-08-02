---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalSecondaryIndex.html
---

# GlobalSecondaryIndex
<a name="API_GlobalSecondaryIndex"></a>

Represents the properties of a global secondary index.

## Contents
<a name="API_GlobalSecondaryIndex_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IndexName **   <a name="DDB-Type-GlobalSecondaryIndex-IndexName"></a>
The name of the global secondary index. The name must be unique among all other indexes on this table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** KeySchema **   <a name="DDB-Type-GlobalSecondaryIndex-KeySchema"></a>
The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:
+  `HASH` - partition key
+  `RANGE` - sort key
The partition key of an item is also known as its *hash attribute*. The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its *range attribute*. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.
Type: Array of [KeySchemaElement](API_KeySchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** Projection **   <a name="DDB-Type-GlobalSecondaryIndex-Projection"></a>
Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.
Type: [Projection](API_Projection.md) object
Required: Yes

 ** OnDemandThroughput **   <a name="DDB-Type-GlobalSecondaryIndex-OnDemandThroughput"></a>
The maximum number of read and write units for the specified global secondary index. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both. You must use either `OnDemandThroughput` or `ProvisionedThroughput` based on your table's capacity mode.
Type: [OnDemandThroughput](API_OnDemandThroughput.md) object
Required: No

 ** ProvisionedThroughput **   <a name="DDB-Type-GlobalSecondaryIndex-ProvisionedThroughput"></a>
Represents the provisioned throughput settings for the specified global secondary index. You must use either `OnDemandThroughput` or `ProvisionedThroughput` based on your table's capacity mode.
For current minimum and maximum provisioned throughput values, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide*.
Type: [ProvisionedThroughput](API_ProvisionedThroughput.md) object
Required: No

 ** WarmThroughput **   <a name="DDB-Type-GlobalSecondaryIndex-WarmThroughput"></a>
Represents the warm throughput value (in read units per second and write units per second) for the specified secondary index. If you use this parameter, you must specify `ReadUnitsPerSecond`, `WriteUnitsPerSecond`, or both.
Type: [WarmThroughput](API_WarmThroughput.md) object
Required: No

## See Also
<a name="API_GlobalSecondaryIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/GlobalSecondaryIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/GlobalSecondaryIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/GlobalSecondaryIndex)
