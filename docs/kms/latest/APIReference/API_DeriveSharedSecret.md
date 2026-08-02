---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html
---

# DeriveSharedSecret
<a name="API_DeriveSharedSecret"></a>

Derives a shared secret using a key agreement algorithm.

**Note**
You must use an asymmetric NIST-standard elliptic curve (ECC) or SM2 (China Regions only) KMS key pair with a `KeyUsage` value of `KEY_AGREEMENT` to call DeriveSharedSecret.

DeriveSharedSecret uses the [Elliptic Curve Cryptography Cofactor Diffie-Hellman Primitive](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Ar3.pdf#page=60) (ECDH) to establish a key agreement between two peers by deriving a shared secret from their elliptic curve public-private key pairs. You can use the raw shared secret that DeriveSharedSecret returns to derive a symmetric key that can encrypt and decrypt data that is sent between the two peers, or that can generate and verify HMACs. AWS KMS recommends that you follow [NIST recommendations for key derivation](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Cr2.pdf) when using the raw shared secret to derive a symmetric key.

The following workflow demonstrates how to establish key agreement over an insecure communication channel using DeriveSharedSecret.

1.  **Alice** calls [CreateKey](API_CreateKey.md) to create an asymmetric KMS key pair with a `KeyUsage` value of `KEY_AGREEMENT`.

   The asymmetric KMS key must use a NIST-standard elliptic curve (ECC) or SM2 (China Regions only) key spec.

1.  **Bob** creates an elliptic curve key pair.

   Bob can call [CreateKey](API_CreateKey.md) to create an asymmetric KMS key pair or generate a key pair outside of AWS KMS. Bob's key pair must use the same NIST-standard elliptic curve (ECC) or SM2 (China Regions ony) curve as Alice.

1. Alice and Bob **exchange their public keys** through an insecure communication channel (like the internet).

   Use [GetPublicKey](API_GetPublicKey.md) to download the public key of your asymmetric KMS key pair.
**Note**
 AWS KMS strongly recommends verifying that the public key you receive came from the expected party before using it to derive a shared secret.

1.  **Alice** calls DeriveSharedSecret.

    AWS KMS uses the private key from the KMS key pair generated in **Step 1**, Bob's public key, and the Elliptic Curve Cryptography Cofactor Diffie-Hellman Primitive to derive the shared secret. The private key in your KMS key pair never leaves AWS KMS unencrypted. DeriveSharedSecret returns the raw shared secret.

1.  **Bob** uses the Elliptic Curve Cryptography Cofactor Diffie-Hellman Primitive to calculate the same raw secret using his private key and Alice's public key.

To derive a shared secret you must provide a key agreement algorithm, the private key of the caller's asymmetric NIST-standard elliptic curve or SM2 (China Regions only) KMS key pair, and the public key from your peer's NIST-standard elliptic curve or SM2 (China Regions only) key pair. The public key can be from another asymmetric KMS key pair or from a key pair generated outside of AWS KMS, but both key pairs must be on the same elliptic curve.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: Yes. To perform this operation with a KMS key in a different AWS account, specify the key ARN or alias ARN in the value of the `KeyId` parameter.

 **Required permissions**: [kms:DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [CreateKey](API_CreateKey.md)
+  [GetPublicKey](API_GetPublicKey.md)
+  [DescribeKey](API_DescribeKey.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_DeriveSharedSecret_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "GrantTokens": [ "{{string}}" ],
   "KeyAgreementAlgorithm": "{{string}}",
   "KeyId": "{{string}}",
   "PublicKey": {{blob}},
   "Recipient": {
      "AttestationDocument": {{blob}},
      "KeyEncryptionAlgorithm": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_DeriveSharedSecret_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyAgreementAlgorithm](#API_DeriveSharedSecret_RequestSyntax) **   <a name="KMS-DeriveSharedSecret-request-KeyAgreementAlgorithm"></a>
Specifies the key agreement algorithm used to derive the shared secret. The only valid value is `ECDH`.
Type: String
Valid Values: `ECDH`
Required: Yes

 ** [KeyId](#API_DeriveSharedSecret_RequestSyntax) **   <a name="KMS-DeriveSharedSecret-request-KeyId"></a>
Identifies an asymmetric NIST-standard ECC or SM2 (China Regions only) KMS key. AWS KMS uses the private key in the specified key pair to derive the shared secret. The key usage of the KMS key must be `KEY_AGREEMENT`. To find the `KeyUsage` of a KMS key, use the [DescribeKey](API_DescribeKey.md) operation.
To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with `"alias/"`. To specify a KMS key in a different AWS account, you must use the key ARN or alias ARN.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
+ Alias name: `alias/ExampleAlias`
+ Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md). To get the alias name and alias ARN, use [ListAliases](API_ListAliases.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [PublicKey](#API_DeriveSharedSecret_RequestSyntax) **   <a name="KMS-DeriveSharedSecret-request-PublicKey"></a>
Specifies the public key in your peer's NIST-standard elliptic curve (ECC) or SM2 (China Regions only) key pair.
The public key must be a DER-encoded X.509 public key, also known as `SubjectPublicKeyInfo` (SPKI), as defined in [RFC 5280](https://tools.ietf.org/html/rfc5280).
 [GetPublicKey](API_GetPublicKey.md) returns the public key of an asymmetric KMS key pair in the required DER-encoded format.
If you use [AWS CLI version 1](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-welcome.html), you must provide the DER-encoded X.509 public key in a file. Otherwise, the AWS CLI Base64-encodes the public key a second time, resulting in a `ValidationException`.
You can specify the public key as binary data in a file using fileb (`fileb://<path-to-file>`) or in-line using a Base64 encoded string.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: Yes

 ** [DryRun](#API_DeriveSharedSecret_RequestSyntax) **   <a name="KMS-DeriveSharedSecret-request-DryRun"></a>
Checks if your request will succeed. `DryRun` is an optional parameter.
To learn more about how to use this parameter, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the * AWS Key Management Service Developer Guide*.
Type: Boolean
Required: No

 ** [GrantTokens](#API_DeriveSharedSecret_RequestSyntax) **   <a name="KMS-DeriveSharedSecret-request-GrantTokens"></a>
A list of grant tokens.
Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency*. For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html) in the * AWS Key Management Service Developer Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [Recipient](#API_DeriveSharedSecret_RequestSyntax) **   <a name="KMS-DeriveSharedSecret-request-Recipient"></a>
A signed [attestation document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitro-enclave-how.html#term-attestdoc) from an AWS Nitro enclave or NitroTPM, and the encryption algorithm to use with the public key in the attestation document. The only valid encryption algorithm is `RSAES_OAEP_SHA_256`.
This parameter only supports attestation documents for AWS Nitro Enclaves or AWS NitroTPM. To call DeriveSharedSecret generate an attestation document use either [AWS Nitro Enclaves SDK](https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk) for an AWS Nitro Enclaves or [AWS NitroTPM tools](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attestation-get-doc.html) for AWS NitroTPM. Then use the Recipient parameter from any AWS SDK to provide the attestation document for the attested environment.
When you use this parameter, instead of returning a plaintext copy of the shared secret, AWS KMS encrypts the plaintext shared secret under the public key in the attestation document, and returns the resulting ciphertext in the `CiphertextForRecipient` field in the response. This ciphertext can be decrypted only with the private key in the attested environment. The `CiphertextBlob` field in the response contains the encrypted shared secret derived from the KMS key specified by the `KeyId` parameter and public key specified by the `PublicKey` parameter. The `SharedSecret` field in the response is null or empty.
For information about the interaction between AWS KMS and AWS Nitro Enclaves or AWS NitroTPM, see [Cryptographic attestation support in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html) in the * AWS Key Management Service Developer Guide*.
Type: [RecipientInfo](API_RecipientInfo.md) object
Required: No

## Response Syntax
<a name="API_DeriveSharedSecret_ResponseSyntax"></a>

```
{
   "CiphertextForRecipient": blob,
   "KeyAgreementAlgorithm": "string",
   "KeyId": "string",
   "KeyOrigin": "string",
   "SharedSecret": blob
}
```

## Response Elements
<a name="API_DeriveSharedSecret_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CiphertextForRecipient](#API_DeriveSharedSecret_ResponseSyntax) **   <a name="KMS-DeriveSharedSecret-response-CiphertextForRecipient"></a>
The plaintext shared secret encrypted with the public key from the attestation document. This ciphertext can be decrypted only by using a private key from the attested environment.
This field is included in the response only when the `Recipient` parameter in the request includes a valid attestation document from an AWS Nitro enclave or NitroTPM. For information about the interaction between AWS KMS and AWS Nitro Enclaves or AWS NitroTPM, see [Cryptographic attestation support in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html) in the * AWS Key Management Service Developer Guide*.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [KeyAgreementAlgorithm](#API_DeriveSharedSecret_ResponseSyntax) **   <a name="KMS-DeriveSharedSecret-response-KeyAgreementAlgorithm"></a>
Identifies the key agreement algorithm used to derive the shared secret.
Type: String
Valid Values: `ECDH`

 ** [KeyId](#API_DeriveSharedSecret_ResponseSyntax) **   <a name="KMS-DeriveSharedSecret-response-KeyId"></a>
Identifies the KMS key used to derive the shared secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [KeyOrigin](#API_DeriveSharedSecret_ResponseSyntax) **   <a name="KMS-DeriveSharedSecret-response-KeyOrigin"></a>
The source of the key material for the specified KMS key.
When this value is `AWS_KMS`, AWS KMS created the key material. When this value is `EXTERNAL`, the key material was imported or the KMS key doesn't have any key material.
The only valid values for DeriveSharedSecret are `AWS_KMS` and `EXTERNAL`. DeriveSharedSecret does not support KMS keys with a `KeyOrigin` value of `AWS_CLOUDHSM` or `EXTERNAL_KEY_STORE`.
Type: String
Valid Values: `AWS_KMS | EXTERNAL | AWS_CLOUDHSM | EXTERNAL_KEY_STORE`

 ** [SharedSecret](#API_DeriveSharedSecret_ResponseSyntax) **   <a name="KMS-DeriveSharedSecret-response-SharedSecret"></a>
The raw secret derived from the specified key agreement algorithm, private key in the asymmetric KMS key, and your peer's public key.
If the response includes the `CiphertextForRecipient` field, the `SharedSecret` field is null or empty.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_DeriveSharedSecret_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

 ** DisabledException **
The request was rejected because the specified KMS key is not enabled.
HTTP Status Code: 400

 ** DryRunOperationException **
 The request was rejected because the DryRun parameter was specified.
HTTP Status Code: 400

 ** InvalidGrantTokenException **
The request was rejected because the specified grant token is not valid.
HTTP Status Code: 400

 ** InvalidKeyUsageException **
The request was rejected for one of the following reasons:
+ The `KeyUsage` value of the KMS key is incompatible with the API operation.
+ The encryption algorithm or signing algorithm specified for the operation is incompatible with the type of key material in the KMS key `(KeySpec`).
For encrypting, decrypting, re-encrypting, and generating data keys, the `KeyUsage` must be `ENCRYPT_DECRYPT`. For signing and verifying messages, the `KeyUsage` must be `SIGN_VERIFY`. For generating and verifying message authentication codes (MACs), the `KeyUsage` must be `GENERATE_VERIFY_MAC`. For deriving key agreement secrets, the `KeyUsage` must be `KEY_AGREEMENT`. To find the `KeyUsage` of a KMS key, use the [DescribeKey](API_DescribeKey.md) operation.
To find the encryption or signing algorithms supported for a particular KMS key, use the [DescribeKey](API_DescribeKey.md) operation.
HTTP Status Code: 400

 ** KeyUnavailableException **
The request was rejected because the specified KMS key was not available. You can retry the request.
HTTP Status Code: 500

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

 ** KMSInvalidStateException **
The request was rejected because the state of the specified resource is not valid for this request.
This exceptions means one of the following:
+ The key state of the KMS key is not compatible with the operation.

  To find the key state, use the [DescribeKey](API_DescribeKey.md) operation. For more information about which key states are compatible with each AWS KMS operation, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * * AWS Key Management Service Developer Guide* *.
+ For cryptographic operations on KMS keys in custom key stores, this exception represents a general failure with many possible causes. To identify the cause, see the error message that accompanies the exception.
HTTP Status Code: 400

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

## Examples
<a name="API_DeriveSharedSecret_Examples"></a>

### Example Request
<a name="API_DeriveSharedSecret_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 48
X-Amz-Target: TrentService.DeriveSharedSecret
X-Amz-Date: 20161107T213532Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161107/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=2cea34fe55d5858295a377448a1e053d0edd45ce571da7cf69b202905759f272

{
    "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "PublicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvH3Yj0wbkLEpUl95Cv1cJVjsVNSjwGq3tCLnzXfhVwVvmzGN8pYj3U8nKwgouaHbBWNJYjP5VutbbkKS4Kv4GojwZBJyHN17kmxo8yTjRmjR15SKIQ8cqRA2uaERMLnpztIXdZp232PQPbWGxDyXYJ0aJ5EFSag+iSK341kr2kFTpINN7T1ZaX9vfXBdGR+VtkRKMWoHQeWzHrPZ+3irvpXNCKxGUxmPNsJSjPUhuSXT5+0VrY/LEYLQ5lUTrhU6z5/OK0kzaCc66DXc5ipSloS4Xyg+QcYSMxe9xuqO5HtzFImUSKBm1W6eDT6lHnSbpi7vXzNbIX7pWxKw9nmQvQIDAQAB",
    "KeyAgreementAlgorithm": "ECDH"
}
```

### Example Response
<a name="API_DeriveSharedSecret_Example_2"></a>

This example illustrates one usage of DeriveSharedSecret.

```
HTTP/1.1 200 OK
Server: Server
Date: Mon, 07 Nov 2016 21:35:35 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Connection: keep-alive
x-amzn-RequestId: 1e76aa81-a532-11e6-a265-d3aef78e1a90

{
   "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
   "KeyAgreementAlgorithm": "ECDH",
   "SharedSecret": "MEYCIQCKZLWyTk5runarx6XiAkU9gv3lbwPO/pHa+DXFehzdDwIhANwpsIV2g/9SPWLLsF6p/hiSskuIXMTRwqrMdVKWTMHG"
}
```

## See Also
<a name="API_DeriveSharedSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/DeriveSharedSecret)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/DeriveSharedSecret)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/DeriveSharedSecret)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/DeriveSharedSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/DeriveSharedSecret)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/DeriveSharedSecret)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/DeriveSharedSecret)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/DeriveSharedSecret)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/DeriveSharedSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/DeriveSharedSecret)
