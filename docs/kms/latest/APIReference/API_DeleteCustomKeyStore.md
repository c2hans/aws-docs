---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteCustomKeyStore.html
---

# DeleteCustomKeyStore
<a name="API_DeleteCustomKeyStore"></a>

Deletes a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html). This operation does not affect any backing elements of the custom key store. It does not delete the AWS CloudHSM cluster that is associated with an AWS CloudHSM key store, or affect any users or keys in the cluster. For an external key store, it does not affect the external key store proxy, external key manager, or any external keys.

 This operation is part of the custom key stores feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a key store that you own and manage.

The custom key store that you delete cannot contain any [KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys). Before deleting the key store, verify that you will never need to use any of the KMS keys in the key store for any [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#cryptographic-operations). Then, use [ScheduleKeyDeletion](API_ScheduleKeyDeletion.md) to delete the KMS keys from the key store. After the required waiting period expires and all KMS keys are deleted from the custom key store, use [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md) to disconnect the key store from AWS KMS. Then, you can delete the custom key store.

For keys in an AWS CloudHSM key store, the `ScheduleKeyDeletion` operation makes a best effort to delete the key material from the associated cluster. However, you might need to manually [delete the orphaned key material](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#fix-keystore-orphaned-key) from the cluster and its backups. AWS KMS never creates, manages, or deletes cryptographic keys in the external key manager associated with an external key store. You must manage them using your external key manager tools.

Instead of deleting the custom key store, consider using the [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md) operation to disconnect the custom key store from its backing key store. While the key store is disconnected, you cannot create or use the KMS keys in the key store. But, you do not need to delete KMS keys and you can reconnect a disconnected custom key store at any time.

If the operation succeeds, it returns a JSON object with no properties.

 **Cross-account use**: No. You cannot perform this operation on a custom key store in a different AWS account.

 **Required permissions**: [kms:DeleteCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy)

 **Related operations:**
+  [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md)
+  [CreateCustomKeyStore](API_CreateCustomKeyStore.md)
+  [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md)
+  [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md)
+  [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_DeleteCustomKeyStore_RequestSyntax"></a>

```
{
   "CustomKeyStoreId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCustomKeyStore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [CustomKeyStoreId](#API_DeleteCustomKeyStore_RequestSyntax) **   <a name="KMS-DeleteCustomKeyStore-request-CustomKeyStoreId"></a>
Enter the ID of the custom key store you want to delete. To find the ID of a custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Elements
<a name="API_DeleteCustomKeyStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCustomKeyStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CustomKeyStoreHasCMKsException **
The request was rejected because the custom key store contains KMS keys. After verifying that you do not need to use the KMS keys, use the [ScheduleKeyDeletion](API_ScheduleKeyDeletion.md) operation to delete the KMS keys. After they are deleted, you can delete the custom key store.
HTTP Status Code: 400

 ** CustomKeyStoreInvalidStateException **
The request was rejected because of the `ConnectionState` of the custom key store. To get the `ConnectionState` of a custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.
This exception is thrown under the following conditions:
+ You requested the [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md) operation on a custom key store with a `ConnectionState` of `DISCONNECTING` or `FAILED`. This operation is valid for all other `ConnectionState` values. To reconnect a custom key store in a `FAILED` state, disconnect it ([DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md)), then connect it (`ConnectCustomKeyStore`).
+ You requested the [CreateKey](API_CreateKey.md) operation in a custom key store that is not connected. This operations is valid only when the custom key store `ConnectionState` is `CONNECTED`.
+ You requested the [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md) operation on a custom key store with a `ConnectionState` of `DISCONNECTING` or `DISCONNECTED`. This operation is valid for all other `ConnectionState` values.
+ You requested the [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md) or [DeleteCustomKeyStore](#API_DeleteCustomKeyStore) operation on a custom key store that is not disconnected. `UpdateCustomKeyStore` can be called on a custom key store in the `CONNECTED` state only to update `NewCustomKeyStoreName`. For all other properties, the custom key store `ConnectionState` must be `DISCONNECTED`.
+ You requested the [GenerateRandom](API_GenerateRandom.md) operation in an AWS CloudHSM key store that is not connected. This operation is valid only when the AWS CloudHSM key store `ConnectionState` is `CONNECTED`.
HTTP Status Code: 400

 ** CustomKeyStoreNotFoundException **
The request was rejected because AWS KMS cannot find a custom key store with the specified key store name or ID.
HTTP Status Code: 400

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

## See Also
<a name="API_DeleteCustomKeyStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/DeleteCustomKeyStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/DeleteCustomKeyStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/DeleteCustomKeyStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/DeleteCustomKeyStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/DeleteCustomKeyStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/DeleteCustomKeyStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/DeleteCustomKeyStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/DeleteCustomKeyStore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/DeleteCustomKeyStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/DeleteCustomKeyStore)
