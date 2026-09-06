---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_TagResource.html
---

# TagResource
<a name="API_S3VectorBuckets_TagResource"></a>

Applies one or more user-defined tags to an Amazon S3 Vectors resource or updates existing tags. Each tag is a label consisting of a key and value pair. Tags can help you organize, track costs for, and control access to your resources. You can add up to 50 tags for each resource.

**Note**
For a list of S3 resources that support tagging, see [Managing tags for Amazon S3 resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags).

Permissions
For vector buckets and vector indexes, you must have the `s3vectors:TagResource` permission to use this operation.

## Request Syntax
<a name="API_S3VectorBuckets_TagResource_RequestSyntax"></a>

```
POST /tags/{{resourceArn}} HTTP/1.1
Content-type: application/json

{
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_S3VectorBuckets_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_S3VectorBuckets_TagResource_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_TagResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 Vectors resource that you're applying tags to. The tagged resource can be a vector bucket or a vector index.
Length Constraints: Minimum length of 0. Maximum length of 1011.
Required: Yes

## Request Body
<a name="API_S3VectorBuckets_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_S3VectorBuckets_TagResource_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_TagResource-request-tags"></a>
The user-defined tag that you want to add to the specified S3 Vectors resource. For more information, see [Tagging for cost allocation or attribute-based access control (ABAC)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html).
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

## Response Syntax
<a name="API_S3VectorBuckets_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_S3VectorBuckets_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_S3VectorBuckets_TagResource_Errors"></a>

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
<a name="API_S3VectorBuckets_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3vectors-2025-07-15/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/TagResource)
