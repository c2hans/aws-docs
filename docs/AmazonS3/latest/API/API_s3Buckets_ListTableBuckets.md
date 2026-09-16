---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ListTableBuckets.html
---

# ListTableBuckets
<a name="API_s3Buckets_ListTableBuckets"></a>

Lists table buckets for your account. For more information, see [S3 Table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets.html) in the *Amazon Simple Storage Service User Guide*.

Permissions
You must have the `s3tables:ListTableBuckets` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_ListTableBuckets_RequestSyntax"></a>

```
GET /buckets?continuationToken={{continuationToken}}&maxBuckets={{maxBuckets}}&prefix={{prefix}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_ListTableBuckets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [continuationToken](#API_s3Buckets_ListTableBuckets_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListTableBuckets-request-uri-continuationToken"></a>
 `ContinuationToken` indicates to Amazon S3 that the list is being continued on this bucket with a token. `ContinuationToken` is obfuscated and is not a real key. You can use this `ContinuationToken` for pagination of the list results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [maxBuckets](#API_s3Buckets_ListTableBuckets_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListTableBuckets-request-uri-maxBuckets"></a>
The maximum number of table buckets to return in the list.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [prefix](#API_s3Buckets_ListTableBuckets_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListTableBuckets-request-uri-prefix"></a>
The prefix of the table buckets.
Length Constraints: Minimum length of 1. Maximum length of 63.

 ** [type](#API_s3Buckets_ListTableBuckets_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListTableBuckets-request-uri-type"></a>
The type of table buckets to filter by in the list.
Valid Values: `customer | aws`

## Request Body
<a name="API_s3Buckets_ListTableBuckets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_ListTableBuckets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "continuationToken": "string",
   "tableBuckets": [
      {
         "arn": "string",
         "createdAt": "string",
         "name": "string",
         "ownerAccountId": "string",
         "tableBucketId": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_s3Buckets_ListTableBuckets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [continuationToken](#API_s3Buckets_ListTableBuckets_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_ListTableBuckets-response-continuationToken"></a>
You can use this `ContinuationToken` for pagination of the list results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [tableBuckets](#API_s3Buckets_ListTableBuckets_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_ListTableBuckets-response-tableBuckets"></a>
A list of table buckets.
Type: Array of [TableBucketSummary](API_s3Buckets_TableBucketSummary.md) objects

## Errors
<a name="API_s3Buckets_ListTableBuckets_Errors"></a>

 ** AccessDeniedException **
The action cannot be performed because you do not have the required permission.
HTTP Status Code: 403

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
<a name="API_s3Buckets_ListTableBuckets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/ListTableBuckets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/ListTableBuckets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/ListTableBuckets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/ListTableBuckets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/ListTableBuckets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/ListTableBuckets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/ListTableBuckets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/ListTableBuckets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/ListTableBuckets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/ListTableBuckets)
