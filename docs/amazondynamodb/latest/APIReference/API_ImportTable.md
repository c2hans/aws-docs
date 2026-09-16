---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ImportTable.html
---

# ImportTable
<a name="API_ImportTable"></a>

 Imports table data from an S3 bucket.

## Request Syntax
<a name="API_ImportTable_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "InputCompressionType": "{{string}}",
   "InputFormat": "{{string}}",
   "InputFormatOptions": {
      "Csv": {
         "Delimiter": "{{string}}",
         "HeaderList": [ "{{string}}" ]
      }
   },
   "S3BucketSource": {
      "S3Bucket": "{{string}}",
      "S3BucketOwner": "{{string}}",
      "S3KeyPrefix": "{{string}}"
   },
   "TableCreationParameters": {
      "AttributeDefinitions": [
         {
            "AttributeName": "{{string}}",
            "AttributeType": "{{string}}"
         }
      ],
      "BillingMode": "{{string}}",
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
      "ProvisionedThroughput": {
         "ReadCapacityUnits": {{number}},
         "WriteCapacityUnits": {{number}}
      },
      "SSESpecification": {
         "Enabled": {{boolean}},
         "KMSMasterKeyId": "{{string}}",
         "SSEType": "{{string}}"
      },
      "TableName": "{{string}}",
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
      ]
   }
}
```

## Request Parameters
<a name="API_ImportTable_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [InputFormat](#API_ImportTable_RequestSyntax) **   <a name="DDB-ImportTable-request-InputFormat"></a>
 The format of the source data. Valid values for `ImportFormat` are `CSV`, `DYNAMODB_JSON` or `ION`.
Type: String
Valid Values: `DYNAMODB_JSON | ION | CSV`
Required: Yes

 ** [S3BucketSource](#API_ImportTable_RequestSyntax) **   <a name="DDB-ImportTable-request-S3BucketSource"></a>
 The S3 bucket that provides the source for the import.
Type: [S3BucketSource](API_S3BucketSource.md) object
Required: Yes

 ** [TableCreationParameters](#API_ImportTable_RequestSyntax) **   <a name="DDB-ImportTable-request-TableCreationParameters"></a>
Parameters for the table to import the data into.
Type: [TableCreationParameters](API_TableCreationParameters.md) object
Required: Yes

 ** [ClientToken](#API_ImportTable_RequestSyntax) **   <a name="DDB-ImportTable-request-ClientToken"></a>
Providing a `ClientToken` makes the call to `ImportTableInput` idempotent, meaning that multiple identical calls have the same effect as one single call.
A client token is valid for 8 hours after the first request that uses it is completed. After 8 hours, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 8 hours, or the result might not be idempotent.
If you submit a request with the same client token but a change in other parameters within the 8-hour idempotency window, DynamoDB returns an `IdempotentParameterMismatch` exception.
Type: String
Pattern: `^[^\$]+$`
Required: No

 ** [InputCompressionType](#API_ImportTable_RequestSyntax) **   <a name="DDB-ImportTable-request-InputCompressionType"></a>
 Type of compression to be used on the input coming from the imported table.
Type: String
Valid Values: `GZIP | ZSTD | NONE`
Required: No

 ** [InputFormatOptions](#API_ImportTable_RequestSyntax) **   <a name="DDB-ImportTable-request-InputFormatOptions"></a>
 Additional properties that specify how the input is formatted,
Type: [InputFormatOptions](API_InputFormatOptions.md) object
Required: No

## Response Syntax
<a name="API_ImportTable_ResponseSyntax"></a>

```
{
   "ImportTableDescription": {
      "ClientToken": "string",
      "CloudWatchLogGroupArn": "string",
      "EndTime": number,
      "ErrorCount": number,
      "FailureCode": "string",
      "FailureMessage": "string",
      "ImportArn": "string",
      "ImportedItemCount": number,
      "ImportStatus": "string",
      "InputCompressionType": "string",
      "InputFormat": "string",
      "InputFormatOptions": {
         "Csv": {
            "Delimiter": "string",
            "HeaderList": [ "string" ]
         }
      },
      "ProcessedItemCount": number,
      "ProcessedSizeBytes": number,
      "S3BucketSource": {
         "S3Bucket": "string",
         "S3BucketOwner": "string",
         "S3KeyPrefix": "string"
      },
      "StartTime": number,
      "TableArn": "string",
      "TableCreationParameters": {
         "AttributeDefinitions": [
            {
               "AttributeName": "string",
               "AttributeType": "string"
            }
         ],
         "BillingMode": "string",
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
               },
               "WarmThroughput": {
                  "ReadUnitsPerSecond": number,
                  "WriteUnitsPerSecond": number
               }
            }
         ],
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
         "SSESpecification": {
            "Enabled": boolean,
            "KMSMasterKeyId": "string",
            "SSEType": "string"
         },
         "TableName": "string",
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
      },
      "TableId": "string"
   }
}
```

## Response Elements
<a name="API_ImportTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImportTableDescription](#API_ImportTable_ResponseSyntax) **   <a name="DDB-ImportTable-response-ImportTableDescription"></a>
 Represents the properties of the table created for the import, and parameters of the import. The import parameters include import status, how many items were processed, and how many errors were encountered.
Type: [ImportTableDescription](API_ImportTableDescription.md) object

## Errors
<a name="API_ImportTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ImportConflictException **
 There was a conflict when importing from the specified S3 source. This can occur when the current import conflicts with a previous import request that had the same client token.
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

 ** ResourceInUseException **
The operation conflicts with the resource's availability. For example:
+ You attempted to recreate an existing table.
+ You tried to delete a table currently in the `CREATING` state.
+ You tried to update a resource that was already being updated.
When appropriate, wait for the ongoing update to complete and attempt the request again.
 ** message **
The resource which is being attempted to be changed is in use.
HTTP Status Code: 400

## See Also
<a name="API_ImportTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/ImportTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/ImportTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ImportTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/ImportTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ImportTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/ImportTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/ImportTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/ImportTable)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/ImportTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ImportTable)
