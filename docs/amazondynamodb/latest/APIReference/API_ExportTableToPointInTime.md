---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExportTableToPointInTime.html
---

# ExportTableToPointInTime
<a name="API_ExportTableToPointInTime"></a>

Exports table data to an S3 bucket. The table must have point in time recovery enabled, and you can export data from any time within the point in time recovery window.

## Request Syntax
<a name="API_ExportTableToPointInTime_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "ExportFormat": "{{string}}",
   "ExportTime": {{number}},
   "ExportType": "{{string}}",
   "IncrementalExportSpecification": {
      "ExportFromTime": {{number}},
      "ExportToTime": {{number}},
      "ExportViewType": "{{string}}"
   },
   "S3Bucket": "{{string}}",
   "S3BucketOwner": "{{string}}",
   "S3Prefix": "{{string}}",
   "S3SseAlgorithm": "{{string}}",
   "S3SseKmsKeyId": "{{string}}",
   "TableArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ExportTableToPointInTime_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [S3Bucket](#API_ExportTableToPointInTime_RequestSyntax) **   <a name="DDB-ExportTableToPointInTime-request-S3Bucket"></a>
The name of the Amazon S3 bucket to export the snapshot to.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[a-z0-9A-Z]+[\.\-\w]*[a-z0-9A-Z]+$`
Required: Yes

 ** [TableArn](#API_ExportTableToPointInTime_RequestSyntax) **   <a name="DDB-ExportTableToPointInTime-request-TableArn"></a>
The Amazon Resource Name (ARN) associated with the table to export.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [ClientToken](#API_ExportTableToPointInTime_RequestSyntax) **   <a name="DDB-ExportTableToPointInTime-request-ClientToken"></a>
Providing a `ClientToken` makes the call to `ExportTableToPointInTimeInput` idempotent, meaning that multiple identical calls have the same effect as one single call.
A client token is valid for 8 hours after the first request that uses it is completed. After 8 hours, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 8 hours, or the result might not be idempotent.
If you submit a request with the same client token but a change in other parameters within the 8-hour idempotency window, DynamoDB returns an `ExportConflictException`.
Type: String
Pattern: `^[^\$]+$`
Required: No

 ** [ExportFormat](#API_ExportTableToPointInTime_RequestSyntax) **   <a name="DDB-ExportTableToPointInTime-request-ExportFormat"></a>
The format for the exported data. Valid values for `ExportFormat` are `DYNAMODB_JSON` or `ION`.
Type: String
Valid Values: `DYNAMODB_JSON | ION`
Required: No

 ** [ExportTime](#API_ExportTableToPointInTime_RequestSyntax) **   <a name="DDB-ExportTableToPointInTime-request-ExportTime"></a>
Time in the past from which to export table data, counted in seconds from the start of the Unix epoch. The table export will be a snapshot of the table's state at this point in time.
Type: Timestamp
Required: No

 ** [ExportType](#API_ExportTableToPointInTime_RequestSyntax) **   <a name="DDB-ExportTableToPointInTime-request-ExportType"></a>
Choice of whether to execute as a full export or incremental export. Valid values are FULL\_EXPORT or INCREMENTAL\_EXPORT. The default value is FULL\_EXPORT. If INCREMENTAL\_EXPORT is provided, the IncrementalExportSpecification must also be used.
Type: String
Valid Values: `FULL_EXPORT | INCREMENTAL_EXPORT`
Required: No

 ** [IncrementalExportSpecification](#API_ExportTableToPointInTime_RequestSyntax) **   <a name="DDB-ExportTableToPointInTime-request-IncrementalExportSpecification"></a>
Optional object containing the parameters specific to an incremental export.
Type: [IncrementalExportSpecification](API_IncrementalExportSpecification.md) object
Required: No

 ** [S3BucketOwner](#API_ExportTableToPointInTime_RequestSyntax) **   <a name="DDB-ExportTableToPointInTime-request-S3BucketOwner"></a>
The ID of the AWS account that owns the bucket the export will be stored in.
S3BucketOwner is a required parameter when exporting to a S3 bucket in another account.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [S3Prefix](#API_ExportTableToPointInTime_RequestSyntax) **   <a name="DDB-ExportTableToPointInTime-request-S3Prefix"></a>
The Amazon S3 bucket prefix to use as the file name and path of the exported snapshot.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [S3SseAlgorithm](#API_ExportTableToPointInTime_RequestSyntax) **   <a name="DDB-ExportTableToPointInTime-request-S3SseAlgorithm"></a>
Type of encryption used on the bucket where export data will be stored. Valid values for `S3SseAlgorithm` are:
+  `AES256` - server-side encryption with Amazon S3 managed keys
+  `KMS` - server-side encryption with AWS KMS managed keys
Type: String
Valid Values: `AES256 | KMS`
Required: No

 ** [S3SseKmsKeyId](#API_ExportTableToPointInTime_RequestSyntax) **   <a name="DDB-ExportTableToPointInTime-request-S3SseKmsKeyId"></a>
The ID of the AWS KMS managed key used to encrypt the S3 bucket where export data will be stored (if applicable).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ExportTableToPointInTime_ResponseSyntax"></a>

```
{
   "ExportDescription": {
      "BilledSizeBytes": number,
      "ClientToken": "string",
      "EndTime": number,
      "ExportArn": "string",
      "ExportFormat": "string",
      "ExportManifest": "string",
      "ExportStatus": "string",
      "ExportTime": number,
      "ExportType": "string",
      "FailureCode": "string",
      "FailureMessage": "string",
      "IncrementalExportSpecification": {
         "ExportFromTime": number,
         "ExportToTime": number,
         "ExportViewType": "string"
      },
      "ItemCount": number,
      "S3Bucket": "string",
      "S3BucketOwner": "string",
      "S3Prefix": "string",
      "S3SseAlgorithm": "string",
      "S3SseKmsKeyId": "string",
      "StartTime": number,
      "TableArn": "string",
      "TableId": "string"
   }
}
```

## Response Elements
<a name="API_ExportTableToPointInTime_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExportDescription](#API_ExportTableToPointInTime_ResponseSyntax) **   <a name="DDB-ExportTableToPointInTime-response-ExportDescription"></a>
Contains a description of the table export.
Type: [ExportDescription](API_ExportDescription.md) object

## Errors
<a name="API_ExportTableToPointInTime_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ExportConflictException **
There was a conflict when writing to the specified S3 bucket.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** InvalidExportTimeException **
The specified `ExportTime` is outside of the point in time recovery window.
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

 ** TableNotFoundException **
A source table with the name `TableName` does not currently exist within the subscriber's account or the subscriber is operating in the wrong AWS Region.
HTTP Status Code: 400

## See Also
<a name="API_ExportTableToPointInTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/ExportTableToPointInTime)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/ExportTableToPointInTime)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ExportTableToPointInTime)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/ExportTableToPointInTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ExportTableToPointInTime)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/ExportTableToPointInTime)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/ExportTableToPointInTime)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/ExportTableToPointInTime)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/ExportTableToPointInTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ExportTableToPointInTime)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
