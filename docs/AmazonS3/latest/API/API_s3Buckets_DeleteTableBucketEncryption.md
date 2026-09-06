---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableBucketEncryption.html
---

# DeleteTableBucketEncryption
<a name="API_s3Buckets_DeleteTableBucketEncryption"></a>

Deletes the encryption configuration for a table bucket.

Permissions
You must have the `s3tables:DeleteTableBucketEncryption` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_DeleteTableBucketEncryption_RequestSyntax"></a>

```
DELETE /buckets/{{tableBucketARN}}/encryption HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_DeleteTableBucketEncryption_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableBucketARN](#API_s3Buckets_DeleteTableBucketEncryption_RequestSyntax) **   <a name="AmazonS3-s3Buckets_DeleteTableBucketEncryption-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

## Request Body
<a name="API_s3Buckets_DeleteTableBucketEncryption_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_DeleteTableBucketEncryption_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_s3Buckets_DeleteTableBucketEncryption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_s3Buckets_DeleteTableBucketEncryption_Errors"></a>

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
<a name="API_s3Buckets_DeleteTableBucketEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/DeleteTableBucketEncryption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/DeleteTableBucketEncryption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/DeleteTableBucketEncryption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/DeleteTableBucketEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/DeleteTableBucketEncryption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/DeleteTableBucketEncryption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/DeleteTableBucketEncryption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/DeleteTableBucketEncryption)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/DeleteTableBucketEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/DeleteTableBucketEncryption)
