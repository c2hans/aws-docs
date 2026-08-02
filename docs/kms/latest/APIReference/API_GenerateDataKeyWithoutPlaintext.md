---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html
---

# GenerateDataKeyWithoutPlaintext
<a name="API_GenerateDataKeyWithoutPlaintext"></a>

Returns a unique symmetric data key for use outside of AWS KMS. This operation returns a data key that is encrypted under a symmetric encryption KMS key that you specify. The bytes in the key are random; they are not related to the caller or to the KMS key.

 `GenerateDataKeyWithoutPlaintext` is identical to the [GenerateDataKey](API_GenerateDataKey.md) operation except that it does not return a plaintext copy of the data key.

This operation is useful for systems that need to encrypt data at some point, but not immediately. When you need to encrypt the data, you call the [Decrypt](API_Decrypt.md) operation on the encrypted copy of the key.

It's also useful in distributed systems with different levels of trust. For example, you might store encrypted data in containers. One component of your system creates new containers and stores an encrypted data key with each container. Then, a different component puts the data into the containers. That component first decrypts the data key, uses the plaintext data key to encrypt data, puts the encrypted data into the container, and then destroys the plaintext data key. In this system, the component that creates the containers never sees the plaintext data key.

To request an asymmetric data key pair, use the [GenerateDataKeyPair](API_GenerateDataKeyPair.md) or [GenerateDataKeyPairWithoutPlaintext](API_GenerateDataKeyPairWithoutPlaintext.md) operations.

To generate a data key, you must specify the symmetric encryption KMS key that is used to encrypt the data key. You cannot use an asymmetric KMS key or a key in a custom key store to generate a data key. To get the type of your KMS key, use the [DescribeKey](API_DescribeKey.md) operation.

You must also specify the length of the data key. Use either the `KeySpec` or `NumberOfBytes` parameters (but not both). For 128-bit and 256-bit data keys, use the `KeySpec` parameter.

To generate an SM4 data key (China Regions only), specify a `KeySpec` value of `AES_128` or `NumberOfBytes` value of `16`. The symmetric encryption key used in China Regions to encrypt your data key is an SM4 encryption key.

If the operation succeeds, you will find the encrypted copy of the data key in the `CiphertextBlob` field.

You can use an optional encryption context to add additional security to the encryption operation. If you specify an `EncryptionContext`, you must specify the same encryption context (a case-sensitive exact match) when decrypting the encrypted data key. Otherwise, the request to decrypt fails with an `InvalidCiphertextException`. For more information, see [Encryption Context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) in the * AWS Key Management Service Developer Guide*.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: Yes. To perform this operation with a KMS key in a different AWS account, specify the key ARN or alias ARN in the value of the `KeyId` parameter.

 **Required permissions**: [kms:GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [Decrypt](API_Decrypt.md)
+  [Encrypt](API_Encrypt.md)
+  [GenerateDataKey](API_GenerateDataKey.md)
+  [GenerateDataKeyPair](API_GenerateDataKeyPair.md)
+  [GenerateDataKeyPairWithoutPlaintext](API_GenerateDataKeyPairWithoutPlaintext.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_GenerateDataKeyWithoutPlaintext_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "EncryptionContext": {
      "{{string}}" : "{{string}}"
   },
   "GrantTokens": [ "{{string}}" ],
   "KeyId": "{{string}}",
   "KeySpec": "{{string}}",
   "NumberOfBytes": {{number}}
}
```

## Request Parameters
<a name="API_GenerateDataKeyWithoutPlaintext_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_GenerateDataKeyWithoutPlaintext_RequestSyntax) **   <a name="KMS-GenerateDataKeyWithoutPlaintext-request-KeyId"></a>
Specifies the symmetric encryption KMS key that encrypts the data key. You cannot specify an asymmetric KMS key or a KMS key in a custom key store. To get the type and origin of your KMS key, use the [DescribeKey](API_DescribeKey.md) operation.
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

 ** [DryRun](#API_GenerateDataKeyWithoutPlaintext_RequestSyntax) **   <a name="KMS-GenerateDataKeyWithoutPlaintext-request-DryRun"></a>
Checks if your request will succeed. `DryRun` is an optional parameter.
To learn more about how to use this parameter, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the * AWS Key Management Service Developer Guide*.
Type: Boolean
Required: No

 ** [EncryptionContext](#API_GenerateDataKeyWithoutPlaintext_RequestSyntax) **   <a name="KMS-GenerateDataKeyWithoutPlaintext-request-EncryptionContext"></a>
Specifies the encryption context that will be used when encrypting the data key.
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.
An *encryption context* is a collection of non-secret key-value pairs that represent additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is supported only on operations with symmetric encryption KMS keys. On operations with symmetric encryption KMS keys, an encryption context is optional, but it is strongly recommended.
For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) in the * AWS Key Management Service Developer Guide*.
Type: String to string map
Required: No

 ** [GrantTokens](#API_GenerateDataKeyWithoutPlaintext_RequestSyntax) **   <a name="KMS-GenerateDataKeyWithoutPlaintext-request-GrantTokens"></a>
A list of grant tokens.
Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency*. For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html) in the * AWS Key Management Service Developer Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [KeySpec](#API_GenerateDataKeyWithoutPlaintext_RequestSyntax) **   <a name="KMS-GenerateDataKeyWithoutPlaintext-request-KeySpec"></a>
The length of the data key. Use `AES_128` to generate a 128-bit symmetric key, or `AES_256` to generate a 256-bit symmetric key.
Type: String
Valid Values: `AES_256 | AES_128`
Required: No

 ** [NumberOfBytes](#API_GenerateDataKeyWithoutPlaintext_RequestSyntax) **   <a name="KMS-GenerateDataKeyWithoutPlaintext-request-NumberOfBytes"></a>
The length of the data key in bytes. For example, use the value 64 to generate a 512-bit data key (64 bytes is 512 bits). For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use the `KeySpec` field instead of this one.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

## Response Syntax
<a name="API_GenerateDataKeyWithoutPlaintext_ResponseSyntax"></a>

```
{
   "CiphertextBlob": blob,
   "KeyId": "string",
   "KeyMaterialId": "string"
}
```

## Response Elements
<a name="API_GenerateDataKeyWithoutPlaintext_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CiphertextBlob](#API_GenerateDataKeyWithoutPlaintext_ResponseSyntax) **   <a name="KMS-GenerateDataKeyWithoutPlaintext-response-CiphertextBlob"></a>
The encrypted data key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [KeyId](#API_GenerateDataKeyWithoutPlaintext_ResponseSyntax) **   <a name="KMS-GenerateDataKeyWithoutPlaintext-response-KeyId"></a>
The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN)) of the KMS key that encrypted the data key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [KeyMaterialId](#API_GenerateDataKeyWithoutPlaintext_ResponseSyntax) **   <a name="KMS-GenerateDataKeyWithoutPlaintext-response-KeyMaterialId"></a>
The identifier of the key material used to encrypt the data key.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `^[a-f0-9]+$`

## Errors
<a name="API_GenerateDataKeyWithoutPlaintext_Errors"></a>

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
<a name="API_GenerateDataKeyWithoutPlaintext_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_GenerateDataKeyWithoutPlaintext_Example_1"></a>

This example illustrates one usage of GenerateDataKeyWithoutPlaintext.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 50
X-Amz-Target: TrentService.GenerateDataKeyWithoutPlaintext
X-Amz-Date: 20161112T001941Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161112/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=c86e7fc0218461e537c0d06ac29d865d94dba6fbfad00a844f61200e651df483

{
  "KeyId": "alias/ExampleAlias",
  "KeySpec": "AES_256"
}
```

### Example Response
<a name="API_GenerateDataKeyWithoutPlaintext_Example_2"></a>

This example illustrates one usage of GenerateDataKeyWithoutPlaintext.

```
HTTP/1.1 200 OK
Server: Server
Date: Sat, 12 Nov 2016 00:19:41 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 331
Connection: keep-alive
x-amzn-RequestId: b4ca7ee7-a86d-11e6-8a4e-2f341b963ed6

{
  "CiphertextBlob": "AQEDAHjRYf5WytIc0C857tFSnBaPn2F8DgfmThbJlGfR8P3WlwAAAH4wfAYJKoZIhvcNAQcGoG8wbQIBADBoBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDEvihQE/ntdQTL16wQIBEIA7BE/3LB7F1meU8z4e1vEKBGZgXPwMvkZXbKnf3wxCD9lB4hU29lii4euOqxp8pESb+7oCN9f1R75ac3s=",
  "KeyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
  "KeyMaterialId": "0b7fd7ddbac6eef27907413567cad8c810e2883dc8a7534067a82ee1142fc1e6",
}
```

## See Also
<a name="API_GenerateDataKeyWithoutPlaintext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/GenerateDataKeyWithoutPlaintext)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/GenerateDataKeyWithoutPlaintext)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/GenerateDataKeyWithoutPlaintext)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/GenerateDataKeyWithoutPlaintext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/GenerateDataKeyWithoutPlaintext)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/GenerateDataKeyWithoutPlaintext)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/GenerateDataKeyWithoutPlaintext)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/GenerateDataKeyWithoutPlaintext)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/GenerateDataKeyWithoutPlaintext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/GenerateDataKeyWithoutPlaintext)
