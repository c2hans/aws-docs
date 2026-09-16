---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_AssociateEmailIdentityCertificate.html
---

# AssociateEmailIdentityCertificate
<a name="API_AssociateEmailIdentityCertificate"></a>

Associates an S/MIME certificate with an email identity. After the certificate is active, Amazon SES API v2 can add an S/MIME signature to messages that you send from the associated address when signing is enabled on the configuration set used to send the message.

The certificate is an X.509 certificate that you manage in AWS Certificate Manager (ACM). You identify it by its Amazon Resource Name (ARN).
+ If the email identity is a domain, you must specify a `FromAddress` that belongs to that domain or one of its subdomains. The certificate applies to messages sent from that address.
+ If the email identity is an email address, `FromAddress` is optional. If you specify it, it must exactly match the email identity.

When the association is created, the certificate begins provisioning and its status is `PROVISIONING`. The status changes to `ACTIVE` when the certificate is ready to use for signing. Each email address can have only one certificate association. If an association already exists for the address, this operation returns an error, unless the existing association is in the `DEPROVISIONING` state.

## Request Syntax
<a name="API_AssociateEmailIdentityCertificate_RequestSyntax"></a>

```
POST /v2/email/identity/certificates HTTP/1.1
Content-type: application/json

{
   "CertificateArn": "{{string}}",
   "EmailIdentity": "{{string}}",
   "FromAddress": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateEmailIdentityCertificate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AssociateEmailIdentityCertificate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CertificateArn](#API_AssociateEmailIdentityCertificate_RequestSyntax) **   <a name="SES-AssociateEmailIdentityCertificate-request-CertificateArn"></a>
The Amazon Resource Name (ARN) of the AWS Certificate Manager (ACM) certificate to associate with the email identity.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:[\w+=/,.@-]*:[0-9]+:certificate/[\w+=,.@-]+`
Required: Yes

 ** [EmailIdentity](#API_AssociateEmailIdentityCertificate_RequestSyntax) **   <a name="SES-AssociateEmailIdentityCertificate-request-EmailIdentity"></a>
The email identity, either an email address or a domain, to associate the certificate with.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [FromAddress](#API_AssociateEmailIdentityCertificate_RequestSyntax) **   <a name="SES-AssociateEmailIdentityCertificate-request-FromAddress"></a>
The email address that the certificate applies to. This value is required when the email identity is a domain, and the address must belong to that domain or one of its subdomains. When the email identity is an email address, this value is optional. If you specify it, it must exactly match the email identity.
Type: String
Required: No

## Response Syntax
<a name="API_AssociateEmailIdentityCertificate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AssociateEmailIdentityCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateEmailIdentityCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
The resource specified in your request already exists.
HTTP Status Code: 400

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
<a name="API_AssociateEmailIdentityCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/AssociateEmailIdentityCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/AssociateEmailIdentityCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/AssociateEmailIdentityCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/AssociateEmailIdentityCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/AssociateEmailIdentityCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/AssociateEmailIdentityCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/AssociateEmailIdentityCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/AssociateEmailIdentityCertificate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/AssociateEmailIdentityCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/AssociateEmailIdentityCertificate)
