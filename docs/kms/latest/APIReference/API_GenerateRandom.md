---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateRandom.html
---

# GenerateRandom
<a name="API_GenerateRandom"></a>

Returns a random byte string that is cryptographically secure.

You must use the `NumberOfBytes` parameter to specify the length of the random byte string. There is no default value for string length.

By default, the random byte string is generated in AWS KMS. To generate the byte string in the AWS CloudHSM cluster associated with an AWS CloudHSM key store, use the `CustomKeyStoreId` parameter.

 `GenerateRandom` also supports [AWS Nitro Enclaves](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitro-enclave.html), which provide an isolated compute environment in Amazon EC2. To call `GenerateRandom` for a Nitro enclave or NitroTPM, use the [AWS Nitro Enclaves SDK](https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk) or any AWS SDK. Use the `Recipient` parameter to provide the attestation document for the attested environment. Instead of plaintext bytes, the response includes the plaintext bytes encrypted under the public key from the attestation document (`CiphertextForRecipient`). For information about the interaction between AWS KMS and AWS Nitro Enclaves or AWS NitroTPM, see [Cryptographic attestation support in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html) in the * AWS Key Management Service Developer Guide*.

For more information about entropy and random number generation, see [Entropy and random number generation](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#entropy-and-random-numbers) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: Not applicable. `GenerateRandom` does not use any account-specific resources, such as KMS keys.

 **Required permissions**: [kms:GenerateRandom](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_GenerateRandom_RequestSyntax"></a>

```
{
   "CustomKeyStoreId": "{{string}}",
   "NumberOfBytes": {{number}},
   "Recipient": {
      "AttestationDocument": {{blob}},
      "KeyEncryptionAlgorithm": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GenerateRandom_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [CustomKeyStoreId](#API_GenerateRandom_RequestSyntax) **   <a name="KMS-GenerateRandom-request-CustomKeyStoreId"></a>
Generates the random byte string in the AWS CloudHSM cluster that is associated with the specified AWS CloudHSM key store. To find the ID of a custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.
External key store IDs are not valid for this parameter. If you specify the ID of an external key store, `GenerateRandom` throws an `UnsupportedOperationException`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [NumberOfBytes](#API_GenerateRandom_RequestSyntax) **   <a name="KMS-GenerateRandom-request-NumberOfBytes"></a>
The length of the random byte string. This parameter is required.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

 ** [Recipient](#API_GenerateRandom_RequestSyntax) **   <a name="KMS-GenerateRandom-request-Recipient"></a>
A signed [attestation document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitro-enclave-how.html#term-attestdoc) from an AWS Nitro enclave or NitroTPM, and the encryption algorithm to use with the public key in the attestation document. The only valid encryption algorithm is `RSAES_OAEP_SHA_256`.
This parameter supports the [AWS Nitro Enclaves SDK](https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk) or any AWS SDK for AWS Nitro Enclaves. It supports any AWS SDK for AWS NitroTPM.
When you use this parameter, instead of returning plaintext bytes, AWS KMS encrypts the plaintext bytes under the public key in the attestation document, and returns the resulting ciphertext in the `CiphertextForRecipient` field in the response. This ciphertext can be decrypted only with the private key in the attested environment. The `Plaintext` field in the response is null or empty.
For information about the interaction between AWS KMS and AWS Nitro Enclaves or AWS NitroTPM, see [Cryptographic attestation support in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html) in the * AWS Key Management Service Developer Guide*.
Type: [RecipientInfo](API_RecipientInfo.md) object
Required: No

## Response Syntax
<a name="API_GenerateRandom_ResponseSyntax"></a>

```
{
   "CiphertextForRecipient": blob,
   "Plaintext": blob
}
```

## Response Elements
<a name="API_GenerateRandom_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CiphertextForRecipient](#API_GenerateRandom_ResponseSyntax) **   <a name="KMS-GenerateRandom-response-CiphertextForRecipient"></a>
The plaintext random bytes encrypted with the public key from the attestation document. This ciphertext can be decrypted only by using a private key from the attested environment.
This field is included in the response only when the `Recipient` parameter in the request includes a valid attestation document from an AWS Nitro enclave or NitroTPM. For information about the interaction between AWS KMS and AWS Nitro Enclaves or AWS NitroTPM, see [Cryptographic attestation support in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html) in the * AWS Key Management Service Developer Guide*.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [Plaintext](#API_GenerateRandom_ResponseSyntax) **   <a name="KMS-GenerateRandom-response-Plaintext"></a>
The random byte string. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.
If the response includes the `CiphertextForRecipient` field, the `Plaintext` field is null or empty.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_GenerateRandom_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CustomKeyStoreInvalidStateException **
The request was rejected because of the `ConnectionState` of the custom key store. To get the `ConnectionState` of a custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.
This exception is thrown under the following conditions:
+ You requested the [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md) operation on a custom key store with a `ConnectionState` of `DISCONNECTING` or `FAILED`. This operation is valid for all other `ConnectionState` values. To reconnect a custom key store in a `FAILED` state, disconnect it ([DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md)), then connect it (`ConnectCustomKeyStore`).
+ You requested the [CreateKey](API_CreateKey.md) operation in a custom key store that is not connected. This operations is valid only when the custom key store `ConnectionState` is `CONNECTED`.
+ You requested the [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md) operation on a custom key store with a `ConnectionState` of `DISCONNECTING` or `DISCONNECTED`. This operation is valid for all other `ConnectionState` values.
+ You requested the [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md) or [DeleteCustomKeyStore](API_DeleteCustomKeyStore.md) operation on a custom key store that is not disconnected. `UpdateCustomKeyStore` can be called on a custom key store in the `CONNECTED` state only to update `NewCustomKeyStoreName`. For all other properties, the custom key store `ConnectionState` must be `DISCONNECTED`.
+ You requested the [GenerateRandom](#API_GenerateRandom) operation in an AWS CloudHSM key store that is not connected. This operation is valid only when the AWS CloudHSM key store `ConnectionState` is `CONNECTED`.
HTTP Status Code: 400

 ** CustomKeyStoreNotFoundException **
The request was rejected because AWS KMS cannot find a custom key store with the specified key store name or ID.
HTTP Status Code: 400

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## Examples
<a name="API_GenerateRandom_Examples"></a>

### Example Request
<a name="API_GenerateRandom_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 21
X-Amz-Target: TrentService.GenerateRandom
X-Amz-Date: 20161114T215101Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161114/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=e3a0cfdbfb71fae5c89e422ad8322b6a44aed85bf68e3d11f3f315bbaa82ad22

{"NumberOfBytes": 32}
```

### Example Response
<a name="API_GenerateRandom_Example_2"></a>

This example illustrates one usage of GenerateRandom.

```
HTTP/1.1 200 OK
Server: Server
Date: Mon, 14 Nov 2016 21:51:02 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 60
Connection: keep-alive
x-amzn-RequestId: 6f79b0ad-aab4-11e6-971f-0f7b7e5b6782

{"Plaintext":"+Q2hxK6OBuU6K6ZIIBucFMCW2NJkhiSWDySSQyWp9zA="}
```

## See Also
<a name="API_GenerateRandom_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/GenerateRandom)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/GenerateRandom)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/GenerateRandom)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/GenerateRandom)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/GenerateRandom)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/GenerateRandom)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/GenerateRandom)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/GenerateRandom)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/GenerateRandom)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/GenerateRandom)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
