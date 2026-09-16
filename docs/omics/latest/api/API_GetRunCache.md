---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetRunCache.html
---

# GetRunCache
<a name="API_GetRunCache"></a>

Retrieves detailed information about the specified run cache using its ID.

For more information, see [Call caching for AWS HealthOmics runs](https://docs.aws.amazon.com/omics/latest/dev/workflows-call-caching.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_GetRunCache_RequestSyntax"></a>

```
GET /runCache/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRunCache_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetRunCache_RequestSyntax) **   <a name="omics-GetRunCache-request-uri-id"></a>
The identifier of the run cache to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetRunCache_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRunCache_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "cacheBehavior": "string",
   "cacheBucketOwnerId": "string",
   "cacheS3Uri": "string",
   "creationTime": "string",
   "description": "string",
   "id": "string",
   "name": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetRunCache_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetRunCache_ResponseSyntax) **   <a name="omics-GetRunCache-response-arn"></a>
Unique resource identifier for the run cache.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`

 ** [cacheBehavior](#API_GetRunCache_ResponseSyntax) **   <a name="omics-GetRunCache-response-cacheBehavior"></a>
The default cache behavior for runs using this cache.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CACHE_ON_FAILURE | CACHE_ALWAYS`

 ** [cacheBucketOwnerId](#API_GetRunCache_ResponseSyntax) **   <a name="omics-GetRunCache-response-cacheBucketOwnerId"></a>
The identifier of the bucket owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`

 ** [cacheS3Uri](#API_GetRunCache_ResponseSyntax) **   <a name="omics-GetRunCache-response-cacheS3Uri"></a>
The S3 URI where the cache data is stored.
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])(/(.{0,1024}))?`

 ** [creationTime](#API_GetRunCache_ResponseSyntax) **   <a name="omics-GetRunCache-response-creationTime"></a>
Creation time of the run cache (an ISO 8601 formatted string).
Type: Timestamp

 ** [description](#API_GetRunCache_ResponseSyntax) **   <a name="omics-GetRunCache-response-description"></a>
The run cache description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [id](#API_GetRunCache_ResponseSyntax) **   <a name="omics-GetRunCache-response-id"></a>
The run cache ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [name](#API_GetRunCache_ResponseSyntax) **   <a name="omics-GetRunCache-response-name"></a>
The run cache name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [status](#API_GetRunCache_ResponseSyntax) **   <a name="omics-GetRunCache-response-status"></a>
The run cache status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `ACTIVE | DELETED | FAILED`

 ** [tags](#API_GetRunCache_ResponseSyntax) **   <a name="omics-GetRunCache-response-tags"></a>
The tags associated with the run cache.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetRunCache_Errors"></a>

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
<a name="API_GetRunCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetRunCache)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetRunCache)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetRunCache)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetRunCache)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetRunCache)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetRunCache)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetRunCache)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetRunCache)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetRunCache)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetRunCache)
