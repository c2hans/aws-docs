---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetAsset.html
---

# GetAsset
<a name="API_GetAsset"></a>

Gets an asset from the specified agent space

## Request Syntax
<a name="API_GetAsset_RequestSyntax"></a>

```
GET /asset/agent-space/{{agentSpaceId}}/assets/{{assetId}}?assetVersion={{assetVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAsset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentSpaceId](#API_GetAsset_RequestSyntax) **   <a name="devopsagent-GetAsset-request-uri-agentSpaceId"></a>
The unique identifier for the agent space containing the asset
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [assetId](#API_GetAsset_RequestSyntax) **   <a name="devopsagent-GetAsset-request-uri-assetId"></a>
The unique identifier of the asset to retrieve
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [assetVersion](#API_GetAsset_RequestSyntax) **   <a name="devopsagent-GetAsset-request-uri-assetVersion"></a>
The specific version of the asset to retrieve. If omitted, the latest version is returned.
Valid Range: Minimum value of 1.

## Request Body
<a name="API_GetAsset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAsset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "asset": {
      "assetId": "string",
      "assetType": "string",
      "createdAt": number,
      "metadata": JSON value,
      "updatedAt": number,
      "version": number
   }
}
```

## Response Elements
<a name="API_GetAsset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [asset](#API_GetAsset_ResponseSyntax) **   <a name="devopsagent-GetAsset-response-asset"></a>
The asset object
Type: [Asset](API_Asset.md) object

## Errors
<a name="API_GetAsset_Errors"></a>

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
<a name="API_GetAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/GetAsset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/GetAsset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/GetAsset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/GetAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/GetAsset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/GetAsset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/GetAsset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/GetAsset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/GetAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/GetAsset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
