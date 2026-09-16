---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableMetadataLocation.html
---

# GetTableMetadataLocation
<a name="API_s3Buckets_GetTableMetadataLocation"></a>

Gets the location of the table metadata.

Permissions
You must have the `s3tables:GetTableMetadataLocation` permission to use this operation.

## Request Syntax
<a name="API_s3Buckets_GetTableMetadataLocation_RequestSyntax"></a>

```
GET /tables/{{tableBucketARN}}/{{namespace}}/{{name}}/metadata-location HTTP/1.1
```

## URI Request Parameters
<a name="API_s3Buckets_GetTableMetadataLocation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_s3Buckets_GetTableMetadataLocation_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMetadataLocation-request-uri-name"></a>
The name of the table.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

 ** [namespace](#API_s3Buckets_GetTableMetadataLocation_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMetadataLocation-request-uri-namespace"></a>
The namespace of the table.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

 ** [tableBucketARN](#API_s3Buckets_GetTableMetadataLocation_RequestSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMetadataLocation-request-uri-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket.
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

## Request Body
<a name="API_s3Buckets_GetTableMetadataLocation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3Buckets_GetTableMetadataLocation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "metadataLocation": "string",
   "versionToken": "string",
   "warehouseLocation": "string"
}
```

## Response Elements
<a name="API_s3Buckets_GetTableMetadataLocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [metadataLocation](#API_s3Buckets_GetTableMetadataLocation_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMetadataLocation-response-metadataLocation"></a>
The metadata location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [versionToken](#API_s3Buckets_GetTableMetadataLocation_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMetadataLocation-response-versionToken"></a>
The version token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [warehouseLocation](#API_s3Buckets_GetTableMetadataLocation_ResponseSyntax) **   <a name="AmazonS3-s3Buckets_GetTableMetadataLocation-response-warehouseLocation"></a>
The warehouse location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_s3Buckets_GetTableMetadataLocation_Errors"></a>

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
<a name="API_s3Buckets_GetTableMetadataLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3tables-2018-05-10/GetTableMetadataLocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3tables-2018-05-10/GetTableMetadataLocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GetTableMetadataLocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3tables-2018-05-10/GetTableMetadataLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GetTableMetadataLocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3tables-2018-05-10/GetTableMetadataLocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3tables-2018-05-10/GetTableMetadataLocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3tables-2018-05-10/GetTableMetadataLocation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3tables-2018-05-10/GetTableMetadataLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GetTableMetadataLocation)
