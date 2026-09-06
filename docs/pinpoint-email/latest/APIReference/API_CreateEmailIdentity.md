---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateEmailIdentity.html
---

# CreateEmailIdentity
<a name="API_CreateEmailIdentity"></a>

Verifies an email identity for use with Amazon Pinpoint. In Amazon Pinpoint, an identity is an email address or domain that you use when you send email. Before you can use an identity to send email with Amazon Pinpoint, you first have to verify it. By verifying an address, you demonstrate that you're the owner of the address, and that you've given Amazon Pinpoint permission to send email from the address.

When you verify an email address, Amazon Pinpoint sends an email to the address. Your email address is verified as soon as you follow the link in the verification email.

When you verify a domain, this operation provides a set of DKIM tokens, which you can convert into CNAME tokens. You add these CNAME tokens to the DNS configuration for your domain. Your domain is verified when Amazon Pinpoint detects these records in the DNS configuration for your domain. It usually takes around 72 hours to complete the domain verification process.

## Request Syntax
<a name="API_CreateEmailIdentity_RequestSyntax"></a>

```
POST /v1/email/identities HTTP/1.1
Content-type: application/json

{
   "EmailIdentity": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateEmailIdentity_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEmailIdentity_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EmailIdentity](#API_CreateEmailIdentity_RequestSyntax) **   <a name="pinpoint-CreateEmailIdentity-request-EmailIdentity"></a>
The email address or domain that you want to verify.
Type: String
Required: Yes

 ** [Tags](#API_CreateEmailIdentity_RequestSyntax) **   <a name="pinpoint-CreateEmailIdentity-request-Tags"></a>
An array of objects that define the tags (keys and values) that you want to associate with the email identity.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateEmailIdentity_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DkimAttributes": {
      "SigningEnabled": boolean,
      "Status": "string",
      "Tokens": [ "string" ]
   },
   "IdentityType": "string",
   "VerifiedForSendingStatus": boolean
}
```

## Response Elements
<a name="API_CreateEmailIdentity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DkimAttributes](#API_CreateEmailIdentity_ResponseSyntax) **   <a name="pinpoint-CreateEmailIdentity-response-DkimAttributes"></a>
An object that contains information about the DKIM attributes for the identity. This object includes the tokens that you use to create the CNAME records that are required to complete the DKIM verification process.
Type: [DkimAttributes](API_DkimAttributes.md) object

 ** [IdentityType](#API_CreateEmailIdentity_ResponseSyntax) **   <a name="pinpoint-CreateEmailIdentity-response-IdentityType"></a>
The email identity type.
Type: String
Valid Values: `EMAIL_ADDRESS | DOMAIN | MANAGED_DOMAIN`

 ** [VerifiedForSendingStatus](#API_CreateEmailIdentity_ResponseSyntax) **   <a name="pinpoint-CreateEmailIdentity-response-VerifiedForSendingStatus"></a>
Specifies whether or not the identity is verified. In Amazon Pinpoint, you can only send email from verified email addresses or domains. For more information about verifying identities, see the [Amazon Pinpoint User Guide](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html).
Type: Boolean

## Errors
<a name="API_CreateEmailIdentity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** ConcurrentModificationException **
The resource is being modified by another operation or thread.
HTTP Status Code: 500

 ** LimitExceededException **
There are too many instances of the specified resource type.
HTTP Status Code: 400

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_CreateEmailIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/CreateEmailIdentity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/CreateEmailIdentity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/CreateEmailIdentity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/CreateEmailIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/CreateEmailIdentity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/CreateEmailIdentity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/CreateEmailIdentity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/CreateEmailIdentity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/CreateEmailIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/CreateEmailIdentity)
