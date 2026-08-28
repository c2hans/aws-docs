---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EncryptData.html
---

# EncryptData
<a name="API_EncryptData"></a>

Encrypts plaintext data to ciphertext using a symmetric (TDES, AES), asymmetric (RSA), or derived (DUKPT or EMV) encryption key scheme. For more information, see [Encrypt data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/encrypt-data.html) in the * AWS Payment Cryptography User Guide*.

You can generate an encryption key within AWS Payment Cryptography by calling [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html). You can import your own encryption key by calling [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html).

For this operation, the key must have `KeyModesOfUse` set to `Encrypt`. In asymmetric encryption, plaintext is encrypted using public component. You can import the public component of an asymmetric key pair created outside AWS Payment Cryptography by calling [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html).

This operation also supports dynamic keys, allowing you to pass a dynamic encryption key as a TR-31 WrappedKeyBlock. This can be used when key material is frequently rotated, such as during every card transaction, and there is need to avoid importing short-lived keys into AWS Payment Cryptography. To encrypt using dynamic keys, the `keyARN` is the Key Encryption Key (KEK) of the TR-31 wrapped encryption key material. The incoming wrapped key shall have a key purpose of D0 with a mode of use of B or D. For more information, see [Using Dynamic Keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-acquirers-dynamickeys.html) in the * AWS Payment Cryptography User Guide*.

For symmetric and DUKPT encryption, AWS Payment Cryptography supports `TDES` and `AES` algorithms. For EMV encryption, AWS Payment Cryptography supports `TDES` algorithms.For asymmetric encryption, AWS Payment Cryptography supports `RSA`.

When you use TDES or TDES DUKPT, the plaintext data length must be a multiple of 8 bytes. For AES or AES DUKPT, the plaintext data length must be a multiple of 16 bytes. For RSA, it sould be equal to the key size unless padding is enabled.

To encrypt using DUKPT, you must already have a BDK (Base Derivation Key) key in your account with `KeyModesOfUse` set to `DeriveKey`, or you can generate a new DUKPT key by calling [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html). To encrypt using EMV, you must already have an IMK (Issuer Master Key) key in your account with `KeyModesOfUse` set to `DeriveKey`.

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the * AWS Payment Cryptography User Guide*.

 **Cross-account use**: This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [DecryptData](API_DecryptData.md)
+  [GetPublicCertificate](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetPublicKeyCertificate.html)
+  [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html)
+  [ReEncryptData](API_ReEncryptData.md)

## Request Syntax
<a name="API_EncryptData_RequestSyntax"></a>

```
POST /keys/{{KeyIdentifier}}/encrypt HTTP/1.1
Content-type: application/json

{
   "EncryptionAttributes": { ... },
   "PlainText": "{{string}}",
   "WrappedKey": {
      "KeyCheckValueAlgorithm": "{{string}}",
      "WrappedKeyMaterial": { ... }
   }
}
```

## URI Request Parameters
<a name="API_EncryptData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [KeyIdentifier](#API_EncryptData_RequestSyntax) **   <a name="paymentcryptographydata-EncryptData-request-uri-KeyIdentifier"></a>
The `keyARN` of the encryption key that AWS Payment Cryptography uses for plaintext encryption.
When a WrappedKeyBlock is provided, this value will be the identifier to the key wrapping key. Otherwise, it is the key identifier used to perform the operation.
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

## Request Body
<a name="API_EncryptData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EncryptionAttributes](#API_EncryptData_RequestSyntax) **   <a name="paymentcryptographydata-EncryptData-request-EncryptionAttributes"></a>
The encryption key type and attributes for plaintext encryption.
Type: [EncryptionDecryptionAttributes](API_EncryptionDecryptionAttributes.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [PlainText](#API_EncryptData_RequestSyntax) **   <a name="paymentcryptographydata-EncryptData-request-PlainText"></a>
The plaintext to be encrypted.
For encryption using asymmetric keys, plaintext data length is constrained by encryption key strength that you define in `KeyAlgorithm` and padding type that you define in `AsymmetricEncryptionAttributes`. For more information, see [Encrypt data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/encrypt-data.html) in the * AWS Payment Cryptography User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 4096.
Pattern: `(?:[0-9a-fA-F][0-9a-fA-F])+`
Required: Yes

 ** [WrappedKey](#API_EncryptData_RequestSyntax) **   <a name="paymentcryptographydata-EncryptData-request-WrappedKey"></a>
The WrappedKeyBlock containing the encryption key for plaintext encryption.
Type: [WrappedKey](API_WrappedKey.md) object
Required: No

## Response Syntax
<a name="API_EncryptData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CipherText": "string",
   "KeyArn": "string",
   "KeyCheckValue": "string"
}
```

## Response Elements
<a name="API_EncryptData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CipherText](#API_EncryptData_ResponseSyntax) **   <a name="paymentcryptographydata-EncryptData-response-CipherText"></a>
The encrypted ciphertext.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 4224.
Pattern: `(?:[0-9a-fA-F][0-9a-fA-F])+`

 ** [KeyArn](#API_EncryptData_ResponseSyntax) **   <a name="paymentcryptographydata-EncryptData-response-KeyArn"></a>
The `keyARN` of the encryption key that AWS Payment Cryptography uses for plaintext encryption.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

 ** [KeyCheckValue](#API_EncryptData_ResponseSyntax) **   <a name="paymentcryptographydata-EncryptData-response-KeyCheckValue"></a>
The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.
 AWS Payment Cryptography computes the KCV according to the CMAC specification.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`

## Errors
<a name="API_EncryptData_Errors"></a>

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
<a name="API_EncryptData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-data-2022-02-03/EncryptData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-data-2022-02-03/EncryptData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/EncryptData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-data-2022-02-03/EncryptData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/EncryptData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-data-2022-02-03/EncryptData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-data-2022-02-03/EncryptData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-data-2022-02-03/EncryptData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-data-2022-02-03/EncryptData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/EncryptData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
