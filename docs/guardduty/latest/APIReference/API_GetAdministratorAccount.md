---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetAdministratorAccount.html
---

# GetAdministratorAccount
<a name="API_GetAdministratorAccount"></a>

Provides the details of the GuardDuty administrator account associated with the current GuardDuty member account.

Based on the type of account that runs this API, the following list shows how the API behavior varies:
+ When the GuardDuty administrator account runs this API, it will return success (`HTTP 200`) but no content.
+ When a member account runs this API, it will return the details of the GuardDuty administrator account that is associated with this calling member account.
+ When an individual account (not associated with an organization) runs this API, it will return success (`HTTP 200`) but no content.

## Request Syntax
<a name="API_GetAdministratorAccount_RequestSyntax"></a>

```
GET /detector/{{DetectorId}}/administrator HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAdministratorAccount_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_GetAdministratorAccount_RequestSyntax) **   <a name="guardduty-GetAdministratorAccount-request-uri-DetectorId"></a>
The unique ID of the detector of the GuardDuty member account.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_GetAdministratorAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAdministratorAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "administrator": {
      "accountId": "string",
      "invitationId": "string",
      "invitedAt": "string",
      "relationshipStatus": "string"
   }
}
```

## Response Elements
<a name="API_GetAdministratorAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [administrator](#API_GetAdministratorAccount_ResponseSyntax) **   <a name="guardduty-GetAdministratorAccount-response-administrator"></a>
The administrator account details.
Type: [Administrator](API_Administrator.md) object

## Errors
<a name="API_GetAdministratorAccount_Errors"></a>

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
<a name="API_GetAdministratorAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetAdministratorAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetAdministratorAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetAdministratorAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetAdministratorAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetAdministratorAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetAdministratorAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetAdministratorAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetAdministratorAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetAdministratorAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetAdministratorAccount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
