---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableReplication.html
---

# DeleteTableReplication
<a name="API_s3Buckets_DeleteTableReplication"></a>

Deletes the replication configuration for a specific table. After deletion, new updates to this table will no longer be replicated to destination tables, though existing replicated copies will remain in destination buckets.

Permissions
You must have the `s3tables:DeleteTableReplication` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_DeleteTableReplication_RequestSyntax"></a>

```
DELETE /table-replication?tableArn={{tableArn}}&versionToken={{versionToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_DeleteTableReplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableArn](#API_s3Buckets_DeleteTableReplication_RequestSyntax) **   <a name="AmazonS3-s3Buckets_DeleteTableReplication-request-uri-tableArn"></a>
The Amazon Resource Name (ARN) of the table.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63}/table/[a-zA-Z0-9-_]{1,255})`
Required: Yes

 ** [versionToken](#API_s3Buckets_DeleteTableReplication_RequestSyntax) **   <a name="AmazonS3-s3Buckets_DeleteTableReplication-request-uri-versionToken"></a>
A version token from a previous GetTableReplication call. Use this token to ensure you're deleting the expected version of the configuration.
Required: Yes

## Request Body
<a name="API_s3Buckets_DeleteTableReplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_DeleteTableReplication_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_s3Buckets_DeleteTableReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_s3Buckets_DeleteTableReplication_Errors"></a>

 ** AccessDeniedException **
The action cannot be performed because you do not have the required permission.
HTTP Status Code: 403

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
<a name="API_s3Buckets_DeleteTableReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/DeleteTableReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/DeleteTableReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/DeleteTableReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/DeleteTableReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/DeleteTableReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/DeleteTableReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/DeleteTableReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/DeleteTableReplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/DeleteTableReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/DeleteTableReplication)
