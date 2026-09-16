---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_DeleteFileSystemPolicy.html
---

# DeleteFileSystemPolicy
<a name="API_S3Files_DeleteFileSystemPolicy"></a>

Deletes the IAM resource policy of an S3 File System.

## Request Syntax
<a name="API_S3Files_DeleteFileSystemPolicy_RequestSyntax"></a>

```
DELETE /file-systems/{{fileSystemId}}/policy HTTP/1.1
```

## URI Request Parameters
<a name="API_S3Files_DeleteFileSystemPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [fileSystemId](#API_S3Files_DeleteFileSystemPolicy_RequestSyntax) **   <a name="AmazonS3-S3Files_DeleteFileSystemPolicy-request-uri-fileSystemId"></a>
The ID or Amazon Resource Name (ARN) of the S3 File System whose resource policy to delete.
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})`
Required: Yes

## Request Body
<a name="API_S3Files_DeleteFileSystemPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_S3Files_DeleteFileSystemPolicy_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_S3Files_DeleteFileSystemPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_S3Files_DeleteFileSystemPolicy_Errors"></a>

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
<a name="API_S3Files_DeleteFileSystemPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3files-2025-05-05/DeleteFileSystemPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3files-2025-05-05/DeleteFileSystemPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/DeleteFileSystemPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3files-2025-05-05/DeleteFileSystemPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/DeleteFileSystemPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3files-2025-05-05/DeleteFileSystemPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3files-2025-05-05/DeleteFileSystemPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3files-2025-05-05/DeleteFileSystemPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3files-2025-05-05/DeleteFileSystemPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/DeleteFileSystemPolicy)
