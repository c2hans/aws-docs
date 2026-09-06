---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutEmailIdentityFeedbackAttributes.html
---

# PutEmailIdentityFeedbackAttributes
<a name="API_PutEmailIdentityFeedbackAttributes"></a>

Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.

When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.

When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).

## Request Syntax
<a name="API_PutEmailIdentityFeedbackAttributes_RequestSyntax"></a>

```
PUT /v1/email/identities/{{EmailIdentity}}/feedback HTTP/1.1
Content-type: application/json

{
   "EmailForwardingEnabled": {{boolean}}
}
```

## URI Request Parameters
<a name="API_PutEmailIdentityFeedbackAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailIdentity](#API_PutEmailIdentityFeedbackAttributes_RequestSyntax) **   <a name="pinpoint-PutEmailIdentityFeedbackAttributes-request-uri-EmailIdentity"></a>
The email identity that you want to configure bounce and complaint feedback forwarding for.
Required: Yes

## Request Body
<a name="API_PutEmailIdentityFeedbackAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EmailForwardingEnabled](#API_PutEmailIdentityFeedbackAttributes_RequestSyntax) **   <a name="pinpoint-PutEmailIdentityFeedbackAttributes-request-EmailForwardingEnabled"></a>
Sets the feedback forwarding configuration for the identity.
If the value is `true`, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.
When you set this value to `false`, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic or another event destination. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).
Type: Boolean
Required: No

## Response Syntax
<a name="API_PutEmailIdentityFeedbackAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutEmailIdentityFeedbackAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutEmailIdentityFeedbackAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** NotFoundException **
The resource you attempted to access doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_PutEmailIdentityFeedbackAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/PutEmailIdentityFeedbackAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/PutEmailIdentityFeedbackAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/PutEmailIdentityFeedbackAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/PutEmailIdentityFeedbackAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/PutEmailIdentityFeedbackAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/PutEmailIdentityFeedbackAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/PutEmailIdentityFeedbackAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/PutEmailIdentityFeedbackAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/PutEmailIdentityFeedbackAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/PutEmailIdentityFeedbackAttributes)
