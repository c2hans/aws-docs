---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html
---

# InviteMembers
<a name="API_InviteMembers"></a>

Invites AWS accounts to become members of an organization administered by the AWS account that invokes this API. If you are using AWS Organizations to manage your GuardDuty environment, this step is not needed. For more information, see [Managing accounts with organizations](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html).

To invite AWS accounts, the first step is to ensure that GuardDuty has been enabled in the potential member accounts. You can now invoke this API to add accounts by invitation. The invited accounts can either accept or decline the invitation from their GuardDuty accounts. Each invited AWS account can choose to accept the invitation from only one AWS account. For more information, see [Managing GuardDuty accounts by invitation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_invitations.html).

After the invite has been accepted and you choose to disassociate a member account (by using [DisassociateMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DisassociateMembers.html)) from your account, the details of the member account obtained by invoking [CreateMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html), including the associated email addresses, will be retained. This is done so that you can invoke InviteMembers without the need to invoke [CreateMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html) again. To remove the details associated with a member account, you must also invoke [DeleteMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html).

If you disassociate a member account that was added by invitation, the member account details obtained from this API, including the associated email addresses, will be retained. This is done so that the delegated administrator can invoke the [InviteMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html) API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the [DeleteMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html) API.

When the member accounts added through AWS Organizations are later disassociated, you (administrator) can't invite them by calling the InviteMembers API. You can create an association with these member accounts again only by calling the CreateMembers API.

## Request Syntax
<a name="API_InviteMembers_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/member/invite HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ],
   "disableEmailNotification": {{boolean}},
   "message": "{{string}}"
}
```

## URI Request Parameters
<a name="API_InviteMembers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_InviteMembers_RequestSyntax) **   <a name="guardduty-InviteMembers-request-uri-DetectorId"></a>
The unique ID of the detector of the GuardDuty account with which you want to invite members.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_InviteMembers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_InviteMembers_RequestSyntax) **   <a name="guardduty-InviteMembers-request-accountIds"></a>
A list of account IDs of the accounts that you want to invite to GuardDuty as members.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Fixed length of 12.
Required: Yes

 ** [disableEmailNotification](#API_InviteMembers_RequestSyntax) **   <a name="guardduty-InviteMembers-request-disableEmailNotification"></a>
A Boolean value that specifies whether you want to disable email notification to the accounts that you are inviting to GuardDuty as members.
Type: Boolean
Required: No

 ** [message](#API_InviteMembers_RequestSyntax) **   <a name="guardduty-InviteMembers-request-message"></a>
The invitation message that you want to send to the accounts that you're inviting to GuardDuty as members.
Type: String
Required: No

## Response Syntax
<a name="API_InviteMembers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "unprocessedAccounts": [
      {
         "accountId": "string",
         "result": "string"
      }
   ]
}
```

## Response Elements
<a name="API_InviteMembers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [unprocessedAccounts](#API_InviteMembers_ResponseSyntax) **   <a name="guardduty-InviteMembers-response-unprocessedAccounts"></a>
A list of objects that contain the unprocessed account and a result string that explains why it was unprocessed.
Type: Array of [UnprocessedAccount](API_UnprocessedAccount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_InviteMembers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_InviteMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/InviteMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/InviteMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InviteMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/InviteMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InviteMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/InviteMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/InviteMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/InviteMembers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/InviteMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InviteMembers)
