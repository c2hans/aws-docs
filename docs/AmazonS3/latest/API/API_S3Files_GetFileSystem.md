---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_GetFileSystem.html
---

# GetFileSystem
<a name="API_S3Files_GetFileSystem"></a>

Returns resource information for the specified S3 File System including status, configuration, and metadata.

## Request Syntax
<a name="API_S3Files_GetFileSystem_RequestSyntax"></a>

```
GET /file-systems/{{fileSystemId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_S3Files_GetFileSystem_RequestParameters"></a>

The request uses the following URI parameters.

 ** [fileSystemId](#API_S3Files_GetFileSystem_RequestSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-request-uri-fileSystemId"></a>
The ID or Amazon Resource Name (ARN) of the S3 File System to retrieve information for.
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})`
Required: Yes

## Request Body
<a name="API_S3Files_GetFileSystem_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_S3Files_GetFileSystem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "bucket": "string",
   "clientToken": "string",
   "creationTime": number,
   "fileSystemArn": "string",
   "fileSystemId": "string",
   "kmsKeyId": "string",
   "name": "string",
   "ownerId": "string",
   "prefix": "string",
   "roleArn": "string",
   "status": "string",
   "statusMessage": "string",
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_S3Files_GetFileSystem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [bucket](#API_S3Files_GetFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-response-bucket"></a>
The Amazon Resource Name (ARN) of the S3 bucket.
Type: String
Pattern: `(arn:aws[a-zA-Z0-9-]*:s3:::.+)`

 ** [clientToken](#API_S3Files_GetFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-response-clientToken"></a>
The client token used for idempotency when the file system was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(.+)`

 ** [creationTime](#API_S3Files_GetFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-response-creationTime"></a>
The time when the file system was created.
Type: Timestamp

 ** [fileSystemArn](#API_S3Files_GetFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-response-fileSystemArn"></a>
The Amazon Resource Name (ARN) of the file system.
Type: String
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40})`

 ** [fileSystemId](#API_S3Files_GetFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-response-fileSystemId"></a>
The ID of the file system.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})`

 ** [kmsKeyId](#API_S3Files_GetFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-response-kmsKeyId"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used for encryption.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|mrk-[0-9a-f]{32}|alias/[a-zA-Z0-9/_-]+|(arn:aws[-a-z]*:kms:[a-z0-9-]+:\d{12}:((key/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})|(key/mrk-[0-9a-f]{32})|(alias/[a-zA-Z0-9/_-]+))))`

 ** [name](#API_S3Files_GetFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-response-name"></a>
The name of the file system.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

 ** [ownerId](#API_S3Files_GetFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-response-ownerId"></a>
The AWS account ID of the file system owner.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `(\d{12})|(\d{4}-{4}-\d{4})`

 ** [prefix](#API_S3Files_GetFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-response-prefix"></a>
The prefix in the S3 bucket that the file system provides access to.
Type: String

 ** [roleArn](#API_S3Files_GetFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used for S3 access.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [status](#API_S3Files_GetFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-response-status"></a>
The current status of the file system.
Type: String
Valid Values: `available | creating | deleting | deleted | error | updating`

 ** [statusMessage](#API_S3Files_GetFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-response-statusMessage"></a>
Additional information about the file system status.
Type: String

 ** [tags](#API_S3Files_GetFileSystem_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetFileSystem-response-tags"></a>
The tags associated with the file system.
Type: Array of [Tag](API_S3Files_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

## Errors
<a name="API_S3Files_GetFileSystem_Errors"></a>

 ** InternalServerException **
An internal server error occurred. Retry your request.
 ** errorCode **
The error code associated with the exception.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource exists and that you have permission to access it.
 ** errorCode **
The error code associated with the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled. Retry your request using exponential backoff.
 ** errorCode **
The error code associated with the exception.
HTTP Status Code: 429

 ** ValidationException **
The input parameters are not valid. Check the parameter values and try again.
 ** errorCode **
The error code associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_S3Files_GetFileSystem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3files-2025-05-05/GetFileSystem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3files-2025-05-05/GetFileSystem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/GetFileSystem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3files-2025-05-05/GetFileSystem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/GetFileSystem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3files-2025-05-05/GetFileSystem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3files-2025-05-05/GetFileSystem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3files-2025-05-05/GetFileSystem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3files-2025-05-05/GetFileSystem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/GetFileSystem)
