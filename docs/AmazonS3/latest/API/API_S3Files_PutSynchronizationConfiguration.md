---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_PutSynchronizationConfiguration.html
---

# PutSynchronizationConfiguration
<a name="API_S3Files_PutSynchronizationConfiguration"></a>

Creates or updates the synchronization configuration for the specified S3 File System, including import data rules and expiration data rules.

## Request Syntax
<a name="API_S3Files_PutSynchronizationConfiguration_RequestSyntax"></a>

```
PUT /file-systems/{{fileSystemId}}/synchronization-configuration HTTP/1.1
Content-type: application/json

{
   "expirationDataRules": [
      {
         "daysAfterLastAccess": {{number}}
      }
   ],
   "importDataRules": [
      {
         "prefix": "{{string}}",
         "sizeLessThan": {{number}},
         "trigger": "{{string}}"
      }
   ],
   "latestVersionNumber": {{number}}
}
```

## URI Request Parameters
<a name="API_S3Files_PutSynchronizationConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [fileSystemId](#API_S3Files_PutSynchronizationConfiguration_RequestSyntax) **   <a name="AmazonS3-S3Files_PutSynchronizationConfiguration-request-uri-fileSystemId"></a>
The ID or Amazon Resource Name (ARN) of the S3 File System to configure synchronization for.
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})`
Required: Yes

## Request Body
<a name="API_S3Files_PutSynchronizationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [expirationDataRules](#API_S3Files_PutSynchronizationConfiguration_RequestSyntax) **   <a name="AmazonS3-S3Files_PutSynchronizationConfiguration-request-expirationDataRules"></a>
An array of expiration data rules that control when cached data expires from the file system.
Type: Array of [ExpirationDataRule](API_S3Files_ExpirationDataRule.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [importDataRules](#API_S3Files_PutSynchronizationConfiguration_RequestSyntax) **   <a name="AmazonS3-S3Files_PutSynchronizationConfiguration-request-importDataRules"></a>
An array of import data rules that control how data is imported from S3 into the file system.
Type: Array of [ImportDataRule](API_S3Files_ImportDataRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [latestVersionNumber](#API_S3Files_PutSynchronizationConfiguration_RequestSyntax) **   <a name="AmazonS3-S3Files_PutSynchronizationConfiguration-request-latestVersionNumber"></a>
The version number of the current synchronization configuration. Omit this value when creating a synchronization configuration for the first time. For subsequent updates, provide this value for optimistic concurrency control. If the version number does not match the current configuration, the request fails with a `ConflictException`.
Type: Integer
Required: No

## Response Syntax
<a name="API_S3Files_PutSynchronizationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_S3Files_PutSynchronizationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_S3Files_PutSynchronizationConfiguration_Errors"></a>

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
<a name="API_S3Files_PutSynchronizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3files-2025-05-05/PutSynchronizationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3files-2025-05-05/PutSynchronizationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/PutSynchronizationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3files-2025-05-05/PutSynchronizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/PutSynchronizationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3files-2025-05-05/PutSynchronizationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3files-2025-05-05/PutSynchronizationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3files-2025-05-05/PutSynchronizationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3files-2025-05-05/PutSynchronizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/PutSynchronizationConfiguration)
