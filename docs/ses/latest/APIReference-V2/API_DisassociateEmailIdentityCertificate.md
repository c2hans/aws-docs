---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DisassociateEmailIdentityCertificate.html
---

# DisassociateEmailIdentityCertificate
<a name="API_DisassociateEmailIdentityCertificate"></a>

Removes the association between an S/MIME certificate and an email identity. After the association is removed, Amazon SES API v2 stops adding an S/MIME signature to messages sent from that address.

If the email identity is a domain, specify the `FromAddress` whose certificate association you want to remove.

This operation is idempotent. If the specified email identity exists but there's no matching certificate association, the operation succeeds without making any changes. Amazon SES API v2 returns a `NotFoundException` only when the specified email identity doesn't exist.

## Request Syntax
<a name="API_DisassociateEmailIdentityCertificate_RequestSyntax"></a>

```
POST /v2/email/identity/certificates/delete HTTP/1.1
Content-type: application/json

{
   "EmailIdentity": "{{string}}",
   "FromAddress": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DisassociateEmailIdentityCertificate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DisassociateEmailIdentityCertificate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EmailIdentity](#API_DisassociateEmailIdentityCertificate_RequestSyntax) **   <a name="SES-DisassociateEmailIdentityCertificate-request-EmailIdentity"></a>
The email identity whose certificate association you want to remove.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [FromAddress](#API_DisassociateEmailIdentityCertificate_RequestSyntax) **   <a name="SES-DisassociateEmailIdentityCertificate-request-FromAddress"></a>
The email address whose certificate association you want to remove. This value is required when the email identity is a domain. When the email identity is an email address, this value is optional.
Type: String
Required: No

## Response Syntax
<a name="API_DisassociateEmailIdentityCertificate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateEmailIdentityCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateEmailIdentityCertificate_Errors"></a>

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
<a name="API_DisassociateEmailIdentityCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/DisassociateEmailIdentityCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/DisassociateEmailIdentityCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DisassociateEmailIdentityCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/DisassociateEmailIdentityCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DisassociateEmailIdentityCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/DisassociateEmailIdentityCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/DisassociateEmailIdentityCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/DisassociateEmailIdentityCertificate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/DisassociateEmailIdentityCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DisassociateEmailIdentityCertificate)
