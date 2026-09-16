---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchGetArtifactMetadata.html
---

# BatchGetArtifactMetadata
<a name="API_BatchGetArtifactMetadata"></a>

Retrieves metadata for one or more artifacts in an agent space.

## Request Syntax
<a name="API_BatchGetArtifactMetadata_RequestSyntax"></a>

```
POST /BatchGetArtifactMetadata HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "artifactIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetArtifactMetadata_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetArtifactMetadata_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_BatchGetArtifactMetadata_RequestSyntax) **   <a name="securityagent-BatchGetArtifactMetadata-request-agentSpaceId"></a>
The unique identifier of the agent space that contains the artifacts.
Type: String
Required: Yes

 ** [artifactIds](#API_BatchGetArtifactMetadata_RequestSyntax) **   <a name="securityagent-BatchGetArtifactMetadata-request-artifactIds"></a>
The list of artifact identifiers to retrieve metadata for.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetArtifactMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "artifactMetadataList": [
      {
         "agentSpaceId": "string",
         "artifactId": "string",
         "fileName": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetArtifactMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [artifactMetadataList](#API_BatchGetArtifactMetadata_ResponseSyntax) **   <a name="securityagent-BatchGetArtifactMetadata-response-artifactMetadataList"></a>
The list of artifact metadata items that were found.
Type: Array of [ArtifactMetadataItem](API_ArtifactMetadataItem.md) objects

## Errors
<a name="API_BatchGetArtifactMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
Error description.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of your request.
 ** message **
Error description.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.
 ** message **
Error description.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
Error description.
 ** quotaCode **
Quota code for throttling limit.
 ** serviceCode **
Service code for throttling limit.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered during validation.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetArtifactMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchGetArtifactMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchGetArtifactMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchGetArtifactMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchGetArtifactMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchGetArtifactMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchGetArtifactMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchGetArtifactMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchGetArtifactMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchGetArtifactMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchGetArtifactMetadata)
