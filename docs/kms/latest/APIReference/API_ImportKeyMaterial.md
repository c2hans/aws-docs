---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_ImportKeyMaterial.html
---

# ImportKeyMaterial
<a name="API_ImportKeyMaterial"></a>

Imports or reimports key material into an existing KMS key that was created without key material. You can also use this operation to set or update the expiration model and expiration date of the imported key material.

By default, AWS KMS creates KMS keys with key material that it generates. You can also generate and import your own key material. For more information about importing key material, see [Importing key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html).

For asymmetric and HMAC keys, you cannot change the key material after the initial import. You can import multiple key materials into symmetric encryption keys and rotate the key material on demand using `RotateKeyOnDemand`.

You can import new key materials into multi-Region symmetric encryption keys. To do so, you must import the new key material into the primary Region key. Then you can import the same key materials into the replica Region keys. You cannot directly import new key material into the replica Region keys.

To import new key material for a multi-Region symmetric key, you’ll need to complete the following:

1. Call `ImportKeyMaterial` on the primary Region key with the `ImportType`set to `NEW_KEY_MATERIAL`.

1. Call `ImportKeyMaterial` on the replica Region key with the `ImportType` set to `EXISTING_KEY_MATERIAL` using the same key material imported to the primary Region key. You must do this for every replica Region key before you can perform the [RotateKeyOnDemand](API_RotateKeyOnDemand.md) operation on the primary Region key.

After you import key material, you can [reimport the same key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-import-key-material.html#reimport-key-material) into that KMS key or, if the key supports on-demand rotation, import new key material. You can use the `ImportType` parameter to indicate whether you are importing new key material or re-importing previously imported key material. You might reimport key material to replace key material that expired or key material that you deleted. You might also reimport key material to change the expiration model or expiration date of the key material.

Each time you import key material into AWS KMS, you can determine whether (`ExpirationModel`) and when (`ValidTo`) the key material expires. To change the expiration of your key material, you must import it again, either by calling `ImportKeyMaterial` or using the [import features](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-import-key-material.html#importing-keys-import-key-material-console) of the AWS KMS console.

Before you call `ImportKeyMaterial`, complete these steps:
+ Create or identify a KMS key with `EXTERNAL` origin, which indicates that the KMS key is designed for imported key material.

  To create a new KMS key for imported key material, call the [CreateKey](API_CreateKey.md) operation with an `Origin` value of `EXTERNAL`. You can create a symmetric encryption KMS key, HMAC KMS key, asymmetric encryption KMS key, asymmetric key agreement key, or asymmetric signing KMS key. You can also import key material into a [multi-Region key](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) of any supported type. However, you can't import key material into a KMS key in a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html).
+ Call the [GetParametersForImport](API_GetParametersForImport.md) operation to get a public key and import token set for importing key material.
+ Use the public key in the [GetParametersForImport](API_GetParametersForImport.md) response to encrypt your key material.

Then, in an `ImportKeyMaterial` request, you submit your encrypted key material and import token. When calling this operation, you must specify the following values:
+ The key ID or key ARN of the KMS key to associate with the imported key material. Its `Origin` must be `EXTERNAL` and its `KeyState` must be `PendingImport` or `Enabled`. You cannot perform this operation on a KMS key in a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html), or on a KMS key in a different AWS account. To get the `Origin` and `KeyState` of a KMS key, call [DescribeKey](API_DescribeKey.md).
+ The encrypted key material.
+ The import token that [GetParametersForImport](API_GetParametersForImport.md) returned. You must use a public key and token from the same `GetParametersForImport` response.
+ Whether the key material expires (`ExpirationModel`) and, if so, when (`ValidTo`). For help with this choice, see [Setting an expiration time](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-import-key-material.html#importing-keys-expiration) in the * AWS Key Management Service Developer Guide*.

  If you set an expiration date, AWS KMS deletes the key material from the KMS key on the specified date, making the KMS key unusable. To use the KMS key in cryptographic operations again, you must reimport the same key material. However, you can delete and reimport the key material at any time, including before the key material expires. Each time you reimport, you can eliminate or reset the expiration time.

When this operation is successful, the state of the KMS key changes to `Enabled`, and you can use the KMS key in cryptographic operations. For symmetric encryption keys, you will need to import all of the key materials associated with the KMS key to change its state to `Enabled`. Use the `ListKeyRotations` operation to list the ID and import state of each key material associated with a KMS key.

If this operation fails, use the exception to help determine the problem. If the error is related to the key material, the import token, or wrapping key, use [GetParametersForImport](API_GetParametersForImport.md) to get a new public key and import token for the KMS key and repeat the import procedure. For help, see [Create a KMS key with imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-conceptual.html) in the * AWS Key Management Service Developer Guide*.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: No. You cannot perform this operation on a KMS key in a different AWS account.

 **Required permissions**: [kms:ImportKeyMaterial](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [DeleteImportedKeyMaterial](API_DeleteImportedKeyMaterial.md)
+  [GetParametersForImport](API_GetParametersForImport.md)
+  [ListKeyRotations](API_ListKeyRotations.md)
+  [RotateKeyOnDemand](API_RotateKeyOnDemand.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_ImportKeyMaterial_RequestSyntax"></a>

```
{
   "EncryptedKeyMaterial": {{blob}},
   "ExpirationModel": "{{string}}",
   "ImportToken": {{blob}},
   "ImportType": "{{string}}",
   "KeyId": "{{string}}",
   "KeyMaterialDescription": "{{string}}",
   "KeyMaterialId": "{{string}}",
   "ValidTo": {{number}}
}
```

## Request Parameters
<a name="API_ImportKeyMaterial_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [EncryptedKeyMaterial](#API_ImportKeyMaterial_RequestSyntax) **   <a name="KMS-ImportKeyMaterial-request-EncryptedKeyMaterial"></a>
The encrypted key material to import. The key material must be encrypted under the public wrapping key that [GetParametersForImport](API_GetParametersForImport.md) returned, using the wrapping algorithm that you specified in the same `GetParametersForImport` request.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6144.
Required: Yes

 ** [ImportToken](#API_ImportKeyMaterial_RequestSyntax) **   <a name="KMS-ImportKeyMaterial-request-ImportToken"></a>
The import token that you received in the response to a previous [GetParametersForImport](API_GetParametersForImport.md) request. It must be from the same response that contained the public key that you used to encrypt the key material.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6144.
Required: Yes

 ** [KeyId](#API_ImportKeyMaterial_RequestSyntax) **   <a name="KMS-ImportKeyMaterial-request-KeyId"></a>
The identifier of the KMS key that will be associated with the imported key material. This must be the same KMS key specified in the `KeyID` parameter of the corresponding [GetParametersForImport](API_GetParametersForImport.md) request. The `Origin` of the KMS key must be `EXTERNAL` and its `KeyState` must be `PendingImport`.
The KMS key can be a symmetric encryption KMS key, HMAC KMS key, asymmetric encryption KMS key, or asymmetric signing KMS key, including a [multi-Region key](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) of any supported type. You cannot perform this operation on a KMS key in a custom key store, or on a KMS key in a different AWS account.
Specify the key ID or key ARN of the KMS key.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [ExpirationModel](#API_ImportKeyMaterial_RequestSyntax) **   <a name="KMS-ImportKeyMaterial-request-ExpirationModel"></a>
Specifies whether the key material expires. The default is `KEY_MATERIAL_EXPIRES`. For help with this choice, see [Setting an expiration time](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-import-key-material.html#importing-keys-expiration) in the * AWS Key Management Service Developer Guide*.
When the value of `ExpirationModel` is `KEY_MATERIAL_EXPIRES`, you must specify a value for the `ValidTo` parameter. When value is `KEY_MATERIAL_DOES_NOT_EXPIRE`, you must omit the `ValidTo` parameter.
You cannot change the `ExpirationModel` or `ValidTo` values for the current import after the request completes. To change either value, you must reimport the key material.
Type: String
Valid Values: `KEY_MATERIAL_EXPIRES | KEY_MATERIAL_DOES_NOT_EXPIRE`
Required: No

 ** [ImportType](#API_ImportKeyMaterial_RequestSyntax) **   <a name="KMS-ImportKeyMaterial-request-ImportType"></a>
Indicates whether the key material being imported is previously associated with this KMS key or not. This parameter is optional and only usable with symmetric encryption keys. If no key material has ever been imported into the KMS key, and this parameter is omitted, the parameter defaults to `NEW_KEY_MATERIAL`. After the first key material is imported, if this parameter is omitted then the parameter defaults to `EXISTING_KEY_MATERIAL`.
For multi-Region keys, you must first import new key material into the primary Region key. You should use the `NEW_KEY_MATERIAL` import type when importing key material into the primary Region key. Then, you can import the same key material into the replica Region key. The import type for the replica Region key should be `EXISTING_KEY_MATERIAL`.
Type: String
Valid Values: `NEW_KEY_MATERIAL | EXISTING_KEY_MATERIAL`
Required: No

 ** [KeyMaterialDescription](#API_ImportKeyMaterial_RequestSyntax) **   <a name="KMS-ImportKeyMaterial-request-KeyMaterialDescription"></a>
Description for the key material being imported. This parameter is optional and only usable with symmetric encryption keys. If you do not specify a key material description, AWS KMS retains the value you specified when you last imported the same key material into this KMS key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9:/_\s.-]+$`
Required: No

 ** [KeyMaterialId](#API_ImportKeyMaterial_RequestSyntax) **   <a name="KMS-ImportKeyMaterial-request-KeyMaterialId"></a>
Identifies the key material being imported. This parameter is optional and only usable with symmetric encryption keys. You cannot specify a key material ID with `ImportType` set to `NEW_KEY_MATERIAL`. Whenever you import key material into a symmetric encryption key, AWS KMS assigns a unique identifier to the key material based on the KMS key ID and the imported key material. When you re-import key material with a specified key material ID, AWS KMS:
+ Computes the identifier for the key material
+ Matches the computed identifier against the specified key material ID
+ Verifies that the key material ID is already associated with the KMS key
To get the list of key material IDs associated with a KMS key, use [ListKeyRotations](API_ListKeyRotations.md).
Type: String
Length Constraints: Fixed length of 64.
Pattern: `^[a-f0-9]+$`
Required: No

 ** [ValidTo](#API_ImportKeyMaterial_RequestSyntax) **   <a name="KMS-ImportKeyMaterial-request-ValidTo"></a>
The date and time when the imported key material expires. This parameter is required when the value of the `ExpirationModel` parameter is `KEY_MATERIAL_EXPIRES`. Otherwise it is not valid.
The value of this parameter must be a future date and time. The maximum value is 365 days from the request date.
When the key material expires, AWS KMS deletes the key material from the KMS key. Without its key material, the KMS key is unusable. To use the KMS key in cryptographic operations, you must reimport the same key material.
You cannot change the `ExpirationModel` or `ValidTo` values for the current import after the request completes. To change either value, you must delete ([DeleteImportedKeyMaterial](API_DeleteImportedKeyMaterial.md)) and reimport the key material.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_ImportKeyMaterial_ResponseSyntax"></a>

```
{
   "KeyId": "string",
   "KeyMaterialId": "string"
}
```

## Response Elements
<a name="API_ImportKeyMaterial_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyId](#API_ImportKeyMaterial_ResponseSyntax) **   <a name="KMS-ImportKeyMaterial-response-KeyId"></a>
The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN)) of the KMS key into which key material was imported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [KeyMaterialId](#API_ImportKeyMaterial_ResponseSyntax) **   <a name="KMS-ImportKeyMaterial-response-KeyMaterialId"></a>
Identifies the imported key material.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `^[a-f0-9]+$`

## Errors
<a name="API_ImportKeyMaterial_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

 ** ExpiredImportTokenException **
The request was rejected because the specified import token is expired. Use [GetParametersForImport](API_GetParametersForImport.md) to get a new import token and public key, use the new public key to encrypt the key material, and then try the request again.
HTTP Status Code: 400

 ** IncorrectKeyMaterialException **
The request was rejected because the key material in the request is, expired, invalid, or does not meet expectations. For example, it is not the same key material that was previously imported or AWS KMS expected new key material but the key material being imported is already associated with the KMS key.
HTTP Status Code: 400

 ** InvalidArnException **
The request was rejected because a specified ARN, or an ARN in a key policy, is not valid.
HTTP Status Code: 400

 ** InvalidCiphertextException **
From the [Decrypt](API_Decrypt.md) or [ReEncrypt](API_ReEncrypt.md) operation, the request was rejected because the specified ciphertext, or additional authenticated data incorporated into the ciphertext, such as the encryption context, is corrupted, missing, or otherwise invalid.
From the [ImportKeyMaterial](#API_ImportKeyMaterial) operation, the request was rejected because AWS KMS could not decrypt the encrypted (wrapped) key material.
HTTP Status Code: 400

 ** InvalidImportTokenException **
The request was rejected because the provided import token is invalid or is associated with a different KMS key.
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
<a name="API_ImportKeyMaterial_Examples"></a>

### Example Request
<a name="API_ImportKeyMaterial_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 2835
X-Amz-Target: TrentService.ImportKeyMaterial
X-Amz-Date: 20161201T212609Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161201/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=dda4e269d4fd93decf1401aeb651e49c206c412c609141f6c743f146e1afb4e3

{
  "ExpirationModel": "KEY_MATERIAL_DOES_NOT_EXPIRE",
  "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
  "ImportToken": "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",
  "EncryptedKeyMaterial": "CubeyZ4cm/xMEA0UG5jP1iBzh/0E+uUg407JDcXhIC+iuMm+wPgITaEby+Y3nM/e6gjUls5vy9TdBRFv4+JtksvB5hW4Znb2lUQhTUv+SSAZpaI14kAgTq/jC2GTLkaC6Vf5zJx2xaLrOKGV2Xu4YgONIGslubHNffTC3aL/YBJ/FXTXaVu7rS2phOFCrZ+ATittS03w4DiCVoNwo2v0QE0+dVoUNjXNQC1veWxhPlC7FezfK7AIsBSSXotJfANxRkybg8KcmkSoYdzr3N0L0v7oMorgbTgaTvdrLXu/PzphK6RWJGJig4tk+lxUT8hV7xiLkFskGjIHFmp6Xbon8w=="
}
```

### Example Response
<a name="API_ImportKeyMaterial_Example_2"></a>

This example illustrates one usage of ImportKeyMaterial.

```
HTTP/1.1 200 OK
Server: Server
Date: Thu, 01 Dec 2016 21:26:10 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Connection: keep-alive
x-amzn-RequestId: c72fb6ff-b80c-11e6-ae07-61b14fe11739

{
  "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
  "KeyMaterialId": "0b7fd7ddbac6eef27907413567cad8c810e2883dc8a7534067a82ee1142fc1e6",
}
```

## See Also
<a name="API_ImportKeyMaterial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/ImportKeyMaterial)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/ImportKeyMaterial)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/ImportKeyMaterial)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/ImportKeyMaterial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/ImportKeyMaterial)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/ImportKeyMaterial)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/ImportKeyMaterial)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/ImportKeyMaterial)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/ImportKeyMaterial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/ImportKeyMaterial)
