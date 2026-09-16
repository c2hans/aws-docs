---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListRunCaches.html
---

# ListRunCaches
<a name="API_ListRunCaches"></a>

Retrieves a list of your run caches and the metadata for each cache.

## Request Syntax
<a name="API_ListRunCaches_RequestSyntax"></a>

```
GET /runCache?maxResults={{maxResults}}&startingToken={{startingToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRunCaches_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListRunCaches_RequestSyntax) **   <a name="omics-ListRunCaches-request-uri-maxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [startingToken](#API_ListRunCaches_RequestSyntax) **   <a name="omics-ListRunCaches-request-uri-startingToken"></a>
Optional pagination token returned from a prior call to the `ListRunCaches` API operation.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Request Body
<a name="API_ListRunCaches_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRunCaches_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "cacheBehavior": "string",
         "cacheS3Uri": "string",
         "creationTime": "string",
         "id": "string",
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListRunCaches_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListRunCaches_ResponseSyntax) **   <a name="omics-ListRunCaches-response-items"></a>
Details about each run cache in the response.
Type: Array of [RunCacheListItem](API_RunCacheListItem.md) objects

 ** [nextToken](#API_ListRunCaches_ResponseSyntax) **   <a name="omics-ListRunCaches-response-nextToken"></a>
Pagination token to retrieve additional run caches. If the response does not have a `nextToken`value, you have reached to the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_ListRunCaches_Errors"></a>

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
<a name="API_ListRunCaches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListRunCaches)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListRunCaches)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListRunCaches)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListRunCaches)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListRunCaches)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListRunCaches)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListRunCaches)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListRunCaches)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListRunCaches)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListRunCaches)
