---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ListNamespaces.html
---

# ListNamespaces
<a name="API_s3Buckets_ListNamespaces"></a>

Lists the namespaces within a table bucket. For more information, see [Table namespaces](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace.html) in the *Amazon Simple Storage Service User Guide*.

Permissions
You must have the `s3tables:ListNamespaces` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_ListNamespaces_RequestSyntax"></a>

```
GET /namespaces/{{tableBucketARN}}?continuationToken={{continuationToken}}&maxNamespaces={{maxNamespaces}}&prefix={{prefix}} HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_ListNamespaces_RequestParameters"></a>

The request uses the following URI parameters.

 ** [continuationToken](#API_s3Buckets_ListNamespaces_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListNamespaces-request-uri-continuationToken"></a>
 `ContinuationToken` indicates to Amazon S3 that the list is being continued on this bucket with a token. `ContinuationToken` is obfuscated and is not a real key. You can use this `ContinuationToken` for pagination of the list results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [maxNamespaces](#API_s3Buckets_ListNamespaces_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListNamespaces-request-uri-maxNamespaces"></a>
The maximum number of namespaces to return in the list.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [prefix](#API_s3Buckets_ListNamespaces_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListNamespaces-request-uri-prefix"></a>
The prefix of the namespaces.
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [tableBucketARN](#API_s3Buckets_ListNamespaces_RequestSyntax) **   <a name="AmazonS3-s3Buckets_ListNamespaces-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

## Request Body
<a name="API_s3Buckets_ListNamespaces_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_ListNamespaces_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "continuationToken": "string",
   "namespaces": [
      {
         "createdAt": "string",
         "createdBy": "string",
         "namespace": [ "string" ],
         "namespaceId": "string",
         "ownerAccountId": "string",
         "tableBucketId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_s3Buckets_ListNamespaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [continuationToken](#API_s3Buckets_ListNamespaces_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_ListNamespaces-response-continuationToken"></a>
The `ContinuationToken` for pagination of the list results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [namespaces](#API_s3Buckets_ListNamespaces_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_ListNamespaces-response-namespaces"></a>
A list of namespaces.
Type: Array of [NamespaceSummary](API_s3Buckets_NamespaceSummary.md) objects

## Errors
<a name="API_s3Buckets_ListNamespaces_Errors"></a>

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
<a name="API_s3Buckets_ListNamespaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/ListNamespaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/ListNamespaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/ListNamespaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/ListNamespaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/ListNamespaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/ListNamespaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/ListNamespaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/ListNamespaces)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/ListNamespaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/ListNamespaces)
