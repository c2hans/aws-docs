---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html
---

# CreateTable
<a name="API_CreateTable"></a>

The `CreateTable` operation adds a new table to your account. In an AWS account, table names must be unique within each Region. That is, you can have two tables with same name if you create the tables in different Regions.

 `CreateTable` is an asynchronous operation. Upon receiving a `CreateTable` request, DynamoDB immediately returns a response with a `TableStatus` of `CREATING`. After the table is created, DynamoDB sets the `TableStatus` to `ACTIVE`. You can perform read and write operations only on an `ACTIVE` table.

You can optionally define secondary indexes on the new table, as part of the `CreateTable` operation. If you want to create multiple tables with secondary indexes on them, you must create the tables sequentially. Only one table with secondary indexes can be in the `CREATING` state at any given time.

You can use the `DescribeTable` action to check the table status.

## Request Syntax
<a name="API_CreateTable_RequestSyntax"></a>

```
{
   "AttributeDefinitions": [
      {
         "AttributeName": "{{string}}",
         "AttributeType": "{{string}}"
      }
   ],
   "BillingMode": "{{string}}",
   "DeletionProtectionEnabled": {{boolean}},
   "GlobalSecondaryIndexes": [
      {
         "IndexName": "{{string}}",
         "KeySchema": [
            {
               "AttributeName": "{{string}}",
               "KeyType": "{{string}}"
            }
         ],
         "OnDemandThroughput": {
            "MaxReadRequestUnits": {{number}},
            "MaxWriteRequestUnits": {{number}}
         },
         "Projection": {
            "NonKeyAttributes": [ "{{string}}" ],
            "ProjectionType": "{{string}}"
         },
         "ProvisionedThroughput": {
            "ReadCapacityUnits": {{number}},
            "WriteCapacityUnits": {{number}}
         },
         "WarmThroughput": {
            "ReadUnitsPerSecond": {{number}},
            "WriteUnitsPerSecond": {{number}}
         }
      }
   ],
   "GlobalTableSettingsReplicationMode": "{{string}}",
   "GlobalTableSourceArn": "{{string}}",
   "KeySchema": [
      {
         "AttributeName": "{{string}}",
         "KeyType": "{{string}}"
      }
   ],
   "LocalSecondaryIndexes": [
      {
         "IndexName": "{{string}}",
         "KeySchema": [
            {
               "AttributeName": "{{string}}",
               "KeyType": "{{string}}"
            }
         ],
         "Projection": {
            "NonKeyAttributes": [ "{{string}}" ],
            "ProjectionType": "{{string}}"
         }
      }
   ],
   "OnDemandThroughput": {
      "MaxReadRequestUnits": {{number}},
      "MaxWriteRequestUnits": {{number}}
   },
   "ProvisionedThroughput": {
      "ReadCapacityUnits": {{number}},
      "WriteCapacityUnits": {{number}}
   },
   "ResourcePolicy": "{{string}}",
   "SSESpecification": {
      "Enabled": {{boolean}},
      "KMSMasterKeyId": "{{string}}",
      "SSEType": "{{string}}"
   },
   "StreamSpecification": {
      "StreamEnabled": {{boolean}},
      "StreamViewType": "{{string}}"
   },
   "TableClass": "{{string}}",
   "TableName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VectorIndexes": [
      {
         "Dimensions": {{number}},
         "DistanceFunction": "{{string}}",
         "IndexName": "{{string}}",
         "Projection": {
            "NonKeyAttributes": [ "{{string}}" ],
            "ProjectionType": "{{string}}"
         },
         "SearchSchema": [
            {
               "AttributeName": "{{string}}",
               "SearchSchemaElementType": "{{string}}"
            }
         ],
         "VectorAttribute": {
            "AttributeName": "{{string}}"
         }
      }
   ],
   "WarmThroughput": {
      "ReadUnitsPerSecond": {{number}},
      "WriteUnitsPerSecond": {{number}}
   }
}
```

## Request Parameters
<a name="API_CreateTable_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [TableName](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-TableName"></a>
The name of the table to create. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [AttributeDefinitions](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-AttributeDefinitions"></a>
An array of attributes that describe the key schema for the table and indexes.
Type: Array of [AttributeDefinition](API_AttributeDefinition.md) objects
Required: No

 ** [BillingMode](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-BillingMode"></a>
Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.
+  `PAY_PER_REQUEST` - We recommend using `PAY_PER_REQUEST` for most DynamoDB workloads. `PAY_PER_REQUEST` sets the billing mode to [On-demand capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html).
+  `PROVISIONED` - We recommend using `PROVISIONED` for steady workloads with predictable growth where capacity requirements can be reliably forecasted. `PROVISIONED` sets the billing mode to [Provisioned capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html).
Type: String
Valid Values: `PROVISIONED | PAY_PER_REQUEST`
Required: No

 ** [DeletionProtectionEnabled](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-DeletionProtectionEnabled"></a>
Indicates whether deletion protection is to be enabled (true) or disabled (false) on the table.
Type: Boolean
Required: No

 ** [GlobalSecondaryIndexes](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-GlobalSecondaryIndexes"></a>
One or more global secondary indexes (the maximum is 20) to be created on the table. Each global secondary index in the array includes the following:
+  `IndexName` - The name of the global secondary index. Must be unique only for this table.

+  `KeySchema` - Specifies the key schema for the global secondary index. Each global secondary index supports up to 4 partition keys and up to 4 sort keys.
+  `Projection` - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
  +  `ProjectionType` - One of the following:
    +  `KEYS_ONLY` - Only the index and primary keys are projected into the index.
    +  `INCLUDE` - Only the specified table attributes are projected into the index. The list of projected attributes is in `NonKeyAttributes`.
    +  `ALL` - All of the table attributes are projected into the index.
  +  `NonKeyAttributes` - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in `NonKeyAttributes`, summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of `INCLUDE`. You still can specify the ProjectionType of `ALL` to project all attributes from the source table, even if the table has more than 100 attributes.
+  `ProvisionedThroughput` - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units.
Type: Array of [GlobalSecondaryIndex](API_GlobalSecondaryIndex.md) objects
Required: No

 ** [GlobalTableSettingsReplicationMode](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-GlobalTableSettingsReplicationMode"></a>
Controls the settings synchronization mode for the global table. For multi-account global tables, this parameter is required and the only supported value is ENABLED. For same-account global tables, this parameter is set to ENABLED\_WITH\_OVERRIDES.
Type: String
Valid Values: `ENABLED | DISABLED | ENABLED_WITH_OVERRIDES`
Required: No

 ** [GlobalTableSourceArn](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-GlobalTableSourceArn"></a>
The Amazon Resource Name (ARN) of the source table used for the creation of a multi-account global table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [KeySchema](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-KeySchema"></a>
Specifies the attributes that make up the primary key for a table or an index. The attributes in `KeySchema` must also be defined in the `AttributeDefinitions` array. For more information, see [Data Model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataModel.html) in the *Amazon DynamoDB Developer Guide*.
Each `KeySchemaElement` in the array is composed of:
+  `AttributeName` - The name of this key attribute.
+  `KeyType` - The role that the key attribute will assume:
  +  `HASH` - partition key
  +  `RANGE` - sort key
The partition key of an item is also known as its *hash attribute*. The term "hash attribute" derives from the DynamoDB usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its *range attribute*. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.
For a simple primary key (partition key), you must provide exactly one element with a `KeyType` of `HASH`.
For a composite primary key (partition key and sort key), you must provide exactly two elements, in this order: The first element must have a `KeyType` of `HASH`, and the second element must have a `KeyType` of `RANGE`.
For more information, see [Working with Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#WorkingWithTables.primary.key) in the *Amazon DynamoDB Developer Guide*.
Type: Array of [KeySchemaElement](API_KeySchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [LocalSecondaryIndexes](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-LocalSecondaryIndexes"></a>
One or more local secondary indexes (the maximum is 5) to be created on the table. Each index is scoped to a given partition key value. There is a 10 GB size limit per partition key value; otherwise, the size of a local secondary index is unconstrained.
Each local secondary index in the array includes the following:
+  `IndexName` - The name of the local secondary index. Must be unique only for this table.

+  `KeySchema` - Specifies the key schema for the local secondary index. The key schema must begin with the same partition key as the table.
+  `Projection` - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
  +  `ProjectionType` - One of the following:
    +  `KEYS_ONLY` - Only the index and primary keys are projected into the index.
    +  `INCLUDE` - Only the specified table attributes are projected into the index. The list of projected attributes is in `NonKeyAttributes`.
    +  `ALL` - All of the table attributes are projected into the index.
  +  `NonKeyAttributes` - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in `NonKeyAttributes`, summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of `INCLUDE`. You still can specify the ProjectionType of `ALL` to project all attributes from the source table, even if the table has more than 100 attributes.
Type: Array of [LocalSecondaryIndex](API_LocalSecondaryIndex.md) objects
Required: No

 ** [OnDemandThroughput](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-OnDemandThroughput"></a>
Sets the maximum number of read and write units for the specified table in on-demand capacity mode. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both.
Type: [OnDemandThroughput](API_OnDemandThroughput.md) object
Required: No

 ** [ProvisionedThroughput](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-ProvisionedThroughput"></a>
Represents the provisioned throughput settings for a specified table or index. The settings can be modified using the `UpdateTable` operation.
 If you set BillingMode as `PROVISIONED`, you must specify this property. If you set BillingMode as `PAY_PER_REQUEST`, you cannot specify this property.
For current minimum and maximum provisioned throughput values, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide*.
Type: [ProvisionedThroughput](API_ProvisionedThroughput.md) object
Required: No

 ** [ResourcePolicy](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-ResourcePolicy"></a>
An AWS resource-based policy document in JSON format that will be attached to the table.
When you attach a resource-based policy while creating a table, the policy application is *strongly consistent*.
The maximum size supported for a resource-based policy document is 20 KB. DynamoDB counts whitespaces when calculating the size of a policy against this limit. For a full list of all considerations that apply for resource-based policies, see [Resource-based policy considerations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-considerations.html).
You need to specify the `CreateTable` and `PutResourcePolicy` IAM actions for authorizing a user to create a table with a resource-based policy.
Type: String
Required: No

 ** [SSESpecification](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-SSESpecification"></a>
Represents the settings used to enable server-side encryption.
Type: [SSESpecification](API_SSESpecification.md) object
Required: No

 ** [StreamSpecification](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-StreamSpecification"></a>
The settings for DynamoDB Streams on the table. These settings consist of:
+  `StreamEnabled` - Indicates whether DynamoDB Streams is to be enabled (true) or disabled (false).
+  `StreamViewType` - When an item in the table is modified, `StreamViewType` determines what information is written to the table's stream. Valid values for `StreamViewType` are:
  +  `KEYS_ONLY` - Only the key attributes of the modified item are written to the stream.
  +  `NEW_IMAGE` - The entire item, as it appears after it was modified, is written to the stream.
  +  `OLD_IMAGE` - The entire item, as it appeared before it was modified, is written to the stream.
  +  `NEW_AND_OLD_IMAGES` - Both the new and the old item images of the item are written to the stream.
Type: [StreamSpecification](API_StreamSpecification.md) object
Required: No

 ** [TableClass](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-TableClass"></a>
The table class of the new table. Valid values are `STANDARD` and `STANDARD_INFREQUENT_ACCESS`.
Type: String
Valid Values: `STANDARD | STANDARD_INFREQUENT_ACCESS`
Required: No

 ** [Tags](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-Tags"></a>
A list of key-value pairs to label the table. For more information, see [Tagging for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [VectorIndexes](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-VectorIndexes"></a>
One or more vector indexes to be created on the table. Each vector index enables similarity search on a vector attribute. Each element in the list consists of:
+  `IndexName` - The name of the vector index. Must be unique within the table.
+  `VectorAttribute` - The attribute that contains vector embeddings. If multiple vector indexes reference the same attribute, they must all use the same number of dimensions.
+  `Dimensions` - The number of dimensions in each vector.
+  `DistanceFunction` - The distance function used to calculate similarity. Valid values: `COSINE`, `EUCLIDEAN`, `DOT_PRODUCT`.
+  `Projection` - Specifies attributes that are copied (projected) from the table into the vector index. The total number of projected non-key attributes is shared across the vector attribute (counts as 1) and `INLINE_FILTER` search schema elements (each counts as 1). `HASH` search schema elements do not count toward this limit.
+  `SearchSchema` - (Optional) Defines the partition key (`HASH`) and inline filter (`INLINE_FILTER`) attributes for the vector index.
Type: Array of [VectorIndex](API_VectorIndex.md) objects
Required: No

 ** [WarmThroughput](#API_CreateTable_RequestSyntax) **   <a name="DDB-CreateTable-request-WarmThroughput"></a>
Represents the warm throughput (in read units per second and write units per second) for creating a table.
Type: [WarmThroughput](API_WarmThroughput.md) object
Required: No

## Response Syntax
<a name="API_CreateTable_ResponseSyntax"></a>

```
{
   "TableDescription": {
      "ArchivalSummary": {
         "ArchivalBackupArn": "string",
         "ArchivalDateTime": number,
         "ArchivalReason": "string"
      },
      "AttributeDefinitions": [
         {
            "AttributeName": "string",
            "AttributeType": "string"
         }
      ],
      "BillingModeSummary": {
         "BillingMode": "string",
         "LastUpdateToPayPerRequestDateTime": number
      },
      "CreationDateTime": number,
      "DeletionProtectionEnabled": boolean,
      "GlobalSecondaryIndexes": [
         {
            "Backfilling": boolean,
            "IndexArn": "string",
            "IndexName": "string",
            "IndexSizeBytes": number,
            "IndexStatus": "string",
            "ItemCount": number,
            "KeySchema": [
               {
                  "AttributeName": "string",
                  "KeyType": "string"
               }
            ],
            "OnDemandThroughput": {
               "MaxReadRequestUnits": number,
               "MaxWriteRequestUnits": number
            },
            "Projection": {
               "NonKeyAttributes": [ "string" ],
               "ProjectionType": "string"
            },
            "ProvisionedThroughput": {
               "LastDecreaseDateTime": number,
               "LastIncreaseDateTime": number,
               "NumberOfDecreasesToday": number,
               "ReadCapacityUnits": number,
               "WriteCapacityUnits": number
            },
            "WarmThroughput": {
               "ReadUnitsPerSecond": number,
               "Status": "string",
               "WriteUnitsPerSecond": number
            }
         }
      ],
      "GlobalTableSettingsReplicationMode": "string",
      "GlobalTableVersion": "string",
      "GlobalTableWitnesses": [
         {
            "RegionName": "string",
            "WitnessStatus": "string"
         }
      ],
      "ItemCount": number,
      "KeySchema": [
         {
            "AttributeName": "string",
            "KeyType": "string"
         }
      ],
      "LatestStreamArn": "string",
      "LatestStreamLabel": "string",
      "LocalSecondaryIndexes": [
         {
            "IndexArn": "string",
            "IndexName": "string",
            "IndexSizeBytes": number,
            "ItemCount": number,
            "KeySchema": [
               {
                  "AttributeName": "string",
                  "KeyType": "string"
               }
            ],
            "Projection": {
               "NonKeyAttributes": [ "string" ],
               "ProjectionType": "string"
            }
         }
      ],
      "MultiRegionConsistency": "string",
      "OnDemandThroughput": {
         "MaxReadRequestUnits": number,
         "MaxWriteRequestUnits": number
      },
      "ProvisionedThroughput": {
         "LastDecreaseDateTime": number,
         "LastIncreaseDateTime": number,
         "NumberOfDecreasesToday": number,
         "ReadCapacityUnits": number,
         "WriteCapacityUnits": number
      },
      "Replicas": [
         {
            "GlobalSecondaryIndexes": [
               {
                  "IndexName": "string",
                  "OnDemandThroughputOverride": {
                     "MaxReadRequestUnits": number
                  },
                  "ProvisionedThroughputOverride": {
                     "ReadCapacityUnits": number
                  },
                  "WarmThroughput": {
                     "ReadUnitsPerSecond": number,
                     "Status": "string",
                     "WriteUnitsPerSecond": number
                  }
               }
            ],
            "GlobalTableSettingsReplicationMode": "string",
            "KMSMasterKeyId": "string",
            "OnDemandThroughputOverride": {
               "MaxReadRequestUnits": number
            },
            "ProvisionedThroughputOverride": {
               "ReadCapacityUnits": number
            },
            "RegionName": "string",
            "ReplicaArn": "string",
            "ReplicaInaccessibleDateTime": number,
            "ReplicaStatus": "string",
            "ReplicaStatusDescription": "string",
            "ReplicaStatusPercentProgress": "string",
            "ReplicaTableClassSummary": {
               "LastUpdateDateTime": number,
               "TableClass": "string"
            },
            "WarmThroughput": {
               "ReadUnitsPerSecond": number,
               "Status": "string",
               "WriteUnitsPerSecond": number
            }
         }
      ],
      "RestoreSummary": {
         "RestoreDateTime": number,
         "RestoreInProgress": boolean,
         "SourceBackupArn": "string",
         "SourceTableArn": "string"
      },
      "SSEDescription": {
         "InaccessibleEncryptionDateTime": number,
         "KMSMasterKeyArn": "string",
         "SSEType": "string",
         "Status": "string"
      },
      "StreamSpecification": {
         "StreamEnabled": boolean,
         "StreamViewType": "string"
      },
      "TableArn": "string",
      "TableClassSummary": {
         "LastUpdateDateTime": number,
         "TableClass": "string"
      },
      "TableId": "string",
      "TableName": "string",
      "TableSizeBytes": number,
      "TableStatus": "string",
      "VectorIndexes": [
         {
            "Backfilling": boolean,
            "Dimensions": number,
            "DistanceFunction": "string",
            "IndexArn": "string",
            "IndexName": "string",
            "IndexSizeBytes": number,
            "IndexStatus": "string",
            "ItemCount": number,
            "Projection": {
               "NonKeyAttributes": [ "string" ],
               "ProjectionType": "string"
            },
            "SearchSchema": [
               {
                  "AttributeName": "string",
                  "SearchSchemaElementType": "string"
               }
            ],
            "VectorAttribute": {
               "AttributeName": "string"
            }
         }
      ],
      "WarmThroughput": {
         "ReadUnitsPerSecond": number,
         "Status": "string",
         "WriteUnitsPerSecond": number
      }
   }
}
```

## Response Elements
<a name="API_CreateTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TableDescription](#API_CreateTable_ResponseSyntax) **   <a name="DDB-CreateTable-response-TableDescription"></a>
Represents the properties of the table.
Type: [TableDescription](API_TableDescription.md) object

## Errors
<a name="API_CreateTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** LimitExceededException **
There is no limit to the number of daily on-demand backups that can be taken.
For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include `CreateTable`, `UpdateTable`, `DeleteTable`,`UpdateTimeToLive`, `RestoreTableFromBackup`, and `RestoreTableToPointInTime`.
When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.
When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.
There is a soft account quota of 2,500 tables.
GetRecords was called with a value of more than 1000 for the limit request parameter.
More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.
 ** message **
Too many operations for a given subscriber.
HTTP Status Code: 400

 ** ResourceInUseException **
The operation conflicts with the resource's availability. For example:
+ You attempted to recreate an existing table.
+ You tried to delete a table currently in the `CREATING` state.
+ You tried to update a resource that was already being updated.
When appropriate, wait for the ongoing update to complete and attempt the request again.
 ** message **
The resource which is being attempted to be changed is in use.
HTTP Status Code: 400

## Examples
<a name="API_CreateTable_Examples"></a>

### Create a Table
<a name="API_CreateTable_Example_1"></a>

This example creates a table named `Thread`. The table primary key consists of `ForumName` (partition key) and `Subject` (sort key). A local secondary index is also created; its key consists of `ForumName` (partition key) and `LastPostDateTime` (sort key).

#### Sample Request
<a name="API_CreateTable_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dynamodb.<region>.<domain>;
Accept-Encoding: identity
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: DynamoDB_20120810.CreateTable

{
    "AttributeDefinitions": [
        {
            "AttributeName": "ForumName",
            "AttributeType": "S"
        },
        {
            "AttributeName": "Subject",
            "AttributeType": "S"
        },
        {
            "AttributeName": "LastPostDateTime",
            "AttributeType": "S"
        }
    ],
    "TableName": "Thread",
    "KeySchema": [
        {
            "AttributeName": "ForumName",
            "KeyType": "HASH"
        },
        {
            "AttributeName": "Subject",
            "KeyType": "RANGE"
        }
    ],
    "LocalSecondaryIndexes": [
        {
            "IndexName": "LastPostIndex",
            "KeySchema": [
                {
                    "AttributeName": "ForumName",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "LastPostDateTime",
                    "KeyType": "RANGE"
                }
            ],
            "Projection": {
                "ProjectionType": "KEYS_ONLY"
            }
        }
    ],
    "BillingMode": "PAY_PER_REQUEST",
    "Tags": [
      {
         "Key": "Owner",
         "Value": "BlueTeam"
      }
   ]
}
```

#### Sample Response
<a name="API_CreateTable_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
x-amz-crc32: <Checksum>
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
Date: <Date>
 {
    "TableDescription": {
        "TableArn": "arn:aws:dynamodb:us-west-2:123456789012:table/Thread",
        "AttributeDefinitions": [
            {
                "AttributeName": "ForumName",
                "AttributeType": "S"
            },
            {
                "AttributeName": "LastPostDateTime",
                "AttributeType": "S"
            },
            {
                "AttributeName": "Subject",
                "AttributeType": "S"
            }
        ],
        "CreationDateTime": 1.36372808007E9,
        "ItemCount": 0,
        "KeySchema": [
            {
                "AttributeName": "ForumName",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "Subject",
                "KeyType": "RANGE"
            }
        ],
        "LocalSecondaryIndexes": [
            {
                "IndexArn": "arn:aws:dynamodb:us-west-2:123456789012:table/Thread/index/LastPostIndex",
                "IndexName": "LastPostIndex",
                "IndexSizeBytes": 0,
                "ItemCount": 0,
                "KeySchema": [
                    {
                        "AttributeName": "ForumName",
                        "KeyType": "HASH"
                    },
                    {
                        "AttributeName": "LastPostDateTime",
                        "KeyType": "RANGE"
                    }
                ],
                "Projection": {
                    "ProjectionType": "KEYS_ONLY"
                }
            }
        ],
        "TableName": "Thread",
        "TableSizeBytes": 0,
        "TableStatus": "CREATING"
    }
}
```

## See Also
<a name="API_CreateTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/CreateTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/CreateTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/CreateTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/CreateTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/CreateTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/CreateTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/CreateTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/CreateTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/CreateTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/CreateTable)
