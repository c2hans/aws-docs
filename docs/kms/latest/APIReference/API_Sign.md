---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html
---

# Sign
<a name="API_Sign"></a>

Creates a [digital signature](https://en.wikipedia.org/wiki/Digital_signature) for a message or message digest by using the private key in an asymmetric signing KMS key. To verify the signature, use the [Verify](API_Verify.md) operation, or use the public key in the same asymmetric KMS key outside of AWS KMS. For information about asymmetric KMS keys, see [Asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the * AWS Key Management Service Developer Guide*.

Digital signatures are generated and verified by using asymmetric key pair, such as an RSA, ECC, or ML-DSA pair that is represented by an asymmetric KMS key. The key owner (or an authorized user) uses their private key to sign a message. Anyone with the public key can verify that the message was signed with that particular private key and that the message hasn't changed since it was signed.

To use the `Sign` operation, provide the following information:
+ Use the `KeyId` parameter to identify an asymmetric KMS key with a `KeyUsage` value of `SIGN_VERIFY`. To get the `KeyUsage` value of a KMS key, use the [DescribeKey](API_DescribeKey.md) operation. The caller must have `kms:Sign` permission on the KMS key.
+ Use the `Message` parameter to specify the message or message digest to sign. You can submit messages of up to 4096 bytes. To sign a larger message, generate a hash digest of the message, and then provide the hash digest in the `Message` parameter. To indicate whether the message is a full message, a digest, or an ML-DSA EXTERNAL\_MU, use the `MessageType` parameter.
+ Choose a signing algorithm that is compatible with the KMS key.

**Important**
When signing a message, be sure to record the KMS key and the signing algorithm. This information is required to verify the signature.

**Note**
Best practices recommend that you limit the time during which any signature is effective. This deters an attack where the actor uses a signed message to establish validity repeatedly or long after the message is superseded. Signatures do not include a timestamp, but you can include a timestamp in the signed message to help you detect when its time to refresh the signature.

To verify the signature that this operation generates, use the [Verify](API_Verify.md) operation. Or use the [GetPublicKey](API_GetPublicKey.md) operation to download the public key and then use the public key to verify the signature outside of AWS KMS.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: Yes. To perform this operation with a KMS key in a different AWS account, specify the key ARN or alias ARN in the value of the `KeyId` parameter.

 **Required permissions**: [kms:Sign](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations**: [Verify](API_Verify.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_Sign_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "GrantTokens": [ "{{string}}" ],
   "KeyId": "{{string}}",
   "Message": {{blob}},
   "MessageType": "{{string}}",
   "SigningAlgorithm": "{{string}}"
}
```

## Request Parameters
<a name="API_Sign_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_Sign_RequestSyntax) **   <a name="KMS-Sign-request-KeyId"></a>
Identifies an asymmetric KMS key. AWS KMS uses the private key in the asymmetric KMS key to sign the message. The `KeyUsage` type of the KMS key must be `SIGN_VERIFY`. To find the `KeyUsage` of a KMS key, use the [DescribeKey](API_DescribeKey.md) operation.
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

 ** [Message](#API_Sign_RequestSyntax) **   <a name="KMS-Sign-request-Message"></a>
Specifies the message or message digest to sign. Messages can be 0-4096 bytes. To sign a larger message, provide a message digest.
If you provide a message digest, use the `DIGEST` value of `MessageType` to prevent the digest from being hashed again while signing.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** [SigningAlgorithm](#API_Sign_RequestSyntax) **   <a name="KMS-Sign-request-SigningAlgorithm"></a>
Specifies the signing algorithm to use when signing the message.
Choose an algorithm that is compatible with the type and size of the specified asymmetric KMS key. When signing with RSA key pairs, RSASSA-PSS algorithms are preferred. We include RSASSA-PKCS1-v1\_5 algorithms for compatibility with existing applications.
Type: String
Valid Values: `RSASSA_PSS_SHA_256 | RSASSA_PSS_SHA_384 | RSASSA_PSS_SHA_512 | RSASSA_PKCS1_V1_5_SHA_256 | RSASSA_PKCS1_V1_5_SHA_384 | RSASSA_PKCS1_V1_5_SHA_512 | ECDSA_SHA_256 | ECDSA_SHA_384 | ECDSA_SHA_512 | SM2DSA | ML_DSA_SHAKE_256 | ED25519_SHA_512 | ED25519_PH_SHA_512`
Required: Yes

 ** [DryRun](#API_Sign_RequestSyntax) **   <a name="KMS-Sign-request-DryRun"></a>
Checks if your request will succeed. `DryRun` is an optional parameter.
To learn more about how to use this parameter, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the * AWS Key Management Service Developer Guide*.
Type: Boolean
Required: No

 ** [GrantTokens](#API_Sign_RequestSyntax) **   <a name="KMS-Sign-request-GrantTokens"></a>
A list of grant tokens.
Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency*. For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html) in the * AWS Key Management Service Developer Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [MessageType](#API_Sign_RequestSyntax) **   <a name="KMS-Sign-request-MessageType"></a>
Tells AWS KMS whether the value of the `Message` parameter should be hashed as part of the signing algorithm. Use `RAW` for unhashed messages; use `DIGEST` for message digests, which are already hashed; use `EXTERNAL_MU` for 64-byte representative μ used in ML-DSA signing as defined in NIST FIPS 204 Section 6.2.
When the value of `MessageType` is `RAW`, AWS KMS uses the standard signing algorithm, which begins with a hash function. When the value is `DIGEST`, AWS KMS skips the hashing step in the signing algorithm. When the value is `EXTERNAL_MU` AWS KMS skips the concatenated hashing of the public key hash and the message done in the ML-DSA signing algorithm.
Use the `DIGEST` or `EXTERNAL_MU` value only when the value of the `Message` parameter is a message digest. If you use the `DIGEST` value with an unhashed message, the security of the signing operation can be compromised.
When using ECC\_NIST\_EDWARDS25519 KMS keys:
+ ED25519\_SHA\_512 signing algorithm requires AWS KMS `MessageType:RAW`
+ ED25519\_PH\_SHA\_512 signing algorithm requires AWS KMS `MessageType:DIGEST`
When you specify the ED25519\_PH\_SHA\_512 signing algorithm with `MessageType:DIGEST`, AWS KMS still performs the SHA-512 prehash described in [Step 1 of Section 7.8.1 in FIPS 186-5](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf#page=39). This means the input is hashed twice: once by you and once by KMS.
When the value of `MessageType` is `DIGEST`, the length of the `Message` value must match the length of hashed messages for the specified signing algorithm.
When the value of `MessageType` is `EXTERNAL_MU` the length of the `Message` value must be 64 bytes.
You can submit a message digest and omit the `MessageType` or specify `RAW` so the digest is hashed again while signing. However, this can cause verification failures when verifying with a system that assumes a single hash.
The hashing algorithm that `Sign` uses is based on the `SigningAlgorithm` value.
+ Signing algorithms that end in SHA\_256 use the SHA\_256 hashing algorithm.
+ Signing algorithms that end in SHA\_384 use the SHA\_384 hashing algorithm.
+ Signing algorithms that end in SHA\_512 use the SHA\_512 hashing algorithm.
+ Signing algorithms that end in SHAKE\_256 use the SHAKE\_256 hashing algorithm.
+ SM2DSA uses the SM3 hashing algorithm. For details, see [Offline verification with SM2 key pairs](https://docs.aws.amazon.com/kms/latest/developerguide/offline-operations.html#key-spec-sm-offline-verification).
Type: String
Valid Values: `RAW | DIGEST | EXTERNAL_MU`
Required: No

## Response Syntax
<a name="API_Sign_ResponseSyntax"></a>

```
{
   "KeyId": "string",
   "Signature": blob,
   "SigningAlgorithm": "string"
}
```

## Response Elements
<a name="API_Sign_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyId](#API_Sign_ResponseSyntax) **   <a name="KMS-Sign-response-KeyId"></a>
The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN)) of the asymmetric KMS key that was used to sign the message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Signature](#API_Sign_ResponseSyntax) **   <a name="KMS-Sign-response-Signature"></a>
The cryptographic signature that was generated for the message.
+ When used with the supported RSA signing algorithms, the encoding of this value is defined by [PKCS \#1 in RFC 8017](https://tools.ietf.org/html/rfc8017).
+ When used with the `ECDSA_SHA_256`, `ECDSA_SHA_384`, or `ECDSA_SHA_512` signing algorithms, this value is a DER-encoded object as defined by ANSI X9.62–2005 and [RFC 3279 Section 2.2.3](https://tools.ietf.org/html/rfc3279#section-2.2.3). This is the most commonly used signature format and is appropriate for most uses.
When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [SigningAlgorithm](#API_Sign_ResponseSyntax) **   <a name="KMS-Sign-response-SigningAlgorithm"></a>
The signing algorithm that was used to sign the message.
Type: String
Valid Values: `RSASSA_PSS_SHA_256 | RSASSA_PSS_SHA_384 | RSASSA_PSS_SHA_512 | RSASSA_PKCS1_V1_5_SHA_256 | RSASSA_PKCS1_V1_5_SHA_384 | RSASSA_PKCS1_V1_5_SHA_512 | ECDSA_SHA_256 | ECDSA_SHA_384 | ECDSA_SHA_512 | SM2DSA | ML_DSA_SHAKE_256 | ED25519_SHA_512 | ED25519_PH_SHA_512`

## Errors
<a name="API_Sign_Errors"></a>

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

## See Also
<a name="API_Sign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/Sign)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/Sign)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/Sign)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/Sign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/Sign)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/Sign)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/Sign)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/Sign)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/Sign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/Sign)
