---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_UpdateRunCache.html
---

# UpdateRunCache
<a name="API_UpdateRunCache"></a>

Updates a run cache using its ID and returns a response with no body if the operation is successful. You can update the run cache description, name, or the default run cache behavior with `CACHE_ON_FAILURE` or `CACHE_ALWAYS`. To confirm that your run cache settings have been properly updated, use the `GetRunCache` API operation.

For more information, see [How call caching works](https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_UpdateRunCache_RequestSyntax"></a>

```
POST /runCache/{{id}} HTTP/1.1
Content-type: application/json

{
   "cacheBehavior": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRunCache_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateRunCache_RequestSyntax) **   <a name="omics-UpdateRunCache-request-uri-id"></a>
The identifier of the run cache you want to update.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateRunCache_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [cacheBehavior](#API_UpdateRunCache_RequestSyntax) **   <a name="omics-UpdateRunCache-request-cacheBehavior"></a>
Update the default run cache behavior.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CACHE_ON_FAILURE | CACHE_ALWAYS`
Required: No

 ** [description](#API_UpdateRunCache_RequestSyntax) **   <a name="omics-UpdateRunCache-request-description"></a>
Update the run cache description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [name](#API_UpdateRunCache_RequestSyntax) **   <a name="omics-UpdateRunCache-request-name"></a>
Update the name of the run cache.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

## Response Syntax
<a name="API_UpdateRunCache_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_UpdateRunCache_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_UpdateRunCache_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRunCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/UpdateRunCache)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/UpdateRunCache)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/UpdateRunCache)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/UpdateRunCache)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/UpdateRunCache)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/UpdateRunCache)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/UpdateRunCache)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/UpdateRunCache)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/UpdateRunCache)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/UpdateRunCache)
