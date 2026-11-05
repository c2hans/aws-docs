---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StartBulkPutItems.html
---

# StartBulkPutItems
<a name="API_StartBulkPutItems"></a>

Starts an asynchronous bulk operation that reads items from Amazon S3 and writes them to an existing DynamoDB table, so you can efficiently load or migrate large datasets.

## Request Syntax
<a name="API_StartBulkPutItems_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "InputS3Configuration": {
      "InputCompressionType": "{{string}}",
      "InputFormat": "{{string}}",
      "S3Bucket": "{{string}}",
      "S3BucketOwner": "{{string}}",
      "S3KeyPrefix": "{{string}}"
   },
   "MaxWriteRequestUnits": {{number}},
   "OutputS3Configuration": {
      "OutputType": [ "{{string}}" ],
      "S3Bucket": "{{string}}",
      "S3BucketOwner": "{{string}}",
      "S3KeyPrefix": "{{string}}",
      "S3SseAlgorithm": "{{string}}",
      "S3SseKmsKeyId": "{{string}}"
   },
   "PerformanceTier": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartBulkPutItems_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [InputS3Configuration](#API_StartBulkPutItems_RequestSyntax) **   <a name="DDB-StartBulkPutItems-request-InputS3Configuration"></a>
The Amazon S3 location, data format, and compression settings for the input objects.
Type: [InputS3Configuration](API_InputS3Configuration.md) object
Required: Yes

 ** [OutputS3Configuration](#API_StartBulkPutItems_RequestSyntax) **   <a name="DDB-StartBulkPutItems-request-OutputS3Configuration"></a>
The Amazon S3 location, encryption settings, and output types for the bulk operation.
Type: [OutputS3Configuration](API_OutputS3Configuration.md) object
Required: Yes

 ** [TableName](#API_StartBulkPutItems_RequestSyntax) **   <a name="DDB-StartBulkPutItems-request-TableName"></a>
The name or ARN of the existing DynamoDB table that receives the items.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [ClientToken](#API_StartBulkPutItems_RequestSyntax) **   <a name="DDB-StartBulkPutItems-request-ClientToken"></a>
A unique, case-sensitive identifier that ensures the bulk operation starts no more than one time. During the 8 hours after the initial request, repeated requests that use the same token and parameters return the same bulk operation. If a request reuses the token with different parameters, DynamoDB returns an `IdempotentParameterMismatchException`. If you omit the token, an AWS SDK automatically generates one.
Type: String
Pattern: `^[^\$]+$`
Required: No

 ** [MaxWriteRequestUnits](#API_StartBulkPutItems_RequestSyntax) **   <a name="DDB-StartBulkPutItems-request-MaxWriteRequestUnits"></a>
The maximum rate, in write request units per second, at which the bulk operation attempts to write. The value must be at least 1,024. With this setting, you limit only the bulk operation; the table's provisioned or on-demand capacity settings don't change. The actual write rate can be lower.
Type: Long
Valid Range: Minimum value of 1024.
Required: No

 ** [PerformanceTier](#API_StartBulkPutItems_RequestSyntax) **   <a name="DDB-StartBulkPutItems-request-PerformanceTier"></a>
The performance tier for the bulk operation. Valid values are `STANDARD` and `ACCELERATED`. If you don't specify a value, the operation uses `STANDARD`.
Type: String
Valid Values: `STANDARD | ACCELERATED`
Required: No

## Response Syntax
<a name="API_StartBulkPutItems_ResponseSyntax"></a>

```
{
   "BulkOperationDescription": {
      "BulkOperationArn": "string",
      "BulkOperationStatus": "string",
      "BulkOperationUsage": [
         {
            "BulkPutBytes": number,
            "GlobalSecondaryIndexes": {
               "string" : {
                  "BulkPutBytes": number
               }
            },
            "LocalSecondaryIndexes": {
               "string" : {
                  "BulkPutBytes": number
               }
            },
            "Table": {
               "BulkPutBytes": number
            },
            "TableName": "string",
            "VectorIndexes": {
               "string" : {
                  "BulkPutVectorBytes": number
               }
            }
         }
      ],
      "ClientToken": "string",
      "EndTime": number,
      "FailedItemCount": number,
      "FailureCode": "string",
      "FailureMessage": "string",
      "InputS3Configuration": {
         "InputCompressionType": "string",
         "InputFormat": "string",
         "S3Bucket": "string",
         "S3BucketOwner": "string",
         "S3KeyPrefix": "string"
      },
      "MaxWriteRequestUnits": number,
      "OutputS3Configuration": {
         "OutputType": [ "string" ],
         "S3Bucket": "string",
         "S3BucketOwner": "string",
         "S3KeyPrefix": "string",
         "S3SseAlgorithm": "string",
         "S3SseKmsKeyId": "string"
      },
      "PerformanceTier": "string",
      "ProcessedInputBytes": number,
      "ProcessedItemCount": number,
      "StartTime": number,
      "TableDetails": [
         {
            "TableId": "string",
            "TableName": "string"
         }
      ],
      "TotalInputBytes": number
   }
}
```

## Response Elements
<a name="API_StartBulkPutItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BulkOperationDescription](#API_StartBulkPutItems_ResponseSyntax) **   <a name="DDB-StartBulkPutItems-response-BulkOperationDescription"></a>
Contains detailed information about a bulk operation.
Type: [BulkOperationDescription](API_BulkOperationDescription.md) object

## Errors
<a name="API_StartBulkPutItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IdempotentParameterMismatchException **
DynamoDB rejected the request because you retried a request with a different payload but with an idempotent token that was already used.
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

 ** ResourceNotFoundException **
The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The resource which is being requested does not exist.
HTTP Status Code: 400

## See Also
<a name="API_StartBulkPutItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/StartBulkPutItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/StartBulkPutItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/StartBulkPutItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/StartBulkPutItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/StartBulkPutItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/StartBulkPutItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/StartBulkPutItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/StartBulkPutItems)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/StartBulkPutItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/StartBulkPutItems)
