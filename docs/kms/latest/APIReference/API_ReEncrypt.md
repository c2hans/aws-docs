---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html
---

# ReEncrypt
<a name="API_ReEncrypt"></a>

Decrypts ciphertext and then reencrypts it entirely within AWS KMS. You can use this operation to change the KMS key under which data is encrypted, such as when you [manually rotate](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys-manually.html) a KMS key or change the KMS key that protects a ciphertext. You can also use it to reencrypt ciphertext under the same KMS key, such as to change the [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) of a ciphertext.

The `ReEncrypt` operation can decrypt ciphertext that was encrypted by using a KMS key in an AWS KMS operation, such as [Encrypt](API_Encrypt.md) or [GenerateDataKey](API_GenerateDataKey.md). It can also decrypt ciphertext that was encrypted by using the public key of an [asymmetric KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) outside of AWS KMS. However, it cannot decrypt ciphertext produced by other libraries, such as the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/) or [Amazon S3 client-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html). These libraries return a ciphertext format that is incompatible with AWS KMS.

When you use the `ReEncrypt` operation, you need to provide information for the decrypt operation and the subsequent encrypt operation.
+ If your ciphertext was encrypted under an asymmetric KMS key, you must use the `SourceKeyId` parameter to identify the KMS key that encrypted the ciphertext. You must also supply the encryption algorithm that was used. This information is required to decrypt the data.
+ If your ciphertext was encrypted under a symmetric encryption KMS key, the `SourceKeyId` parameter is optional. AWS KMS can get this information from metadata that it adds to the symmetric ciphertext blob. This feature adds durability to your implementation by ensuring that authorized users can decrypt ciphertext decades after it was encrypted, even if they've lost track of the key ID. However, specifying the source KMS key is always recommended as a best practice. When you use the `SourceKeyId` parameter to specify a KMS key, AWS KMS uses only the KMS key you specify. If the ciphertext was encrypted under a different KMS key, the `ReEncrypt` operation fails. This practice ensures that you use the KMS key that you intend.
+ To reencrypt the data, you must use the `DestinationKeyId` parameter to specify the KMS key that re-encrypts the data after it is decrypted. If the destination KMS key is an asymmetric KMS key, you must also provide the encryption algorithm. The algorithm that you choose must be compatible with the KMS key.
**Important**
When you use an asymmetric KMS key to encrypt or reencrypt data, be sure to record the KMS key and encryption algorithm that you choose. You will be required to provide the same KMS key and encryption algorithm when you decrypt the data. If the KMS key and algorithm do not match the values used to encrypt the data, the decrypt operation fails.
You are not required to supply the key ID and encryption algorithm when you decrypt with symmetric encryption KMS keys because AWS KMS stores this information in the ciphertext blob. AWS KMS cannot store metadata in ciphertext generated with asymmetric keys. The standard format for asymmetric key ciphertext does not include configurable fields.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

**Note**
When using grants with `SourceArn` constraints for `ReEncrypt` operations, the grants on both the source KMS key (for `ReEncryptFrom`) and the destination KMS key (for `ReEncryptTo`) must specify the same `SourceArn` value.

 **Cross-account use**: Yes. The source KMS key and destination KMS key can be in different AWS accounts. Either or both KMS keys can be in a different account than the caller. To specify a KMS key in a different account, use the [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) or [alias ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-alias-ARN). A short [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) is also acceptable for the source key when decrypting symmetric ciphertexts, though using a full key ARN is recommended to be more explicit about the intended KMS key.

 **Required permissions**:
+  [kms:ReEncryptFrom](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) permission on the source KMS key (key policy)
+  [kms:ReEncryptTo](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) permission on the destination KMS key (key policy)

To permit reencryption from or to a KMS key, include the `"kms:ReEncrypt*"` permission in your [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html). This permission is automatically included in the key policy when you use the console to create a KMS key. But you must include it manually when you create a KMS key programmatically or when you use the [PutKeyPolicy](API_PutKeyPolicy.md) operation to set a key policy.

 **Related operations:**
+  [Decrypt](API_Decrypt.md)
+  [Encrypt](API_Encrypt.md)
+  [GenerateDataKey](API_GenerateDataKey.md)
+  [GenerateDataKeyPair](API_GenerateDataKeyPair.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_ReEncrypt_RequestSyntax"></a>

```
{
   "CiphertextBlob": {{blob}},
   "DestinationEncryptionAlgorithm": "{{string}}",
   "DestinationEncryptionContext": {
      "{{string}}" : "{{string}}"
   },
   "DestinationKeyId": "{{string}}",
   "DryRun": {{boolean}},
   "DryRunModifiers": [ "{{string}}" ],
   "GrantTokens": [ "{{string}}" ],
   "SourceEncryptionAlgorithm": "{{string}}",
   "SourceEncryptionContext": {
      "{{string}}" : "{{string}}"
   },
   "SourceKeyId": "{{string}}"
}
```

## Request Parameters
<a name="API_ReEncrypt_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [DestinationKeyId](#API_ReEncrypt_RequestSyntax) **   <a name="KMS-ReEncrypt-request-DestinationKeyId"></a>
A unique identifier for the KMS key that is used to reencrypt the data. Specify a symmetric encryption KMS key or an asymmetric KMS key with a `KeyUsage` value of `ENCRYPT_DECRYPT`. To find the `KeyUsage` value of a KMS key, use the [DescribeKey](API_DescribeKey.md) operation.
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

 ** [CiphertextBlob](#API_ReEncrypt_RequestSyntax) **   <a name="KMS-ReEncrypt-request-CiphertextBlob"></a>
Ciphertext of the data to reencrypt.
This parameter is required in all cases except when `DryRun` is `true` and `DryRunModifiers` is set to `IGNORE_CIPHERTEXT`.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6144.
Required: No

 ** [DestinationEncryptionAlgorithm](#API_ReEncrypt_RequestSyntax) **   <a name="KMS-ReEncrypt-request-DestinationEncryptionAlgorithm"></a>
Specifies the encryption algorithm that AWS KMS will use to reecrypt the data after it has decrypted it. The default value, `SYMMETRIC_DEFAULT`, represents the encryption algorithm used for symmetric encryption KMS keys.
This parameter is required only when the destination KMS key is an asymmetric KMS key.
Type: String
Valid Values: `SYMMETRIC_DEFAULT | RSAES_OAEP_SHA_1 | RSAES_OAEP_SHA_256 | SM2PKE`
Required: No

 ** [DestinationEncryptionContext](#API_ReEncrypt_RequestSyntax) **   <a name="KMS-ReEncrypt-request-DestinationEncryptionContext"></a>
Specifies that encryption context to use when the reencrypting the data.
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.
A destination encryption context is valid only when the destination KMS key is a symmetric encryption KMS key. The standard ciphertext format for asymmetric KMS keys does not include fields for metadata.
An *encryption context* is a collection of non-secret key-value pairs that represent additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is supported only on operations with symmetric encryption KMS keys. On operations with symmetric encryption KMS keys, an encryption context is optional, but it is strongly recommended.
For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) in the * AWS Key Management Service Developer Guide*.
Type: String to string map
Required: No

 ** [DryRun](#API_ReEncrypt_RequestSyntax) **   <a name="KMS-ReEncrypt-request-DryRun"></a>
Checks if your request will succeed. `DryRun` is an optional parameter.
To learn more about how to use this parameter, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the * AWS Key Management Service Developer Guide*.
Type: Boolean
Required: No

 ** [DryRunModifiers](#API_ReEncrypt_RequestSyntax) **   <a name="KMS-ReEncrypt-request-DryRunModifiers"></a>
Specifies the modifiers to apply to the dry run operation. `DryRunModifiers` is an optional parameter that only applies when `DryRun` is set to `true`.
When set to `IGNORE_CIPHERTEXT`, AWS KMS performs only authorization validation without ciphertext validation. This allows you to test permissions without requiring a valid ciphertext blob.
To learn more about how to use this parameter, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the * AWS Key Management Service Developer Guide*.
Type: Array of strings
Valid Values: `IGNORE_CIPHERTEXT`
Required: No

 ** [GrantTokens](#API_ReEncrypt_RequestSyntax) **   <a name="KMS-ReEncrypt-request-GrantTokens"></a>
A list of grant tokens.
Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency*. For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html) in the * AWS Key Management Service Developer Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [SourceEncryptionAlgorithm](#API_ReEncrypt_RequestSyntax) **   <a name="KMS-ReEncrypt-request-SourceEncryptionAlgorithm"></a>
Specifies the encryption algorithm that AWS KMS will use to decrypt the ciphertext before it is reencrypted. The default value, `SYMMETRIC_DEFAULT`, represents the algorithm used for symmetric encryption KMS keys.
Specify the same algorithm that was used to encrypt the ciphertext. If you specify a different algorithm, the decrypt attempt fails.
This parameter is required only when the ciphertext was encrypted under an asymmetric KMS key.
Type: String
Valid Values: `SYMMETRIC_DEFAULT | RSAES_OAEP_SHA_1 | RSAES_OAEP_SHA_256 | SM2PKE`
Required: No

 ** [SourceEncryptionContext](#API_ReEncrypt_RequestSyntax) **   <a name="KMS-ReEncrypt-request-SourceEncryptionContext"></a>
Specifies the encryption context to use to decrypt the ciphertext. Enter the same encryption context that was used to encrypt the ciphertext.
An *encryption context* is a collection of non-secret key-value pairs that represent additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is supported only on operations with symmetric encryption KMS keys. On operations with symmetric encryption KMS keys, an encryption context is optional, but it is strongly recommended.
For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) in the * AWS Key Management Service Developer Guide*.
Type: String to string map
Required: No

 ** [SourceKeyId](#API_ReEncrypt_RequestSyntax) **   <a name="KMS-ReEncrypt-request-SourceKeyId"></a>
Specifies the KMS key that AWS KMS will use to decrypt the ciphertext before it is re-encrypted.
Enter a key ID of the KMS key that was used to encrypt the ciphertext. If you identify a different KMS key, the `ReEncrypt` operation throws an `IncorrectKeyException`.
This parameter is required only when the ciphertext was encrypted under an asymmetric KMS key or when `DryRun` is `true` and `DryRunModifiers` is set to `IGNORE_CIPHERTEXT`. If you used a symmetric encryption KMS key, AWS KMS can get the KMS key from metadata that it adds to the symmetric ciphertext blob. However, it is always recommended as a best practice. This practice ensures that you use the KMS key that you intend.
To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with `"alias/"`. To specify a KMS key in a different AWS account, you should use the key ARN or alias ARN.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
+ Alias name: `alias/ExampleAlias`
+ Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md). To get the alias name and alias ARN, use [ListAliases](API_ListAliases.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ReEncrypt_ResponseSyntax"></a>

```
{
   "CiphertextBlob": blob,
   "DestinationEncryptionAlgorithm": "string",
   "DestinationKeyMaterialId": "string",
   "KeyId": "string",
   "SourceEncryptionAlgorithm": "string",
   "SourceKeyId": "string",
   "SourceKeyMaterialId": "string"
}
```

## Response Elements
<a name="API_ReEncrypt_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CiphertextBlob](#API_ReEncrypt_ResponseSyntax) **   <a name="KMS-ReEncrypt-response-CiphertextBlob"></a>
The reencrypted data. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [DestinationEncryptionAlgorithm](#API_ReEncrypt_ResponseSyntax) **   <a name="KMS-ReEncrypt-response-DestinationEncryptionAlgorithm"></a>
The encryption algorithm that was used to reencrypt the data.
Type: String
Valid Values: `SYMMETRIC_DEFAULT | RSAES_OAEP_SHA_1 | RSAES_OAEP_SHA_256 | SM2PKE`

 ** [DestinationKeyMaterialId](#API_ReEncrypt_ResponseSyntax) **   <a name="KMS-ReEncrypt-response-DestinationKeyMaterialId"></a>
The identifier of the key material used to reencrypt the data. This field is present only when data is reencrypted using a symmetric encryption KMS key.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `^[a-f0-9]+$`

 ** [KeyId](#API_ReEncrypt_ResponseSyntax) **   <a name="KMS-ReEncrypt-response-KeyId"></a>
The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN)) of the KMS key that was used to reencrypt the data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [SourceEncryptionAlgorithm](#API_ReEncrypt_ResponseSyntax) **   <a name="KMS-ReEncrypt-response-SourceEncryptionAlgorithm"></a>
The encryption algorithm that was used to decrypt the ciphertext before it was reencrypted.
Type: String
Valid Values: `SYMMETRIC_DEFAULT | RSAES_OAEP_SHA_1 | RSAES_OAEP_SHA_256 | SM2PKE`

 ** [SourceKeyId](#API_ReEncrypt_ResponseSyntax) **   <a name="KMS-ReEncrypt-response-SourceKeyId"></a>
Unique identifier of the KMS key used to originally encrypt the data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [SourceKeyMaterialId](#API_ReEncrypt_ResponseSyntax) **   <a name="KMS-ReEncrypt-response-SourceKeyMaterialId"></a>
The identifier of the key material used to originally encrypt the data. This field is present only when the original encryption used a symmetric encryption KMS key.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `^[a-f0-9]+$`

## Errors
<a name="API_ReEncrypt_Errors"></a>

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

 ** IncorrectKeyException **
The request was rejected because the specified KMS key cannot decrypt the data. The `KeyId` in a [Decrypt](API_Decrypt.md) request and the `SourceKeyId` in a [ReEncrypt](#API_ReEncrypt) request must identify the same KMS key that was used to encrypt the ciphertext.
HTTP Status Code: 400

 ** InvalidCiphertextException **
From the [Decrypt](API_Decrypt.md) or [ReEncrypt](#API_ReEncrypt) operation, the request was rejected because the specified ciphertext, or additional authenticated data incorporated into the ciphertext, such as the encryption context, is corrupted, missing, or otherwise invalid.
From the [ImportKeyMaterial](API_ImportKeyMaterial.md) operation, the request was rejected because AWS KMS could not decrypt the encrypted (wrapped) key material.
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
<a name="API_ReEncrypt_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_ReEncrypt_Example_1"></a>

This example illustrates one usage of ReEncrypt.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 306
X-Amz-Target: TrentService.ReEncrypt
X-Amz-Date: 20161207T225816Z
Content-Type: application/x-amz-json-1.1* ReEncrypt
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161207/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=7afd339e2a680e0726592ddf687aabe48e1d8a7933a60ebbdc0154b8e2936ef2

{
  "SourceKeyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
  "DestinationKeyId": "0987dcba-09fe-87dc-65ba-ab0987654321",
  "CiphertextBlob": "AQECAHj/M9MyvNsMT8kW+K5DVkMfunTHr0w6V6crnuAGw80uRwAAAH0wewYJKoZIhvcNAQcGoG4wbAIBADBnBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDPXExREUtnnGy1wC3wIBEIA6LvpU7BRMW+FSkUmNmmE0H0aHHRYRD6XqUnaCNnzAuhhq4VTGBfii6oWtjVU83pGmradvUawxE/tbCg=="
}
```

### Example Response
<a name="API_ReEncrypt_Example_2"></a>

This example illustrates one usage of ReEncrypt.

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 07 Dec 2016 22:58:17 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 423
Connection: keep-alive
x-amzn-RequestId: a434eca2-bcd0-11e6-b60b-ffb5eb2d1d15

{
  "CiphertextBlob": "AQECAHjRYf5WytIc0C857tFSnBaPn2F8DgfmThbJlGfR8P3WlwAAAH0wewYJKoZIhvcNAQcGoG4wbAIBADBnBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDIwicafp/vwjXjPBhQIBEIA6wjfzufQPhuU+nVqa3Kj4nqSTdhDw1PTkImKCUEuvQDui6qsooyB4Qxe8OOBqciRNC7ENQN8lKaEijg==",
  "KeyId": "arn:aws:kms:us-east-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321",
  "SourceKeyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
  "SourceEncryptionAlgorithm": "SYMMETRIC_DEFAULT",
  "SourceKeyMaterialId": "0b7fd7ddbac6eef27907413567cad8c810e2883dc8a7534067a82ee1142fc1e6",
  "DestinationEncryptionAlgorithm": "SYMMETRIC_DEFAULT",
  "DestinationKeyMaterialId": "2067e8b4da7b0d8ffa80ff7afb5ea4637e103c98c3c110bdb84cc0a9de75e733"
}
```

## See Also
<a name="API_ReEncrypt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/ReEncrypt)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/ReEncrypt)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/ReEncrypt)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/ReEncrypt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/ReEncrypt)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/ReEncrypt)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/ReEncrypt)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/ReEncrypt)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/ReEncrypt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/ReEncrypt)
