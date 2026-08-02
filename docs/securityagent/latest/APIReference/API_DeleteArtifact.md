---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_DeleteArtifact.html
---

# DeleteArtifact
<a name="API_DeleteArtifact"></a>

Deletes an artifact from an agent space.

## Request Syntax
<a name="API_DeleteArtifact_RequestSyntax"></a>

```
POST /DeleteArtifact HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "artifactId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteArtifact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteArtifact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_DeleteArtifact_RequestSyntax) **   <a name="securityagent-DeleteArtifact-request-agentSpaceId"></a>
The unique identifier of the agent space that contains the artifact.
Type: String
Required: Yes

 ** [artifactId](#API_DeleteArtifact_RequestSyntax) **   <a name="securityagent-DeleteArtifact-request-artifactId"></a>
The unique identifier of the artifact to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteArtifact_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteArtifact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteArtifact_Errors"></a>

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
<a name="API_DeleteArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/DeleteArtifact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/DeleteArtifact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/DeleteArtifact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/DeleteArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/DeleteArtifact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/DeleteArtifact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/DeleteArtifact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/DeleteArtifact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/DeleteArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/DeleteArtifact)
