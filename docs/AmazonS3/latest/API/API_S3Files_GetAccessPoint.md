---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_GetAccessPoint.html
---

# GetAccessPoint
<a name="API_S3Files_GetAccessPoint"></a>

Returns resource information for an S3 File System Access Point.

## Request Syntax
<a name="API_S3Files_GetAccessPoint_RequestSyntax"></a>

```
GET /access-points/{{accessPointId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_S3Files_GetAccessPoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accessPointId](#API_S3Files_GetAccessPoint_RequestSyntax) **   <a name="AmazonS3-S3Files_GetAccessPoint-request-uri-accessPointId"></a>
The ID or Amazon Resource Name (ARN) of the access point to retrieve information for.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}|fsap-[0-9a-f]{17,40})`
Required: Yes

## Request Body
<a name="API_S3Files_GetAccessPoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_S3Files_GetAccessPoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accessPointArn": "string",
   "accessPointId": "string",
   "clientToken": "string",
   "fileSystemId": "string",
   "name": "string",
   "ownerId": "string",
   "posixUser": {
      "gid": number,
      "secondaryGids": [ number ],
      "uid": number
   },
   "rootDirectory": {
      "creationPermissions": {
         "ownerGid": number,
         "ownerUid": number,
         "permissions": "string"
      },
      "path": "string"
   },
   "status": "string",
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_S3Files_GetAccessPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessPointArn](#API_S3Files_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetAccessPoint-response-accessPointArn"></a>
The ARN of the access point.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}`

 ** [accessPointId](#API_S3Files_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetAccessPoint-response-accessPointId"></a>
The ID of the access point.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}|fsap-[0-9a-f]{17,40})`

 ** [clientToken](#API_S3Files_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetAccessPoint-response-clientToken"></a>
The client token used for idempotency when the access point was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(.+)`

 ** [fileSystemId](#API_S3Files_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetAccessPoint-response-fileSystemId"></a>
The ID of the S3 File System.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})`

 ** [name](#API_S3Files_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetAccessPoint-response-name"></a>
The name of the access point.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

 ** [ownerId](#API_S3Files_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetAccessPoint-response-ownerId"></a>
The AWS account ID of the access point owner.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `(\d{12})|(\d{4}-{4}-\d{4})`

 ** [posixUser](#API_S3Files_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetAccessPoint-response-posixUser"></a>
The POSIX identity configured for this access point.
Type: [PosixUser](API_S3Files_PosixUser.md) object

 ** [rootDirectory](#API_S3Files_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetAccessPoint-response-rootDirectory"></a>
The root directory configuration for this access point.
Type: [RootDirectory](API_S3Files_RootDirectory.md) object

 ** [status](#API_S3Files_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetAccessPoint-response-status"></a>
The current status of the access point.
Type: String
Valid Values: `available | creating | deleting | deleted | error | updating`

 ** [tags](#API_S3Files_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-S3Files_GetAccessPoint-response-tags"></a>
The tags associated with the access point.
Type: Array of [Tag](API_S3Files_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

## Errors
<a name="API_S3Files_GetAccessPoint_Errors"></a>

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
<a name="API_S3Files_GetAccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3files-2025-05-05/GetAccessPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3files-2025-05-05/GetAccessPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/GetAccessPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3files-2025-05-05/GetAccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/GetAccessPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3files-2025-05-05/GetAccessPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3files-2025-05-05/GetAccessPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3files-2025-05-05/GetAccessPoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3files-2025-05-05/GetAccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/GetAccessPoint)
