---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_CreateCodeFinding.html
---

# CreateCodeFinding
<a name="API_CreateCodeFinding"></a>

Ingests a customer-supplied security finding into an environment. Continuum validates the document synchronously against the required overlay fields for the declared format; invalid documents are rejected with a ValidationException. The maximum accepted document size is 256 KB. The environment must have a source configured, and the finding must identify a code location so Continuum can tie it to a repository in the environment's build. Continuum assigns a findingId and stores the verbatim document. When no successful build yet contains the finding's repository, the finding stays SUBMITTED until the next successful build; if that build does not contain it either, the finding is DISCARDED with discardReason SOURCE\_REPO\_NOT\_FOUND.

## Request Syntax
<a name="API_CreateCodeFinding_RequestSyntax"></a>

```
POST /environments/{{environmentId}}/code-findings HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "ocsfDocument": {{JSON value}}
}
```

## URI Request Parameters
<a name="API_CreateCodeFinding_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_CreateCodeFinding_RequestSyntax) **   <a name="continuum-CreateCodeFinding-request-uri-environmentId"></a>
The identifier of the environment.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_CreateCodeFinding_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateCodeFinding_RequestSyntax) **   <a name="continuum-CreateCodeFinding-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[!-~]+`
Required: No

 ** [ocsfDocument](#API_CreateCodeFinding_RequestSyntax) **   <a name="continuum-CreateCodeFinding-request-ocsfDocument"></a>
The ocsf Document.
Type: JSON value
Required: Yes

## Response Syntax
<a name="API_CreateCodeFinding_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdAt": "string",
   "findingArn": "string",
   "findingId": "string",
   "status": "string",
   "title": "string"
}
```

## Response Elements
<a name="API_CreateCodeFinding_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateCodeFinding_ResponseSyntax) **   <a name="continuum-CreateCodeFinding-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [findingArn](#API_CreateCodeFinding_ResponseSyntax) **   <a name="continuum-CreateCodeFinding-response-findingArn"></a>
The Amazon Resource Name (ARN) of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:environments/[a-z0-9]+/code-findings/[a-z0-9]+`

 ** [findingId](#API_CreateCodeFinding_ResponseSyntax) **   <a name="continuum-CreateCodeFinding-response-findingId"></a>
The identifier of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [status](#API_CreateCodeFinding_ResponseSyntax) **   <a name="continuum-CreateCodeFinding-response-status"></a>
The lifecycle status of a finding as it moves through Continuum's processing pipeline. CONFIRMED and DISCARDED are terminal states — a CONFIRMED finding is promoted into a separate Issue (not yet implemented), which owns the subsequent remediation lifecycle; the finding's own status does not change after that.
Type: String
Valid Values: `SUBMITTED | VALIDATING | CONFIRMED | DISCARDED`

 ** [title](#API_CreateCodeFinding_ResponseSyntax) **   <a name="continuum-CreateCodeFinding-response-title"></a>
The title.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_CreateCodeFinding_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
HTTP Status Code: 409

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
<a name="API_CreateCodeFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/CreateCodeFinding)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/CreateCodeFinding)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/CreateCodeFinding)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/CreateCodeFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/CreateCodeFinding)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/CreateCodeFinding)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/CreateCodeFinding)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/CreateCodeFinding)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/CreateCodeFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/CreateCodeFinding)
