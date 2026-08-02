---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_DeleteInactiveApprovalTeamVersion.html
---

# DeleteInactiveApprovalTeamVersion
<a name="API_DeleteInactiveApprovalTeamVersion"></a>

Deletes an inactive approval team. For more information, see [Team health](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html) in the *Multi-party approval User Guide*.

You can also use this operation to delete a team draft. For more information, see [Interacting with drafts](https://docs.aws.amazon.com/mpa/latest/userguide/update-team.html#update-team-draft-status) in the *Multi-party approval User Guide*.

## Request Syntax
<a name="API_DeleteInactiveApprovalTeamVersion_RequestSyntax"></a>

```
DELETE /approval-teams/{{Arn}}/{{VersionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteInactiveApprovalTeamVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Arn](#API_DeleteInactiveApprovalTeamVersion_RequestSyntax) **   <a name="mpa-DeleteInactiveApprovalTeamVersion-request-uri-Arn"></a>
Amaazon Resource Name (ARN) for the team.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:approval-team/[a-zA-Z0-9._-]+`
Required: Yes

 ** [VersionId](#API_DeleteInactiveApprovalTeamVersion_RequestSyntax) **   <a name="mpa-DeleteInactiveApprovalTeamVersion-request-uri-VersionId"></a>
Version ID for the team.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_DeleteInactiveApprovalTeamVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteInactiveApprovalTeamVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteInactiveApprovalTeamVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteInactiveApprovalTeamVersion_Errors"></a>

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
<a name="API_DeleteInactiveApprovalTeamVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/DeleteInactiveApprovalTeamVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/DeleteInactiveApprovalTeamVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/DeleteInactiveApprovalTeamVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/DeleteInactiveApprovalTeamVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/DeleteInactiveApprovalTeamVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/DeleteInactiveApprovalTeamVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/DeleteInactiveApprovalTeamVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/DeleteInactiveApprovalTeamVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/DeleteInactiveApprovalTeamVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/DeleteInactiveApprovalTeamVersion)
