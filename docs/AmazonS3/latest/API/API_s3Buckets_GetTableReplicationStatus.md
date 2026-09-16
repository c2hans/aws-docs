---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableReplicationStatus.html
---

# GetTableReplicationStatus
<a name="API_s3Buckets_GetTableReplicationStatus"></a>

Retrieves the replication status for a table, including the status of replication to each destination. This operation provides visibility into replication health and progress.

Permissions
You must have the `s3tables:GetTableReplicationStatus` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_GetTableReplicationStatus_RequestSyntax"></a>

```
GET /replication-status?tableArn={{tableArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_GetTableReplicationStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableArn](#API_s3Buckets_GetTableReplicationStatus_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableReplicationStatus-request-uri-tableArn"></a>
The Amazon Resource Name (ARN) of the table.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
Required: Yes

## Request Body
<a name="API_s3Buckets_GetTableReplicationStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_GetTableReplicationStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "destinations": [
      {
         "destinationTableArn": "string",
         "destinationTableBucketArn": "string",
         "failureMessage": "string",
         "lastSuccessfulReplicatedUpdate": {
            "metadataLocation": "string",
            "timestamp": "string"
         },
         "replicationStatus": "string"
      }
   ],
   "sourceTableArn": "string"
}
```

## Response Elements
<a name="API_s3Buckets_GetTableReplicationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destinations](#API_s3Buckets_GetTableReplicationStatus_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableReplicationStatus-response-destinations"></a>
An array of status information for each replication destination, including the current state, last successful update, and any error messages.
Type: Array of [ReplicationDestinationStatusModel](API_s3Buckets_ReplicationDestinationStatusModel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [sourceTableArn](#API_s3Buckets_GetTableReplicationStatus_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableReplicationStatus-response-sourceTableArn"></a>
The Amazon Resource Name (ARN) of the source table being replicated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`

## Errors
<a name="API_s3Buckets_GetTableReplicationStatus_Errors"></a>

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
<a name="API_s3Buckets_GetTableReplicationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableReplicationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/GetTableReplicationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableReplicationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableReplicationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableReplicationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableReplicationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableReplicationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableReplicationStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableReplicationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableReplicationStatus)
