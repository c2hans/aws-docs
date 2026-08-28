---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TableDescription.html
---

# TableDescription
<a name="API_TableDescription"></a>

Represents the properties of a table.

## Contents
<a name="API_TableDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ArchivalSummary **   <a name="DDB-Type-TableDescription-ArchivalSummary"></a>
Contains information about the table archive.
Type: [ArchivalSummary](API_ArchivalSummary.md) object
Required: No

 ** AttributeDefinitions **   <a name="DDB-Type-TableDescription-AttributeDefinitions"></a>
An array of `AttributeDefinition` objects. Each of these objects describes one attribute in the table and index key schema.
Each `AttributeDefinition` object in this array is composed of:
+  `AttributeName` - The name of the attribute.
+  `AttributeType` - The data type for the attribute.
Type: Array of [AttributeDefinition](API_AttributeDefinition.md) objects
Required: No

 ** BillingModeSummary **   <a name="DDB-Type-TableDescription-BillingModeSummary"></a>
Contains the details for the read/write capacity mode.
Type: [BillingModeSummary](API_BillingModeSummary.md) object
Required: No

 ** CreationDateTime **   <a name="DDB-Type-TableDescription-CreationDateTime"></a>
The date and time when the table was created, in [UNIX epoch time](http://www.epochconverter.com/) format.
Type: Timestamp
Required: No

 ** DeletionProtectionEnabled **   <a name="DDB-Type-TableDescription-DeletionProtectionEnabled"></a>
Indicates whether deletion protection is enabled (true) or disabled (false) on the table.
Type: Boolean
Required: No

 ** GlobalSecondaryIndexes **   <a name="DDB-Type-TableDescription-GlobalSecondaryIndexes"></a>
The global secondary indexes, if any, on the table. Each index is scoped to a given partition key value. Each element is composed of:
+  `Backfilling` - If true, then the index is currently in the backfilling phase. Backfilling occurs only when a new global secondary index is added to the table. It is the process by which DynamoDB populates the new index with data from the table. (This attribute does not appear for indexes that were created during a `CreateTable` operation.)

   You can delete an index that is being created during the `Backfilling` phase when `IndexStatus` is set to CREATING and `Backfilling` is true. You can't delete the index that is being created when `IndexStatus` is set to CREATING and `Backfilling` is false. (This attribute does not appear for indexes that were created during a `CreateTable` operation.)
+  `IndexName` - The name of the global secondary index.
+  `IndexSizeBytes` - The total size of the global secondary index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
+  `IndexStatus` - The current status of the global secondary index:
  +  `CREATING` - The index is being created.
  +  `UPDATING` - The index is being updated.
  +  `DELETING` - The index is being deleted.
  +  `ACTIVE` - The index is ready for use.
+  `ItemCount` - The number of items in the global secondary index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
+  `KeySchema` - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
+  `Projection` - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
  +  `ProjectionType` - One of the following:
    +  `KEYS_ONLY` - Only the index and primary keys are projected into the index.
    +  `INCLUDE` - In addition to the attributes described in `KEYS_ONLY`, the secondary index will include other non-key attributes that you specify.
    +  `ALL` - All of the table attributes are projected into the index.
  +  `NonKeyAttributes` - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in `NonKeyAttributes`, summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of `INCLUDE`. You still can specify the ProjectionType of `ALL` to project all attributes from the source table, even if the table has more than 100 attributes.
+  `ProvisionedThroughput` - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units, along with data about increases and decreases.
If the table is in the `DELETING` state, no information about indexes will be returned.
Type: Array of [GlobalSecondaryIndexDescription](API_GlobalSecondaryIndexDescription.md) objects
Required: No

 ** GlobalTableSettingsReplicationMode **   <a name="DDB-Type-TableDescription-GlobalTableSettingsReplicationMode"></a>
Indicates one of the settings synchronization modes for the global table:
+  `ENABLED`: Indicates that the settings synchronization mode for the global table is enabled.
+  `DISABLED`: Indicates that the settings synchronization mode for the global table is disabled.
+  `ENABLED_WITH_OVERRIDES`: This mode is set by default for a same account global table. Indicates that certain global table settings can be overridden.
Type: String
Valid Values: `ENABLED | DISABLED | ENABLED_WITH_OVERRIDES`
Required: No

 ** GlobalTableVersion **   <a name="DDB-Type-TableDescription-GlobalTableVersion"></a>
Represents the version of [global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) in use, if the table is replicated across AWS Regions.
Type: String
Required: No

 ** GlobalTableWitnesses **   <a name="DDB-Type-TableDescription-GlobalTableWitnesses"></a>
The witness Region and its current status in the MRSC global table. Only one witness Region can be configured per MRSC global table.
Type: Array of [GlobalTableWitnessDescription](API_GlobalTableWitnessDescription.md) objects
Required: No

 ** ItemCount **   <a name="DDB-Type-TableDescription-ItemCount"></a>
The number of items in the specified table. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
Type: Long
Required: No

 ** KeySchema **   <a name="DDB-Type-TableDescription-KeySchema"></a>
The primary key structure for the table. Each `KeySchemaElement` consists of:
+  `AttributeName` - The name of the attribute.
+  `KeyType` - The role of the attribute:
  +  `HASH` - partition key
  +  `RANGE` - sort key
**Note**
The partition key of an item is also known as its *hash attribute*. The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its *range attribute*. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.
For more information about primary keys, see [Primary Key](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataModel.html#DataModelPrimaryKey) in the *Amazon DynamoDB Developer Guide*.
Type: Array of [KeySchemaElement](API_KeySchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** LatestStreamArn **   <a name="DDB-Type-TableDescription-LatestStreamArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the latest stream for this table.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: No

 ** LatestStreamLabel **   <a name="DDB-Type-TableDescription-LatestStreamLabel"></a>
A timestamp, in ISO 8601 format, for this stream.
Note that `LatestStreamLabel` is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:
+  AWS customer ID
+ Table name
+  `StreamLabel`
Type: String
Required: No

 ** LocalSecondaryIndexes **   <a name="DDB-Type-TableDescription-LocalSecondaryIndexes"></a>
Represents one or more local secondary indexes on the table. Each index is scoped to a given partition key value. Tables with one or more local secondary indexes are subject to an item collection size limit, where the amount of data within a given item collection cannot exceed 10 GB. Each element is composed of:
+  `IndexName` - The name of the local secondary index.
+  `KeySchema` - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
+  `Projection` - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
  +  `ProjectionType` - One of the following:
    +  `KEYS_ONLY` - Only the index and primary keys are projected into the index.
    +  `INCLUDE` - Only the specified table attributes are projected into the index. The list of projected attributes is in `NonKeyAttributes`.
    +  `ALL` - All of the table attributes are projected into the index.
  +  `NonKeyAttributes` - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in `NonKeyAttributes`, summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of `INCLUDE`. You still can specify the ProjectionType of `ALL` to project all attributes from the source table, even if the table has more than 100 attributes.
+  `IndexSizeBytes` - Represents the total size of the index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
+  `ItemCount` - Represents the number of items in the index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
If the table is in the `DELETING` state, no information about indexes will be returned.
Type: Array of [LocalSecondaryIndexDescription](API_LocalSecondaryIndexDescription.md) objects
Required: No

 ** MultiRegionConsistency **   <a name="DDB-Type-TableDescription-MultiRegionConsistency"></a>
Indicates one of the following consistency modes for a global table:
+  `EVENTUAL`: Indicates that the global table is configured for multi-Region eventual consistency (MREC).
+  `STRONG`: Indicates that the global table is configured for multi-Region strong consistency (MRSC).
If you don't specify this field, the global table consistency mode defaults to `EVENTUAL`. For more information about global tables consistency modes, see [ Consistency modes](https://docs.aws.amazon.com/V2globaltables_HowItWorks.html#V2globaltables_HowItWorks.consistency-modes) in DynamoDB developer guide.
Type: String
Valid Values: `EVENTUAL | STRONG`
Required: No

 ** OnDemandThroughput **   <a name="DDB-Type-TableDescription-OnDemandThroughput"></a>
The maximum number of read and write units for the specified on-demand table. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both.
Type: [OnDemandThroughput](API_OnDemandThroughput.md) object
Required: No

 ** ProvisionedThroughput **   <a name="DDB-Type-TableDescription-ProvisionedThroughput"></a>
The provisioned throughput settings for the table, consisting of read and write capacity units, along with data about increases and decreases.
Type: [ProvisionedThroughputDescription](API_ProvisionedThroughputDescription.md) object
Required: No

 ** Replicas **   <a name="DDB-Type-TableDescription-Replicas"></a>
Represents replicas of the table.
Type: Array of [ReplicaDescription](API_ReplicaDescription.md) objects
Required: No

 ** RestoreSummary **   <a name="DDB-Type-TableDescription-RestoreSummary"></a>
Contains details for the restore.
Type: [RestoreSummary](API_RestoreSummary.md) object
Required: No

 ** SSEDescription **   <a name="DDB-Type-TableDescription-SSEDescription"></a>
The description of the server-side encryption status on the specified table.
Type: [SSEDescription](API_SSEDescription.md) object
Required: No

 ** StreamSpecification **   <a name="DDB-Type-TableDescription-StreamSpecification"></a>
The current DynamoDB Streams configuration for the table.
Type: [StreamSpecification](API_StreamSpecification.md) object
Required: No

 ** TableArn **   <a name="DDB-Type-TableDescription-TableArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the table.
Type: String
Required: No

 ** TableClassSummary **   <a name="DDB-Type-TableDescription-TableClassSummary"></a>
Contains details of the table class.
Type: [TableClassSummary](API_TableClassSummary.md) object
Required: No

 ** TableId **   <a name="DDB-Type-TableDescription-TableId"></a>
A unique identifier for the table, in UUID format, generated by DynamoDB when the table is created.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** TableName **   <a name="DDB-Type-TableDescription-TableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** TableSizeBytes **   <a name="DDB-Type-TableDescription-TableSizeBytes"></a>
The total size of the specified table, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
Type: Long
Required: No

 ** TableStatus **   <a name="DDB-Type-TableDescription-TableStatus"></a>
The current state of the table:
+  `CREATING` - The table is being created.
+  `UPDATING` - The table/index configuration is being updated. The table/index remains available for data operations when `UPDATING`.
+  `DELETING` - The table is being deleted.
+  `ACTIVE` - The table is ready for use.
+  `INACCESSIBLE_ENCRYPTION_CREDENTIALS` - The AWS KMS key used to encrypt the table in inaccessible. Table operations may fail due to failure to use the AWS KMS key. DynamoDB will initiate the table archival process when a table's AWS KMS key remains inaccessible for more than seven days.
+  `ARCHIVING` - The table is being archived. Operations are not allowed until archival is complete.
+  `ARCHIVED` - The table has been archived. See the ArchivalReason for more information.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | INACCESSIBLE_ENCRYPTION_CREDENTIALS | ARCHIVING | ARCHIVED | REPLICATION_NOT_AUTHORIZED`
Required: No

 ** VectorIndexes **   <a name="DDB-Type-TableDescription-VectorIndexes"></a>
The vector indexes, if any, on the table. Each element is composed of:
+  `IndexName` - The name of the vector index.
+  `IndexStatus` - The current status of the vector index: `CREATING`, `UPDATING`, `ACTIVE`, or `DELETING`.
+  `Backfilling` - Specifies whether the index is currently backfilling. `SearchVectors` returns a `ValidationException` while the index is backfilling. This field is reported for an index added with `UpdateTable`, and is absent for an index created as part of `CreateTable`.
+  `VectorAttribute` - The attribute that contains vector embeddings.
+  `Dimensions` - The number of dimensions in each vector.
+  `DistanceFunction` - The distance function used to calculate similarity (`COSINE`, `EUCLIDEAN`, or `DOT_PRODUCT`).
+  `SearchSchema` - The partition key and inline filter attributes for the vector index.
+  `Projection` - Specifies attributes that are copied (projected) from the table into the vector index.
+  `IndexArn` - The Amazon Resource Name (ARN) that uniquely identifies the index.
+  `IndexSizeBytes` - The total size of the vector index, in bytes. Amazon DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
+  `ItemCount` - The number of items indexed in the vector index. Amazon DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
Type: Array of [VectorIndexDescription](API_VectorIndexDescription.md) objects
Required: No

 ** WarmThroughput **   <a name="DDB-Type-TableDescription-WarmThroughput"></a>
Describes the warm throughput value of the base table.
Type: [TableWarmThroughputDescription](API_TableWarmThroughputDescription.md) object
Required: No

## See Also
<a name="API_TableDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/TableDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/TableDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/TableDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
