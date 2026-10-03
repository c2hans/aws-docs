---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_ValidateNotifyCodeVerification.html
---

# ValidateNotifyCodeVerification
<a name="API_ValidateNotifyCodeVerification"></a>

Validates a one-time passcode that a recipient submitted. Validation succeeds when the passcode matches, the validity period has not elapsed, and the maximum number of attempts has not been exceeded.

## Request Syntax
<a name="API_ValidateNotifyCodeVerification_RequestSyntax"></a>

```
POST /v1/notify-code-verifications/validate HTTP/1.1
Content-type: application/json

{
   "code": "{{string}}",
   "destinationIdentity": "{{string}}",
   "referenceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ValidateNotifyCodeVerification_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ValidateNotifyCodeVerification_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [code](#API_ValidateNotifyCodeVerification_RequestSyntax) **   <a name="endusermessaging-ValidateNotifyCodeVerification-request-code"></a>
The one-time passcode that the recipient submitted for validation.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 8.
Pattern: `[A-Za-z0-9]+`
Required: Yes

 ** [destinationIdentity](#API_ValidateNotifyCodeVerification_RequestSyntax) **   <a name="endusermessaging-ValidateNotifyCodeVerification-request-destinationIdentity"></a>
The recipient identifier. For the TEXT and VOICE channels, specify an E.164 phone number. For the WhatsApp channel, specify a WhatsApp address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[\x21-\x22\x24-\x7E]+`
Required: Yes

 ** [referenceId](#API_ValidateNotifyCodeVerification_RequestSyntax) **   <a name="endusermessaging-ValidateNotifyCodeVerification-request-referenceId"></a>
The caller-supplied reference identifier used to locate the verification. This value must match the value that you supplied to the SendNotifyCodeVerification operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_-]+`
Required: No

## Response Syntax
<a name="API_ValidateNotifyCodeVerification_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_ValidateNotifyCodeVerification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_ValidateNotifyCodeVerification_ResponseSyntax) **   <a name="endusermessaging-ValidateNotifyCodeVerification-response-status"></a>
The outcome of the validation attempt. VALID indicates that the submitted passcode matched an active verification. INVALID indicates that the passcode did not match, expired, or exceeded its attempt limit.
Type: String
Valid Values: `VALID | INVALID`

## Errors
<a name="API_ValidateNotifyCodeVerification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because it exceeded the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_ValidateNotifyCodeVerification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/ValidateNotifyCodeVerification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/ValidateNotifyCodeVerification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/ValidateNotifyCodeVerification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/ValidateNotifyCodeVerification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/ValidateNotifyCodeVerification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/ValidateNotifyCodeVerification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/ValidateNotifyCodeVerification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/ValidateNotifyCodeVerification)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/ValidateNotifyCodeVerification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/ValidateNotifyCodeVerification)
