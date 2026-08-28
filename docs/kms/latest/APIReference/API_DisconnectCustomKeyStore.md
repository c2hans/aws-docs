---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_DisconnectCustomKeyStore.html
---

# DisconnectCustomKeyStore
<a name="API_DisconnectCustomKeyStore"></a>

Disconnects the [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html) from its backing key store. This operation disconnects an AWS CloudHSM key store from its associated AWS CloudHSM cluster or disconnects an external key store from the external key store proxy that communicates with your external key manager.

 This operation is part of the custom key stores feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a key store that you own and manage.

While a custom key store is disconnected, you can manage the custom key store and its KMS keys, but you cannot create or use its KMS keys. You can reconnect the custom key store at any time.

**Note**
While a custom key store is disconnected, all attempts to create KMS keys in the custom key store or to use existing KMS keys in [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#cryptographic-operations) will fail. This action can prevent users from storing and accessing sensitive data.

When you disconnect a custom key store, its `ConnectionState` changes to `Disconnected`. To find the connection state of a custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation. To reconnect a custom key store, use the [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md) operation.

If the operation succeeds, it returns a JSON object with no properties.

 **Cross-account use**: No. You cannot perform this operation on a custom key store in a different AWS account.

 **Required permissions**: [kms:DisconnectCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy)

 **Related operations:**
+  [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md)
+  [CreateCustomKeyStore](API_CreateCustomKeyStore.md)
+  [DeleteCustomKeyStore](API_DeleteCustomKeyStore.md)
+  [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md)
+  [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_DisconnectCustomKeyStore_RequestSyntax"></a>

```
{
   "CustomKeyStoreId": "{{string}}"
}
```

## Request Parameters
<a name="API_DisconnectCustomKeyStore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [CustomKeyStoreId](#API_DisconnectCustomKeyStore_RequestSyntax) **   <a name="KMS-DisconnectCustomKeyStore-request-CustomKeyStoreId"></a>
Enter the ID of the custom key store you want to disconnect. To find the ID of a custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Elements
<a name="API_DisconnectCustomKeyStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisconnectCustomKeyStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CustomKeyStoreInvalidStateException **
The request was rejected because of the `ConnectionState` of the custom key store. To get the `ConnectionState` of a custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.
This exception is thrown under the following conditions:
+ You requested the [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md) operation on a custom key store with a `ConnectionState` of `DISCONNECTING` or `FAILED`. This operation is valid for all other `ConnectionState` values. To reconnect a custom key store in a `FAILED` state, disconnect it ([DisconnectCustomKeyStore](#API_DisconnectCustomKeyStore)), then connect it (`ConnectCustomKeyStore`).
+ You requested the [CreateKey](API_CreateKey.md) operation in a custom key store that is not connected. This operations is valid only when the custom key store `ConnectionState` is `CONNECTED`.
+ You requested the [DisconnectCustomKeyStore](#API_DisconnectCustomKeyStore) operation on a custom key store with a `ConnectionState` of `DISCONNECTING` or `DISCONNECTED`. This operation is valid for all other `ConnectionState` values.
+ You requested the [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md) or [DeleteCustomKeyStore](API_DeleteCustomKeyStore.md) operation on a custom key store that is not disconnected. `UpdateCustomKeyStore` can be called on a custom key store in the `CONNECTED` state only to update `NewCustomKeyStoreName`. For all other properties, the custom key store `ConnectionState` must be `DISCONNECTED`.
+ You requested the [GenerateRandom](API_GenerateRandom.md) operation in an AWS CloudHSM key store that is not connected. This operation is valid only when the AWS CloudHSM key store `ConnectionState` is `CONNECTED`.
HTTP Status Code: 400

 ** CustomKeyStoreNotFoundException **
The request was rejected because AWS KMS cannot find a custom key store with the specified key store name or ID.
HTTP Status Code: 400

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

## See Also
<a name="API_DisconnectCustomKeyStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/DisconnectCustomKeyStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/DisconnectCustomKeyStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/DisconnectCustomKeyStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/DisconnectCustomKeyStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/DisconnectCustomKeyStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/DisconnectCustomKeyStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/DisconnectCustomKeyStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/DisconnectCustomKeyStore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/DisconnectCustomKeyStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/DisconnectCustomKeyStore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
