---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteBackup.html
---

# DeleteBackup
<a name="API_DeleteBackup"></a>

Deletes an existing backup of a table.

You can call `DeleteBackup` at a maximum rate of 10 times per second.

## Request Syntax
<a name="API_DeleteBackup_RequestSyntax"></a>

```
{
   "BackupArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteBackup_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [BackupArn](#API_DeleteBackup_RequestSyntax) **   <a name="DDB-DeleteBackup-request-BackupArn"></a>
The ARN associated with the backup.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_DeleteBackup_ResponseSyntax"></a>

```
{
   "BackupDescription": {
      "BackupDetails": {
         "BackupArn": "string",
         "BackupCreationDateTime": number,
         "BackupExpiryDateTime": number,
         "BackupName": "string",
         "BackupSizeBytes": number,
         "BackupStatus": "string",
         "BackupType": "string"
      },
      "SourceTableDetails": {
         "BillingMode": "string",
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
         "ProvisionedThroughput": {
            "ReadCapacityUnits": number,
            "WriteCapacityUnits": number
         },
         "TableArn": "string",
         "TableCreationDateTime": number,
         "TableId": "string",
         "TableName": "string",
         "TableSizeBytes": number
      },
      "SourceTableFeatureDetails": {
         "GlobalSecondaryIndexes": [
            {
               "IndexName": "string",
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
                  "ReadCapacityUnits": number,
                  "WriteCapacityUnits": number
               }
            }
         ],
         "LocalSecondaryIndexes": [
            {
               "IndexName": "string",
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
         "SSEDescription": {
            "InaccessibleEncryptionDateTime": number,
            "KMSMasterKeyArn": "string",
            "SSEType": "string",
            "Status": "string"
         },
         "StreamDescription": {
            "StreamEnabled": boolean,
            "StreamViewType": "string"
         },
         "TimeToLiveDescription": {
            "AttributeName": "string",
            "TimeToLiveStatus": "string"
         },
         "VectorIndexes": [
            {
               "Dimensions": number,
               "DistanceFunction": "string",
               "IndexName": "string",
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
         ]
      }
   }
}
```

## Response Elements
<a name="API_DeleteBackup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackupDescription](#API_DeleteBackup_ResponseSyntax) **   <a name="DDB-DeleteBackup-response-BackupDescription"></a>
Contains the description of the backup created for the table.
Type: [BackupDescription](API_BackupDescription.md) object

## Errors
<a name="API_DeleteBackup_Errors"></a>

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

## See Also
<a name="API_DeleteBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/DeleteBackup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/DeleteBackup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DeleteBackup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/DeleteBackup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DeleteBackup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/DeleteBackup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/DeleteBackup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/DeleteBackup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/DeleteBackup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DeleteBackup)
