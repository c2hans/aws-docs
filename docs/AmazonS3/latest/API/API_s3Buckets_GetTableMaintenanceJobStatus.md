---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableMaintenanceJobStatus.html
---

# GetTableMaintenanceJobStatus
<a name="API_s3Buckets_GetTableMaintenanceJobStatus"></a>

Gets the status of a maintenance job for a table. For more information, see [S3 Tables maintenance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html) in the *Amazon Simple Storage Service User Guide*.

Permissions
You must have the `s3tables:GetTableMaintenanceJobStatus` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_GetTableMaintenanceJobStatus_RequestSyntax"></a>

```
GET /tables/{{tableBucketARN}}/{{namespace}}/{{name}}/maintenance-job-status HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_GetTableMaintenanceJobStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_s3Buckets_GetTableMaintenanceJobStatus_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMaintenanceJobStatus-request-uri-name"></a>
The name of the table containing the maintenance job status you want to check.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

 ** [namespace](#API_s3Buckets_GetTableMaintenanceJobStatus_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMaintenanceJobStatus-request-uri-namespace"></a>
The name of the namespace the table is associated with.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

 ** [tableBucketARN](#API_s3Buckets_GetTableMaintenanceJobStatus_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMaintenanceJobStatus-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

## Request Body
<a name="API_s3Buckets_GetTableMaintenanceJobStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_GetTableMaintenanceJobStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": {
      "string" : {
         "failureMessage": "string",
         "lastRunTimestamp": "string",
         "status": "string"
      }
   },
   "tableARN": "string"
}
```

## Response Elements
<a name="API_s3Buckets_GetTableMaintenanceJobStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_s3Buckets_GetTableMaintenanceJobStatus_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMaintenanceJobStatus-response-status"></a>
The status of the maintenance job.
Type: String to [TableMaintenanceJobStatusValue](API_s3Buckets_TableMaintenanceJobStatusValue.md) object map
Valid Keys: `icebergCompaction | icebergSnapshotManagement | icebergUnreferencedFileRemoval`

 ** [tableARN](#API_s3Buckets_GetTableMaintenanceJobStatus_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMaintenanceJobStatus-response-tableARN"></a>
The Amazon Resource Name (ARN) of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`

## Errors
<a name="API_s3Buckets_GetTableMaintenanceJobStatus_Errors"></a>

 ** BadRequestException **
The request is invalid or malformed.
HTTP Status Code: 400

 ** ConflictException **
The request failed because there is a conflict with a previous write. You can retry the request.
HTTP Status Code: 409

 ** ForbiddenException **
The caller isn't authorized to make the request.
HTTP Status Code: 403

 ** InternalServerErrorException **
The request failed due to an internal server error.
HTTP Status Code: 500

 ** NotFoundException **
The request was rejected because the specified resource could not be found.
HTTP Status Code: 404

 ** TooManyRequestsException **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

## See Also
<a name="API_s3Buckets_GetTableMaintenanceJobStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableMaintenanceJobStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/GetTableMaintenanceJobStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableMaintenanceJobStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableMaintenanceJobStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableMaintenanceJobStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableMaintenanceJobStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableMaintenanceJobStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableMaintenanceJobStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableMaintenanceJobStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableMaintenanceJobStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
