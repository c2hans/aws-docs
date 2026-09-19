---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_PutWhatsAppBusinessPublicKey.html
---

# PutWhatsAppBusinessPublicKey
<a name="API_PutWhatsAppBusinessPublicKey"></a>

Sets the business public key used to encrypt the data exchanged with the endpoint of a data exchange Flow.

## Request Syntax
<a name="API_PutWhatsAppBusinessPublicKey_RequestSyntax"></a>

```
PUT /v1/whatsapp/business-public-key HTTP/1.1
Content-type: application/json

{
   "businessPublicKey": "{{string}}",
   "kmsKeyArn": "{{string}}",
   "originationPhoneNumberId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutWhatsAppBusinessPublicKey_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutWhatsAppBusinessPublicKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [businessPublicKey](#API_PutWhatsAppBusinessPublicKey_RequestSyntax) **   <a name="Social-PutWhatsAppBusinessPublicKey-request-businessPublicKey"></a>
The PEM-encoded 2048-bit RSA public key to set. Mutually exclusive with `kmsKeyArn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [kmsKeyArn](#API_PutWhatsAppBusinessPublicKey_RequestSyntax) **   <a name="Social-PutWhatsAppBusinessPublicKey-request-kmsKeyArn"></a>
The ARN of a customer managed asymmetric RSA key in AWS KMS. Mutually exclusive with `businessPublicKey`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z-]*:kms:[a-z0-9-]+:[0-9]{12}:(key/.+|alias/.+)`
Required: No

 ** [originationPhoneNumberId](#API_PutWhatsAppBusinessPublicKey_RequestSyntax) **   <a name="Social-PutWhatsAppBusinessPublicKey-request-originationPhoneNumberId"></a>
The unique identifier of the phone number to associate with the business public key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^phone-number-id-.*$)|(^arn:.*:phone-number-id/[0-9a-zA-Z]+$).*`
Required: Yes

## Response Syntax
<a name="API_PutWhatsAppBusinessPublicKey_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutWhatsAppBusinessPublicKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutWhatsAppBusinessPublicKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedByMetaException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** DependencyException **
Thrown when performing an action because a dependency would be broken.
HTTP Status Code: 502

 ** InternalServiceException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** InvalidParametersException **
One or more parameters provided to the action are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource was not found.
HTTP Status Code: 404

 ** ThrottledRequestException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request contains an invalid parameter value.
HTTP Status Code: 400

## See Also
<a name="API_PutWhatsAppBusinessPublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/PutWhatsAppBusinessPublicKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/PutWhatsAppBusinessPublicKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/PutWhatsAppBusinessPublicKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/PutWhatsAppBusinessPublicKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/PutWhatsAppBusinessPublicKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/PutWhatsAppBusinessPublicKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/PutWhatsAppBusinessPublicKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/PutWhatsAppBusinessPublicKey)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/PutWhatsAppBusinessPublicKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/PutWhatsAppBusinessPublicKey)
