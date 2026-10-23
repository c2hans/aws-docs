---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetCodeIssueArtifact.html
---

# GetCodeIssueArtifact
<a name="API_GetCodeIssueArtifact"></a>

Retrieves one immutable artifact attached to an issue, including its content.

## Request Syntax
<a name="API_GetCodeIssueArtifact_RequestSyntax"></a>

```
GET /environments/{{environmentId}}/code-issues/{{issueId}}/artifacts/{{artifactId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCodeIssueArtifact_RequestParameters"></a>

The request uses the following URI parameters.

 ** [artifactId](#API_GetCodeIssueArtifact_RequestSyntax) **   <a name="continuum-GetCodeIssueArtifact-request-uri-artifactId"></a>
The identifier of the artifact.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** [environmentId](#API_GetCodeIssueArtifact_RequestSyntax) **   <a name="continuum-GetCodeIssueArtifact-request-uri-environmentId"></a>
The identifier of the environment.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** [issueId](#API_GetCodeIssueArtifact_RequestSyntax) **   <a name="continuum-GetCodeIssueArtifact-request-uri-issueId"></a>
The identifier of the issue.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetCodeIssueArtifact_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCodeIssueArtifact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "artifactId": "string",
   "artifactType": "string",
   "body": { ... },
   "createdAt": "string",
   "mediaType": "string",
   "metadata": JSON value,
   "producer": {
      "agent": "string"
   }
}
```

## Response Elements
<a name="API_GetCodeIssueArtifact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [artifactId](#API_GetCodeIssueArtifact_ResponseSyntax) **   <a name="continuum-GetCodeIssueArtifact-response-artifactId"></a>
The identifier of the artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [artifactType](#API_GetCodeIssueArtifact_ResponseSyntax) **   <a name="continuum-GetCodeIssueArtifact-response-artifactType"></a>
The artifact Type.
Type: String
Valid Values: `EVIDENCE | AGENT_COMMUNICATION | VALIDATION_EVIDENCE | REMEDIATION_PROPOSAL | DECISION | PATCH`

 ** [body](#API_GetCodeIssueArtifact_ResponseSyntax) **   <a name="continuum-GetCodeIssueArtifact-response-body"></a>
The projected body of an artifact. The active member is selected by the artifact's artifactType, and for a type that carries more than one payload kind by the stored content's own discriminator; `raw` carries content for types with no defined shape yet and for content that did not match its shape.
Type: [IssueArtifactBody](API_IssueArtifactBody.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_GetCodeIssueArtifact_ResponseSyntax) **   <a name="continuum-GetCodeIssueArtifact-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [mediaType](#API_GetCodeIssueArtifact_ResponseSyntax) **   <a name="continuum-GetCodeIssueArtifact-response-mediaType"></a>
The media Type.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [metadata](#API_GetCodeIssueArtifact_ResponseSyntax) **   <a name="continuum-GetCodeIssueArtifact-response-metadata"></a>
The metadata.
Type: JSON value

 ** [producer](#API_GetCodeIssueArtifact_ResponseSyntax) **   <a name="continuum-GetCodeIssueArtifact-response-producer"></a>
The producer.
Type: [IssueArtifactProducerSummary](API_IssueArtifactProducerSummary.md) object

## Errors
<a name="API_GetCodeIssueArtifact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_GetCodeIssueArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/GetCodeIssueArtifact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/GetCodeIssueArtifact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/GetCodeIssueArtifact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/GetCodeIssueArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/GetCodeIssueArtifact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/GetCodeIssueArtifact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/GetCodeIssueArtifact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/GetCodeIssueArtifact)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/GetCodeIssueArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/GetCodeIssueArtifact)
