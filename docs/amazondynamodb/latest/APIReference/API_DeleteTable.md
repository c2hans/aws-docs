---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteTable.html
---

# DeleteTable
<a name="API_DeleteTable"></a>

The `DeleteTable` operation deletes a table and all of its items. After a `DeleteTable` request, the specified table is in the `DELETING` state until DynamoDB completes the deletion. If the table is in the `ACTIVE` state, you can delete it. If a table is in `CREATING` or `UPDATING` states, then DynamoDB returns a `ResourceInUseException`. If the specified table does not exist, DynamoDB returns a `ResourceNotFoundException`. If table is already in the `DELETING` state, no error is returned.

**Note**
DynamoDB might continue to accept data read and write operations, such as `GetItem` and `PutItem`, on a table in the `DELETING` state until the table deletion is complete. For the full list of table states, see [TableStatus](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TableDescription.html#DDB-Type-TableDescription-TableStatus).

When you delete a table, any indexes on that table are also deleted.

If you have DynamoDB Streams enabled on the table, then the corresponding stream on that table goes into the `DISABLED` state, and the stream is automatically deleted after 24 hours.

Use the `DescribeTable` action to check the status of the table.

## Request Syntax
<a name="API_DeleteTable_RequestSyntax"></a>

```
{
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteTable_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [TableName](#API_DeleteTable_RequestSyntax) **   <a name="DDB-DeleteTable-request-TableName"></a>
The name of the table to delete. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_DeleteTable_ResponseSyntax"></a>

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
      "WarmThroughput": {
         "ReadUnitsPerSecond": number,
         "Status": "string",
         "WriteUnitsPerSecond": number
      }
   }
}
```

## Response Elements
<a name="API_DeleteTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TableDescription](#API_DeleteTable_ResponseSyntax) **   <a name="DDB-DeleteTable-response-TableDescription"></a>
Represents the properties of a table.
Type: [TableDescription](API_TableDescription.md) object

## Errors
<a name="API_DeleteTable_Errors"></a>

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
<a name="API_DeleteTable_Examples"></a>

### Delete a Table
<a name="API_DeleteTable_Example_1"></a>

This example deletes the Reply table.

#### Sample Request
<a name="API_DeleteTable_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dynamodb.<region>.<domain>;
Accept-Encoding: identity
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: DynamoDB_20120810.DeleteTable

{
    "TableName": "Reply"
}
```

#### Sample Response
<a name="API_DeleteTable_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
x-amz-crc32: <Checksum>
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
Date: <Date>
 {
    "TableDescription": {
        "TableArn": "arn:aws:dynamodb:us-west-2:123456789012:table/Reply",
        "ItemCount": 0,
        "ProvisionedThroughput": {
            "NumberOfDecreasesToday": 0,
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        },
        "TableName": "Reply",
        "TableSizeBytes": 0,
        "TableStatus": "DELETING"
    }
}
```

## See Also
<a name="API_DeleteTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/DeleteTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/DeleteTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DeleteTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/DeleteTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DeleteTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/DeleteTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/DeleteTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/DeleteTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/DeleteTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DeleteTable)
