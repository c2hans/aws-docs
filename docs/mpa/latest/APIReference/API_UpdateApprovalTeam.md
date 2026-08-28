---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_UpdateApprovalTeam.html
---

# UpdateApprovalTeam
<a name="API_UpdateApprovalTeam"></a>

Updates an approval team. You can request to update the team description, approval threshold, and approvers in the team.

**Note**
 **Updates require team approval**
Updates to an active team must be approved by the team.

## Request Syntax
<a name="API_UpdateApprovalTeam_RequestSyntax"></a>

```
PATCH /approval-teams/{{Arn}} HTTP/1.1
Content-type: application/json

{
   "ApprovalStrategy": { ... },
   "Approvers": [
      {
         "PrimaryIdentityId": "{{string}}",
         "PrimaryIdentitySourceArn": "{{string}}"
      }
   ],
   "Description": "{{string}}",
   "UpdateActions": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateApprovalTeam_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Arn](#API_UpdateApprovalTeam_RequestSyntax) **   <a name="mpa-UpdateApprovalTeam-request-uri-Arn"></a>
Amazon Resource Name (ARN) for the team.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:approval-team/[a-zA-Z0-9._-]+`
Required: Yes

## Request Body
<a name="API_UpdateApprovalTeam_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApprovalStrategy](#API_UpdateApprovalTeam_RequestSyntax) **   <a name="mpa-UpdateApprovalTeam-request-ApprovalStrategy"></a>
An `ApprovalStrategy` object. Contains details for how the team grants approval.
Type: [ApprovalStrategy](API_ApprovalStrategy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [Approvers](#API_UpdateApprovalTeam_RequestSyntax) **   <a name="mpa-UpdateApprovalTeam-request-Approvers"></a>
An array of `ApprovalTeamRequestApprover` objects. Contains details for the approvers in the team.
Type: Array of [ApprovalTeamRequestApprover](API_ApprovalTeamRequestApprover.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** [Description](#API_UpdateApprovalTeam_RequestSyntax) **   <a name="mpa-UpdateApprovalTeam-request-Description"></a>
Description for the team.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [UpdateActions](#API_UpdateApprovalTeam_RequestSyntax) **   <a name="mpa-UpdateApprovalTeam-request-UpdateActions"></a>
A list of `UpdateAction` to perform when updating the team.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Valid Values: `SYNCHRONIZE_MFA_DEVICES`
Required: No

## Response Syntax
<a name="API_UpdateApprovalTeam_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "VersionId": "string"
}
```

## Response Elements
<a name="API_UpdateApprovalTeam_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VersionId](#API_UpdateApprovalTeam_ResponseSyntax) **   <a name="mpa-UpdateApprovalTeam-response-VersionId"></a>
Version ID for the team that was created. When an approval team is updated, the version ID changes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Errors
<a name="API_UpdateApprovalTeam_Errors"></a>

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

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The specified resource doesn't exist. Check the resource ID, and try again.
 ** Message **
Message for the `ResourceNotFoundException` error.
HTTP Status Code: 404

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
<a name="API_UpdateApprovalTeam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/UpdateApprovalTeam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/UpdateApprovalTeam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/UpdateApprovalTeam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/UpdateApprovalTeam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/UpdateApprovalTeam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/UpdateApprovalTeam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/UpdateApprovalTeam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/UpdateApprovalTeam)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/UpdateApprovalTeam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/UpdateApprovalTeam)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
