---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateTableBucket.html
---

# CreateTableBucket
<a name="API_s3Buckets_CreateTableBucket"></a>

Creates a table bucket. For more information, see [Creating a table bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-create.html) in the *Amazon Simple Storage Service User Guide*.

Permissions
+ You must have the `s3tables:CreateTableBucket` permission to use this operation.
+ If you use this operation with the optional `encryptionConfiguration` parameter you must have the `s3tables:PutTableBucketEncryption` permission.
+ If you use this operation with the `storageClassConfiguration` request parameter, you must have the `s3tables:PutTableBucketStorageClass` permission.
+ To create a table bucket with tags, you must have the `s3tables:TagResource` permission in addition to `s3tables:CreateTableBucket` permission.

## Request Syntax
<a name="API_s3Buckets_CreateTableBucket_RequestSyntax"></a>

```
PUT /buckets HTTP/1.1
Content-type: application/json

{
   "encryptionConfiguration": {
      "kmsKeyArn": "{{string}}",
      "sseAlgorithm": "{{string}}"
   },
   "name": "{{string}}",
   "storageClassConfiguration": {
      "storageClass": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_s3Buckets_CreateTableBucket_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_s3Buckets_CreateTableBucket_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [encryptionConfiguration](#API_s3Buckets_CreateTableBucket_RequestSyntax) **   <a name="AmazonS3-s3Buckets_CreateTableBucket-request-encryptionConfiguration"></a>
The encryption configuration to use for the table bucket. This configuration specifies the default encryption settings that will be applied to all tables created in this bucket unless overridden at the table level. The configuration includes the encryption algorithm and, if using SSE-KMS, the KMS key to use.
Type: [EncryptionConfiguration](API_s3Buckets_EncryptionConfiguration.md) object
Required: No

 ** [name](#API_s3Buckets_CreateTableBucket_RequestSyntax) **   <a name="AmazonS3-s3Buckets_CreateTableBucket-request-name"></a>
The name for the table bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[0-9a-z-]*`
Required: Yes

 ** [storageClassConfiguration](#API_s3Buckets_CreateTableBucket_RequestSyntax) **   <a name="AmazonS3-s3Buckets_CreateTableBucket-request-storageClassConfiguration"></a>
The default storage class configuration for the table bucket. This configuration will be applied to all new tables created in this bucket unless overridden at the table level. If not specified, the service default storage class will be used.
Type: [StorageClassConfiguration](API_s3Buckets_StorageClassConfiguration.md) object
Required: No

 ** [tags](#API_s3Buckets_CreateTableBucket_RequestSyntax) **   <a name="AmazonS3-s3Buckets_CreateTableBucket-request-tags"></a>
A map of user-defined tags that you would like to apply to the table bucket that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize and control access to resources. For more information, see [Tagging for cost allocation or attribute-based access control (ABAC)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html).
You must have the `s3tables:TagResource` permission in addition to `s3tables:CreateTableBucket` permisson to create a table bucket with tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_s3Buckets_CreateTableBucket_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string"
}
```

## Response Elements
<a name="API_s3Buckets_CreateTableBucket_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_s3Buckets_CreateTableBucket_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_CreateTableBucket-response-arn"></a>
The Amazon Resource Name (ARN) of the table bucket.
Type: String
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`

## Errors
<a name="API_s3Buckets_CreateTableBucket_Errors"></a>

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
<a name="API_s3Buckets_CreateTableBucket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/CreateTableBucket)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/CreateTableBucket)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/CreateTableBucket)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/CreateTableBucket)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/CreateTableBucket)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/CreateTableBucket)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/CreateTableBucket)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/CreateTableBucket)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/CreateTableBucket)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/CreateTableBucket)
