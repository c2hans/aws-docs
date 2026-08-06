---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_RestoreTableFromBackup.html
---

# RestoreTableFromBackup
<a name="API_RestoreTableFromBackup"></a>

Creates a new table from an existing backup. Any number of users can execute up to 50 concurrent restores (any type of restore) in a given account.

You can call `RestoreTableFromBackup` at a maximum rate of 10 times per second.

You must manually set up the following on the restored table:
+ Auto scaling policies
+ IAM policies
+ Amazon CloudWatch metrics and alarms
+ Tags
+ Stream settings
+ Time to Live (TTL) settings

## Request Syntax
<a name="API_RestoreTableFromBackup_RequestSyntax"></a>

```
{
   "BackupArn": "{{string}}",
   "BillingModeOverride": "{{string}}",
   "GlobalSecondaryIndexOverride": [
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
   "LocalSecondaryIndexOverride": [
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
   "OnDemandThroughputOverride": {
      "MaxReadRequestUnits": {{number}},
      "MaxWriteRequestUnits": {{number}}
   },
   "ProvisionedThroughputOverride": {
      "ReadCapacityUnits": {{number}},
      "WriteCapacityUnits": {{number}}
   },
   "SSESpecificationOverride": {
      "Enabled": {{boolean}},
      "KMSMasterKeyId": "{{string}}",
      "SSEType": "{{string}}"
   },
   "TargetTableName": "{{string}}",
   "VectorIndexOverride": [
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
   ]
}
```

## Request Parameters
<a name="API_RestoreTableFromBackup_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [BackupArn](#API_RestoreTableFromBackup_RequestSyntax) **   <a name="DDB-RestoreTableFromBackup-request-BackupArn"></a>
The Amazon Resource Name (ARN) associated with the backup.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: Yes

 ** [TargetTableName](#API_RestoreTableFromBackup_RequestSyntax) **   <a name="DDB-RestoreTableFromBackup-request-TargetTableName"></a>
The name of the new table to which the backup must be restored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [BillingModeOverride](#API_RestoreTableFromBackup_RequestSyntax) **   <a name="DDB-RestoreTableFromBackup-request-BillingModeOverride"></a>
The billing mode of the restored table.
Type: String
Valid Values: `PROVISIONED | PAY_PER_REQUEST`
Required: No

 ** [GlobalSecondaryIndexOverride](#API_RestoreTableFromBackup_RequestSyntax) **   <a name="DDB-RestoreTableFromBackup-request-GlobalSecondaryIndexOverride"></a>
List of global secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.
Type: Array of [GlobalSecondaryIndex](API_GlobalSecondaryIndex.md) objects
Required: No

 ** [LocalSecondaryIndexOverride](#API_RestoreTableFromBackup_RequestSyntax) **   <a name="DDB-RestoreTableFromBackup-request-LocalSecondaryIndexOverride"></a>
List of local secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.
Type: Array of [LocalSecondaryIndex](API_LocalSecondaryIndex.md) objects
Required: No

 ** [OnDemandThroughputOverride](#API_RestoreTableFromBackup_RequestSyntax) **   <a name="DDB-RestoreTableFromBackup-request-OnDemandThroughputOverride"></a>
Sets the maximum number of read and write units for the specified on-demand table. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both.
Type: [OnDemandThroughput](API_OnDemandThroughput.md) object
Required: No

 ** [ProvisionedThroughputOverride](#API_RestoreTableFromBackup_RequestSyntax) **   <a name="DDB-RestoreTableFromBackup-request-ProvisionedThroughputOverride"></a>
Provisioned throughput settings for the restored table.
Type: [ProvisionedThroughput](API_ProvisionedThroughput.md) object
Required: No

 ** [SSESpecificationOverride](#API_RestoreTableFromBackup_RequestSyntax) **   <a name="DDB-RestoreTableFromBackup-request-SSESpecificationOverride"></a>
The new server-side encryption settings for the restored table.
Type: [SSESpecification](API_SSESpecification.md) object
Required: No

 ** [VectorIndexOverride](#API_RestoreTableFromBackup_RequestSyntax) **   <a name="DDB-RestoreTableFromBackup-request-VectorIndexOverride"></a>
The vector indexes for the restored table. If not specified, all vector indexes from the backup are restored. The indexes provided must match existing vector indexes from the backup. You can choose to exclude some or all of the vector indexes at the time of restore.
Type: Array of [VectorIndex](API_VectorIndex.md) objects
Required: No

## Response Syntax
<a name="API_RestoreTableFromBackup_ResponseSyntax"></a>

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
<a name="API_RestoreTableFromBackup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TableDescription](#API_RestoreTableFromBackup_ResponseSyntax) **   <a name="DDB-RestoreTableFromBackup-response-TableDescription"></a>
The description of the table created from an existing backup.
Type: [TableDescription](API_TableDescription.md) object

## Errors
<a name="API_RestoreTableFromBackup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BackupInUseException **
There is another ongoing conflicting backup control plane operation on the table. The backup is either being created, deleted or restored to a table.
HTTP Status Code: 400

 ** BackupNotFoundException **
Backup not found for the given BackupARN.
HTTP Status Code: 400

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

 ** TableAlreadyExistsException **
A target table with the specified name already exists.
HTTP Status Code: 400

 ** TableInUseException **
A target table with the specified name is either being created or deleted.
HTTP Status Code: 400

## See Also
<a name="API_RestoreTableFromBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/RestoreTableFromBackup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/RestoreTableFromBackup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/RestoreTableFromBackup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/RestoreTableFromBackup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/RestoreTableFromBackup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/RestoreTableFromBackup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/RestoreTableFromBackup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/RestoreTableFromBackup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/RestoreTableFromBackup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/RestoreTableFromBackup)
