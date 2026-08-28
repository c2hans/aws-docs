---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketStorageClass.html
---

# PutTableBucketStorageClass
<a name="API_s3Buckets_PutTableBucketStorageClass"></a>

Sets or updates the storage class configuration for a table bucket. This configuration serves as the default storage class for all new tables created in the bucket, allowing you to optimize storage costs at the bucket level.

Permissions
You must have the `s3tables:PutTableBucketStorageClass` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_PutTableBucketStorageClass_RequestSyntax"></a>

```
PUT /buckets/{{tableBucketARN}}/storage-class HTTP/1.1
Content-type: application/json

{
   "storageClassConfiguration": {
      "storageClass": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_s3Buckets_PutTableBucketStorageClass_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableBucketARN](#API_s3Buckets_PutTableBucketStorageClass_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableBucketStorageClass-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

## Request Body
<a name="API_s3Buckets_PutTableBucketStorageClass_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [storageClassConfiguration](#API_s3Buckets_PutTableBucketStorageClass_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableBucketStorageClass-request-storageClassConfiguration"></a>
The storage class configuration to apply to the table bucket. This configuration will serve as the default for new tables created in this bucket.
Type: [StorageClassConfiguration](API_s3Buckets_StorageClassConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_s3Buckets_PutTableBucketStorageClass_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_s3Buckets_PutTableBucketStorageClass_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_s3Buckets_PutTableBucketStorageClass_Errors"></a>

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
<a name="API_s3Buckets_PutTableBucketStorageClass_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/PutTableBucketStorageClass)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/PutTableBucketStorageClass)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PutTableBucketStorageClass)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/PutTableBucketStorageClass)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PutTableBucketStorageClass)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/PutTableBucketStorageClass)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/PutTableBucketStorageClass)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/PutTableBucketStorageClass)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/PutTableBucketStorageClass)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PutTableBucketStorageClass)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
