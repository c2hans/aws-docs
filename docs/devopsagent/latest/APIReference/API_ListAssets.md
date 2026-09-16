---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListAssets.html
---

# ListAssets
<a name="API_ListAssets"></a>

Lists assets in the specified agent space

## Request Syntax
<a name="API_ListAssets_RequestSyntax"></a>

```
GET /asset/agent-space/{{agentSpaceId}}/assets?assetType={{assetType}}&maxResults={{maxResults}}&nextToken={{nextToken}}&updatedAfter={{updatedAfter}}&updatedBefore={{updatedBefore}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentSpaceId](#API_ListAssets_RequestSyntax) **   <a name="devopsagent-ListAssets-request-uri-agentSpaceId"></a>
The unique identifier for the agent space to list assets from
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [assetType](#API_ListAssets_RequestSyntax) **   <a name="devopsagent-ListAssets-request-uri-assetType"></a>
Filter results to only assets of this type
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [maxResults](#API_ListAssets_RequestSyntax) **   <a name="devopsagent-ListAssets-request-uri-maxResults"></a>
The maximum number of results to return in a single response
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAssets_RequestSyntax) **   <a name="devopsagent-ListAssets-request-uri-nextToken"></a>
Pagination token from a previous response to retrieve the next page of results
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [updatedAfter](#API_ListAssets_RequestSyntax) **   <a name="devopsagent-ListAssets-request-uri-updatedAfter"></a>
Filter results to only assets updated after this timestamp

 ** [updatedBefore](#API_ListAssets_RequestSyntax) **   <a name="devopsagent-ListAssets-request-uri-updatedBefore"></a>
Filter results to only assets updated before this timestamp

## Request Body
<a name="API_ListAssets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "assetId": "string",
         "assetType": "string",
         "createdAt": number,
         "metadata": JSON value,
         "updatedAt": number,
         "version": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAssets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListAssets_ResponseSyntax) **   <a name="devopsagent-ListAssets-response-items"></a>
The list of assets for the agent space
Type: Array of [Asset](API_Asset.md) objects

 ** [nextToken](#API_ListAssets_ResponseSyntax) **   <a name="devopsagent-ListAssets-response-nextToken"></a>
Pagination token to retrieve the next page of results. Absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListAssets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the requested resource is denied due to insufficient permissions.
 ** message **
Detailed error message describing why access was denied.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** message **
Detailed error message describing the conflict.
HTTP Status Code: 409

 ** ContentSizeExceededException **
This exception is thrown when the content size exceeds the allowed limit.
HTTP Status Code: 413

 ** InternalServerException **
This exception is thrown when an unexpected error occurs in the processing of a request.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more parameters provided in the request are invalid.
 ** message **
Detailed error message describing which parameter is invalid and why.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** message **
Detailed error message describing which resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed the service quota limit.
 ** message **
Detailed error message describing which quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled due to too many requests. Please slow down and try again.
 ** message **
Detailed error message describing the throttling condition.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered while validating the input. A member can appear in this list more than once if it failed to satisfy multiple constraints.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListAssets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/ListAssets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/ListAssets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ListAssets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/ListAssets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ListAssets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/ListAssets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/ListAssets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/ListAssets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/ListAssets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ListAssets)
