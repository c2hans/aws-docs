---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_UpdateSequenceStore.html
---

# UpdateSequenceStore
<a name="API_UpdateSequenceStore"></a>

Update one or more parameters for the sequence store.

## Request Syntax
<a name="API_UpdateSequenceStore_RequestSyntax"></a>

```
PATCH /sequencestore/{{id}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "fallbackLocation": "{{string}}",
   "name": "{{string}}",
   "propagatedSetLevelTags": [ "{{string}}" ],
   "s3AccessConfig": {
      "accessLogLocation": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateSequenceStore_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateSequenceStore_RequestSyntax) **   <a name="omics-UpdateSequenceStore-request-uri-id"></a>
The ID of the sequence store.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateSequenceStore_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateSequenceStore_RequestSyntax) **   <a name="omics-UpdateSequenceStore-request-clientToken"></a>
To ensure that requests don't run multiple times, specify a unique token for each request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [description](#API_UpdateSequenceStore_RequestSyntax) **   <a name="omics-UpdateSequenceStore-request-description"></a>
A description for the sequence store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [fallbackLocation](#API_UpdateSequenceStore_RequestSyntax) **   <a name="omics-UpdateSequenceStore-request-fallbackLocation"></a>
The S3 URI of a bucket and folder to store Read Sets that fail to upload.
Type: String
Pattern: `$|^s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/?((.{1,1024})/)?`
Required: No

 ** [name](#API_UpdateSequenceStore_RequestSyntax) **   <a name="omics-UpdateSequenceStore-request-name"></a>
A name for the sequence store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [propagatedSetLevelTags](#API_UpdateSequenceStore_RequestSyntax) **   <a name="omics-UpdateSequenceStore-request-propagatedSetLevelTags"></a>
The tags keys to propagate to the S3 objects associated with read sets in the sequence store.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [s3AccessConfig](#API_UpdateSequenceStore_RequestSyntax) **   <a name="omics-UpdateSequenceStore-request-s3AccessConfig"></a>
S3 access configuration parameters.
Type: [S3AccessConfig](API_S3AccessConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateSequenceStore_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationTime": "string",
   "description": "string",
   "eTagAlgorithmFamily": "string",
   "fallbackLocation": "string",
   "id": "string",
   "name": "string",
   "propagatedSetLevelTags": [ "string" ],
   "s3Access": {
      "accessLogLocation": "string",
      "s3AccessPointArn": "string",
      "s3Uri": "string"
   },
   "sseConfig": {
      "keyArn": "string",
      "type": "string"
   },
   "status": "string",
   "statusMessage": "string",
   "updateTime": "string"
}
```

## Response Elements
<a name="API_UpdateSequenceStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateSequenceStore_ResponseSyntax) **   <a name="omics-UpdateSequenceStore-response-arn"></a>
The ARN of the sequence store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`

 ** [creationTime](#API_UpdateSequenceStore_ResponseSyntax) **   <a name="omics-UpdateSequenceStore-response-creationTime"></a>
The time when the store was created.
Type: Timestamp

 ** [description](#API_UpdateSequenceStore_ResponseSyntax) **   <a name="omics-UpdateSequenceStore-response-description"></a>
Description of the sequence store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [eTagAlgorithmFamily](#API_UpdateSequenceStore_ResponseSyntax) **   <a name="omics-UpdateSequenceStore-response-eTagAlgorithmFamily"></a>
The ETag algorithm family to use on ingested read sets.
Type: String
Valid Values: `MD5up | SHA256up | SHA512up`

 ** [fallbackLocation](#API_UpdateSequenceStore_ResponseSyntax) **   <a name="omics-UpdateSequenceStore-response-fallbackLocation"></a>
The S3 URI of a bucket and folder to store Read Sets that fail to upload.
Type: String
Pattern: `$|^s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/?((.{1,1024})/)?`

 ** [id](#API_UpdateSequenceStore_ResponseSyntax) **   <a name="omics-UpdateSequenceStore-response-id"></a>
The ID of the sequence store.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [name](#API_UpdateSequenceStore_ResponseSyntax) **   <a name="omics-UpdateSequenceStore-response-name"></a>
The name of the sequence store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [propagatedSetLevelTags](#API_UpdateSequenceStore_ResponseSyntax) **   <a name="omics-UpdateSequenceStore-response-propagatedSetLevelTags"></a>
The tags keys to propagate to the S3 objects associated with read sets in the sequence store.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [s3Access](#API_UpdateSequenceStore_ResponseSyntax) **   <a name="omics-UpdateSequenceStore-response-s3Access"></a>
The S3 access metadata of the sequence store.
Type: [SequenceStoreS3Access](API_SequenceStoreS3Access.md) object

 ** [sseConfig](#API_UpdateSequenceStore_ResponseSyntax) **   <a name="omics-UpdateSequenceStore-response-sseConfig"></a>
Server-side encryption (SSE) settings for a store.
Type: [SseConfig](API_SseConfig.md) object

 ** [status](#API_UpdateSequenceStore_ResponseSyntax) **   <a name="omics-UpdateSequenceStore-response-status"></a>
The status of the sequence store.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`

 ** [statusMessage](#API_UpdateSequenceStore_ResponseSyntax) **   <a name="omics-UpdateSequenceStore-response-statusMessage"></a>
The status message of the sequence store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [updateTime](#API_UpdateSequenceStore_ResponseSyntax) **   <a name="omics-UpdateSequenceStore-response-updateTime"></a>
The last-updated time of the Sequence Store.
Type: Timestamp

## Errors
<a name="API_UpdateSequenceStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSequenceStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/UpdateSequenceStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/UpdateSequenceStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/UpdateSequenceStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/UpdateSequenceStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/UpdateSequenceStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/UpdateSequenceStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/UpdateSequenceStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/UpdateSequenceStore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/UpdateSequenceStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/UpdateSequenceStore)
