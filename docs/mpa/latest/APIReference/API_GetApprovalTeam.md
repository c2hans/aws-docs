---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetApprovalTeam.html
---

# GetApprovalTeam
<a name="API_GetApprovalTeam"></a>

Returns details for an approval team.

## Request Syntax
<a name="API_GetApprovalTeam_RequestSyntax"></a>

```
GET /approval-teams/{{Arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApprovalTeam_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Arn](#API_GetApprovalTeam_RequestSyntax) **   <a name="mpa-GetApprovalTeam-request-uri-Arn"></a>
Amazon Resource Name (ARN) for the team.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:approval-team/[a-zA-Z0-9._-]+`
Required: Yes

## Request Body
<a name="API_GetApprovalTeam_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetApprovalTeam_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApprovalStrategy": { ... },
   "Approvers": [
      {
         "ApproverId": "string",
         "LastActivity": "string",
         "LastActivityTime": "string",
         "MfaMethods": [
            {
               "SyncStatus": "string",
               "Type": "string"
            }
         ],
         "PendingBaselineSessionArn": "string",
         "PrimaryIdentityId": "string",
         "PrimaryIdentitySourceArn": "string",
         "PrimaryIdentityStatus": "string",
         "ResponseTime": "string"
      }
   ],
   "Arn": "string",
   "CreationTime": "string",
   "Description": "string",
   "LastUpdateTime": "string",
   "Name": "string",
   "NumberOfApprovers": number,
   "PendingUpdate": {
      "ApprovalStrategy": { ... },
      "Approvers": [
         {
            "ApproverId": "string",
            "LastActivity": "string",
            "LastActivityTime": "string",
            "MfaMethods": [
               {
                  "SyncStatus": "string",
                  "Type": "string"
               }
            ],
            "PendingBaselineSessionArn": "string",
            "PrimaryIdentityId": "string",
            "PrimaryIdentitySourceArn": "string",
            "PrimaryIdentityStatus": "string",
            "ResponseTime": "string"
         }
      ],
      "Description": "string",
      "NumberOfApprovers": number,
      "Status": "string",
      "StatusCode": "string",
      "StatusMessage": "string",
      "UpdateInitiationTime": "string",
      "VersionId": "string"
   },
   "Policies": [
      {
         "PolicyArn": "string"
      }
   ],
   "Status": "string",
   "StatusCode": "string",
   "StatusMessage": "string",
   "UpdateSessionArn": "string",
   "VersionId": "string"
}
```

## Response Elements
<a name="API_GetApprovalTeam_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApprovalStrategy](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-ApprovalStrategy"></a>
An `ApprovalStrategyResponse` object. Contains details for how the team grants approval.
Type: [ApprovalStrategyResponse](API_ApprovalStrategyResponse.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [Approvers](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-Approvers"></a>
An array of `GetApprovalTeamResponseApprover ` objects. Contains details for the approvers in the team.
Type: Array of [GetApprovalTeamResponseApprover](API_GetApprovalTeamResponseApprover.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [Arn](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-Arn"></a>
Amazon Resource Name (ARN) for the team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [CreationTime](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-CreationTime"></a>
Timestamp when the team was created.
Type: Timestamp

 ** [Description](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-Description"></a>
Description for the team.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [LastUpdateTime](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-LastUpdateTime"></a>
Timestamp when the team was last updated.
Type: Timestamp

 ** [Name](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-Name"></a>
Name of the approval team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [NumberOfApprovers](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-NumberOfApprovers"></a>
Total number of approvers in the team.
Type: Integer

 ** [PendingUpdate](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-PendingUpdate"></a>
A `PendingUpdate` object. Contains details for the pending updates for the team, if applicable.
Type: [PendingUpdate](API_PendingUpdate.md) object

 ** [Policies](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-Policies"></a>
An array of `PolicyReference` objects. Contains a list of policies that define the permissions for team resources.
Type: Array of [PolicyReference](API_PolicyReference.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [Status](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-Status"></a>
Status for the team. For more information, see [Team health](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html) in the *Multi-party approval User Guide*.
Type: String
Valid Values: `ACTIVE | INACTIVE | DELETING | PENDING`

 ** [StatusCode](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-StatusCode"></a>
Status code for the approval team. For more information, see [Team health](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html) in the *Multi-party approval User Guide*.
Type: String
Valid Values: `VALIDATING | PENDING_ACTIVATION | FAILED_VALIDATION | FAILED_ACTIVATION | UPDATE_PENDING_APPROVAL | UPDATE_PENDING_ACTIVATION | UPDATE_FAILED_APPROVAL | UPDATE_FAILED_ACTIVATION | UPDATE_FAILED_VALIDATION | DELETE_PENDING_APPROVAL | DELETE_FAILED_APPROVAL | DELETE_FAILED_VALIDATION`

 ** [StatusMessage](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-StatusMessage"></a>
Message describing the status for the team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [UpdateSessionArn](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-UpdateSessionArn"></a>
Amazon Resource Name (ARN) for the session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [VersionId](#API_GetApprovalTeam_ResponseSyntax) **   <a name="mpa-GetApprovalTeam-response-VersionId"></a>
Version ID for the team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Errors
<a name="API_GetApprovalTeam_Errors"></a>

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
<a name="API_GetApprovalTeam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/GetApprovalTeam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/GetApprovalTeam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/GetApprovalTeam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/GetApprovalTeam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/GetApprovalTeam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/GetApprovalTeam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/GetApprovalTeam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/GetApprovalTeam)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/GetApprovalTeam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/GetApprovalTeam)
