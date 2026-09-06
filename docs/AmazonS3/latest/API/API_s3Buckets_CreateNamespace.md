---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateNamespace.html
---

# CreateNamespace
<a name="API_s3Buckets_CreateNamespace"></a>

Creates a namespace. A namespace is a logical grouping of tables within your table bucket, which you can use to organize tables. For more information, see [Create a namespace](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-create.html) in the *Amazon Simple Storage Service User Guide*.

Permissions
You must have the `s3tables:CreateNamespace` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_CreateNamespace_RequestSyntax"></a>

```
PUT /namespaces/{{tableBucketARN}} HTTP/1.1
Content-type: application/json

{
   "namespace": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_s3Buckets_CreateNamespace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tableBucketARN](#API_s3Buckets_CreateNamespace_RequestSyntax) **   <a name="AmazonS3-s3Buckets_CreateNamespace-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket to create the namespace in.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

## Request Body
<a name="API_s3Buckets_CreateNamespace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [namespace](#API_s3Buckets_CreateNamespace_RequestSyntax) **   <a name="AmazonS3-s3Buckets_CreateNamespace-request-namespace"></a>
A name for the namespace.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

## Response Syntax
<a name="API_s3Buckets_CreateNamespace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "namespace": [ "string" ],
   "tableBucketARN": "string"
}
```

## Response Elements
<a name="API_s3Buckets_CreateNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [namespace](#API_s3Buckets_CreateNamespace_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_CreateNamespace-response-namespace"></a>
The name of the namespace.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`

 ** [tableBucketARN](#API_s3Buckets_CreateNamespace_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_CreateNamespace-response-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket the namespace was created in.
Type: String
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`

## Errors
<a name="API_s3Buckets_CreateNamespace_Errors"></a>

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
<a name="API_s3Buckets_CreateNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/CreateNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/CreateNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/CreateNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/CreateNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/CreateNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/CreateNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/CreateNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/CreateNamespace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/CreateNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/CreateNamespace)
