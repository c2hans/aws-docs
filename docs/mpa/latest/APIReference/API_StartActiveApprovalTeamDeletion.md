---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_StartActiveApprovalTeamDeletion.html
---

# StartActiveApprovalTeamDeletion
<a name="API_StartActiveApprovalTeamDeletion"></a>

Starts the deletion process for an active approval team.

**Note**
 **Deletions require team approval**
Requests to delete an active team must be approved by the team.

## Request Syntax
<a name="API_StartActiveApprovalTeamDeletion_RequestSyntax"></a>

```
POST /approval-teams/{Arn}?Delete HTTP/1.1
Content-type: application/json

{
   "PendingWindowDays": {{number}}
}
```

## URI Request Parameters
<a name="API_StartActiveApprovalTeamDeletion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Arn](#API_StartActiveApprovalTeamDeletion_RequestSyntax) **   <a name="mpa-StartActiveApprovalTeamDeletion-request-uri-Arn"></a>
Amazon Resource Name (ARN) for the team.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:approval-team/[a-zA-Z0-9._-]+`
Required: Yes

## Request Body
<a name="API_StartActiveApprovalTeamDeletion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PendingWindowDays](#API_StartActiveApprovalTeamDeletion_RequestSyntax) **   <a name="mpa-StartActiveApprovalTeamDeletion-request-PendingWindowDays"></a>
Number of days between when the team approves the delete request and when the team is deleted.
Type: Integer
Required: No

## Response Syntax
<a name="API_StartActiveApprovalTeamDeletion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DeletionCompletionTime": "string",
   "DeletionStartTime": "string"
}
```

## Response Elements
<a name="API_StartActiveApprovalTeamDeletion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeletionCompletionTime](#API_StartActiveApprovalTeamDeletion_ResponseSyntax) **   <a name="mpa-StartActiveApprovalTeamDeletion-response-DeletionCompletionTime"></a>
Timestamp when the deletion process is scheduled to complete.
Type: Timestamp

 ** [DeletionStartTime](#API_StartActiveApprovalTeamDeletion_ResponseSyntax) **   <a name="mpa-StartActiveApprovalTeamDeletion-response-DeletionStartTime"></a>
Timestamp when the deletion process was initiated.
Type: Timestamp

## Errors
<a name="API_StartActiveApprovalTeamDeletion_Errors"></a>

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
<a name="API_StartActiveApprovalTeamDeletion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/StartActiveApprovalTeamDeletion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/StartActiveApprovalTeamDeletion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/StartActiveApprovalTeamDeletion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/StartActiveApprovalTeamDeletion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/StartActiveApprovalTeamDeletion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/StartActiveApprovalTeamDeletion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/StartActiveApprovalTeamDeletion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/StartActiveApprovalTeamDeletion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/StartActiveApprovalTeamDeletion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/StartActiveApprovalTeamDeletion)
