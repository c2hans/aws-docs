---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_Decapsulate.html
---

# Decapsulate
<a name="API_Decapsulate"></a>

Recovers the shared secret that was encapsulated with the public key of an ML-KEM KMS key. Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM), specified in [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) on the NIST website, is a post-quantum algorithm for establishing a shared secret between two parties. For an example of how two parties establish a shared secret over an insecure channel using ML-KEM, see [ML-KEM keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/pqkeys.html#mlkem) in the * AWS Key Management Service Developer Guide*.

The Decapsulate operation is not available in China Regions.

 `Decapsulate` returns the shared secret as a 32-byte value. You can use it directly as key material, or run it through a key derivation function to derive multiple keys and nonces.

**Important**
 `Decapsulate` returns an `InvalidCiphertextException` when the length of the `SharedSecretCiphertextBlob` is inconsistent with the ML-KEM key spec. In all other cases, `Decapsulate` returns a 32-byte pseudo-random value. This is true even when the `SharedSecretCiphertextBlob` was created using a different ML-KEM key or altered from its original value. This behavior is a security feature called *implicit rejection* that helps protect against chosen-ciphertext attacks.
Because a response does not indicate that the ciphertext and key are valid, confirm the two parties derived the same shared secret before using it.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: Yes. To perform this operation with a KMS key in a different AWS account, specify the key ARN or alias ARN in the value of the `KeyId` parameter.

 **Required permissions**: [kms:Decapsulate](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [Encapsulate](API_Encapsulate.md)
+  [CreateKey](API_CreateKey.md)
+  [GetPublicKey](API_GetPublicKey.md)
+  [DescribeKey](API_DescribeKey.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_Decapsulate_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "EncapsulationAlgorithm": "{{string}}",
   "GrantTokens": [ "{{string}}" ],
   "KeyId": "{{string}}",
   "SharedSecretCiphertextBlob": {{blob}}
}
```

## Request Parameters
<a name="API_Decapsulate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [EncapsulationAlgorithm](#API_Decapsulate_RequestSyntax) **   <a name="KMS-Decapsulate-request-EncapsulationAlgorithm"></a>
Specifies the key encapsulation algorithm used to recover the shared secret. The only valid value is `ML_KEM`.
Type: String
Valid Values: `ML_KEM`
Required: Yes

 ** [KeyId](#API_Decapsulate_RequestSyntax) **   <a name="KMS-Decapsulate-request-KeyId"></a>
Identifies the asymmetric ML-KEM KMS key whose public key was used to produce the encapsulated shared secret. AWS KMS uses the private key in the specified key pair to decapsulate the shared secret.
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

 ** [SharedSecretCiphertextBlob](#API_Decapsulate_RequestSyntax) **   <a name="KMS-Decapsulate-request-SharedSecretCiphertextBlob"></a>
The encapsulated (ciphertext) form of the shared secret to recover. This is the `SharedSecretCiphertextBlob` value that the [Encapsulate](API_Encapsulate.md) operation returns. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6144.
Required: Yes

 ** [DryRun](#API_Decapsulate_RequestSyntax) **   <a name="KMS-Decapsulate-request-DryRun"></a>
Checks if your request will succeed. `DryRun` is an optional parameter.
To learn more about how to use this parameter, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the * AWS Key Management Service Developer Guide*.
Type: Boolean
Required: No

 ** [GrantTokens](#API_Decapsulate_RequestSyntax) **   <a name="KMS-Decapsulate-request-GrantTokens"></a>
A list of grant tokens.
Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency*. For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html) in the * AWS Key Management Service Developer Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

## Response Syntax
<a name="API_Decapsulate_ResponseSyntax"></a>

```
{
   "EncapsulationAlgorithm": "string",
   "KeyId": "string",
   "SharedSecret": blob
}
```

## Response Elements
<a name="API_Decapsulate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EncapsulationAlgorithm](#API_Decapsulate_ResponseSyntax) **   <a name="KMS-Decapsulate-response-EncapsulationAlgorithm"></a>
The key encapsulation algorithm used to recover the shared secret.
Type: String
Valid Values: `ML_KEM`

 ** [KeyId](#API_Decapsulate_ResponseSyntax) **   <a name="KMS-Decapsulate-response-KeyId"></a>
The identifier of the ML-KEM KMS key used to decapsulate the shared secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [SharedSecret](#API_Decapsulate_ResponseSyntax) **   <a name="KMS-Decapsulate-response-SharedSecret"></a>
The plaintext shared secret recovered from the encapsulated form. It is a 32-byte value that matches the shared secret held by the encapsulating party. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_Decapsulate_Errors"></a>

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

 ** InvalidCiphertextException **
From the [Decrypt](API_Decrypt.md) or [ReEncrypt](API_ReEncrypt.md) operation, the request was rejected because the specified ciphertext, or additional authenticated data incorporated into the ciphertext, such as the encryption context, is corrupted, missing, or otherwise invalid.
From the [ImportKeyMaterial](API_ImportKeyMaterial.md) operation, the request was rejected because AWS KMS could not decrypt the encrypted (wrapped) key material.
From the [Decapsulate](#API_Decapsulate) operation, the request was rejected because the length of the `SharedSecretCiphertextBlob` is inconsistent with the specified ML-KEM key spec.
HTTP Status Code: 400

 ** InvalidGrantTokenException **
The request was rejected because the specified grant token is not valid.
HTTP Status Code: 400

 ** InvalidKeyUsageException **
The request was rejected for one of the following reasons:
+ The `KeyUsage` value of the KMS key is incompatible with the API operation.
+ The encryption algorithm or signing algorithm specified for the operation is incompatible with the type of key material in the KMS key `(KeySpec`).
For encrypting, decrypting, re-encrypting, and generating data keys, the `KeyUsage` must be `ENCRYPT_DECRYPT`. For signing and verifying messages, the `KeyUsage` must be `SIGN_VERIFY`. For generating and verifying message authentication codes (MACs), the `KeyUsage` must be `GENERATE_VERIFY_MAC`. For deriving key agreement secrets, the `KeyUsage` must be `KEY_AGREEMENT`. For encapsulating and decapsulating shared secrets, the `KeyUsage` must be `ENCAPSULATE_DECAPSULATE`. To find the `KeyUsage` of a KMS key, use the [DescribeKey](API_DescribeKey.md) operation.
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
<a name="API_Decapsulate_Examples"></a>

### Example Request
<a name="API_Decapsulate_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 1571
X-Amz-Target: TrentService.Decapsulate
X-Amz-Date: 20261018T233819Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20261018/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=2cea34fe55d5858295a377448a1e053d0edd45ce571da7cf69b202905759f272

{
    "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "SharedSecretCiphertextBlob": "kGuVROOrf4ZLP3rR7DB64O803VeoevUmGCDvJ/vc2vBEYkYwZoc2NmNYeX0g55i/Pz4uvqnwhVFC2KDZJD5Rdob4GoaRphStzM87F30tq7Xui3zfHO8X5aZCXJpPB3lh/DTiRoitmjo+mwleYyL6IOG8PurEPASSROB3SdfhmVPsTY6ZaUARqtY6BFBIyHbnWzI0a2HLdl1DGnMuvy3yTdhXzE5/Z7ZUAe5edL+WLao7vWWl2InU1TDlPE+kDu540aCoIX37ke4dmTJIe/+e20nzINEmuhCzUVIoRGrYyT8ZnuyMq9kZtd+SmhfKRA5PQT0vrp0PSHE2653724YPKvLSuEoNbMSXPTbB8rBeP3kXg0p+4ZLjRda3SoMEvqbQdWLVRclMI+PtXUSCJkKWrbmg9/2eyO9fPNCsck36zVEpZaw4irP1bZguM+7qAYDhxPupO+Ks7/vkgDh6myzjslSBHCGWqnMLmoiatJinsI2NdFLprGvqZqzJrbIABI54OfFs6B7pSqLdNATbXuRRMUMRX/2+c2WcL6YR62tQUACTGI8BBM6Abb5IrD7VRWzzNW0nVgSEV56W8Bb0/lgbmiyeZfhsvpUPPAX8QDfkZUPG1xeTn2ao7it+jO48OOPFbzj+zwt2ZCiIpxN1lR41R0ubD18WQynI9jIz5R3nY6RTtx8kJ4Y+br62NdpsczIr6tWDgpGfqY6XGyW5SncB2EJ85AIrQrEUFbPva2inHPgxdkCOEgLp8VYwabNXiLJf7D8BiU90QyPUyFdoZWOKtPZX4tXkLoeCgt+8EbfiSLwoDqDbgGgbAbItCrrdwFA6vUBXG2AQfvsdq+9L3OcUmPajCwnTnf/BTMR4mnHT+0Eu5gamKmb86SjCa9uRzIosVGTvaMLuQBMD+507rKJwr5+Ia5k9TMjtfNO4oQglNKDVORumiyxOvTDQDYbWcT9B4g9ygOA0GZts7qmJzM44wGtXpfrQpZCWX8X0zKE9LesVRM5f8+oLnf8oopJ/9ClhC9SReLztP+W7h/LqG0qzisKX97vLXIdGUSC14On2iPQWgO3qyXfkt8xwXohc/veWoRsS9MFUtLHabYJ25o8VZdtwWJfVcDSrCaSFDHJeAFFihA/F3FlVZuMoWy2DwadoL4xMG2ZmGgs68rPIeLq27dXZFaF5PemCsrQKMhlo4X1tGQROgehoj0Kr8Dab17DgBZJrzvvrecWzoTdMdeyFBzxtnQKXknkKxwVW/WJqGDxkLVlwP9z6fIbEy4vbhe2vhbVtetjlbh0F0JQFnMMet29j6bs+506K88MPYyHRZBC5HIODmrYDlMjUdPaUGOUYM5VBLqEwnUvCY82SdFMKeuUxVSgQ2dyF2W41Sybf4pzRWfLMzkWuExbIbtt8OfGCcvXvcDjZFipCKoSDm75X+eXb4nhIGJVGQBXSWefN61Q=",
    "EncapsulationAlgorithm": "ML_KEM"
}
```

### Example Response
<a name="API_Decapsulate_Example_2"></a>

This example illustrates one usage of Decapsulate.

```
HTTP/1.1 200 OK
Server: Server
Date: Sun, 18 Oct 2026 23:38:19 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 149
Connection: keep-alive
x-amzn-RequestId: 1e76aa81-a532-11e6-a265-d3aef78e1a90

{
    "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "SharedSecret": "oJ2H4lIMwHD2VgqkBf63bGY86fwcyxe2DOu/+EGN5bU=",
    "EncapsulationAlgorithm": "ML_KEM"
}
```

## See Also
<a name="API_Decapsulate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/Decapsulate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/Decapsulate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/Decapsulate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/Decapsulate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/Decapsulate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/Decapsulate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/Decapsulate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/Decapsulate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/Decapsulate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/Decapsulate)
