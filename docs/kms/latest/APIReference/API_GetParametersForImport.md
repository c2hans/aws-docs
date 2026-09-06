---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_GetParametersForImport.html
---

# GetParametersForImport
<a name="API_GetParametersForImport"></a>

Returns the public key and an import token you need to import or reimport key material for a KMS key.

By default, KMS keys are created with key material that AWS KMS generates. This operation supports [Importing key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html), an advanced feature that lets you generate and import the cryptographic key material for a KMS key.

Before calling `GetParametersForImport`, use the [CreateKey](API_CreateKey.md) operation with an `Origin` value of `EXTERNAL` to create a KMS key with no key material. You can import key material for a symmetric encryption KMS key, HMAC KMS key, asymmetric encryption KMS key, or asymmetric signing KMS key. You can also import key material into a [multi-Region key](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) of any supported type. However, you can't import key material into a KMS key in a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html). You can also use `GetParametersForImport` to get a public key and import token to [reimport the original key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-import-key-material.html#reimport-key-material) into a KMS key whose key material expired or was deleted.

 `GetParametersForImport` returns the items that you need to import your key material.
+ The public key (or "wrapping key") of an RSA key pair that KMS generates.

  You will use this public key to encrypt ("wrap") your key material while it's in transit to AWS KMS.
+ A import token that ensures that AWS KMS can decrypt your key material and associate it with the correct KMS key.

The public key and its import token are permanently linked and must be used together. Each public key and import token set is valid for 24 hours. The expiration date and time appear in the `ParametersValidTo` field in the `GetParametersForImport` response. You cannot use an expired public key or import token in an [ImportKeyMaterial](API_ImportKeyMaterial.md) request. If your key and token expire, send another `GetParametersForImport` request.

 `GetParametersForImport` requires the following information:
+ The key ID of the KMS key for which you are importing the key material.
+ The key spec of the public key ("wrapping key") that you will use to encrypt your key material during import.
+ The wrapping algorithm that you will use with the public key to encrypt your key material.

You can use the same or a different public key spec and wrapping algorithm each time you import or reimport the same key material.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: No. You cannot perform this operation on a KMS key in a different AWS account.

 **Required permissions**: [kms:GetParametersForImport](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [ImportKeyMaterial](API_ImportKeyMaterial.md)
+  [DeleteImportedKeyMaterial](API_DeleteImportedKeyMaterial.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_GetParametersForImport_RequestSyntax"></a>

```
{
   "KeyId": "{{string}}",
   "WrappingAlgorithm": "{{string}}",
   "WrappingKeySpec": "{{string}}"
}
```

## Request Parameters
<a name="API_GetParametersForImport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_GetParametersForImport_RequestSyntax) **   <a name="KMS-GetParametersForImport-request-KeyId"></a>
The identifier of the KMS key that will be associated with the imported key material. The `Origin` of the KMS key must be `EXTERNAL`.
All KMS key types are supported, including multi-Region keys. However, you cannot import key material into a KMS key in a custom key store.
Specify the key ID or key ARN of the KMS key.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [WrappingAlgorithm](#API_GetParametersForImport_RequestSyntax) **   <a name="KMS-GetParametersForImport-request-WrappingAlgorithm"></a>
The algorithm you will use with the RSA public key (`PublicKey`) in the response to protect your key material during import. For more information, see [Select a wrapping algorithm](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-get-public-key-and-token.html#select-wrapping-algorithm) in the * AWS Key Management Service Developer Guide*.
For RSA\_AES wrapping algorithms, you encrypt your key material with an AES key that you generate, then encrypt your AES key with the RSA public key from AWS KMS. For RSAES wrapping algorithms, you encrypt your key material directly with the RSA public key from AWS KMS.
The wrapping algorithms that you can use depend on the type of key material that you are importing. To import an RSA private key, you must use an RSA\_AES wrapping algorithm.
+  **RSA\_AES\_KEY\_WRAP\_SHA\_256** — Supported for wrapping RSA and ECC key material.
+  **RSA\_AES\_KEY\_WRAP\_SHA\_1** — Supported for wrapping RSA and ECC key material.
+  **RSAES\_OAEP\_SHA\_256** — Supported for all types of key material, except RSA key material (private key).

  You cannot use the RSAES\_OAEP\_SHA\_256 wrapping algorithm with the RSA\_2048 wrapping key spec to wrap ECC\_NIST\_P521 key material.
+  **RSAES\_OAEP\_SHA\_1** — Supported for all types of key material, except RSA key material (private key).

  You cannot use the RSAES\_OAEP\_SHA\_1 wrapping algorithm with the RSA\_2048 wrapping key spec to wrap ECC\_NIST\_P521 key material.
+  **RSAES\_PKCS1\_V1\_5** (Deprecated) — As of October 10, 2023, AWS KMS does not support the RSAES\_PKCS1\_V1\_5 wrapping algorithm.
Type: String
Valid Values: `RSAES_PKCS1_V1_5 | RSAES_OAEP_SHA_1 | RSAES_OAEP_SHA_256 | RSA_AES_KEY_WRAP_SHA_1 | RSA_AES_KEY_WRAP_SHA_256 | SM2PKE`
Required: Yes

 ** [WrappingKeySpec](#API_GetParametersForImport_RequestSyntax) **   <a name="KMS-GetParametersForImport-request-WrappingKeySpec"></a>
The type of RSA public key to return in the response. You will use this wrapping key with the specified wrapping algorithm to protect your key material during import.
Use the longest RSA wrapping key that is practical.
You cannot use an RSA\_2048 public key to directly wrap an ECC\_NIST\_P521 private key. Instead, use an RSA\_AES wrapping algorithm or choose a longer RSA public key.
Type: String
Valid Values: `RSA_2048 | RSA_3072 | RSA_4096 | SM2`
Required: Yes

## Response Syntax
<a name="API_GetParametersForImport_ResponseSyntax"></a>

```
{
   "ImportToken": blob,
   "KeyId": "string",
   "ParametersValidTo": number,
   "PublicKey": blob
}
```

## Response Elements
<a name="API_GetParametersForImport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImportToken](#API_GetParametersForImport_ResponseSyntax) **   <a name="KMS-GetParametersForImport-response-ImportToken"></a>
The import token to send in a subsequent [ImportKeyMaterial](API_ImportKeyMaterial.md) request.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [KeyId](#API_GetParametersForImport_ResponseSyntax) **   <a name="KMS-GetParametersForImport-response-KeyId"></a>
The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN)) of the KMS key to use in a subsequent [ImportKeyMaterial](API_ImportKeyMaterial.md) request. This is the same KMS key specified in the `GetParametersForImport` request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [ParametersValidTo](#API_GetParametersForImport_ResponseSyntax) **   <a name="KMS-GetParametersForImport-response-ParametersValidTo"></a>
The time at which the import token and public key are no longer valid. After this time, you cannot use them to make an [ImportKeyMaterial](API_ImportKeyMaterial.md) request and you must send another `GetParametersForImport` request to get new ones.
Type: Timestamp

 ** [PublicKey](#API_GetParametersForImport_ResponseSyntax) **   <a name="KMS-GetParametersForImport-response-PublicKey"></a>
The public key to use to encrypt the key material before importing it with [ImportKeyMaterial](API_ImportKeyMaterial.md).
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_GetParametersForImport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

 ** InvalidArnException **
The request was rejected because a specified ARN, or an ARN in a key policy, is not valid.
HTTP Status Code: 400

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

## Examples
<a name="API_GetParametersForImport_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_GetParametersForImport_Example_1"></a>

This example illustrates one usage of GetParametersForImport.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 121
X-Amz-Target: TrentService.GetParametersForImport
X-Amz-Date: 20231130T225216Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161130/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=5bcc8e7669b6de719091ad27ae0145daa319f881010958208e960329341421d5

{
  "WrappingAlgorithm": "RSAES_OAEP_SHA_256",
  "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
  "WrappingKeySpec": "RSA_4096"
}
```

### Example Response
<a name="API_GetParametersForImport_Example_2"></a>

This example illustrates one usage of GetParametersForImport.

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 30 Jul 2023 22:52:17 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 2892
Connection: keep-alive
x-amzn-RequestId: a46d61e0-b74f-11e6-b0c0-3343f53dee45

{
  "ImportToken": "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",
  "KeyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
  "ParametersValidTo": 1.480632737044E9,
  "PublicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvH3Yj0wbkLEpUl95Cv1cJVjsVNSjwGq3tCLnzXfhVwVvmzGN8pYj3U8nKwgouaHbBWNJYjP5VutbbkKS4Kv4GojwZBJyHN17kmxo8yTjRmjR15SKIQ8cqRA2uaERMLnpztIXdZp232PQPbWGxDyXYJ0aJ5EFSag+iSK341kr2kFTpINN7T1ZaX9vfXBdGR+VtkRKMWoHQeWzHrPZ+3irvpXNCKxGUxmPNsJSjPUhuSXT5+0VrY/LEYLQ5lUTrhU6z5/OK0kzaCc66DXc5ipSloS4Xyg+QcYSMxe9xuqO5HtzFImUSKBm1W6eDT6lHnSbpi7vXzNbIX7pWxKw9nmQvQIDAQAB"
}
```

## See Also
<a name="API_GetParametersForImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/GetParametersForImport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/GetParametersForImport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/GetParametersForImport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/GetParametersForImport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/GetParametersForImport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/GetParametersForImport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/GetParametersForImport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/GetParametersForImport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/GetParametersForImport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/GetParametersForImport)
