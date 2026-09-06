---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutVectorBucketPolicy.html
---

# PutVectorBucketPolicy
<a name="API_S3VectorBuckets_PutVectorBucketPolicy"></a>

Creates a bucket policy for a vector bucket. To specify the bucket, you must use either the vector bucket name or the vector bucket Amazon Resource Name (ARN).

Permissions
You must have the `s3vectors:PutVectorBucketPolicy` permission to use this operation.

## Request Syntax
<a name="API_S3VectorBuckets_PutVectorBucketPolicy_RequestSyntax"></a>

```
POST /PutVectorBucketPolicy HTTP/1.1
Content-type: application/json

{
   "policy": "{{string}}",
   "vectorBucketArn": "{{string}}",
   "vectorBucketName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_S3VectorBuckets_PutVectorBucketPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_S3VectorBuckets_PutVectorBucketPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policy](#API_S3VectorBuckets_PutVectorBucketPolicy_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_PutVectorBucketPolicy-request-policy"></a>
The `JSON` that defines the policy. For more information about bucket policies for S3 Vectors, see [Managing vector bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-bucket-policy.html) in the *Amazon S3 User Guide*.
Type: String
Required: Yes

 ** [vectorBucketArn](#API_S3VectorBuckets_PutVectorBucketPolicy_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_PutVectorBucketPolicy-request-vectorBucketArn"></a>
The Amazon Resource Name (ARN) of the vector bucket.
Type: String
Pattern: `arn:aws[-a-z0-9]*:s3vectors:[a-z0-9-]+:[0-9]{12}:bucket/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]`
Required: No

 ** [vectorBucketName](#API_S3VectorBuckets_PutVectorBucketPolicy_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_PutVectorBucketPolicy-request-vectorBucketName"></a>
The name of the vector bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

## Response Syntax
<a name="API_S3VectorBuckets_PutVectorBucketPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_S3VectorBuckets_PutVectorBucketPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_S3VectorBuckets_PutVectorBucketPolicy_Errors"></a>

 ** AccessDeniedException **
Access denied.
HTTP Status Code: 403

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
<a name="API_S3VectorBuckets_PutVectorBucketPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/PutVectorBucketPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3vectors-2025-07-15/PutVectorBucketPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/PutVectorBucketPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/PutVectorBucketPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/PutVectorBucketPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/PutVectorBucketPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/PutVectorBucketPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/PutVectorBucketPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/PutVectorBucketPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/PutVectorBucketPolicy)
