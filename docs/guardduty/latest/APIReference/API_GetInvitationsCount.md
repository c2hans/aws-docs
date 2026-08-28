---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetInvitationsCount.html
---

# GetInvitationsCount
<a name="API_GetInvitationsCount"></a>

Returns the count of all GuardDuty membership invitations that were sent to the current member account except the currently accepted invitation.

## Request Syntax
<a name="API_GetInvitationsCount_RequestSyntax"></a>

```
GET /invitation/count HTTP/1.1
```

## URI Request Parameters
<a name="API_GetInvitationsCount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetInvitationsCount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetInvitationsCount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "invitationsCount": number
}
```

## Response Elements
<a name="API_GetInvitationsCount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [invitationsCount](#API_GetInvitationsCount_ResponseSyntax) **   <a name="guardduty-GetInvitationsCount-response-invitationsCount"></a>
The number of received invitations.
Type: Integer

## Errors
<a name="API_GetInvitationsCount_Errors"></a>

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
<a name="API_GetInvitationsCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetInvitationsCount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetInvitationsCount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetInvitationsCount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetInvitationsCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetInvitationsCount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetInvitationsCount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetInvitationsCount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetInvitationsCount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetInvitationsCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetInvitationsCount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
