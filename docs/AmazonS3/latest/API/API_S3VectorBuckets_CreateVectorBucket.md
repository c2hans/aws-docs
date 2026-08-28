---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateVectorBucket.html
---

# CreateVectorBucket
<a name="API_S3VectorBuckets_CreateVectorBucket"></a>

Creates a vector bucket in the AWS Region that you want your bucket to be in.

Permissions
You must have the `s3vectors:CreateVectorBucket` permission to use this operation.
You must have the `s3vectors:TagResource` permission in addition to `s3vectors:CreateVectorBucket` permission to create a vector bucket with tags.

## Request Syntax
<a name="API_S3VectorBuckets_CreateVectorBucket_RequestSyntax"></a>

```
POST /CreateVectorBucket HTTP/1.1
Content-type: application/json

{
   "encryptionConfiguration": {
      "kmsKeyArn": "{{string}}",
      "sseType": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "vectorBucketName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_S3VectorBuckets_CreateVectorBucket_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_S3VectorBuckets_CreateVectorBucket_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [encryptionConfiguration](#API_S3VectorBuckets_CreateVectorBucket_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateVectorBucket-request-encryptionConfiguration"></a>
The encryption configuration for the vector bucket. By default, if you don't specify, all new vectors in Amazon S3 vector buckets use server-side encryption with Amazon S3 managed keys (SSE-S3), specifically `AES256`.
Type: [EncryptionConfiguration](API_S3VectorBuckets_EncryptionConfiguration.md) object
Required: No

 ** [tags](#API_S3VectorBuckets_CreateVectorBucket_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateVectorBucket-request-tags"></a>
An array of user-defined tags that you would like to apply to the vector bucket that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize and control access to resources. For more information, see [Tagging for cost allocation or attribute-based access control (ABAC)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html).
You must have the `s3vectors:TagResource` permission in addition to `s3vectors:CreateVectorBucket` permission to create a vector bucket with tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

 ** [vectorBucketName](#API_S3VectorBuckets_CreateVectorBucket_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateVectorBucket-request-vectorBucketName"></a>
The name of the vector bucket to create.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

## Response Syntax
<a name="API_S3VectorBuckets_CreateVectorBucket_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "vectorBucketArn": "string"
}
```

## Response Elements
<a name="API_S3VectorBuckets_CreateVectorBucket_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [vectorBucketArn](#API_S3VectorBuckets_CreateVectorBucket_ResponseSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateVectorBucket-response-vectorBucketArn"></a>
The Amazon Resource Name (ARN) of the newly created vector bucket.
Type: String
Pattern: `arn:aws[-a-z0-9]*:s3vectors:[a-z0-9-]+:[0-9]{12}:bucket/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]`

## Errors
<a name="API_S3VectorBuckets_CreateVectorBucket_Errors"></a>

 ** AccessDeniedException **
Access denied.
HTTP Status Code: 403

 ** ConflictException **
The request failed because a vector bucket name or a vector index name already exists. Vector bucket names must be unique within your AWS account for each AWS Region. Vector index names must be unique within your vector bucket. Choose a different vector bucket name or vector index name, and try again.
HTTP Status Code: 409

 ** InternalServerException **
The request failed due to an internal server error.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out. Retry your request.
HTTP Status Code: 408

 ** ServiceQuotaExceededException **
Your request exceeds a service quota.
HTTP Status Code: 402

 ** ServiceUnavailableException **
The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The requested action isn't valid.
 ** fieldList **
A list of specific validation failures that are encountered during input processing. Each entry in the list contains a path to the field that failed validation and a detailed message that explains why the validation failed. To satisfy multiple constraints, a field can appear multiple times in this list if it failed. You can use the information to identify and fix the specific validation issues in your request.
HTTP Status Code: 400

## See Also
<a name="API_S3VectorBuckets_CreateVectorBucket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/CreateVectorBucket)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3vectors-2025-07-15/CreateVectorBucket)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/CreateVectorBucket)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/CreateVectorBucket)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/CreateVectorBucket)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/CreateVectorBucket)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/CreateVectorBucket)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/CreateVectorBucket)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/CreateVectorBucket)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/CreateVectorBucket)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
