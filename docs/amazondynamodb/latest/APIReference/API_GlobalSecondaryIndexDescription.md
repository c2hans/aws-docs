---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalSecondaryIndexDescription.html
---

# GlobalSecondaryIndexDescription
<a name="API_GlobalSecondaryIndexDescription"></a>

Represents the properties of a global secondary index.

## Contents
<a name="API_GlobalSecondaryIndexDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Backfilling **   <a name="DDB-Type-GlobalSecondaryIndexDescription-Backfilling"></a>
Indicates whether the index is currently backfilling. *Backfilling* is the process of reading items from the table and determining whether they can be added to the index. (Not all items will qualify: For example, a partition key cannot have any duplicate values.) If an item can be added to the index, DynamoDB will do so. After all items have been processed, the backfilling operation is complete and `Backfilling` is false.
You can delete an index that is being created during the `Backfilling` phase when `IndexStatus` is set to CREATING and `Backfilling` is true. You can't delete the index that is being created when `IndexStatus` is set to CREATING and `Backfilling` is false.
For indexes that were created during a `CreateTable` operation, the `Backfilling` attribute does not appear in the `DescribeTable` output.
Type: Boolean
Required: No

 ** IndexArn **   <a name="DDB-Type-GlobalSecondaryIndexDescription-IndexArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the index.
Type: String
Required: No

 ** IndexName **   <a name="DDB-Type-GlobalSecondaryIndexDescription-IndexName"></a>
The name of the global secondary index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** IndexSizeBytes **   <a name="DDB-Type-GlobalSecondaryIndexDescription-IndexSizeBytes"></a>
The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
Type: Long
Required: No

 ** IndexStatus **   <a name="DDB-Type-GlobalSecondaryIndexDescription-IndexStatus"></a>
The current state of the global secondary index:
+  `CREATING` - The index is being created.
+  `UPDATING` - The index is being updated.
+  `DELETING` - The index is being deleted.
+  `ACTIVE` - The index is ready for use.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE`
Required: No

 ** ItemCount **   <a name="DDB-Type-GlobalSecondaryIndexDescription-ItemCount"></a>
The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
Type: Long
Required: No

 ** KeySchema **   <a name="DDB-Type-GlobalSecondaryIndexDescription-KeySchema"></a>
The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:
+  `HASH` - partition key
+  `RANGE` - sort key
The partition key of an item is also known as its *hash attribute*. The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its *range attribute*. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.
Type: Array of [KeySchemaElement](API_KeySchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** OnDemandThroughput **   <a name="DDB-Type-GlobalSecondaryIndexDescription-OnDemandThroughput"></a>
The maximum number of read and write units for the specified global secondary index. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both.
Type: [OnDemandThroughput](API_OnDemandThroughput.md) object
Required: No

 ** Projection **   <a name="DDB-Type-GlobalSecondaryIndexDescription-Projection"></a>
Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.
Type: [Projection](API_Projection.md) object
Required: No

 ** ProvisionedThroughput **   <a name="DDB-Type-GlobalSecondaryIndexDescription-ProvisionedThroughput"></a>
Represents the provisioned throughput settings for the specified global secondary index.
For current minimum and maximum provisioned throughput values, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide*.
Type: [ProvisionedThroughputDescription](API_ProvisionedThroughputDescription.md) object
Required: No

 ** WarmThroughput **   <a name="DDB-Type-GlobalSecondaryIndexDescription-WarmThroughput"></a>
Represents the warm throughput value (in read units per second and write units per second) for the specified secondary index.
Type: [GlobalSecondaryIndexWarmThroughputDescription](API_GlobalSecondaryIndexWarmThroughputDescription.md) object
Required: No

## See Also
<a name="API_GlobalSecondaryIndexDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/GlobalSecondaryIndexDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/GlobalSecondaryIndexDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/GlobalSecondaryIndexDescription)
