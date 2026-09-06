---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListIndexes.html
---

# ListIndexes
<a name="API_S3VectorBuckets_ListIndexes"></a>

Returns a list of all the vector indexes within the specified vector bucket. To specify the bucket, you must use either the vector bucket name or the vector bucket Amazon Resource Name (ARN).

Permissions
You must have the `s3vectors:ListIndexes` permission to use this operation.

## Request Syntax
<a name="API_S3VectorBuckets_ListIndexes_RequestSyntax"></a>

```
POST /ListIndexes HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "prefix": "{{string}}",
   "vectorBucketArn": "{{string}}",
   "vectorBucketName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_S3VectorBuckets_ListIndexes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_S3VectorBuckets_ListIndexes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_S3VectorBuckets_ListIndexes_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListIndexes-request-maxResults"></a>
The maximum number of items to be returned in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [nextToken](#API_S3VectorBuckets_ListIndexes_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListIndexes-request-nextToken"></a>
The previous pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [prefix](#API_S3VectorBuckets_ListIndexes_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListIndexes-request-prefix"></a>
Limits the response to vector indexes that begin with the specified prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: No

 ** [vectorBucketArn](#API_S3VectorBuckets_ListIndexes_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListIndexes-request-vectorBucketArn"></a>
The ARN of the vector bucket that contains the vector indexes.
Type: String
Pattern: `arn:aws[-a-z0-9]*:s3vectors:[a-z0-9-]+:[0-9]{12}:bucket/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]`
Required: No

 ** [vectorBucketName](#API_S3VectorBuckets_ListIndexes_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListIndexes-request-vectorBucketName"></a>
The name of the vector bucket that contains the vector indexes.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

## Response Syntax
<a name="API_S3VectorBuckets_ListIndexes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "indexes": [
      {
         "creationTime": number,
         "indexArn": "string",
         "indexName": "string",
         "vectorBucketName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_S3VectorBuckets_ListIndexes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [indexes](#API_S3VectorBuckets_ListIndexes_ResponseSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListIndexes-response-indexes"></a>
The attributes of the vector indexes
Type: Array of [IndexSummary](API_S3VectorBuckets_IndexSummary.md) objects

 ** [nextToken](#API_S3VectorBuckets_ListIndexes_ResponseSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListIndexes-response-nextToken"></a>
The next pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

## Errors
<a name="API_S3VectorBuckets_ListIndexes_Errors"></a>

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
<a name="API_S3VectorBuckets_ListIndexes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/ListIndexes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3vectors-2025-07-15/ListIndexes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/ListIndexes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/ListIndexes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/ListIndexes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/ListIndexes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/ListIndexes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/ListIndexes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/ListIndexes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/ListIndexes)
