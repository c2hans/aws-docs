---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html
---

# DeleteMembers
<a name="API_DeleteMembers"></a>

Deletes GuardDuty member accounts (to the current GuardDuty administrator account) specified by the account IDs.

With `autoEnableOrganizationMembers` configuration for your organization set to `ALL`, you'll receive an error if you attempt to disable GuardDuty for a member account in your organization.

## Request Syntax
<a name="API_DeleteMembers_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/member/delete HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DeleteMembers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_DeleteMembers_RequestSyntax) **   <a name="guardduty-DeleteMembers-request-uri-DetectorId"></a>
The unique ID of the detector of the GuardDuty account whose members you want to delete.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_DeleteMembers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_DeleteMembers_RequestSyntax) **   <a name="guardduty-DeleteMembers-request-accountIds"></a>
A list of account IDs of the GuardDuty member accounts that you want to delete.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Fixed length of 12.
Required: Yes

## Response Syntax
<a name="API_DeleteMembers_ResponseSyntax"></a>

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
<a name="API_DeleteMembers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [unprocessedAccounts](#API_DeleteMembers_ResponseSyntax) **   <a name="guardduty-DeleteMembers-response-unprocessedAccounts"></a>
The accounts that could not be processed.
Type: Array of [UnprocessedAccount](API_UnprocessedAccount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_DeleteMembers_Errors"></a>

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
<a name="API_DeleteMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/DeleteMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/DeleteMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DeleteMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/DeleteMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DeleteMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/DeleteMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/DeleteMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/DeleteMembers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/DeleteMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DeleteMembers)
