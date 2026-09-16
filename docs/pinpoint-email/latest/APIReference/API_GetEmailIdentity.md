---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetEmailIdentity.html
---

# GetEmailIdentity
<a name="API_GetEmailIdentity"></a>

Provides information about a specific identity associated with your Amazon Pinpoint account, including the identity's verification status, its DKIM authentication status, and its custom Mail-From settings.

## Request Syntax
<a name="API_GetEmailIdentity_RequestSyntax"></a>

```
GET /v1/email/identities/{{EmailIdentity}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEmailIdentity_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailIdentity](#API_GetEmailIdentity_RequestSyntax) **   <a name="pinpoint-GetEmailIdentity-request-uri-EmailIdentity"></a>
The email identity that you want to retrieve details for.
Required: Yes

## Request Body
<a name="API_GetEmailIdentity_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEmailIdentity_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DkimAttributes": {
      "SigningEnabled": boolean,
      "Status": "string",
      "Tokens": [ "string" ]
   },
   "FeedbackForwardingStatus": boolean,
   "IdentityType": "string",
   "MailFromAttributes": {
      "BehaviorOnMxFailure": "string",
      "MailFromDomain": "string",
      "MailFromDomainStatus": "string"
   },
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ],
   "VerifiedForSendingStatus": boolean
}
```

## Response Elements
<a name="API_GetEmailIdentity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DkimAttributes](#API_GetEmailIdentity_ResponseSyntax) **   <a name="pinpoint-GetEmailIdentity-response-DkimAttributes"></a>
An object that contains information about the DKIM attributes for the identity. This object includes the tokens that you use to create the CNAME records that are required to complete the DKIM verification process.
Type: [DkimAttributes](API_DkimAttributes.md) object

 ** [FeedbackForwardingStatus](#API_GetEmailIdentity_ResponseSyntax) **   <a name="pinpoint-GetEmailIdentity-response-FeedbackForwardingStatus"></a>
The feedback forwarding configuration for the identity.
If the value is `true`, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.
When you set this value to `false`, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic or another event destination. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).
Type: Boolean

 ** [IdentityType](#API_GetEmailIdentity_ResponseSyntax) **   <a name="pinpoint-GetEmailIdentity-response-IdentityType"></a>
The email identity type.
Type: String
Valid Values: `EMAIL_ADDRESS | DOMAIN | MANAGED_DOMAIN`

 ** [MailFromAttributes](#API_GetEmailIdentity_ResponseSyntax) **   <a name="pinpoint-GetEmailIdentity-response-MailFromAttributes"></a>
An object that contains information about the Mail-From attributes for the email identity.
Type: [MailFromAttributes](API_MailFromAttributes.md) object

 ** [Tags](#API_GetEmailIdentity_ResponseSyntax) **   <a name="pinpoint-GetEmailIdentity-response-Tags"></a>
An array of objects that define the tags (keys and values) that are associated with the email identity.
Type: Array of [Tag](API_Tag.md) objects

 ** [VerifiedForSendingStatus](#API_GetEmailIdentity_ResponseSyntax) **   <a name="pinpoint-GetEmailIdentity-response-VerifiedForSendingStatus"></a>
Specifies whether or not the identity is verified. In Amazon Pinpoint, you can only send email from verified email addresses or domains. For more information about verifying identities, see the [Amazon Pinpoint User Guide](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html).
Type: Boolean

## Errors
<a name="API_GetEmailIdentity_Errors"></a>

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
<a name="API_GetEmailIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/GetEmailIdentity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/GetEmailIdentity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/GetEmailIdentity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/GetEmailIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/GetEmailIdentity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/GetEmailIdentity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/GetEmailIdentity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/GetEmailIdentity)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/GetEmailIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/GetEmailIdentity)
