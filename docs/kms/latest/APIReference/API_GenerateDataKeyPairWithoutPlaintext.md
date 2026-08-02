---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPairWithoutPlaintext.html
---

# GenerateDataKeyPairWithoutPlaintext
<a name="API_GenerateDataKeyPairWithoutPlaintext"></a>

Returns a unique asymmetric data key pair for use outside of AWS KMS. This operation returns a plaintext public key and a copy of the private key that is encrypted under the symmetric encryption KMS key you specify. Unlike [GenerateDataKeyPair](API_GenerateDataKeyPair.md), this operation does not return a plaintext private key. The bytes in the keys are random; they are not related to the caller or to the KMS key that is used to encrypt the private key.

You can use the public key that `GenerateDataKeyPairWithoutPlaintext` returns to encrypt data or verify a signature outside of AWS KMS. Then, store the encrypted private key with the data. When you are ready to decrypt data or sign a message, you can use the [Decrypt](API_Decrypt.md) operation to decrypt the encrypted private key.

To generate a data key pair, you must specify a symmetric encryption KMS key to encrypt the private key in a data key pair. You cannot use an asymmetric KMS key or a KMS key in a custom key store. To get the type and origin of your KMS key, use the [DescribeKey](API_DescribeKey.md) operation.

Use the `KeyPairSpec` parameter to choose an RSA or Elliptic Curve (ECC) data key pair. In China Regions, you can also choose an SM2 data key pair. AWS KMS recommends that you use ECC key pairs for signing, and use RSA and SM2 key pairs for either encryption or signing, but not both. However, AWS KMS cannot enforce any restrictions on the use of data key pairs outside of AWS KMS.

 `GenerateDataKeyPairWithoutPlaintext` returns a unique data key pair for each request. The bytes in the key are not related to the caller or KMS key that is used to encrypt the private key. The public key is a DER-encoded X.509 SubjectPublicKeyInfo, as specified in [RFC 5280](https://tools.ietf.org/html/rfc5280).

You can use an optional encryption context to add additional security to the encryption operation. If you specify an `EncryptionContext`, you must specify the same encryption context (a case-sensitive exact match) when decrypting the encrypted data key. Otherwise, the request to decrypt fails with an `InvalidCiphertextException`. For more information, see [Encryption Context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) in the * AWS Key Management Service Developer Guide*.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: Yes. To perform this operation with a KMS key in a different AWS account, specify the key ARN or alias ARN in the value of the `KeyId` parameter.

 **Required permissions**: [kms:GenerateDataKeyPairWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [Decrypt](API_Decrypt.md)
+  [Encrypt](API_Encrypt.md)
+  [GenerateDataKey](API_GenerateDataKey.md)
+  [GenerateDataKeyPair](API_GenerateDataKeyPair.md)
+  [GenerateDataKeyWithoutPlaintext](API_GenerateDataKeyWithoutPlaintext.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_GenerateDataKeyPairWithoutPlaintext_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "EncryptionContext": {
      "{{string}}" : "{{string}}"
   },
   "GrantTokens": [ "{{string}}" ],
   "KeyId": "{{string}}",
   "KeyPairSpec": "{{string}}"
}
```

## Request Parameters
<a name="API_GenerateDataKeyPairWithoutPlaintext_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_GenerateDataKeyPairWithoutPlaintext_RequestSyntax) **   <a name="KMS-GenerateDataKeyPairWithoutPlaintext-request-KeyId"></a>
Specifies the symmetric encryption KMS key that encrypts the private key in the data key pair. You cannot specify an asymmetric KMS key or a KMS key in a custom key store. To get the type and origin of your KMS key, use the [DescribeKey](API_DescribeKey.md) operation.
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

 ** [KeyPairSpec](#API_GenerateDataKeyPairWithoutPlaintext_RequestSyntax) **   <a name="KMS-GenerateDataKeyPairWithoutPlaintext-request-KeyPairSpec"></a>
Determines the type of data key pair that is generated.
The AWS KMS rule that restricts the use of asymmetric RSA and SM2 KMS keys to encrypt and decrypt or to sign and verify (but not both), the rule that permits you to use ECC KMS keys only to sign and verify, and the rule that permits you to use ML-DSA key pairs to sign and verify only are not effective on data key pairs, which are used outside of AWS KMS. The SM2 key spec is only available in China Regions.
Type: String
Valid Values: `RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SM2 | ECC_NIST_EDWARDS25519`
Required: Yes

 ** [DryRun](#API_GenerateDataKeyPairWithoutPlaintext_RequestSyntax) **   <a name="KMS-GenerateDataKeyPairWithoutPlaintext-request-DryRun"></a>
Checks if your request will succeed. `DryRun` is an optional parameter.
To learn more about how to use this parameter, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the * AWS Key Management Service Developer Guide*.
Type: Boolean
Required: No

 ** [EncryptionContext](#API_GenerateDataKeyPairWithoutPlaintext_RequestSyntax) **   <a name="KMS-GenerateDataKeyPairWithoutPlaintext-request-EncryptionContext"></a>
Specifies the encryption context that will be used when encrypting the private key in the data key pair.
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.
An *encryption context* is a collection of non-secret key-value pairs that represent additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is supported only on operations with symmetric encryption KMS keys. On operations with symmetric encryption KMS keys, an encryption context is optional, but it is strongly recommended.
For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) in the * AWS Key Management Service Developer Guide*.
Type: String to string map
Required: No

 ** [GrantTokens](#API_GenerateDataKeyPairWithoutPlaintext_RequestSyntax) **   <a name="KMS-GenerateDataKeyPairWithoutPlaintext-request-GrantTokens"></a>
A list of grant tokens.
Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency*. For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html) in the * AWS Key Management Service Developer Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

## Response Syntax
<a name="API_GenerateDataKeyPairWithoutPlaintext_ResponseSyntax"></a>

```
{
   "KeyId": "string",
   "KeyMaterialId": "string",
   "KeyPairSpec": "string",
   "PrivateKeyCiphertextBlob": blob,
   "PublicKey": blob
}
```

## Response Elements
<a name="API_GenerateDataKeyPairWithoutPlaintext_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyId](#API_GenerateDataKeyPairWithoutPlaintext_ResponseSyntax) **   <a name="KMS-GenerateDataKeyPairWithoutPlaintext-response-KeyId"></a>
The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN)) of the KMS key that encrypted the private key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [KeyMaterialId](#API_GenerateDataKeyPairWithoutPlaintext_ResponseSyntax) **   <a name="KMS-GenerateDataKeyPairWithoutPlaintext-response-KeyMaterialId"></a>
The identifier of the key material used to encrypt the private key.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `^[a-f0-9]+$`

 ** [KeyPairSpec](#API_GenerateDataKeyPairWithoutPlaintext_ResponseSyntax) **   <a name="KMS-GenerateDataKeyPairWithoutPlaintext-response-KeyPairSpec"></a>
The type of data key pair that was generated.
Type: String
Valid Values: `RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SM2 | ECC_NIST_EDWARDS25519`

 ** [PrivateKeyCiphertextBlob](#API_GenerateDataKeyPairWithoutPlaintext_ResponseSyntax) **   <a name="KMS-GenerateDataKeyPairWithoutPlaintext-response-PrivateKeyCiphertextBlob"></a>
The encrypted copy of the private key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [PublicKey](#API_GenerateDataKeyPairWithoutPlaintext_ResponseSyntax) **   <a name="KMS-GenerateDataKeyPairWithoutPlaintext-response-PublicKey"></a>
The public key (in plaintext). When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_GenerateDataKeyPairWithoutPlaintext_Errors"></a>

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

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_GenerateDataKeyPairWithoutPlaintext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/GenerateDataKeyPairWithoutPlaintext)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/GenerateDataKeyPairWithoutPlaintext)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/GenerateDataKeyPairWithoutPlaintext)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/GenerateDataKeyPairWithoutPlaintext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/GenerateDataKeyPairWithoutPlaintext)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/GenerateDataKeyPairWithoutPlaintext)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/GenerateDataKeyPairWithoutPlaintext)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/GenerateDataKeyPairWithoutPlaintext)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/GenerateDataKeyPairWithoutPlaintext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/GenerateDataKeyPairWithoutPlaintext)
