---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketEncryption.html
---

# PutTableBucketEncryption
<a name="API_s3Buckets_PutTableBucketEncryption"></a>

Sets the encryption configuration for a table bucket.

Permissions
You must have the `s3tables:PutTableBucketEncryption` permission to use this operation.
If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see [Permissions requirements for S3 Tables SSE-KMS encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html) in the *Amazon Simple Storage Service User Guide*.

## Request Syntax
<a name="API_s3Buckets_PutTableBucketEncryption_RequestSyntax"></a>

```
PUT /buckets/{{tableBucketARN}}/encryption HTTP/1.1
Content-type: application/json

{
   "encryptionConfiguration": {
      "kmsKeyArn": "{{string}}",
      "sseAlgorithm": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_s3Buckets_PutTableBucketEncryption_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableBucketARN](#API_s3Buckets_PutTableBucketEncryption_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableBucketEncryption-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

## Request Body
<a name="API_s3Buckets_PutTableBucketEncryption_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [encryptionConfiguration](#API_s3Buckets_PutTableBucketEncryption_RequestSyntax) **   <a name="AmazonS3-s3Buckets_PutTableBucketEncryption-request-encryptionConfiguration"></a>
The encryption configuration to apply to the table bucket.
Type: [EncryptionConfiguration](API_s3Buckets_EncryptionConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_s3Buckets_PutTableBucketEncryption_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_s3Buckets_PutTableBucketEncryption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_s3Buckets_PutTableBucketEncryption_Errors"></a>

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
<a name="API_s3Buckets_PutTableBucketEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/PutTableBucketEncryption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/PutTableBucketEncryption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/PutTableBucketEncryption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/PutTableBucketEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/PutTableBucketEncryption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/PutTableBucketEncryption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/PutTableBucketEncryption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/PutTableBucketEncryption)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/PutTableBucketEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/PutTableBucketEncryption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
