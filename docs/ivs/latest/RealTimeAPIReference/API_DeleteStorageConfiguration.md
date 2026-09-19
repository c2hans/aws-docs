---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DeleteStorageConfiguration.html
---

# DeleteStorageConfiguration
<a name="API_DeleteStorageConfiguration"></a>

Deletes the storage configuration for the specified ARN.

If you try to delete a storage configuration that is used by a Composition, you will get an error (409 ConflictException). To avoid this, for all Compositions that reference the storage configuration, first use [StopComposition](API_StopComposition.md) and wait for it to complete, then use DeleteStorageConfiguration.

## Request Syntax
<a name="API_DeleteStorageConfiguration_RequestSyntax"></a>

```
POST /DeleteStorageConfiguration HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteStorageConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteStorageConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_DeleteStorageConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-DeleteStorageConfiguration-request-arn"></a>
ARN of the storage configuration to be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:storage-configuration/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteStorageConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteStorageConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteStorageConfiguration_Errors"></a>

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
<a name="API_DeleteStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/DeleteStorageConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/DeleteStorageConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/DeleteStorageConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/DeleteStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/DeleteStorageConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/DeleteStorageConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/DeleteStorageConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/DeleteStorageConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/DeleteStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/DeleteStorageConfiguration)
