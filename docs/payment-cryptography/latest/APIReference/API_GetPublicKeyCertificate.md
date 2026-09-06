---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetPublicKeyCertificate.html
---

# GetPublicKeyCertificate
<a name="API_GetPublicKeyCertificate"></a>

Gets the public key certificate of the asymmetric key pair that exists within AWS Payment Cryptography.

Unlike the private key of an asymmetric key, which never leaves AWS Payment Cryptography unencrypted, callers with `GetPublicKeyCertificate` permission can download the public key certificate of the asymmetric key. You can share the public key certificate to allow others to encrypt messages and verify signatures outside of AWS Payment Cryptography

 **Cross-account use:** This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

## Request Syntax
<a name="API_GetPublicKeyCertificate_RequestSyntax"></a>

```
{
   "KeyIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPublicKeyCertificate_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [KeyIdentifier](#API_GetPublicKeyCertificate_RequestSyntax) **   <a name="paymentcryptography-GetPublicKeyCertificate-request-KeyIdentifier"></a>
The `KeyARN` of the asymmetric key pair.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

## Response Syntax
<a name="API_GetPublicKeyCertificate_ResponseSyntax"></a>

```
{
   "KeyCertificate": "string",
   "KeyCertificateChain": "string"
}
```

## Response Elements
<a name="API_GetPublicKeyCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyCertificate](#API_GetPublicKeyCertificate_ResponseSyntax) **   <a name="paymentcryptography-GetPublicKeyCertificate-response-KeyCertificate"></a>
The public key component of the asymmetric key pair in a certificate PEM format (base64 encoded). It is signed by the root certificate authority (CA). The certificate is valid for 90 days from the time it is issued. The service returns a cached certificate if one exists with at least 30 days of remaining validity. Otherwise, a new 90-day certificate is issued.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`

 ** [KeyCertificateChain](#API_GetPublicKeyCertificate_ResponseSyntax) **   <a name="paymentcryptography-GetPublicKeyCertificate-response-KeyCertificateChain"></a>
The root certificate authority (CA) that signed the public key certificate in PEM format (base64 encoded) of the asymmetric key pair.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`

## Errors
<a name="API_GetPublicKeyCertificate_Errors"></a>

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific AWS Payment Cryptography action you're attempting.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
This indicates a server-side error within the AWS Payment Cryptography service. If this error persists, contact support for assistance.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was denied due to resource not found.
The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.
 ** ResourceId **
The identifier of the resource that was not found.
This field contains the specific resource identifier (such as a key ARN or alias name) that could not be located.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
The AWS Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
You have exceeded the rate limits for AWS Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.
HTTP Status Code: 400

 ** ValidationException **
The request was denied due to an invalid request error.
One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.
HTTP Status Code: 400

## See Also
<a name="API_GetPublicKeyCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-2021-09-14/GetPublicKeyCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-2021-09-14/GetPublicKeyCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/GetPublicKeyCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-2021-09-14/GetPublicKeyCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/GetPublicKeyCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-2021-09-14/GetPublicKeyCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-2021-09-14/GetPublicKeyCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-2021-09-14/GetPublicKeyCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-2021-09-14/GetPublicKeyCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/GetPublicKeyCertificate)
