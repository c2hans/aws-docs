---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_RestoreTableToPointInTime.html
---

# RestoreTableToPointInTime
<a name="API_RestoreTableToPointInTime"></a>

Restores the specified table to the specified point in time within `EarliestRestorableDateTime` and `LatestRestorableDateTime`. You can restore your table to any point in time in the last 35 days. You can set the recovery period to any value between 1 and 35 days. Any number of users can execute up to 50 concurrent restores (any type of restore) in a given account.

When you restore using point in time recovery, DynamoDB restores your table data to the state based on the selected date and time (day:hour:minute:second) to a new table.

Along with data, the following are also included on the new restored table using point in time recovery:
+ Global secondary indexes (GSIs)
+ Local secondary indexes (LSIs)
+ Provisioned read and write capacity
+ Encryption settings
**Important**
 All these settings come from the current settings of the source table at the time of restore.

You must manually set up the following on the restored table:
+ Auto scaling policies
+ IAM policies
+ Amazon CloudWatch metrics and alarms
+ Tags
+ Stream settings
+ Time to Live (TTL) settings
+ Point in time recovery settings

## Request Syntax
<a name="API_RestoreTableToPointInTime_RequestSyntax"></a>

```
{
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
   "RestoreDateTime": {{number}},
   "SourceTableArn": "{{string}}",
   "SourceTableName": "{{string}}",
   "SSESpecificationOverride": {
      "Enabled": {{boolean}},
      "KMSMasterKeyId": "{{string}}",
      "SSEType": "{{string}}"
   },
   "TargetTableName": "{{string}}",
   "UseLatestRestorableTime": {{boolean}},
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
<a name="API_RestoreTableToPointInTime_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [TargetTableName](#API_RestoreTableToPointInTime_RequestSyntax) **   <a name="DDB-RestoreTableToPointInTime-request-TargetTableName"></a>
The name of the new table to which it must be restored to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [BillingModeOverride](#API_RestoreTableToPointInTime_RequestSyntax) **   <a name="DDB-RestoreTableToPointInTime-request-BillingModeOverride"></a>
The billing mode of the restored table.
Type: String
Valid Values: `PROVISIONED | PAY_PER_REQUEST`
Required: No

 ** [GlobalSecondaryIndexOverride](#API_RestoreTableToPointInTime_RequestSyntax) **   <a name="DDB-RestoreTableToPointInTime-request-GlobalSecondaryIndexOverride"></a>
List of global secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.
The `WarmThroughput` setting is not supported on global secondary indexes when you use `RestoreTableToPointInTime`. Although `WarmThroughput` appears in the shared index definition, including it in a `GlobalSecondaryIndexOverride` entry causes the request to fail with a validation error.
Type: Array of [GlobalSecondaryIndex](API_GlobalSecondaryIndex.md) objects
Required: No

 ** [LocalSecondaryIndexOverride](#API_RestoreTableToPointInTime_RequestSyntax) **   <a name="DDB-RestoreTableToPointInTime-request-LocalSecondaryIndexOverride"></a>
List of local secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.
Type: Array of [LocalSecondaryIndex](API_LocalSecondaryIndex.md) objects
Required: No

 ** [OnDemandThroughputOverride](#API_RestoreTableToPointInTime_RequestSyntax) **   <a name="DDB-RestoreTableToPointInTime-request-OnDemandThroughputOverride"></a>
Sets the maximum number of read and write units for the specified on-demand table. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both.
Type: [OnDemandThroughput](API_OnDemandThroughput.md) object
Required: No

 ** [ProvisionedThroughputOverride](#API_RestoreTableToPointInTime_RequestSyntax) **   <a name="DDB-RestoreTableToPointInTime-request-ProvisionedThroughputOverride"></a>
Provisioned throughput settings for the restored table.
Type: [ProvisionedThroughput](API_ProvisionedThroughput.md) object
Required: No

 ** [RestoreDateTime](#API_RestoreTableToPointInTime_RequestSyntax) **   <a name="DDB-RestoreTableToPointInTime-request-RestoreDateTime"></a>
Time in the past to restore the table to.
Type: Timestamp
Required: No

 ** [SourceTableArn](#API_RestoreTableToPointInTime_RequestSyntax) **   <a name="DDB-RestoreTableToPointInTime-request-SourceTableArn"></a>
The DynamoDB table that will be restored. This value is an Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [SourceTableName](#API_RestoreTableToPointInTime_RequestSyntax) **   <a name="DDB-RestoreTableToPointInTime-request-SourceTableName"></a>
Name of the source table that is being restored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [SSESpecificationOverride](#API_RestoreTableToPointInTime_RequestSyntax) **   <a name="DDB-RestoreTableToPointInTime-request-SSESpecificationOverride"></a>
The new server-side encryption settings for the restored table.
Type: [SSESpecification](API_SSESpecification.md) object
Required: No

 ** [UseLatestRestorableTime](#API_RestoreTableToPointInTime_RequestSyntax) **   <a name="DDB-RestoreTableToPointInTime-request-UseLatestRestorableTime"></a>
Restore the table to the latest possible time. `LatestRestorableDateTime` is typically 5 minutes before the current time.
Type: Boolean
Required: No

 ** [VectorIndexOverride](#API_RestoreTableToPointInTime_RequestSyntax) **   <a name="DDB-RestoreTableToPointInTime-request-VectorIndexOverride"></a>
The vector indexes for the restored table. If not specified, all vector indexes from the source table are restored. The indexes provided must match existing vector indexes from the source table. You can choose to exclude some or all of the vector indexes at the time of restore.
Type: Array of [VectorIndex](API_VectorIndex.md) objects
Required: No

## Response Syntax
<a name="API_RestoreTableToPointInTime_ResponseSyntax"></a>

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
<a name="API_RestoreTableToPointInTime_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TableDescription](#API_RestoreTableToPointInTime_ResponseSyntax) **   <a name="DDB-RestoreTableToPointInTime-response-TableDescription"></a>
Represents the properties of a table.
Type: [TableDescription](API_TableDescription.md) object

## Errors
<a name="API_RestoreTableToPointInTime_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** InvalidRestoreTimeException **
An invalid restore time was specified. RestoreDateTime must be between EarliestRestorableDateTime and LatestRestorableDateTime.
HTTP Status Code: 400

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

 ** PointInTimeRecoveryUnavailableException **
Point in time recovery has not yet been enabled for this source table.
HTTP Status Code: 400

 ** TableAlreadyExistsException **
A target table with the specified name already exists.
HTTP Status Code: 400

 ** TableInUseException **
A target table with the specified name is either being created or deleted.
HTTP Status Code: 400

 ** TableNotFoundException **
A source table with the name `TableName` does not currently exist within the subscriber's account or the subscriber is operating in the wrong AWS Region.
HTTP Status Code: 400

## See Also
<a name="API_RestoreTableToPointInTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/RestoreTableToPointInTime)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/RestoreTableToPointInTime)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/RestoreTableToPointInTime)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/RestoreTableToPointInTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/RestoreTableToPointInTime)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/RestoreTableToPointInTime)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/RestoreTableToPointInTime)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/RestoreTableToPointInTime)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/RestoreTableToPointInTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/RestoreTableToPointInTime)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
