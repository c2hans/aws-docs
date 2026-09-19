---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateStorageConfiguration.html
---

# CreateStorageConfiguration
<a name="API_CreateStorageConfiguration"></a>

Creates a new storage configuration, used to enable recording to Amazon S3. When a StorageConfiguration is created, IVS will modify the S3 bucketPolicy of the provided bucket. This will ensure that IVS has sufficient permissions to write content to the provided bucket.

## Request Syntax
<a name="API_CreateStorageConfiguration_RequestSyntax"></a>

```
POST /CreateStorageConfiguration HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}",
   "s3": {
      "bucketName": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateStorageConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateStorageConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_CreateStorageConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateStorageConfiguration-request-name"></a>
Storage configuration name. The value does not need to be unique.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [s3](#API_CreateStorageConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateStorageConfiguration-request-s3"></a>
A complex type that contains a storage configuration for where recorded video will be stored.
Type: [S3StorageConfiguration](API_S3StorageConfiguration.md) object
Required: Yes

 ** [tags](#API_CreateStorageConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateStorageConfiguration-request-tags"></a>
Tags attached to the resource. Array of maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateStorageConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "storageConfiguration": {
      "arn": "string",
      "name": "string",
      "s3": {
         "bucketName": "string"
      },
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateStorageConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [storageConfiguration](#API_CreateStorageConfiguration_ResponseSyntax) **   <a name="ivsrealtimeeapireference-CreateStorageConfiguration-response-storageConfiguration"></a>
The StorageConfiguration that was created.
Type: [StorageConfiguration](API_StorageConfiguration.md) object

## Errors
<a name="API_CreateStorageConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** PendingVerification **
Your account is pending verification.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/CreateStorageConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/CreateStorageConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/CreateStorageConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/CreateStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/CreateStorageConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/CreateStorageConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/CreateStorageConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/CreateStorageConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/CreateStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/CreateStorageConfiguration)
