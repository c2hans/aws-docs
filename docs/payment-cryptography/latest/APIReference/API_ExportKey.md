---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportKey.html
---

# ExportKey
<a name="API_ExportKey"></a>

Exports a key from AWS Payment Cryptography.

 AWS Payment Cryptography simplifies key exchange by replacing the existing paper-based approach with a modern electronic approach. With `ExportKey` you can export symmetric keys using either symmetric and asymmetric key exchange mechanisms. Using this operation, you can share your AWS Payment Cryptography generated keys with other service partners to perform cryptographic operations outside of AWS Payment Cryptography

For symmetric key exchange, AWS Payment Cryptography uses the ANSI X9 TR-31 norm in accordance with PCI PIN guidelines. And for asymmetric key exchange, AWS Payment Cryptography supports ANSI X9 TR-34 norm, RSA unwrap, and ECDH (Elliptic Curve Diffie-Hellman) key exchange mechanisms. Asymmetric key exchange methods are typically used to establish bi-directional trust between the two parties exhanging keys and are used for initial key exchange such as Key Encryption Key (KEK). After which you can export working keys using symmetric method to perform various cryptographic operations within AWS Payment Cryptography.

PCI requires specific minimum key strength of wrapping keys used to protect the keys being exchanged electronically. These requirements can change when PCI standards are revised. The rules specify that wrapping keys used for transport must be at least as strong as the key being protected. For more information on recommended key strength of wrapping keys and key exchange mechanism, see [Importing and exporting keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-importexport.html) in the * AWS Payment Cryptography User Guide*.

You can also use `ExportKey` functionality to generate and export an IPEK (Initial Pin Encryption Key) from AWS Payment Cryptography using either TR-31 or TR-34 export key exchange. IPEK is generated from BDK (Base Derivation Key) and `ExportDukptInitialKey` attribute KSN (`KeySerialNumber`). The generated IPEK does not persist within AWS Payment Cryptography and has to be re-generated each time during export.

For key exchange using TR-31 or TR-34 key blocks, you can also export optional blocks within the key block header which contain additional attribute information about the key. The `KeyVersion` within `KeyBlockHeaders` indicates the version of the key within the key block. Furthermore, `KeyExportability` within `KeyBlockHeaders` can be used to further restrict exportability of the key after export from AWS Payment Cryptography.

The `OptionalBlocks` contain the additional data related to the key. For information on data type that can be included within optional blocks, refer to [ASC X9.143-2022](https://webstore.ansi.org/standards/ascx9/ansix91432022).

**Note**
Data included in key block headers is signed but transmitted in clear text. Sensitive or confidential information should not be included in optional blocks. Refer to ASC X9.143-2022 standard for information on allowed data type.

 **To export initial keys (KEK) or IPEK using TR-34**

Using this operation, you can export initial key using TR-34 asymmetric key exchange. You can only export KEK generated within AWS Payment Cryptography. In TR-34 terminology, the sending party of the key is called Key Distribution Host (KDH) and the receiving party of the key is called Key Receiving Device (KRD). During key export process, KDH is AWS Payment Cryptography which initiates key export and KRD is the user receiving the key.

To initiate TR-34 key export, the KRD must obtain an export token by calling [GetParametersForExport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html). This operation also generates a key pair for the purpose of key export, signs the key and returns back the signing public key certificate (also known as KDH signing certificate) and root certificate chain. The KDH uses the private key to sign the the export payload and the signing public key certificate is provided to KRD to verify the signature. The KRD can import the root certificate into its Hardware Security Module (HSM), as required. The export token and the associated KDH signing certificate expires after 30 days.

Next the KRD generates a key pair for the the purpose of encrypting the KDH key and provides the public key cerificate (also known as KRD wrapping certificate) back to KDH. The KRD will also import the root cerificate chain into AWS Payment Cryptography by calling [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html) for `RootCertificatePublicKey`. The KDH, AWS Payment Cryptography, will use the KRD wrapping cerificate to encrypt (wrap) the key under export and signs it with signing private key to generate a TR-34 WrappedKeyBlock. For more information on TR-34 key export, see section [Exporting symmetric keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-export.html) in the * AWS Payment Cryptography User Guide*.

Set the following parameters:
+  `ExportAttributes`: Specify export attributes in case of IPEK export. This parameter is optional for KEK export.
+  `ExportKeyIdentifier`: The `KeyARN` of the KEK or BDK (in case of IPEK) under export.
+  `KeyMaterial`: Use `Tr34KeyBlock` parameters.
+  `CertificateAuthorityPublicKeyIdentifier`: The `KeyARN` of the certificate chain that signed the KRD wrapping key certificate.
+  `ExportToken`: Obtained from KDH by calling [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html).
+  `WrappingKeyCertificate`: The public key certificate in PEM format (base64 encoded) of the KRD wrapping key AWS Payment Cryptography uses for encryption of the TR-34 export payload. This certificate must be signed by the root certificate (CertificateAuthorityPublicKeyIdentifier) imported into AWS Payment Cryptography.

When this operation is successful, AWS Payment Cryptography returns the KEK or IPEK as a TR-34 WrappedKeyBlock.

 **To export initial keys (KEK) or IPEK using RSA Wrap and Unwrap**

Using this operation, you can export initial key using asymmetric RSA wrap and unwrap key exchange method. To initiate export, generate an asymmetric key pair on the receiving HSM and obtain the public key certificate in PEM format (base64 encoded) for the purpose of wrapping and the root certifiate chain. Import the root certificate into AWS Payment Cryptography by calling [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html) for `RootCertificatePublicKey`.

Next call `ExportKey` and set the following parameters:
+  `CertificateAuthorityPublicKeyIdentifier`: The `KeyARN` of the certificate chain that signed wrapping key certificate.
+  `KeyMaterial`: Set to `KeyCryptogram`.
+  `WrappingKeyCertificate`: The public key certificate in PEM format (base64 encoded) obtained by the receiving HSM and signed by the root certificate (CertificateAuthorityPublicKeyIdentifier) imported into AWS Payment Cryptography. The receiving HSM uses its private key component to unwrap the WrappedKeyCryptogram.

When this operation is successful, AWS Payment Cryptography returns the WrappedKeyCryptogram.

 **To export working keys or IPEK using TR-31**

Using this operation, you can export working keys or IPEK using TR-31 symmetric key exchange. In TR-31, you must use an initial key such as KEK to encrypt or wrap the key under export. To establish a KEK, you can use [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html) or [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html).

Set the following parameters:
+  `ExportAttributes`: Specify export attributes in case of IPEK export. This parameter is optional for KEK export.
+  `ExportKeyIdentifier`: The `KeyARN` of the KEK or BDK (in case of IPEK) under export.
+  `KeyMaterial`: Use `Tr31KeyBlock` parameters.

 **To export working keys using ECDH**

You can also use ECDH key agreement to export working keys in a TR-31 keyblock, where the wrapping key is an ECDH derived key.

To initiate a TR-31 key export using ECDH, both sides must create an ECC key pair with key usage K3 and exchange public key certificates. In AWS Payment Cryptography, you can do this by calling `CreateKey`. If you have not already done so, you must import the CA chain that issued the receiving public key certificate by calling `ImportKey` with input `RootCertificatePublicKey` for root CA or `TrustedPublicKey` for intermediate CA. You can then complete a TR-31 key export by deriving a shared wrapping key using the service ECC key pair, public certificate of your ECC key pair outside of AWS Payment Cryptography, and the key derivation parameters including key derivation function, hash algorithm, derivation data, key algorithm.
+  `KeyMaterial`: Use `DiffieHellmanTr31KeyBlock` parameters.
+  `PrivateKeyIdentifier`: The `KeyArn` of the ECC key pair created within AWS Payment Cryptography to derive a shared KEK.
+  `PublicKeyCertificate`: The public key certificate of the receiving ECC key pair in PEM format (base64 encoded) to derive a shared KEK.
+  `CertificateAuthorityPublicKeyIdentifier`: The `keyARN` of the CA that signed the public key certificate of the receiving ECC key pair.

When this operation is successful, AWS Payment Cryptography returns the working key as a TR-31 WrappedKeyBlock, where the wrapping key is the ECDH derived key.

 **Cross-account use:** This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [GetParametersForExport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html)
+  [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html)

## Request Syntax
<a name="API_ExportKey_RequestSyntax"></a>

```
{
   "ExportAttributes": {
      "ExportDukptInitialKey": {
         "KeySerialNumber": "{{string}}"
      },
      "KeyCheckValueAlgorithm": "{{string}}"
   },
   "ExportKeyIdentifier": "{{string}}",
   "KeyMaterial": { ... }
}
```

## Request Parameters
<a name="API_ExportKey_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ExportAttributes](#API_ExportKey_RequestSyntax) **   <a name="paymentcryptography-ExportKey-request-ExportAttributes"></a>
The attributes for IPEK generation during export.
Type: [ExportAttributes](API_ExportAttributes.md) object
Required: No

 ** [ExportKeyIdentifier](#API_ExportKey_RequestSyntax) **   <a name="paymentcryptography-ExportKey-request-ExportKeyIdentifier"></a>
The `KeyARN` of the key under export from AWS Payment Cryptography.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** [KeyMaterial](#API_ExportKey_RequestSyntax) **   <a name="paymentcryptography-ExportKey-request-KeyMaterial"></a>
The key block format type, for example, TR-34 or TR-31, to use during key material export.
Type: [ExportKeyMaterial](API_ExportKeyMaterial.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_ExportKey_ResponseSyntax"></a>

```
{
   "WrappedKey": {
      "KeyCheckValue": "string",
      "KeyCheckValueAlgorithm": "string",
      "KeyMaterial": "string",
      "WrappedKeyMaterialFormat": "string",
      "WrappingKeyArn": "string"
   }
}
```

## Response Elements
<a name="API_ExportKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WrappedKey](#API_ExportKey_ResponseSyntax) **   <a name="paymentcryptography-ExportKey-response-WrappedKey"></a>
The key material under export as a TR-34 WrappedKeyBlock or a TR-31 WrappedKeyBlock. or a RSA WrappedKeyCryptogram.
Type: [WrappedKey](API_WrappedKey.md) object

## Errors
<a name="API_ExportKey_Errors"></a>

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
<a name="API_ExportKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-2021-09-14/ExportKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-2021-09-14/ExportKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ExportKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-2021-09-14/ExportKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ExportKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-2021-09-14/ExportKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-2021-09-14/ExportKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-2021-09-14/ExportKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-2021-09-14/ExportKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ExportKey)
