---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html
---

# GetParametersForImport
<a name="API_GetParametersForImport"></a>

Gets the import token and the wrapping key certificate in PEM format (base64 encoded) to initiate a TR-34 WrappedKeyBlock or a RSA WrappedKeyCryptogram import into AWS Payment Cryptography.

The wrapping key certificate wraps the key under import. The import token and wrapping key certificate must be in place and operational before calling [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html). The import token expires in 30 days. You can use the same import token to import multiple keys into your service account.

To return a previously generated import token and wrapping key certificate instead of generating new ones, set `ReuseLastGeneratedToken` to `true`.

 **Cross-account use:** This operation can't be used across different AWS accounts.

 **Related operations:**
+  [GetParametersForExport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html)
+  [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html)

## Request Syntax
<a name="API_GetParametersForImport_RequestSyntax"></a>

```
{
   "KeyMaterialType": "{{string}}",
   "ReuseLastGeneratedToken": {{boolean}},
   "WrappingKeyAlgorithm": "{{string}}"
}
```

## Request Parameters
<a name="API_GetParametersForImport_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [KeyMaterialType](#API_GetParametersForImport_RequestSyntax) **   <a name="paymentcryptography-GetParametersForImport-request-KeyMaterialType"></a>
The method to use for key material import. Import token is only required for TR-34 WrappedKeyBlock (`TR34_KEY_BLOCK`) and RSA WrappedKeyCryptogram (`KEY_CRYPTOGRAM`).
Import token is not required for TR-31, root public key cerificate or trusted public key certificate.
Type: String
Valid Values: `TR34_KEY_BLOCK | TR31_KEY_BLOCK | ROOT_PUBLIC_KEY_CERTIFICATE | TRUSTED_PUBLIC_KEY_CERTIFICATE | KEY_CRYPTOGRAM`
Required: Yes

 ** [ReuseLastGeneratedToken](#API_GetParametersForImport_RequestSyntax) **   <a name="paymentcryptography-GetParametersForImport-request-ReuseLastGeneratedToken"></a>
Specifies whether to reuse the existing import token and wrapping key certificate. If set to `true` and a valid import token exists for the same key material type and wrapping key algorithm with at least 7 days of remaining validity, the existing token and wrapping key certificate are returned. Otherwise, a new import token and wrapping key certificate are generated. The default value is `false`, which generates a new import token and wrapping key certificate on every call.
Type: Boolean
Required: No

 ** [WrappingKeyAlgorithm](#API_GetParametersForImport_RequestSyntax) **   <a name="paymentcryptography-GetParametersForImport-request-WrappingKeyAlgorithm"></a>
The wrapping key algorithm to generate a wrapping key certificate. This certificate wraps the key under import.
At this time, `RSA_2048` is the allowed algorithm for TR-34 WrappedKeyBlock import. Additionally, `RSA_2048`, `RSA_3072`, `RSA_4096` are the allowed algorithms for RSA WrappedKeyCryptogram import.
Type: String
Valid Values: `TDES_2KEY | TDES_3KEY | AES_128 | AES_192 | AES_256 | HMAC_SHA256 | HMAC_SHA384 | HMAC_SHA512 | HMAC_SHA224 | RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521`
Required: Yes

## Response Syntax
<a name="API_GetParametersForImport_ResponseSyntax"></a>

```
{
   "ImportToken": "string",
   "ParametersValidUntilTimestamp": number,
   "WrappingKeyAlgorithm": "string",
   "WrappingKeyCertificate": "string",
   "WrappingKeyCertificateChain": "string"
}
```

## Response Elements
<a name="API_GetParametersForImport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImportToken](#API_GetParametersForImport_ResponseSyntax) **   <a name="paymentcryptography-GetParametersForImport-response-ImportToken"></a>
The import token to initiate key import into AWS Payment Cryptography. The import token expires after 30 days. You can use the same import token to import multiple keys to the same service account.
Type: String
Pattern: `(import-token-[0-9a-zA-Z]{16,64})?`

 ** [ParametersValidUntilTimestamp](#API_GetParametersForImport_ResponseSyntax) **   <a name="paymentcryptography-GetParametersForImport-response-ParametersValidUntilTimestamp"></a>
The validity period of the import token.
Type: Timestamp

 ** [WrappingKeyAlgorithm](#API_GetParametersForImport_ResponseSyntax) **   <a name="paymentcryptography-GetParametersForImport-response-WrappingKeyAlgorithm"></a>
The algorithm of the wrapping key for use within TR-34 WrappedKeyBlock or RSA WrappedKeyCryptogram.
Type: String
Valid Values: `TDES_2KEY | TDES_3KEY | AES_128 | AES_192 | AES_256 | HMAC_SHA256 | HMAC_SHA384 | HMAC_SHA512 | HMAC_SHA224 | RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521`

 ** [WrappingKeyCertificate](#API_GetParametersForImport_ResponseSyntax) **   <a name="paymentcryptography-GetParametersForImport-response-WrappingKeyCertificate"></a>
The wrapping key certificate in PEM format (base64 encoded) of the wrapping key for use within the TR-34 key block. The certificate expires in 30 days.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`

 ** [WrappingKeyCertificateChain](#API_GetParametersForImport_ResponseSyntax) **   <a name="paymentcryptography-GetParametersForImport-response-WrappingKeyCertificateChain"></a>
The AWS Payment Cryptography root certificate authority (CA) that signed the wrapping key certificate in PEM format (base64 encoded).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[^\[;\]<>]+`

## Errors
<a name="API_GetParametersForImport_Errors"></a>

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific AWS Payment Cryptography action you're attempting.
HTTP Status Code: 400

 ** ConflictException **
This request can cause an inconsistent state for the resource.
The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.
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

 ** ServiceQuotaExceededException **
This request would cause a service quota to be exceeded.
You have reached the maximum number of keys, aliases, or other resources allowed in your account. Review your current usage and consider deleting unused resources or requesting a quota increase.
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
<a name="API_GetParametersForImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-2021-09-14/GetParametersForImport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-2021-09-14/GetParametersForImport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/GetParametersForImport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-2021-09-14/GetParametersForImport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/GetParametersForImport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-2021-09-14/GetParametersForImport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-2021-09-14/GetParametersForImport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-2021-09-14/GetParametersForImport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-2021-09-14/GetParametersForImport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/GetParametersForImport)
