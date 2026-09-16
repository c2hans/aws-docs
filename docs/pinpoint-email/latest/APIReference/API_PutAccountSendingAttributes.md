---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutAccountSendingAttributes.html
---

# PutAccountSendingAttributes
<a name="API_PutAccountSendingAttributes"></a>

Enable or disable the ability of your account to send email.

## Request Syntax
<a name="API_PutAccountSendingAttributes_RequestSyntax"></a>

```
PUT /v1/email/account/sending HTTP/1.1
Content-type: application/json

{
   "SendingEnabled": {{boolean}}
}
```

## URI Request Parameters
<a name="API_PutAccountSendingAttributes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutAccountSendingAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SendingEnabled](#API_PutAccountSendingAttributes_RequestSyntax) **   <a name="pinpoint-PutAccountSendingAttributes-request-SendingEnabled"></a>
Enables or disables your account's ability to send email. Set to `true` to enable email sending, or set to `false` to disable email sending.
If AWS paused your account's ability to send email, you can't use this operation to resume your account's ability to send email.
Type: Boolean
Required: No

## Response Syntax
<a name="API_PutAccountSendingAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutAccountSendingAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutAccountSendingAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_PutAccountSendingAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/PutAccountSendingAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/PutAccountSendingAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/PutAccountSendingAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/PutAccountSendingAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/PutAccountSendingAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/PutAccountSendingAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/PutAccountSendingAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/PutAccountSendingAttributes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/PutAccountSendingAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/PutAccountSendingAttributes)
