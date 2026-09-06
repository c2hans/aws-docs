---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AcceptAdministratorInvitation.html
---

# AcceptAdministratorInvitation
<a name="API_AcceptAdministratorInvitation"></a>

Accepts the invitation to be a member account and get monitored by a GuardDuty administrator account that sent the invitation.

## Request Syntax
<a name="API_AcceptAdministratorInvitation_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/administrator HTTP/1.1
Content-type: application/json

{
   "administratorId": "{{string}}",
   "invitationId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AcceptAdministratorInvitation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_AcceptAdministratorInvitation_RequestSyntax) **   <a name="guardduty-AcceptAdministratorInvitation-request-uri-DetectorId"></a>
The unique ID of the detector of the GuardDuty member account.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_AcceptAdministratorInvitation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [administratorId](#API_AcceptAdministratorInvitation_RequestSyntax) **   <a name="guardduty-AcceptAdministratorInvitation-request-administratorId"></a>
The account ID of the GuardDuty administrator account whose invitation you're accepting.
Type: String
Required: Yes

 ** [invitationId](#API_AcceptAdministratorInvitation_RequestSyntax) **   <a name="guardduty-AcceptAdministratorInvitation-request-invitationId"></a>
The value that is used to validate the administrator account to the member account.
Type: String
Required: Yes

## Response Syntax
<a name="API_AcceptAdministratorInvitation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AcceptAdministratorInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AcceptAdministratorInvitation_Errors"></a>

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
<a name="API_AcceptAdministratorInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/AcceptAdministratorInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/AcceptAdministratorInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AcceptAdministratorInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/AcceptAdministratorInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AcceptAdministratorInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/AcceptAdministratorInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/AcceptAdministratorInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/AcceptAdministratorInvitation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/AcceptAdministratorInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AcceptAdministratorInvitation)
