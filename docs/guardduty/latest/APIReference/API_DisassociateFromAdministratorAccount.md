---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DisassociateFromAdministratorAccount.html
---

# DisassociateFromAdministratorAccount
<a name="API_DisassociateFromAdministratorAccount"></a>

Disassociates the current GuardDuty member account from its administrator account.

When you disassociate an invited member from a GuardDuty delegated administrator, the member account details obtained from the [CreateMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html) API, including the associated email addresses, are retained. This is done so that the delegated administrator can invoke the [InviteMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html) API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the [DeleteMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html) API.

With `autoEnableOrganizationMembers` configuration for your organization set to `ALL`, you'll receive an error if you attempt to disable GuardDuty in a member account.

## Request Syntax
<a name="API_DisassociateFromAdministratorAccount_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/administrator/disassociate HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateFromAdministratorAccount_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_DisassociateFromAdministratorAccount_RequestSyntax) **   <a name="guardduty-DisassociateFromAdministratorAccount-request-uri-DetectorId"></a>
The unique ID of the detector of the GuardDuty member account.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_DisassociateFromAdministratorAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateFromAdministratorAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateFromAdministratorAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateFromAdministratorAccount_Errors"></a>

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
<a name="API_DisassociateFromAdministratorAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/DisassociateFromAdministratorAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/DisassociateFromAdministratorAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DisassociateFromAdministratorAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/DisassociateFromAdministratorAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DisassociateFromAdministratorAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/DisassociateFromAdministratorAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/DisassociateFromAdministratorAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/DisassociateFromAdministratorAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/DisassociateFromAdministratorAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DisassociateFromAdministratorAccount)
