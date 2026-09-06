---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_DeleteAccessPoint.html
---

# DeleteAccessPoint
<a name="API_S3Files_DeleteAccessPoint"></a>

Deletes an S3 File System Access Point. This operation is irreversible.

## Request Syntax
<a name="API_S3Files_DeleteAccessPoint_RequestSyntax"></a>

```
DELETE /access-points/{{accessPointId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_S3Files_DeleteAccessPoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accessPointId](#API_S3Files_DeleteAccessPoint_RequestSyntax) **   <a name="AmazonS3-S3Files_DeleteAccessPoint-request-uri-accessPointId"></a>
The ID or Amazon Resource Name (ARN) of the access point to delete.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}|fsap-[0-9a-f]{17,40})`
Required: Yes

## Request Body
<a name="API_S3Files_DeleteAccessPoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_S3Files_DeleteAccessPoint_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_S3Files_DeleteAccessPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_S3Files_DeleteAccessPoint_Errors"></a>

 ** ConflictException **
The request conflicts with the current state of the resource. This can occur when trying to create a resource that already exists or delete a resource that is in use.
 ** errorCode **
The error code associated with the exception.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of the resource that caused the conflict.
HTTP Status Code: 409

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
<a name="API_S3Files_DeleteAccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3files-2025-05-05/DeleteAccessPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3files-2025-05-05/DeleteAccessPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/DeleteAccessPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3files-2025-05-05/DeleteAccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/DeleteAccessPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3files-2025-05-05/DeleteAccessPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3files-2025-05-05/DeleteAccessPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3files-2025-05-05/DeleteAccessPoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3files-2025-05-05/DeleteAccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/DeleteAccessPoint)
