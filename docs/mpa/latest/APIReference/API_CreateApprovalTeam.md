---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_CreateApprovalTeam.html
---

# CreateApprovalTeam
<a name="API_CreateApprovalTeam"></a>

Creates a new approval team. For more information, see [Approval team](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html) in the *Multi-party approval User Guide*.

## Request Syntax
<a name="API_CreateApprovalTeam_RequestSyntax"></a>

```
POST /approval-teams HTTP/1.1
Content-type: application/json

{
   "ApprovalStrategy": { ... },
   "Approvers": [
      {
         "PrimaryIdentityId": "{{string}}",
         "PrimaryIdentitySourceArn": "{{string}}"
      }
   ],
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Policies": [
      {
         "PolicyArn": "{{string}}"
      }
   ],
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateApprovalTeam_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateApprovalTeam_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApprovalStrategy](#API_CreateApprovalTeam_RequestSyntax) **   <a name="mpa-CreateApprovalTeam-request-ApprovalStrategy"></a>
An `ApprovalStrategy` object. Contains details for how the team grants approval.
Type: [ApprovalStrategy](API_ApprovalStrategy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Approvers](#API_CreateApprovalTeam_RequestSyntax) **   <a name="mpa-CreateApprovalTeam-request-Approvers"></a>
An array of `ApprovalTeamRequesterApprovers` objects. Contains details for the approvers in the team.
Type: Array of [ApprovalTeamRequestApprover](API_ApprovalTeamRequestApprover.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** [ClientToken](#API_CreateApprovalTeam_RequestSyntax) **   <a name="mpa-CreateApprovalTeam-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS populates this field.
 **What is idempotency?**
When you make a mutating API request, the request typically returns a result before the operation's asynchronous workflows have completed. Operations might also time out or encounter other server issues before they complete, even though the request has already returned a result. This could make it difficult to determine whether the request succeeded or not, and could lead to multiple retries to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation is completed multiple times. This means that you might create more resources than you intended.
 *Idempotency* ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [Description](#API_CreateApprovalTeam_RequestSyntax) **   <a name="mpa-CreateApprovalTeam-request-Description"></a>
Description for the team.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [Name](#API_CreateApprovalTeam_RequestSyntax) **   <a name="mpa-CreateApprovalTeam-request-Name"></a>
Name of the team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9._-]+`
Required: Yes

 ** [Policies](#API_CreateApprovalTeam_RequestSyntax) **   <a name="mpa-CreateApprovalTeam-request-Policies"></a>
An array of `PolicyReference` objects. Contains a list of policies that define the permissions for team resources.
Type: Array of [PolicyReference](API_PolicyReference.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [Tags](#API_CreateApprovalTeam_RequestSyntax) **   <a name="mpa-CreateApprovalTeam-request-Tags"></a>
Tags you want to attach to the team.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateApprovalTeam_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreationTime": "string",
   "Name": "string",
   "VersionId": "string"
}
```

## Response Elements
<a name="API_CreateApprovalTeam_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateApprovalTeam_ResponseSyntax) **   <a name="mpa-CreateApprovalTeam-response-Arn"></a>
Amazon Resource Name (ARN) for the team that was created.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:approval-team/[a-zA-Z0-9._-]+`

 ** [CreationTime](#API_CreateApprovalTeam_ResponseSyntax) **   <a name="mpa-CreateApprovalTeam-response-CreationTime"></a>
Timestamp when the team was created.
Type: Timestamp

 ** [Name](#API_CreateApprovalTeam_ResponseSyntax) **   <a name="mpa-CreateApprovalTeam-response-Name"></a>
Name of the team that was created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [VersionId](#API_CreateApprovalTeam_ResponseSyntax) **   <a name="mpa-CreateApprovalTeam-response-VersionId"></a>
Version ID for the team that was created. When a team is updated, the version ID changes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Errors
<a name="API_CreateApprovalTeam_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You do not have sufficient access to perform this action. Check your permissions, and try again.
 ** Message **
Message for the `AccessDeniedException` error.
HTTP Status Code: 403

 [ConflictException](API_ConflictException.md)
The request cannot be completed because it conflicts with the current state of a resource.
 ** Message **
Message for the `ConflictException` error.
HTTP Status Code: 409

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error. Try your request again. If the problem persists, contact AWS Support.
 ** Message **
Message for the `InternalServerException` error.
HTTP Status Code: 500

 [ServiceQuotaExceededException](API_ServiceQuotaExceededException.md)
The request exceeds the service quota for your account. Request a quota increase or reduce your request size.
 ** Message **
Message for the `ServiceQuotaExceededException` error.
HTTP Status Code: 402

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
<a name="API_CreateApprovalTeam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/CreateApprovalTeam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/CreateApprovalTeam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/CreateApprovalTeam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/CreateApprovalTeam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/CreateApprovalTeam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/CreateApprovalTeam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/CreateApprovalTeam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/CreateApprovalTeam)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/CreateApprovalTeam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/CreateApprovalTeam)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
