---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableBucketReplication.html
---

# DeleteTableBucketReplication
<a name="API_s3Buckets_DeleteTableBucketReplication"></a>

Deletes the replication configuration for a table bucket. After deletion, new table updates will no longer be replicated to destination buckets, though existing replicated tables will remain in destination buckets.

Permissions
You must have the `s3tables:DeleteTableBucketReplication` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_DeleteTableBucketReplication_RequestSyntax"></a>

```
DELETE /table-bucket-replication?tableBucketARN={{tableBucketARN}}&versionToken={{versionToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_DeleteTableBucketReplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableBucketARN](#API_s3Buckets_DeleteTableBucketReplication_RequestSyntax) **   <a name="AmazonS3-s3Buckets_DeleteTableBucketReplication-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

 ** [versionToken](#API_s3Buckets_DeleteTableBucketReplication_RequestSyntax) **   <a name="AmazonS3-s3Buckets_DeleteTableBucketReplication-request-uri-versionToken"></a>
A version token from a previous GetTableBucketReplication call. Use this token to ensure you're deleting the expected version of the configuration.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_s3Buckets_DeleteTableBucketReplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_DeleteTableBucketReplication_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_s3Buckets_DeleteTableBucketReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_s3Buckets_DeleteTableBucketReplication_Errors"></a>

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
<a name="API_s3Buckets_DeleteTableBucketReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/DeleteTableBucketReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/DeleteTableBucketReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/DeleteTableBucketReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/DeleteTableBucketReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/DeleteTableBucketReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/DeleteTableBucketReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/DeleteTableBucketReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/DeleteTableBucketReplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/DeleteTableBucketReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/DeleteTableBucketReplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
