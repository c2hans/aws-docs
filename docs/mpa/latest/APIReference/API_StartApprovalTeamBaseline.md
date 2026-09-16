---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_StartApprovalTeamBaseline.html
---

# StartApprovalTeamBaseline
<a name="API_StartApprovalTeamBaseline"></a>

Starts a baseline session for specified approvers on an `ACTIVE` approval team.

## Request Syntax
<a name="API_StartApprovalTeamBaseline_RequestSyntax"></a>

```
POST /approval-teams/{{Arn}}/baseline HTTP/1.1
Content-type: application/json

{
   "ApproverIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_StartApprovalTeamBaseline_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Arn](#API_StartApprovalTeamBaseline_RequestSyntax) **   <a name="mpa-StartApprovalTeamBaseline-request-uri-Arn"></a>
Amazon Resource Name (ARN) for the approval team.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:approval-team/[a-zA-Z0-9._-]+`
Required: Yes

## Request Body
<a name="API_StartApprovalTeamBaseline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApproverIds](#API_StartApprovalTeamBaseline_RequestSyntax) **   <a name="mpa-StartApprovalTeamBaseline-request-ApproverIds"></a>
Array of approver IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Syntax
<a name="API_StartApprovalTeamBaseline_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BaselineSessionArn": "string"
}
```

## Response Elements
<a name="API_StartApprovalTeamBaseline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BaselineSessionArn](#API_StartApprovalTeamBaseline_ResponseSyntax) **   <a name="mpa-StartApprovalTeamBaseline-response-BaselineSessionArn"></a>
Amazon Resource Name (ARN) for the session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:session/[a-zA-Z0-9._-]+/[a-zA-Z0-9_-]+`

## Errors
<a name="API_StartApprovalTeamBaseline_Errors"></a>

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
<a name="API_StartApprovalTeamBaseline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/StartApprovalTeamBaseline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/StartApprovalTeamBaseline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/StartApprovalTeamBaseline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/StartApprovalTeamBaseline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/StartApprovalTeamBaseline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/StartApprovalTeamBaseline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/StartApprovalTeamBaseline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/StartApprovalTeamBaseline)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/StartApprovalTeamBaseline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/StartApprovalTeamBaseline)
