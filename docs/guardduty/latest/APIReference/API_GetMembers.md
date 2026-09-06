---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMembers.html
---

# GetMembers
<a name="API_GetMembers"></a>

Retrieves GuardDuty member accounts (of the current GuardDuty administrator account) specified by the account IDs.

## Request Syntax
<a name="API_GetMembers_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/member/get HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_GetMembers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_GetMembers_RequestSyntax) **   <a name="guardduty-GetMembers-request-uri-DetectorId"></a>
The unique ID of the detector of the GuardDuty account whose members you want to retrieve.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_GetMembers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_GetMembers_RequestSyntax) **   <a name="guardduty-GetMembers-request-accountIds"></a>
A list of account IDs of the GuardDuty member accounts that you want to describe.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Fixed length of 12.
Required: Yes

## Response Syntax
<a name="API_GetMembers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "members": [
      {
         "accountId": "string",
         "administratorId": "string",
         "detectorId": "string",
         "email": "string",
         "invitedAt": "string",
         "masterId": "string",
         "relationshipStatus": "string",
         "updatedAt": "string"
      }
   ],
   "unprocessedAccounts": [
      {
         "accountId": "string",
         "result": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetMembers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [members](#API_GetMembers_ResponseSyntax) **   <a name="guardduty-GetMembers-response-members"></a>
A list of members.
Type: Array of [Member](API_Member.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [unprocessedAccounts](#API_GetMembers_ResponseSyntax) **   <a name="guardduty-GetMembers-response-unprocessedAccounts"></a>
A list of objects that contain the unprocessed account and a result string that explains why it was unprocessed.
Type: Array of [UnprocessedAccount](API_UnprocessedAccount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_GetMembers_Errors"></a>

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
<a name="API_GetMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetMembers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetMembers)
