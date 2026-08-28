---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AcceptInvitation.html
---

# AcceptInvitation
<a name="API_AcceptInvitation"></a>

 *This action has been deprecated.*

Accepts the invitation to be monitored by a GuardDuty administrator account.

## Request Syntax
<a name="API_AcceptInvitation_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/master HTTP/1.1
Content-type: application/json

{
   "invitationId": "{{string}}",
   "masterId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AcceptInvitation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_AcceptInvitation_RequestSyntax) **   <a name="guardduty-AcceptInvitation-request-uri-DetectorId"></a>
The unique ID of the detector of the GuardDuty member account.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_AcceptInvitation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [invitationId](#API_AcceptInvitation_RequestSyntax) **   <a name="guardduty-AcceptInvitation-request-invitationId"></a>
The value that is used to validate the administrator account to the member account.
Type: String
Required: Yes

 ** [masterId](#API_AcceptInvitation_RequestSyntax) **   <a name="guardduty-AcceptInvitation-request-masterId"></a>
The account ID of the GuardDuty administrator account whose invitation you're accepting.
Type: String
Required: Yes

## Response Syntax
<a name="API_AcceptInvitation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AcceptInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AcceptInvitation_Errors"></a>

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
<a name="API_AcceptInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/AcceptInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/AcceptInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AcceptInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/AcceptInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AcceptInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/AcceptInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/AcceptInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/AcceptInvitation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/AcceptInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AcceptInvitation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
