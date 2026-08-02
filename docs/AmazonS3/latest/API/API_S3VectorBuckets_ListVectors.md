---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectors.html
---

# ListVectors
<a name="API_S3VectorBuckets_ListVectors"></a>

List vectors in the specified vector index. To specify the vector index, you can either use both the vector bucket name and the vector index name, or use the vector index Amazon Resource Name (ARN).

 `ListVectors` operations proceed sequentially; however, for faster performance on a large number of vectors in a vector index, applications can request a parallel `ListVectors` operation by providing the `segmentCount` and `segmentIndex` parameters.

Permissions
You must have the `s3vectors:ListVectors` permission to use this operation. Additional permissions are required based on the request parameters you specify:
+ With only `s3vectors:ListVectors` permission, you can list vector keys when `returnData` and `returnMetadata` are both set to false or not specified..
+ If you set `returnData` or `returnMetadata` to true, you must have both `s3vectors:ListVectors` and `s3vectors:GetVectors` permissions. The request fails with a `403 Forbidden` error if you request vector data or metadata without the `s3vectors:GetVectors` permission.

## Request Syntax
<a name="API_S3VectorBuckets_ListVectors_RequestSyntax"></a>

```
POST /ListVectors HTTP/1.1
Content-type: application/json

{
   "indexArn": "{{string}}",
   "indexName": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "returnData": {{boolean}},
   "returnMetadata": {{boolean}},
   "segmentCount": {{number}},
   "segmentIndex": {{number}},
   "vectorBucketName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_S3VectorBuckets_ListVectors_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_S3VectorBuckets_ListVectors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [indexArn](#API_S3VectorBuckets_ListVectors_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectors-request-indexArn"></a>
The Amazon resource Name (ARN) of the vector index.
Type: String
Pattern: `arn:aws[-a-z0-9]*:s3vectors:[a-z0-9-]+:[0-9]{12}:bucket/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]/index/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]`
Required: No

 ** [indexName](#API_S3VectorBuckets_ListVectors_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectors-request-indexName"></a>
The name of the vector index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

 ** [maxResults](#API_S3VectorBuckets_ListVectors_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectors-request-maxResults"></a>
The maximum number of vectors to return on a page.
If you don't specify `maxResults`, the `ListVectors` operation uses a default value of 500.
If the processed dataset size exceeds 1 MB before reaching the `maxResults` value, the operation stops and returns the vectors that are retrieved up to that point, along with a `nextToken` that you can use in a subsequent request to retrieve the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_S3VectorBuckets_ListVectors_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectors-request-nextToken"></a>
Pagination token from a previous request. The value of this field is empty for an initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [returnData](#API_S3VectorBuckets_ListVectors_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectors-request-returnData"></a>
If true, the vector data of each vector will be included in the response. The default value is `false`.
Type: Boolean
Required: No

 ** [returnMetadata](#API_S3VectorBuckets_ListVectors_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectors-request-returnMetadata"></a>
If true, the metadata associated with each vector will be included in the response. The default value is `false`.
Type: Boolean
Required: No

 ** [segmentCount](#API_S3VectorBuckets_ListVectors_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectors-request-segmentCount"></a>
For a parallel `ListVectors` request, `segmentCount` represents the total number of vector segments into which the `ListVectors` operation will be divided. The value of `segmentCount` corresponds to the number of application workers that will perform the parallel `ListVectors` operation. For example, if you want to use four application threads to list vectors in a vector index, specify a `segmentCount` value of 4.
If you specify a `segmentCount` value of 1, the `ListVectors` operation will be sequential rather than parallel.
If you specify `segmentCount`, you must also specify `segmentIndex`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 16.
Required: No

 ** [segmentIndex](#API_S3VectorBuckets_ListVectors_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectors-request-segmentIndex"></a>
For a parallel `ListVectors` request, `segmentIndex` is the index of the segment from which to list vectors in the current request. It identifies an individual segment to be listed by an application worker.
Segment IDs are zero-based, so the first segment is always 0. For example, if you want to use four application threads to list vectors in a vector index, then the first thread specifies a `segmentIndex` value of 0, the second thread specifies 1, and so on.
The value of `segmentIndex` must be less than the value provided for `segmentCount`.
If you provide `segmentIndex`, you must also provide `segmentCount`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** [vectorBucketName](#API_S3VectorBuckets_ListVectors_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectors-request-vectorBucketName"></a>
The name of the vector bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

## Response Syntax
<a name="API_S3VectorBuckets_ListVectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "vectors": [
      {
         "data": { ... },
         "key": "string",
         "metadata": JSON value
      }
   ]
}
```

## Response Elements
<a name="API_S3VectorBuckets_ListVectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_S3VectorBuckets_ListVectors_ResponseSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectors-response-nextToken"></a>
Pagination token to be used in the subsequent request. The field is empty if no further pagination is required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [vectors](#API_S3VectorBuckets_ListVectors_ResponseSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectors-response-vectors"></a>
Vectors in the current segment.
Type: Array of [ListOutputVector](API_S3VectorBuckets_ListOutputVector.md) objects

## Errors
<a name="API_S3VectorBuckets_ListVectors_Errors"></a>

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
<a name="API_S3VectorBuckets_ListVectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/ListVectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3vectors-2025-07-15/ListVectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/ListVectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/ListVectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/ListVectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/ListVectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/ListVectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/ListVectors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/ListVectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/ListVectors)
