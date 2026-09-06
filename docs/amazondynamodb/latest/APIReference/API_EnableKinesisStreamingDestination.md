---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_EnableKinesisStreamingDestination.html
---

# EnableKinesisStreamingDestination
<a name="API_EnableKinesisStreamingDestination"></a>

Starts table data replication to the specified Kinesis data stream at a timestamp chosen during the enable workflow. If this operation doesn't return results immediately, use DescribeKinesisStreamingDestination to check if streaming to the Kinesis data stream is ACTIVE.

## Request Syntax
<a name="API_EnableKinesisStreamingDestination_RequestSyntax"></a>

```
{
   "EnableKinesisStreamingConfiguration": {
      "ApproximateCreationDateTimePrecision": "{{string}}"
   },
   "StreamArn": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_EnableKinesisStreamingDestination_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [StreamArn](#API_EnableKinesisStreamingDestination_RequestSyntax) **   <a name="DDB-EnableKinesisStreamingDestination-request-StreamArn"></a>
The ARN for a Kinesis data stream.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: Yes

 ** [TableName](#API_EnableKinesisStreamingDestination_RequestSyntax) **   <a name="DDB-EnableKinesisStreamingDestination-request-TableName"></a>
The name of the DynamoDB table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [EnableKinesisStreamingConfiguration](#API_EnableKinesisStreamingDestination_RequestSyntax) **   <a name="DDB-EnableKinesisStreamingDestination-request-EnableKinesisStreamingConfiguration"></a>
The source for the Kinesis streaming information that is being enabled.
Type: [EnableKinesisStreamingConfiguration](API_EnableKinesisStreamingConfiguration.md) object
Required: No

## Response Syntax
<a name="API_EnableKinesisStreamingDestination_ResponseSyntax"></a>

```
{
   "DestinationStatus": "string",
   "EnableKinesisStreamingConfiguration": {
      "ApproximateCreationDateTimePrecision": "string"
   },
   "StreamArn": "string",
   "TableName": "string"
}
```

## Response Elements
<a name="API_EnableKinesisStreamingDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DestinationStatus](#API_EnableKinesisStreamingDestination_ResponseSyntax) **   <a name="DDB-EnableKinesisStreamingDestination-response-DestinationStatus"></a>
The current status of the replication.
Type: String
Valid Values: `ENABLING | ACTIVE | DISABLING | DISABLED | ENABLE_FAILED | UPDATING`

 ** [EnableKinesisStreamingConfiguration](#API_EnableKinesisStreamingDestination_ResponseSyntax) **   <a name="DDB-EnableKinesisStreamingDestination-response-EnableKinesisStreamingConfiguration"></a>
The destination for the Kinesis streaming information that is being enabled.
Type: [EnableKinesisStreamingConfiguration](API_EnableKinesisStreamingConfiguration.md) object

 ** [StreamArn](#API_EnableKinesisStreamingDestination_ResponseSyntax) **   <a name="DDB-EnableKinesisStreamingDestination-response-StreamArn"></a>
The ARN for the specific Kinesis data stream.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.

 ** [TableName](#API_EnableKinesisStreamingDestination_ResponseSyntax) **   <a name="DDB-EnableKinesisStreamingDestination-response-TableName"></a>
The name of the table being modified.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_EnableKinesisStreamingDestination_Errors"></a>

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

## See Also
<a name="API_EnableKinesisStreamingDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/EnableKinesisStreamingDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/EnableKinesisStreamingDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/EnableKinesisStreamingDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/EnableKinesisStreamingDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/EnableKinesisStreamingDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/EnableKinesisStreamingDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/EnableKinesisStreamingDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/EnableKinesisStreamingDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/EnableKinesisStreamingDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/EnableKinesisStreamingDestination)
