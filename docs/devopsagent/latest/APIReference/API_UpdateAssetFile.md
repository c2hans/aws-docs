---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateAssetFile.html
---

# UpdateAssetFile
<a name="API_UpdateAssetFile"></a>

Updates a file in an asset

## Request Syntax
<a name="API_UpdateAssetFile_RequestSyntax"></a>

```
PATCH /asset/agent-space/{{agentSpaceId}}/assets/{{assetId}}/files/{{path+}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "content": { ... },
   "metadata": {{JSON value}}
}
```

## URI Request Parameters
<a name="API_UpdateAssetFile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentSpaceId](#API_UpdateAssetFile_RequestSyntax) **   <a name="devopsagent-UpdateAssetFile-request-uri-agentSpaceId"></a>
The unique identifier for the agent space containing the asset
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [assetId](#API_UpdateAssetFile_RequestSyntax) **   <a name="devopsagent-UpdateAssetFile-request-uri-assetId"></a>
The unique identifier of the asset containing the file
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [path](#API_UpdateAssetFile_RequestSyntax) **   <a name="devopsagent-UpdateAssetFile-request-uri-path"></a>
The path of the file within the asset to update
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9_./ ()-]+`
Required: Yes

## Request Body
<a name="API_UpdateAssetFile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateAssetFile_RequestSyntax) **   <a name="devopsagent-UpdateAssetFile-request-clientToken"></a>
A unique, case-sensitive identifier used for idempotent asset file update
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [content](#API_UpdateAssetFile_RequestSyntax) **   <a name="devopsagent-UpdateAssetFile-request-content"></a>
Updated file content. If omitted, the existing content is unchanged.
Type: [AssetFileBody](API_AssetFileBody.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [metadata](#API_UpdateAssetFile_RequestSyntax) **   <a name="devopsagent-UpdateAssetFile-request-metadata"></a>
Metadata fields to update. Only the fields present in this document are updated. Omitted fields retain their current values.
Type: JSON value
Required: No

## Response Syntax
<a name="API_UpdateAssetFile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "file": {
      "content": { ... },
      "createdAt": number,
      "metadata": JSON value,
      "path": "string",
      "updatedAt": number,
      "version": number
   }
}
```

## Response Elements
<a name="API_UpdateAssetFile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [file](#API_UpdateAssetFile_ResponseSyntax) **   <a name="devopsagent-UpdateAssetFile-response-file"></a>
The asset file object
Type: [AssetFile](API_AssetFile.md) object

## Errors
<a name="API_UpdateAssetFile_Errors"></a>

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
<a name="API_UpdateAssetFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/UpdateAssetFile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/UpdateAssetFile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/UpdateAssetFile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/UpdateAssetFile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/UpdateAssetFile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/UpdateAssetFile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/UpdateAssetFile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/UpdateAssetFile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/UpdateAssetFile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/UpdateAssetFile)
