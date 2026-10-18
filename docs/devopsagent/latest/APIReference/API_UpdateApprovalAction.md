---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateApprovalAction.html
---

# UpdateApprovalAction
<a name="API_UpdateApprovalAction"></a>

Updates an approval request with the terminal decision (APPROVED or REJECTED). A single operation handles both verbs via the action enum.

## Request Syntax
<a name="API_UpdateApprovalAction_RequestSyntax"></a>

```
POST /agents/agent-space/{{agentSpaceId}}/approvals/{{approvalId}}/update-action HTTP/1.1
Content-type: application/json

{
   "action": "{{string}}",
   "finalPattern": {
      "argumentPins": {
         "{{string}}" : "{{string}}"
      },
      "tool": "{{string}}"
   },
   "reason": "{{string}}",
   "singleUse": {{boolean}},
   "ttlSeconds": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateApprovalAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentSpaceId](#API_UpdateApprovalAction_RequestSyntax) **   <a name="devopsagent-UpdateApprovalAction-request-uri-agentSpaceId"></a>
The agent space identifier — multi-tenant workspace scope. Bound from the request URI.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [approvalId](#API_UpdateApprovalAction_RequestSyntax) **   <a name="devopsagent-UpdateApprovalAction-request-uri-approvalId"></a>
Identifier of the approval request being resolved. A UUID. Bound from the request URI.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-7[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`
Required: Yes

## Request Body
<a name="API_UpdateApprovalAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_UpdateApprovalAction_RequestSyntax) **   <a name="devopsagent-UpdateApprovalAction-request-action"></a>
The action to take on the approval request — APPROVED or REJECTED.
Type: String
Valid Values: `APPROVED | REJECTED`
Required: Yes

 ** [finalPattern](#API_UpdateApprovalAction_RequestSyntax) **   <a name="devopsagent-UpdateApprovalAction-request-finalPattern"></a>
The finalized pattern (tool \+ argumentPins) that scopes the approval. Required when `action` is APPROVED; must be absent when `action` is REJECTED. The pattern narrows, and must not widen, the invocation originally requested by the agent. This cross-field invariant is enforced by service-side validation.
Type: [ApprovalPattern](API_ApprovalPattern.md) object
Required: No

 ** [reason](#API_UpdateApprovalAction_RequestSyntax) **   <a name="devopsagent-UpdateApprovalAction-request-reason"></a>
Optional free-text rationale for the decision. Permitted when `action` is REJECTED; ignored when `action` is APPROVED.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [singleUse](#API_UpdateApprovalAction_RequestSyntax) **   <a name="devopsagent-UpdateApprovalAction-request-singleUse"></a>
Whether the approved action backs a single executed tool call (true) or is reusable within ttlSeconds (false). Required when `action` is APPROVED; must be absent when `action` is REJECTED. When true, ttlSeconds must be absent (the redemption window collapses to the single use). When false, ttlSeconds is required and bounds the reuse window. Cross-field invariants are enforced by service-side validation.
Type: Boolean
Required: No

 ** [ttlSeconds](#API_UpdateApprovalAction_RequestSyntax) **   <a name="devopsagent-UpdateApprovalAction-request-ttlSeconds"></a>
Approval lifetime in seconds, starting from when the decision is submitted. Required when `action` is APPROVED AND `singleUse` is false; must be absent when `action` is REJECTED or when `singleUse` is true (a single-use approval backs one executed action and the redemption window collapses). Cross-field invariants are enforced by service-side validation; the @range bound here is the operation-boundary check that always applies (a maximum of 4 hours).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 14400.
Required: No

## Response Syntax
<a name="API_UpdateApprovalAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "approvalId": "string",
   "expiresAt": number,
   "status": "string"
}
```

## Response Elements
<a name="API_UpdateApprovalAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalId](#API_UpdateApprovalAction_ResponseSyntax) **   <a name="devopsagent-UpdateApprovalAction-response-approvalId"></a>
Identifier of the approval request that was resolved. Echoed back so the client can correlate the response with the request.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-7[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`

 ** [expiresAt](#API_UpdateApprovalAction_ResponseSyntax) **   <a name="devopsagent-UpdateApprovalAction-response-expiresAt"></a>
Absolute timestamp at which the approval expires. Set when status is APPROVED (computed as the submission time plus ttlSeconds); absent when status is REJECTED.
Type: Timestamp

 ** [status](#API_UpdateApprovalAction_ResponseSyntax) **   <a name="devopsagent-UpdateApprovalAction-response-status"></a>
Lifecycle status of the approval request immediately after submission. Expected post-submission states are APPROVED (when the action is APPROVED) or REJECTED (when the action is REJECTED); PENDING is not returned from this operation, and REVOKED and REDEEMED are reachable only via subsequent reads.
Type: String
Valid Values: `PENDING | APPROVED | REJECTED | REVOKED | REDEEMED`

## Errors
<a name="API_UpdateApprovalAction_Errors"></a>

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
<a name="API_UpdateApprovalAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/UpdateApprovalAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/UpdateApprovalAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/UpdateApprovalAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/UpdateApprovalAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/UpdateApprovalAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/UpdateApprovalAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/UpdateApprovalAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/UpdateApprovalAction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/UpdateApprovalAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/UpdateApprovalAction)
