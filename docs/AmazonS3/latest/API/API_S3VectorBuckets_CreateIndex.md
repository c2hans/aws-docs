---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateIndex.html
---

# CreateIndex
<a name="API_S3VectorBuckets_CreateIndex"></a>

Creates a vector index within a vector bucket. To specify the vector bucket, you must use either the vector bucket name or the vector bucket Amazon Resource Name (ARN).

Permissions
You must have the `s3vectors:CreateIndex` permission to use this operation.
You must have the `s3vectors:TagResource` permission in addition to `s3vectors:CreateIndex` permission to create a vector index with tags.

## Request Syntax
<a name="API_S3VectorBuckets_CreateIndex_RequestSyntax"></a>

```
POST /CreateIndex HTTP/1.1
Content-type: application/json

{
   "dataType": "{{string}}",
   "dimension": {{number}},
   "distanceMetric": "{{string}}",
   "encryptionConfiguration": {
      "kmsKeyArn": "{{string}}",
      "sseType": "{{string}}"
   },
   "indexName": "{{string}}",
   "metadataConfiguration": {
      "nonFilterableMetadataKeys": [ "{{string}}" ]
   },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "vectorBucketArn": "{{string}}",
   "vectorBucketName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_S3VectorBuckets_CreateIndex_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_S3VectorBuckets_CreateIndex_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dataType](#API_S3VectorBuckets_CreateIndex_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateIndex-request-dataType"></a>
The data type of the vectors to be inserted into the vector index.
Type: String
Valid Values: `float32`
Required: Yes

 ** [dimension](#API_S3VectorBuckets_CreateIndex_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateIndex-request-dimension"></a>
The dimensions of the vectors to be inserted into the vector index.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 4096.
Required: Yes

 ** [distanceMetric](#API_S3VectorBuckets_CreateIndex_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateIndex-request-distanceMetric"></a>
The distance metric to be used for similarity search.
Type: String
Valid Values: `euclidean | cosine`
Required: Yes

 ** [encryptionConfiguration](#API_S3VectorBuckets_CreateIndex_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateIndex-request-encryptionConfiguration"></a>
The encryption configuration for a vector index. By default, if you don't specify, all new vectors in the vector index will use the encryption configuration of the vector bucket.
Type: [EncryptionConfiguration](API_S3VectorBuckets_EncryptionConfiguration.md) object
Required: No

 ** [indexName](#API_S3VectorBuckets_CreateIndex_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateIndex-request-indexName"></a>
The name of the vector index to create.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** [metadataConfiguration](#API_S3VectorBuckets_CreateIndex_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateIndex-request-metadataConfiguration"></a>
The metadata configuration for the vector index.
Type: [MetadataConfiguration](API_S3VectorBuckets_MetadataConfiguration.md) object
Required: No

 ** [tags](#API_S3VectorBuckets_CreateIndex_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateIndex-request-tags"></a>
An array of user-defined tags that you would like to apply to the vector index that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize, track costs, and control access to resources. For more information, see [Tagging for cost allocation or attribute-based access control (ABAC)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html).
You must have the `s3vectors:TagResource` permission in addition to `s3vectors:CreateIndex` permission to create a vector index with tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

 ** [vectorBucketArn](#API_S3VectorBuckets_CreateIndex_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateIndex-request-vectorBucketArn"></a>
The Amazon Resource Name (ARN) of the vector bucket to create the vector index in.
Type: String
Pattern: `arn:aws[-a-z0-9]*:s3vectors:[a-z0-9-]+:[0-9]{12}:bucket/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]`
Required: No

 ** [vectorBucketName](#API_S3VectorBuckets_CreateIndex_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateIndex-request-vectorBucketName"></a>
The name of the vector bucket to create the vector index in.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

## Response Syntax
<a name="API_S3VectorBuckets_CreateIndex_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "indexArn": "string"
}
```

## Response Elements
<a name="API_S3VectorBuckets_CreateIndex_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [indexArn](#API_S3VectorBuckets_CreateIndex_ResponseSyntax) **   <a name="AmazonS3-S3VectorBuckets_CreateIndex-response-indexArn"></a>
The Amazon Resource Name (ARN) of the newly created vector index.
Type: String
Pattern: `arn:aws[-a-z0-9]*:s3vectors:[a-z0-9-]+:[0-9]{12}:bucket/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]/index/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]`

## Errors
<a name="API_S3VectorBuckets_CreateIndex_Errors"></a>

 ** AccessDeniedException **
Access denied.
HTTP Status Code: 403

 ** ConflictException **
The request failed because a vector bucket name or a vector index name already exists. Vector bucket names must be unique within your AWS account for each AWS Region. Vector index names must be unique within your vector bucket. Choose a different vector bucket name or vector index name, and try again.
HTTP Status Code: 409

 ** InternalServerException **
The request failed due to an internal server error.
HTTP Status Code: 500

 ** NotFoundException **
The request was rejected because the specified resource can't be found.
HTTP Status Code: 404

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
<a name="API_S3VectorBuckets_CreateIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/CreateIndex)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3vectors-2025-07-15/CreateIndex)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/CreateIndex)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/CreateIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/CreateIndex)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/CreateIndex)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/CreateIndex)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/CreateIndex)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/CreateIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/CreateIndex)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
