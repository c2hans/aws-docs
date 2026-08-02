---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteImportedKeyMaterial.html
---

# DeleteImportedKeyMaterial
<a name="API_DeleteImportedKeyMaterial"></a>

Deletes key material that was previously imported. This operation makes the specified KMS key temporarily unusable. To restore the usability of the KMS key, reimport the same key material. For more information about importing key material into AWS KMS, see [Importing Key Material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) in the * AWS Key Management Service Developer Guide*.

When the specified KMS key is in the `PendingDeletion` state, this operation does not change the KMS key's state. Otherwise, it changes the KMS key's state to `PendingImport`.

**Considerations for multi-Region symmetric encryption keys**
+ When you delete the key material of a primary Region key that is in `PENDING_ROTATION` or `PENDING_MULTI_REGION_IMPORT_AND_ROTATION`state, you'll also be deleting the key materials for the replica Region keys.
+ If you delete any key material of a replica Region key, the primary Region key and other replica Region keys remain unchanged.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: No. You cannot perform this operation on a KMS key in a different AWS account.

 **Required permissions**: [kms:DeleteImportedKeyMaterial](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [GetParametersForImport](API_GetParametersForImport.md)
+  [ListKeyRotations](API_ListKeyRotations.md)
+  [ImportKeyMaterial](API_ImportKeyMaterial.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_DeleteImportedKeyMaterial_RequestSyntax"></a>

```
{
   "KeyId": "{{string}}",
   "KeyMaterialId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteImportedKeyMaterial_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_DeleteImportedKeyMaterial_RequestSyntax) **   <a name="KMS-DeleteImportedKeyMaterial-request-KeyId"></a>
Identifies the KMS key from which you are deleting imported key material. The `Origin` of the KMS key must be `EXTERNAL`.
Specify the key ID or key ARN of the KMS key.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [KeyMaterialId](#API_DeleteImportedKeyMaterial_RequestSyntax) **   <a name="KMS-DeleteImportedKeyMaterial-request-KeyMaterialId"></a>
Identifies the imported key material you are deleting.
If no KeyMaterialId is specified, AWS KMS deletes the current key material.
To get the list of key material IDs associated with a KMS key, use [ListKeyRotations](API_ListKeyRotations.md).
Type: String
Length Constraints: Fixed length of 64.
Pattern: `^[a-f0-9]+$`
Required: No

## Response Syntax
<a name="API_DeleteImportedKeyMaterial_ResponseSyntax"></a>

```
{
   "KeyId": "string",
   "KeyMaterialId": "string"
}
```

## Response Elements
<a name="API_DeleteImportedKeyMaterial_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyId](#API_DeleteImportedKeyMaterial_ResponseSyntax) **   <a name="KMS-DeleteImportedKeyMaterial-response-KeyId"></a>
The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN)) of the KMS key from which the key material was deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [KeyMaterialId](#API_DeleteImportedKeyMaterial_ResponseSyntax) **   <a name="KMS-DeleteImportedKeyMaterial-response-KeyMaterialId"></a>
Identifies the deleted key material.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `^[a-f0-9]+$`

## Errors
<a name="API_DeleteImportedKeyMaterial_Errors"></a>

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
<a name="API_DeleteImportedKeyMaterial_Examples"></a>

### Example Request
<a name="API_DeleteImportedKeyMaterial_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 48
X-Amz-Target: TrentService.DeleteImportedKeyMaterial
X-Amz-Date: 20161107T213532Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161107/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=2cea34fe55d5858295a377448a1e053d0edd45ce571da7cf69b202905759f272

{"KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"}
```

### Example Response
<a name="API_DeleteImportedKeyMaterial_Example_2"></a>

This example illustrates one usage of DeleteImportedKeyMaterial.

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
   "KeyMaterialId": "0b7fd7ddbac6eef27907413567cad8c810e2883dc8a7534067a82ee1142fc1e6",
}
```

## See Also
<a name="API_DeleteImportedKeyMaterial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/DeleteImportedKeyMaterial)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/DeleteImportedKeyMaterial)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/DeleteImportedKeyMaterial)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/DeleteImportedKeyMaterial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/DeleteImportedKeyMaterial)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/DeleteImportedKeyMaterial)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/DeleteImportedKeyMaterial)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/DeleteImportedKeyMaterial)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/DeleteImportedKeyMaterial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/DeleteImportedKeyMaterial)
