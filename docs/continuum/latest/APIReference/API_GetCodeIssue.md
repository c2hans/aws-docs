---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetCodeIssue.html
---

# GetCodeIssue
<a name="API_GetCodeIssue"></a>

Retrieves the current state and details of an issue.

## Request Syntax
<a name="API_GetCodeIssue_RequestSyntax"></a>

```
GET /environments/{{environmentId}}/code-issues/{{issueId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCodeIssue_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_GetCodeIssue_RequestSyntax) **   <a name="continuum-GetCodeIssue-request-uri-environmentId"></a>
The identifier of the environment.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** [issueId](#API_GetCodeIssue_RequestSyntax) **   <a name="continuum-GetCodeIssue-request-uri-issueId"></a>
The identifier of the issue.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetCodeIssue_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCodeIssue_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "confidence": number,
   "createdAt": "string",
   "evidenceAvailability": "string",
   "findingIds": [ "string" ],
   "issueArn": "string",
   "issueId": "string",
   "name": "string",
   "patchDelivery": {
      "failedCount": number,
      "failureReasons": [ "string" ],
      "patchCount": number,
      "status": "string",
      "succeededCount": number
   },
   "phase": "string",
   "severity": "string",
   "severityReasoning": "string",
   "status": "string",
   "statusMessage": "string",
   "statusReason": "string",
   "statusUpdatedAt": "string",
   "summary": "string",
   "synopsis": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetCodeIssue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [confidence](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-confidence"></a>
The confidence.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [createdAt](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [evidenceAvailability](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-evidenceAvailability"></a>
The evidence Availability.
Type: String
Valid Values: `NONE | AVAILABLE`

 ** [findingIds](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-findingIds"></a>
The finding Ids.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [issueArn](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-issueArn"></a>
The Amazon Resource Name (ARN) of the issue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:environments/[a-z0-9]+/code-issues/[a-z0-9]+`

 ** [issueId](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-issueId"></a>
The identifier of the issue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [name](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [patchDelivery](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-patchDelivery"></a>
The patch Delivery.
Type: [IssuePatchDelivery](API_IssuePatchDelivery.md) object

 ** [phase](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-phase"></a>
The phase.
Type: String
Valid Values: `VALIDATION | PRIORITIZATION | REMEDIATION`

 ** [severity](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-severity"></a>
The severity.
Type: String
Valid Values: `LOW | MEDIUM | HIGH | CRITICAL`

 ** [severityReasoning](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-severityReasoning"></a>
The severity Reasoning.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [status](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-status"></a>
The current status of the resource.
Type: String
Valid Values: `CREATED | IN_PROGRESS | COMPLETED | FAILED`

 ** [statusMessage](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-statusMessage"></a>
The status Message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [statusReason](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-statusReason"></a>
The status Reason.
Type: String
Valid Values: `INTERNAL_ERROR | REMEDIATION_FAILED`

 ** [statusUpdatedAt](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-statusUpdatedAt"></a>
The status Updated At.
Type: Timestamp

 ** [summary](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-summary"></a>
The summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [synopsis](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-synopsis"></a>
The synopsis.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [updatedAt](#API_GetCodeIssue_ResponseSyntax) **   <a name="continuum-GetCodeIssue-response-updatedAt"></a>
The timestamp when the resource was last updated.
Type: Timestamp

## Errors
<a name="API_GetCodeIssue_Errors"></a>

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
<a name="API_GetCodeIssue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/GetCodeIssue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/GetCodeIssue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/GetCodeIssue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/GetCodeIssue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/GetCodeIssue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/GetCodeIssue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/GetCodeIssue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/GetCodeIssue)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/GetCodeIssue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/GetCodeIssue)
