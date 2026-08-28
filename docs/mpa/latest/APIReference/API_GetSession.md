---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetSession.html
---

# GetSession
<a name="API_GetSession"></a>

Returns details for an approval session. For more information, see [Session](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html) in the *Multi-party approval User Guide*.

## Request Syntax
<a name="API_GetSession_RequestSyntax"></a>

```
GET /sessions/{{SessionArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SessionArn](#API_GetSession_RequestSyntax) **   <a name="mpa-GetSession-request-uri-SessionArn"></a>
Amazon Resource Name (ARN) for the session.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:session/[a-zA-Z0-9._-]+/[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_GetSession_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ActionCompletionStrategy": "string",
   "ActionName": "string",
   "AdditionalSecurityRequirements": [ "string" ],
   "ApprovalStrategy": { ... },
   "ApprovalTeamArn": "string",
   "ApprovalTeamName": "string",
   "ApproverResponses": [
      {
         "ApproverId": "string",
         "IdentityId": "string",
         "IdentitySourceArn": "string",
         "Response": "string",
         "ResponseTime": "string"
      }
   ],
   "CompletionTime": "string",
   "Description": "string",
   "ExecutionStatus": "string",
   "ExpirationTime": "string",
   "InitiationTime": "string",
   "Metadata": {
      "string" : "string"
   },
   "NumberOfApprovers": number,
   "ProtectedResourceArn": "string",
   "RequesterAccountId": "string",
   "RequesterComment": "string",
   "RequesterPrincipalArn": "string",
   "RequesterRegion": "string",
   "RequesterServicePrincipal": "string",
   "SessionArn": "string",
   "Status": "string",
   "StatusCode": "string",
   "StatusMessage": "string"
}
```

## Response Elements
<a name="API_GetSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActionCompletionStrategy](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-ActionCompletionStrategy"></a>
Strategy for executing the protected operation. `AUTO_COMPLETION_UPON_APPROVAL` means the operation is automatically executed using the requester's permissions, if approved.
Type: String
Valid Values: `AUTO_COMPLETION_UPON_APPROVAL`

 ** [ActionName](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-ActionName"></a>
Name of the protected operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [AdditionalSecurityRequirements](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-AdditionalSecurityRequirements"></a>
A list of `AdditionalSecurityRequirement` applied to the session.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Valid Values: `APPROVER_VERIFICATION_REQUIRED`

 ** [ApprovalStrategy](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-ApprovalStrategy"></a>
An `ApprovalStrategyResponse` object. Contains details for how the team grants approval
Type: [ApprovalStrategyResponse](API_ApprovalStrategyResponse.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [ApprovalTeamArn](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-ApprovalTeamArn"></a>
Amazon Resource Name (ARN) for the approval team.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:approval-team/[a-zA-Z0-9._-]+`

 ** [ApprovalTeamName](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-ApprovalTeamName"></a>
Name of the approval team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9._-]+`

 ** [ApproverResponses](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-ApproverResponses"></a>
An array of `GetSessionResponseApproverResponse` objects. Contains details for approver responses in the session.
Type: Array of [GetSessionResponseApproverResponse](API_GetSessionResponseApproverResponse.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [CompletionTime](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-CompletionTime"></a>
Timestamp when the session completed.
Type: Timestamp

 ** [Description](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-Description"></a>
Description for the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ExecutionStatus](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-ExecutionStatus"></a>
Status for the protected operation. For example, if the operation is `PENDING`.
Type: String
Valid Values: `EXECUTED | FAILED | PENDING`

 ** [ExpirationTime](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-ExpirationTime"></a>
Timestamp when the session will expire.
Type: Timestamp

 ** [InitiationTime](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-InitiationTime"></a>
Timestamp when the session was initiated.
Type: Timestamp

 ** [Metadata](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-Metadata"></a>
Metadata for the session.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[a-zA-Z0-9\p{P}]*`
Value Length Constraints: Minimum length of 1. Maximum length of 200.
Value Pattern: `[a-zA-Z0-9\p{P}]*`

 ** [NumberOfApprovers](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-NumberOfApprovers"></a>
Total number of approvers in the session.
Type: Integer

 ** [ProtectedResourceArn](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-ProtectedResourceArn"></a>
Amazon Resource Name (ARN) for the protected operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [RequesterAccountId](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-RequesterAccountId"></a>
ID for the account that made the operation request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `\d{12}`

 ** [RequesterComment](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-RequesterComment"></a>
Message from the account that made the operation request
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.

 ** [RequesterPrincipalArn](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-RequesterPrincipalArn"></a>
 [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-request) that made the operation request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [RequesterRegion](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-RequesterRegion"></a>
 AWS Region where the operation request originated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.

 ** [RequesterServicePrincipal](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-RequesterServicePrincipal"></a>
 [Service principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services) for the service associated with the protected operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [SessionArn](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-SessionArn"></a>
Amazon Resource Name (ARN) for the session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:session/[a-zA-Z0-9._-]+/[a-zA-Z0-9_-]+`

 ** [Status](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-Status"></a>
Status for the session. For example, if the team has approved the requested operation.
Type: String
Valid Values: `PENDING | CANCELLED | APPROVED | FAILED | CREATING`

 ** [StatusCode](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-StatusCode"></a>
Status code of the session.
Type: String
Valid Values: `REJECTED | EXPIRED | CONFIGURATION_CHANGED | ALL_APPROVERS_IN_SESSION`

 ** [StatusMessage](#API_GetSession_ResponseSyntax) **   <a name="mpa-GetSession-response-StatusMessage"></a>
Message describing the status for session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

## Errors
<a name="API_GetSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You do not have sufficient access to perform this action. Check your permissions, and try again.
 ** Message **
Message for the `AccessDeniedException` error.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error. Try your request again. If the problem persists, contact AWS Support.
 ** Message **
Message for the `InternalServerException` error.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The specified resource doesn't exist. Check the resource ID, and try again.
 ** Message **
Message for the `ResourceNotFoundException` error.
HTTP Status Code: 404

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling.
 ** Message **
Message for the `ThrottlingException` error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the constraints specified by an AWS service.
 ** Message **
Message for the `ValidationException` error.
HTTP Status Code: 400

## See Also
<a name="API_GetSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/GetSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/GetSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/GetSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/GetSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/GetSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/GetSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/GetSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/GetSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/GetSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/GetSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
