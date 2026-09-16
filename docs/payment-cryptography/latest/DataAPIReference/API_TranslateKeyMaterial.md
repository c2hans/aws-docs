---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslateKeyMaterial.html
---

# TranslateKeyMaterial
<a name="API_TranslateKeyMaterial"></a>

Translates an cryptographic key between different wrapping keys without importing the key into AWS Payment Cryptography.

This operation can be used when key material is frequently rotated, such as during every card transaction, and there is a need to avoid importing short-lived keys into AWS Payment Cryptography. It translates short-lived transaction keys such as [PEK](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/terminology.html#terms.pek) generated for each transaction and wrapped with an [ECDH](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/terminology.html#terms.ecdh) derived wrapping key to another [KEK](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/terminology.html#terms.kek) wrapping key.

Before using this operation, you must first request the public key certificate of the ECC key pair generated within AWS Payment Cryptography to establish an ECDH key agreement. In `TranslateKeyData`, the service uses its own ECC key pair, public certificate of receiving ECC key pair, and the key derivation parameters to generate a derived key. The service uses this derived key to unwrap the incoming transaction key received as a TR31WrappedKeyBlock and re-wrap using a user provided KEK to generate an outgoing Tr31WrappedKeyBlock.

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the * AWS Payment Cryptography User Guide*.

 **Cross-account use**: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html)
+  [GetPublicCertificate](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetPublicKeyCertificate.html)
+  [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html)

## Request Syntax
<a name="API_TranslateKeyMaterial_RequestSyntax"></a>

```
POST /keymaterial/translate HTTP/1.1
Content-type: application/json

{
   "IncomingKeyMaterial": { ... },
   "KeyCheckValueAlgorithm": "{{string}}",
   "OutgoingKeyMaterial": { ... }
}
```

## URI Request Parameters
<a name="API_TranslateKeyMaterial_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_TranslateKeyMaterial_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IncomingKeyMaterial](#API_TranslateKeyMaterial_RequestSyntax) **   <a name="paymentcryptographydata-TranslateKeyMaterial-request-IncomingKeyMaterial"></a>
Parameter information of the TR31WrappedKeyBlock containing the transaction key.
Type: [IncomingKeyMaterial](API_IncomingKeyMaterial.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [KeyCheckValueAlgorithm](#API_TranslateKeyMaterial_RequestSyntax) **   <a name="paymentcryptographydata-TranslateKeyMaterial-request-KeyCheckValueAlgorithm"></a>
The key check value (KCV) algorithm used for calculating the KCV of the derived key.
Type: String
Valid Values: `CMAC | ANSI_X9_24 | HMAC | SHA_1`
Required: No

 ** [OutgoingKeyMaterial](#API_TranslateKeyMaterial_RequestSyntax) **   <a name="paymentcryptographydata-TranslateKeyMaterial-request-OutgoingKeyMaterial"></a>
Parameter information of the wrapping key used to wrap the transaction key in the outgoing TR31WrappedKeyBlock.
Type: [OutgoingKeyMaterial](API_OutgoingKeyMaterial.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_TranslateKeyMaterial_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "WrappedKey": {
      "KeyCheckValue": "string",
      "WrappedKeyMaterial": "string",
      "WrappedKeyMaterialFormat": "string"
   }
}
```

## Response Elements
<a name="API_TranslateKeyMaterial_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WrappedKey](#API_TranslateKeyMaterial_ResponseSyntax) **   <a name="paymentcryptographydata-TranslateKeyMaterial-response-WrappedKey"></a>
The outgoing KEK wrapped TR31WrappedKeyBlock.
Type: [WrappedWorkingKey](API_WrappedWorkingKey.md) object

## Errors
<a name="API_TranslateKeyMaterial_Errors"></a>

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was denied due to an invalid resource error.
 ** ResourceId **
The resource that is missing.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request was denied due to an invalid request error.
 ** fieldList **
The request was denied due to an invalid request error.
HTTP Status Code: 400

## See Also
<a name="API_TranslateKeyMaterial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-data-2022-02-03/TranslateKeyMaterial)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-data-2022-02-03/TranslateKeyMaterial)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/TranslateKeyMaterial)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-data-2022-02-03/TranslateKeyMaterial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/TranslateKeyMaterial)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-data-2022-02-03/TranslateKeyMaterial)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-data-2022-02-03/TranslateKeyMaterial)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-data-2022-02-03/TranslateKeyMaterial)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-data-2022-02-03/TranslateKeyMaterial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/TranslateKeyMaterial)
