---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html
---

# ImportKey
<a name="API_ImportKey"></a>

Imports symmetric keys and public key certificates in PEM format (base64 encoded) into AWS Payment Cryptography.

 AWS Payment Cryptography simplifies key exchange by replacing the existing paper-based approach with a modern electronic approach. With `ImportKey` you can import symmetric keys using either symmetric and asymmetric key exchange mechanisms.

For symmetric key exchange, AWS Payment Cryptography uses the ANSI X9 TR-31 norm in accordance with PCI PIN guidelines. And for asymmetric key exchange, AWS Payment Cryptography supports ANSI X9 TR-34 norm, RSA unwrap, and ECDH (Elliptic Curve Diffie-Hellman) key exchange mechanisms. Asymmetric key exchange methods are typically used to establish bi-directional trust between the two parties exhanging keys and are used for initial key exchange such as Key Encryption Key (KEK) or Zone Master Key (ZMK). After which you can import working keys using symmetric method to perform various cryptographic operations within AWS Payment Cryptography.

PCI requires specific minimum key strength of wrapping keys used to protect the keys being exchanged electronically. These requirements can change when PCI standards are revised. The rules specify that wrapping keys used for transport must be at least as strong as the key being protected. For more information on recommended key strength of wrapping keys and key exchange mechanism, see [Importing and exporting keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-importexport.html) in the * AWS Payment Cryptography User Guide*.

You can also import a *root public key certificate*, used to sign other public key certificates, or a *trusted public key certificate* under an already established root public key certificate.

 **To import a public root key certificate**

Using this operation, you can import the public component (in PEM cerificate format) of your private root key. You can use the imported public root key certificate for digital signatures, for example signing wrapping key or signing key in TR-34, within your AWS Payment Cryptography account.

Set the following parameters:
+  `KeyMaterial`: `RootCertificatePublicKey`
+  `KeyClass`: `PUBLIC_KEY`
+  `KeyModesOfUse`: `Verify`
+  `KeyUsage`: `TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE`
+  `PublicKeyCertificate`: The public key certificate in PEM format (base64 encoded) of the private root key under import.

 **To import a trusted public key certificate**

The root public key certificate must be in place and operational before you import a trusted public key certificate. Set the following parameters:
+  `KeyMaterial`: `TrustedCertificatePublicKey`
+  `CertificateAuthorityPublicKeyIdentifier`: `KeyArn` of the `RootCertificatePublicKey`.
+  `KeyModesOfUse` and `KeyUsage`: Corresponding to the cryptographic operations such as wrap, sign, or encrypt that you will allow the trusted public key certificate to perform.
+  `PublicKeyCertificate`: The trusted public key certificate in PEM format (base64 encoded) under import.

 **To import initial keys (KEK or ZMK or similar) using TR-34**

Using this operation, you can import initial key using TR-34 asymmetric key exchange. In TR-34 terminology, the sending party of the key is called Key Distribution Host (KDH) and the receiving party of the key is called Key Receiving Device (KRD). During the key import process, KDH is the user who initiates the key import and KRD is AWS Payment Cryptography who receives the key.

To initiate TR-34 key import, the KDH must obtain an import token by calling [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html). This operation generates an encryption keypair for the purpose of key import, signs the key and returns back the wrapping key certificate (also known as KRD wrapping certificate) and the root certificate chain. The KDH must trust and install the KRD wrapping certificate on its HSM and use it to encrypt (wrap) the KDH key during TR-34 WrappedKeyBlock generation. The import token and associated KRD wrapping certificate expires after 30 days.

Next the KDH generates a key pair for the purpose of signing the encrypted KDH key and provides the public certificate of the signing key to AWS Payment Cryptography. The KDH will also need to import the root certificate chain of the KDH signing certificate by calling `ImportKey` for `RootCertificatePublicKey`. For more information on TR-34 key import, see section [Importing symmetric keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-import.html) in the * AWS Payment Cryptography User Guide*.

Set the following parameters:
+  `KeyMaterial`: Use `Tr34KeyBlock` parameters.
+  `CertificateAuthorityPublicKeyIdentifier`: The `KeyARN` of the certificate chain that signed the KDH signing key certificate.
+  `ImportToken`: Obtained from KRD by calling [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html).
+  `WrappedKeyBlock`: The TR-34 wrapped key material from KDH. It contains the KDH key under import, wrapped with KRD wrapping certificate and signed by KDH signing private key. This TR-34 key block is typically generated by the KDH Hardware Security Module (HSM) outside of AWS Payment Cryptography.
+  `SigningKeyCertificate`: The public key certificate in PEM format (base64 encoded) of the KDH signing key generated under the root certificate (CertificateAuthorityPublicKeyIdentifier) imported in AWS Payment Cryptography.

 **To import initial keys (KEK or ZMK or similar) using RSA Wrap and Unwrap**

Using this operation, you can import initial key using asymmetric RSA wrap and unwrap key exchange method. To initiate import, call [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html) with `KeyMaterial` set to `KEY_CRYPTOGRAM` to generate an import token. This operation also generates an encryption keypair for the purpose of key import, signs the key and returns back the wrapping key certificate in PEM format (base64 encoded) and its root certificate chain. The import token and associated KRD wrapping certificate expires after 30 days.

You must trust and install the wrapping certificate and its certificate chain on the sending HSM and use it to wrap the key under export for WrappedKeyCryptogram generation. Next call `ImportKey` with `KeyMaterial` set to `KEY_CRYPTOGRAM` and provide the `ImportToken` and `KeyAttributes` for the key under import.

 **To import working keys using TR-31**

 AWS Payment Cryptography uses TR-31 symmetric key exchange norm to import working keys. A KEK must be established within AWS Payment Cryptography by using TR-34 key import or by using [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html). To initiate a TR-31 key import, set the following parameters:
+  `KeyMaterial`: Use `Tr31KeyBlock` parameters.
+  `WrappedKeyBlock`: The TR-31 wrapped key material. It contains the key under import, encrypted using KEK. The TR-31 key block is typically generated by a HSM outside of AWS Payment Cryptography.
+  `WrappingKeyIdentifier`: The `KeyArn` of the KEK that AWS Payment Cryptography uses to decrypt or unwrap the key under import.

 **To import working keys using ECDH**

You can also use ECDH key agreement to import working keys as a TR-31 keyblock, where the wrapping key is an ECDH derived key.

To initiate a TR-31 key import using ECDH, both sides must create an ECC key pair with key usage K3 and exchange public key certificates. In AWS Payment Cryptography, you can do this by calling `CreateKey` and then `GetPublicKeyCertificate` to retrieve its public key certificate. Next, you can then generate a TR-31 WrappedKeyBlock using your own ECC key pair, the public certificate of the service's ECC key pair, and the key derivation parameters including key derivation function, hash algorithm, derivation data, and key algorithm. If you have not already done so, you must import the CA chain that issued the receiving public key certificate by calling `ImportKey` with input `RootCertificatePublicKey` for root CA or `TrustedPublicKey` for intermediate CA. To complete the TR-31 key import, you can use the following parameters. It is important that the ECDH key derivation parameters you use should match those used during import to derive the same shared wrapping key within AWS Payment Cryptography.
+  `KeyMaterial`: Use `DiffieHellmanTr31KeyBlock` parameters.
+  `PrivateKeyIdentifier`: The `KeyArn` of the ECC key pair created within AWS Payment Cryptography to derive a shared KEK.
+  `PublicKeyCertificate`: The public key certificate of the receiving ECC key pair in PEM format (base64 encoded) to derive a shared KEK.
+  `CertificateAuthorityPublicKeyIdentifier`: The `keyARN` of the CA that signed the public key certificate of the receiving ECC key pair.

 **Cross-account use:** This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [ExportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportKey.html)
+  [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html)

## Request Syntax
<a name="API_ImportKey_RequestSyntax"></a>

```
{
   "Enabled": {{boolean}},
   "KeyCheckValueAlgorithm": "{{string}}",
   "KeyMaterial": { ... },
   "ReplicationRegions": [ "{{string}}" ],
   "RequesterComment": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ImportKey_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Enabled](#API_ImportKey_RequestSyntax) **   <a name="paymentcryptography-ImportKey-request-Enabled"></a>
Specifies whether import key is enabled.
Type: Boolean
Required: No

 ** [KeyCheckValueAlgorithm](#API_ImportKey_RequestSyntax) **   <a name="paymentcryptography-ImportKey-request-KeyCheckValueAlgorithm"></a>
The algorithm that AWS Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.
For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.
Type: String
Valid Values: `CMAC | ANSI_X9_24 | HMAC | SHA_1`
Required: No

 ** [KeyMaterial](#API_ImportKey_RequestSyntax) **   <a name="paymentcryptography-ImportKey-request-KeyMaterial"></a>
The key or public key certificate type to use during key material import, for example TR-34 or RootCertificatePublicKey.
Type: [ImportKeyMaterial](API_ImportKeyMaterial.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [ReplicationRegions](#API_ImportKey_RequestSyntax) **   <a name="paymentcryptography-ImportKey-request-ReplicationRegions"></a>
A list of AWS Regions for key replication operations.
Each region in the list must be a valid AWS Region identifier where AWS Payment Cryptography is available. This list is used to specify which regions should be added to or removed from a key's replication configuration.
Type: Array of strings
Pattern: `[a-z]{2}-[a-z]{1,16}-[0-9]+`
Required: No

 ** [RequesterComment](#API_ImportKey_RequestSyntax) **   <a name="paymentcryptography-ImportKey-request-RequesterComment"></a>
The comment from the requester explaining the reason for the import.
Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in AWS CloudTrail logs and other output.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** [Tags](#API_ImportKey_RequestSyntax) **   <a name="paymentcryptography-ImportKey-request-Tags"></a>
Assigns one or more tags to the AWS Payment Cryptography key. Use this parameter to tag a key when it is imported. To tag an existing AWS Payment Cryptography key, use the [TagResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html) operation.
Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You can't have more than one tag on an AWS Payment Cryptography key with the same tag key. If you specify an existing tag key with a different tag value, AWS Payment Cryptography replaces the current tag value with the specified one.
Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in AWS CloudTrail logs and other output.
Tagging or untagging an AWS Payment Cryptography key can allow or deny permission to the key.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_ImportKey_ResponseSyntax"></a>

```
{
   "Key": {
      "CreateTimestamp": number,
      "DeletePendingTimestamp": number,
      "DeleteTimestamp": number,
      "DeriveKeyUsage": "string",
      "Enabled": boolean,
      "Exportable": boolean,
      "KeyArn": "string",
      "KeyAttributes": {
         "KeyAlgorithm": "string",
         "KeyClass": "string",
         "KeyModesOfUse": {
            "Decrypt": boolean,
            "DeriveKey": boolean,
            "Encrypt": boolean,
            "Generate": boolean,
            "NoRestrictions": boolean,
            "Sign": boolean,
            "Unwrap": boolean,
            "Verify": boolean,
            "Wrap": boolean
         },
         "KeyUsage": "string"
      },
      "KeyCheckValue": "string",
      "KeyCheckValueAlgorithm": "string",
      "KeyOrigin": "string",
      "KeyState": "string",
      "MpaStatus": {
         "InitiationDate": number,
         "MpaSessionArn": "string",
         "Status": "string",
         "StatusMessage": "string"
      },
      "MultiRegionKeyType": "string",
      "PrimaryRegion": "string",
      "ReplicationStatus": {
         "string" : {
            "Status": "string",
            "StatusMessage": "string"
         }
      },
      "UsageStartTimestamp": number,
      "UsageStopTimestamp": number,
      "UsingDefaultReplicationRegions": boolean
   }
}
```

## Response Elements
<a name="API_ImportKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Key](#API_ImportKey_ResponseSyntax) **   <a name="paymentcryptography-ImportKey-response-Key"></a>
The `KeyARN` of the key material imported within AWS Payment Cryptography.
Type: [Key](API_Key.md) object

## Errors
<a name="API_ImportKey_Errors"></a>

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
<a name="API_ImportKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-2021-09-14/ImportKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-2021-09-14/ImportKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ImportKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-2021-09-14/ImportKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ImportKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-2021-09-14/ImportKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-2021-09-14/ImportKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-2021-09-14/ImportKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-2021-09-14/ImportKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ImportKey)
