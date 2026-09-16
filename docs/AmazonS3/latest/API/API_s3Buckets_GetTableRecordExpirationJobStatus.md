---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableRecordExpirationJobStatus.html
---

# GetTableRecordExpirationJobStatus
<a name="API_s3Buckets_GetTableRecordExpirationJobStatus"></a>

Retrieves the status, metrics, and details of the latest record expiration job for a table. This includes when the job ran, and whether it succeeded or failed. If the job ran successfully, this also includes statistics about the records that were removed.

Permissions
You must have the `s3tables:GetTableRecordExpirationJobStatus` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_GetTableRecordExpirationJobStatus_RequestSyntax"></a>

```
GET /table-record-expiration-job-status?tableArn={{tableArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_GetTableRecordExpirationJobStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableArn](#API_s3Buckets_GetTableRecordExpirationJobStatus_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableRecordExpirationJobStatus-request-uri-tableArn"></a>
The Amazon Resource Name (ARN) of the table.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
Required: Yes

## Request Body
<a name="API_s3Buckets_GetTableRecordExpirationJobStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_GetTableRecordExpirationJobStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failureMessage": "string",
   "lastRunTimestamp": "string",
   "metrics": {
      "deletedDataFiles": number,
      "deletedRecords": number,
      "removedFilesSize": number
   },
   "status": "string"
}
```

## Response Elements
<a name="API_s3Buckets_GetTableRecordExpirationJobStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failureMessage](#API_s3Buckets_GetTableRecordExpirationJobStatus_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableRecordExpirationJobStatus-response-failureMessage"></a>
If the job failed, this field contains an error message describing the failure reason.
Type: String

 ** [lastRunTimestamp](#API_s3Buckets_GetTableRecordExpirationJobStatus_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableRecordExpirationJobStatus-response-lastRunTimestamp"></a>
The timestamp when the expiration job was last executed.
Type: Timestamp

 ** [metrics](#API_s3Buckets_GetTableRecordExpirationJobStatus_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableRecordExpirationJobStatus-response-metrics"></a>
Metrics about the most recent expiration job execution, including the number of records and files deleted.
Type: [TableRecordExpirationJobMetrics](API_s3Buckets_TableRecordExpirationJobMetrics.md) object

 ** [status](#API_s3Buckets_GetTableRecordExpirationJobStatus_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableRecordExpirationJobStatus-response-status"></a>
The current status of the most recent expiration job.
Type: String
Valid Values: `NotYetRun | Successful | Failed | Disabled`

## Errors
<a name="API_s3Buckets_GetTableRecordExpirationJobStatus_Errors"></a>

 ** BadRequestException **
The request is invalid or malformed.
HTTP Status Code: 400

 ** ForbiddenException **
The caller isn't authorized to make the request.
HTTP Status Code: 403

 ** InternalServerErrorException **
The request failed due to an internal server error.
HTTP Status Code: 500

 ** MethodNotAllowedException **
The requested operation is not allowed on this resource. This may occur when attempting to modify a resource that is managed by a service or has restrictions that prevent the operation.
HTTP Status Code: 405

 ** NotFoundException **
The request was rejected because the specified resource could not be found.
HTTP Status Code: 404

 ** TooManyRequestsException **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

## See Also
<a name="API_s3Buckets_GetTableRecordExpirationJobStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableRecordExpirationJobStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/GetTableRecordExpirationJobStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableRecordExpirationJobStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableRecordExpirationJobStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableRecordExpirationJobStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableRecordExpirationJobStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableRecordExpirationJobStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableRecordExpirationJobStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableRecordExpirationJobStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableRecordExpirationJobStatus)
