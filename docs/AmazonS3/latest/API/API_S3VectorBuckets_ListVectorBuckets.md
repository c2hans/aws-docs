---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectorBuckets.html
---

# ListVectorBuckets
<a name="API_S3VectorBuckets_ListVectorBuckets"></a>

Returns a list of all the vector buckets that are owned by the authenticated sender of the request.

Permissions
You must have the `s3vectors:ListVectorBuckets` permission to use this operation.

## Request Syntax
<a name="API_S3VectorBuckets_ListVectorBuckets_RequestSyntax"></a>

```
POST /ListVectorBuckets HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "prefix": "{{string}}"
}
```

## URI Request Parameters
<a name="API_S3VectorBuckets_ListVectorBuckets_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_S3VectorBuckets_ListVectorBuckets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_S3VectorBuckets_ListVectorBuckets_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectorBuckets-request-maxResults"></a>
The maximum number of vector buckets to be returned in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [nextToken](#API_S3VectorBuckets_ListVectorBuckets_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectorBuckets-request-nextToken"></a>
The previous pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [prefix](#API_S3VectorBuckets_ListVectorBuckets_RequestSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectorBuckets-request-prefix"></a>
Limits the response to vector buckets that begin with the specified prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: No

## Response Syntax
<a name="API_S3VectorBuckets_ListVectorBuckets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "vectorBuckets": [
      {
         "creationTime": number,
         "vectorBucketArn": "string",
         "vectorBucketName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_S3VectorBuckets_ListVectorBuckets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_S3VectorBuckets_ListVectorBuckets_ResponseSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectorBuckets-response-nextToken"></a>
The element is included in the response when there are more buckets to be listed with pagination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [vectorBuckets](#API_S3VectorBuckets_ListVectorBuckets_ResponseSyntax) **   <a name="AmazonS3-S3VectorBuckets_ListVectorBuckets-response-vectorBuckets"></a>
The list of vector buckets owned by the requester.
Type: Array of [VectorBucketSummary](API_S3VectorBuckets_VectorBucketSummary.md) objects

## Errors
<a name="API_S3VectorBuckets_ListVectorBuckets_Errors"></a>

 ** AccessDeniedException **
Access denied.
HTTP Status Code: 403

 ** InternalServerException **
The request failed due to an internal server error.
HTTP Status Code: 500

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
<a name="API_S3VectorBuckets_ListVectorBuckets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3vectors-2025-07-15/ListVectorBuckets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3vectors-2025-07-15/ListVectorBuckets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/ListVectorBuckets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3vectors-2025-07-15/ListVectorBuckets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/ListVectorBuckets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3vectors-2025-07-15/ListVectorBuckets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3vectors-2025-07-15/ListVectorBuckets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3vectors-2025-07-15/ListVectorBuckets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3vectors-2025-07-15/ListVectorBuckets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/ListVectorBuckets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
