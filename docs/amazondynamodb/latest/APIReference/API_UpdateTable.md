---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html
---

# UpdateTable
<a name="API_UpdateTable"></a>

Modifies the provisioned throughput settings, global secondary indexes, or DynamoDB Streams settings for a given table.

You can only perform one of the following operations at once:
+ Modify the provisioned throughput settings of the table.
+ Remove a global secondary index from the table.
+ Create a new global secondary index on the table. After the index begins backfilling, you can use `UpdateTable` to perform other operations.

 `UpdateTable` is an asynchronous operation; while it's executing, the table status changes from `ACTIVE` to `UPDATING`. While it's `UPDATING`, you can't issue another `UpdateTable` request. When the table returns to the `ACTIVE` state, the `UpdateTable` operation is complete.

## Request Syntax
<a name="API_UpdateTable_RequestSyntax"></a>

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
   "GlobalSecondaryIndexUpdates": [
      {
         "Create": {
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
         },
         "Delete": {
            "IndexName": "{{string}}"
         },
         "Update": {
            "IndexName": "{{string}}",
            "OnDemandThroughput": {
               "MaxReadRequestUnits": {{number}},
               "MaxWriteRequestUnits": {{number}}
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
      }
   ],
   "GlobalTableSettingsReplicationMode": "{{string}}",
   "GlobalTableWitnessUpdates": [
      {
         "Create": {
            "RegionName": "{{string}}"
         },
         "Delete": {
            "RegionName": "{{string}}"
         }
      }
   ],
   "MultiRegionConsistency": "{{string}}",
   "OnDemandThroughput": {
      "MaxReadRequestUnits": {{number}},
      "MaxWriteRequestUnits": {{number}}
   },
   "ProvisionedThroughput": {
      "ReadCapacityUnits": {{number}},
      "WriteCapacityUnits": {{number}}
   },
   "ReplicaUpdates": [
      {
         "Create": {
            "GlobalSecondaryIndexes": [
               {
                  "IndexName": "{{string}}",
                  "OnDemandThroughputOverride": {
                     "MaxReadRequestUnits": {{number}}
                  },
                  "ProvisionedThroughputOverride": {
                     "ReadCapacityUnits": {{number}}
                  }
               }
            ],
            "KMSMasterKeyId": "{{string}}",
            "OnDemandThroughputOverride": {
               "MaxReadRequestUnits": {{number}}
            },
            "ProvisionedThroughputOverride": {
               "ReadCapacityUnits": {{number}}
            },
            "RegionName": "{{string}}",
            "TableClassOverride": "{{string}}"
         },
         "Delete": {
            "RegionName": "{{string}}"
         },
         "Update": {
            "GlobalSecondaryIndexes": [
               {
                  "IndexName": "{{string}}",
                  "OnDemandThroughputOverride": {
                     "MaxReadRequestUnits": {{number}}
                  },
                  "ProvisionedThroughputOverride": {
                     "ReadCapacityUnits": {{number}}
                  }
               }
            ],
            "KMSMasterKeyId": "{{string}}",
            "OnDemandThroughputOverride": {
               "MaxReadRequestUnits": {{number}}
            },
            "ProvisionedThroughputOverride": {
               "ReadCapacityUnits": {{number}}
            },
            "RegionName": "{{string}}",
            "TableClassOverride": "{{string}}"
         }
      }
   ],
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
   "VectorIndexUpdates": [
      {
         "Create": {
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
         },
         "Delete": {
            "IndexName": "{{string}}"
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
<a name="API_UpdateTable_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [TableName](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-TableName"></a>
The name of the table to be updated. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [AttributeDefinitions](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-AttributeDefinitions"></a>
An array of attributes that describe the key schema for the table and indexes. If you are adding a new global secondary index to the table, `AttributeDefinitions` must include the key element(s) of the new index.
Type: Array of [AttributeDefinition](API_AttributeDefinition.md) objects
Required: No

 ** [BillingMode](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-BillingMode"></a>
Controls how you are charged for read and write throughput and how you manage capacity. When switching from pay-per-request to provisioned capacity, initial provisioned capacity values must be set. The initial provisioned capacity values are estimated based on the consumed read and write capacity of your table and global secondary indexes over the past 30 minutes.
+  `PAY_PER_REQUEST` - We recommend using `PAY_PER_REQUEST` for most DynamoDB workloads. `PAY_PER_REQUEST` sets the billing mode to [On-demand capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html).
+  `PROVISIONED` - We recommend using `PROVISIONED` for steady workloads with predictable growth where capacity requirements can be reliably forecasted. `PROVISIONED` sets the billing mode to [Provisioned capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html).
Type: String
Valid Values: `PROVISIONED | PAY_PER_REQUEST`
Required: No

 ** [DeletionProtectionEnabled](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-DeletionProtectionEnabled"></a>
Indicates whether deletion protection is to be enabled (true) or disabled (false) on the table.
Type: Boolean
Required: No

 ** [GlobalSecondaryIndexUpdates](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-GlobalSecondaryIndexUpdates"></a>
An array of one or more global secondary indexes for the table. For each index in the array, you can request one action:
+  `Create` - add a new global secondary index to the table.
+  `Update` - modify the provisioned throughput settings of an existing global secondary index.
+  `Delete` - remove a global secondary index from the table.
You can create or delete only one global secondary index per `UpdateTable` operation.
For more information, see [Managing Global Secondary Indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.OnlineOps.html) in the *Amazon DynamoDB Developer Guide*.
Type: Array of [GlobalSecondaryIndexUpdate](API_GlobalSecondaryIndexUpdate.md) objects
Required: No

 ** [GlobalTableSettingsReplicationMode](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-GlobalTableSettingsReplicationMode"></a>
Controls the settings replication mode for a global table replica. This attribute can be defined using UpdateTable operation only on a regional table with values:
+  `ENABLED`: Defines settings replication on a regional table to be used as a source table for creating Multi-Account Global Table.
+  `DISABLED`: Remove settings replication on a regional table. Settings replication needs to be defined to ENABLED again in order to create a Multi-Account Global Table using this table.
Type: String
Valid Values: `ENABLED | DISABLED | ENABLED_WITH_OVERRIDES`
Required: No

 ** [GlobalTableWitnessUpdates](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-GlobalTableWitnessUpdates"></a>
A list of witness updates for a MRSC global table. A witness provides a cost-effective alternative to a full replica in a MRSC global table by maintaining replicated change data written to global table replicas. You cannot perform read or write operations on a witness. For each witness, you can request one action:
+  `Create` - add a new witness to the global table.
+  `Delete` - remove a witness from the global table.
You can create or delete only one witness per `UpdateTable` operation.
For more information, see [Multi-Region strong consistency (MRSC)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html#V2globaltables_HowItWorks.consistency-modes) in the Amazon DynamoDB Developer Guide
Type: Array of [GlobalTableWitnessGroupUpdate](API_GlobalTableWitnessGroupUpdate.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [MultiRegionConsistency](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-MultiRegionConsistency"></a>
Specifies the consistency mode for a new global table. This parameter is only valid when you create a global table by specifying one or more [Create](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicationGroupUpdate.html#DDB-Type-ReplicationGroupUpdate-Create) actions in the [ReplicaUpdates](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html#DDB-UpdateTable-request-ReplicaUpdates) action list.
You can specify one of the following consistency modes:
+  `EVENTUAL`: Configures a new global table for multi-Region eventual consistency (MREC). This is the default consistency mode for global tables.
+  `STRONG`: Configures a new global table for multi-Region strong consistency (MRSC).
If you don't specify this field, the global table consistency mode defaults to `EVENTUAL`. For more information about global tables consistency modes, see [ Consistency modes](https://docs.aws.amazon.com/V2globaltables_HowItWorks.html#V2globaltables_HowItWorks.consistency-modes) in DynamoDB developer guide.
Type: String
Valid Values: `EVENTUAL | STRONG`
Required: No

 ** [OnDemandThroughput](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-OnDemandThroughput"></a>
Updates the maximum number of read and write units for the specified table in on-demand capacity mode. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both.
Type: [OnDemandThroughput](API_OnDemandThroughput.md) object
Required: No

 ** [ProvisionedThroughput](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-ProvisionedThroughput"></a>
The new provisioned throughput settings for the specified table or index.
Type: [ProvisionedThroughput](API_ProvisionedThroughput.md) object
Required: No

 ** [ReplicaUpdates](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-ReplicaUpdates"></a>
A list of replica update actions (create, delete, or update) for the table.
Type: Array of [ReplicationGroupUpdate](API_ReplicationGroupUpdate.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [SSESpecification](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-SSESpecification"></a>
The new server-side encryption settings for the specified table.
Type: [SSESpecification](API_SSESpecification.md) object
Required: No

 ** [StreamSpecification](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-StreamSpecification"></a>
Represents the DynamoDB Streams configuration for the table.
You receive a `ValidationException` if you try to enable a stream on a table that already has a stream, or if you try to disable a stream on a table that doesn't have a stream.
Type: [StreamSpecification](API_StreamSpecification.md) object
Required: No

 ** [TableClass](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-TableClass"></a>
The table class of the table to be updated. Valid values are `STANDARD` and `STANDARD_INFREQUENT_ACCESS`.
Type: String
Valid Values: `STANDARD | STANDARD_INFREQUENT_ACCESS`
Required: No

 ** [VectorIndexUpdates](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-VectorIndexUpdates"></a>
A list of vector indexes to be added to or removed from the table. You can add or remove one vector index for each `UpdateTable` operation.
To add a vector index, specify `IndexName`, `VectorAttribute`, `Dimensions`, `DistanceFunction`, and `Projection`. To remove a vector index, specify only the `IndexName`.
Type: Array of [VectorIndexUpdate](API_VectorIndexUpdate.md) objects
Required: No

 ** [WarmThroughput](#API_UpdateTable_RequestSyntax) **   <a name="DDB-UpdateTable-request-WarmThroughput"></a>
Represents the warm throughput (in read units per second and write units per second) for updating a table.
Type: [WarmThroughput](API_WarmThroughput.md) object
Required: No

## Response Syntax
<a name="API_UpdateTable_ResponseSyntax"></a>

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
<a name="API_UpdateTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TableDescription](#API_UpdateTable_ResponseSyntax) **   <a name="DDB-UpdateTable-response-TableDescription"></a>
Represents the properties of the table.
Type: [TableDescription](API_TableDescription.md) object

## Errors
<a name="API_UpdateTable_Errors"></a>

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

 ** ResourceNotFoundException **
The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The resource which is being requested does not exist.
HTTP Status Code: 400

## Examples
<a name="API_UpdateTable_Examples"></a>

### Modify Provisioned Write Throughput
<a name="API_UpdateTable_Example_1"></a>

This example changes both the provisioned read and write throughput of the `Thread` table to 10 capacity units.

#### Sample Request
<a name="API_UpdateTable_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dynamodb.<region>.<domain>;
Accept-Encoding: identity
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: DynamoDB_20120810.UpdateTable

{
    "TableName": "Thread",
    "ProvisionedThroughput": {
        "ReadCapacityUnits": 10,
        "WriteCapacityUnits": 10
    }
}
```

#### Sample Response
<a name="API_UpdateTable_Example_1_Response"></a>

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
        "CreationDateTime": 1.363801528686E9,
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
        "ProvisionedThroughput": {
            "LastIncreaseDateTime": 1.363801701282E9,
            "NumberOfDecreasesToday": 0,
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        },
        "TableName": "Thread",
        "TableSizeBytes": 0,
        "TableStatus": "UPDATING"
    }
}
```

## See Also
<a name="API_UpdateTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/UpdateTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/UpdateTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/UpdateTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/UpdateTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/UpdateTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/UpdateTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/UpdateTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/UpdateTable)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/UpdateTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/UpdateTable)
