---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_ConnectCustomKeyStore.html
---

# ConnectCustomKeyStore
<a name="API_ConnectCustomKeyStore"></a>

Connects or reconnects a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html) to its backing key store. For an AWS CloudHSM key store, `ConnectCustomKeyStore` connects the key store to its associated AWS CloudHSM cluster. For an external key store, `ConnectCustomKeyStore` connects the key store to the external key store proxy that communicates with your external key manager.

The custom key store must be connected before you can create KMS keys in the key store or use the KMS keys it contains. You can disconnect and reconnect a custom key store at any time.

The connection process for a custom key store can take an extended amount of time to complete. This operation starts the connection process, but it does not wait for it to complete. When it succeeds, this operation quickly returns an HTTP 200 response and a JSON object with no properties. However, this response does not indicate that the custom key store is connected. To get the connection state of the custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.

 This operation is part of the custom key stores feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a key store that you own and manage.

The `ConnectCustomKeyStore` operation might fail for various reasons. To find the reason, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation and see the `ConnectionErrorCode` in the response. For help interpreting the `ConnectionErrorCode`, see [CustomKeyStoresListEntry](API_CustomKeyStoresListEntry.md).

To fix the failure, use the [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md) operation to disconnect the custom key store, correct the error, use the [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md) operation if necessary, and then use `ConnectCustomKeyStore` again.

 ** AWS CloudHSM key store**

During the connection process for an AWS CloudHSM key store, AWS KMS finds the AWS CloudHSM cluster that is associated with the custom key store, creates the connection infrastructure, connects to the cluster, logs into the AWS CloudHSM client as the `kmsuser` CU, and rotates its password.

To connect an AWS CloudHSM key store, its associated AWS CloudHSM cluster must have at least one active HSM. To get the number of active HSMs in a cluster, use the [DescribeClusters](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html) operation. To add HSMs to the cluster, use the [CreateHsm](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateHsm.html) operation. Also, the [`kmsuser` crypto user](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html#concept-kmsuser) (CU) must not be logged into the cluster. This prevents AWS KMS from using this account to log in.

If you are having trouble connecting or disconnecting a AWS CloudHSM key store, see [Troubleshooting an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html) in the * AWS Key Management Service Developer Guide*.

 **External key store**

When you connect an external key store that uses public endpoint connectivity, AWS KMS tests its ability to communicate with your external key manager by sending a request via the external key store proxy.

When you connect to an external key store that uses VPC endpoint service connectivity, AWS KMS establishes the networking elements that it needs to communicate with your external key manager via the external key store proxy. This includes creating an interface endpoint to the VPC endpoint service and a private hosted zone for traffic between AWS KMS and the VPC endpoint service.

To connect an external key store, AWS KMS must be able to connect to the external key store proxy, the external key store proxy must be able to communicate with your external key manager, and the external key manager must be available for cryptographic operations.

If you are having trouble connecting or disconnecting an external key store, see [Troubleshooting an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/xks-troubleshooting.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: No. You cannot perform this operation on a custom key store in a different AWS account.

 **Required permissions**: [kms:ConnectCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy)

 **Related operations**
+  [CreateCustomKeyStore](API_CreateCustomKeyStore.md)
+  [DeleteCustomKeyStore](API_DeleteCustomKeyStore.md)
+  [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md)
+  [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md)
+  [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_ConnectCustomKeyStore_RequestSyntax"></a>

```
{
   "CustomKeyStoreId": "{{string}}"
}
```

## Request Parameters
<a name="API_ConnectCustomKeyStore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [CustomKeyStoreId](#API_ConnectCustomKeyStore_RequestSyntax) **   <a name="KMS-ConnectCustomKeyStore-request-CustomKeyStoreId"></a>
Enter the key store ID of the custom key store that you want to connect. To find the ID of a custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Elements
<a name="API_ConnectCustomKeyStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ConnectCustomKeyStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CloudHsmClusterInvalidConfigurationException **
The request was rejected because the associated AWS CloudHSM cluster did not meet the configuration requirements for an AWS CloudHSM key store.
+ The AWS CloudHSM cluster must be configured with private subnets in at least two different Availability Zones in the Region.
+ The [security group for the cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sg.html) (cloudhsm-cluster-*<cluster-id>*-sg) must include inbound rules and outbound rules that allow TCP traffic on ports 2223-2225. The **Source** in the inbound rules and the **Destination** in the outbound rules must match the security group ID. These rules are set by default when you create the AWS CloudHSM cluster. Do not delete or change them. To get information about a particular security group, use the [DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html) operation.
+ The AWS CloudHSM cluster must contain at least as many HSMs as the operation requires. To add HSMs, use the AWS CloudHSM [CreateHsm](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateHsm.html) operation.

  For the [CreateCustomKeyStore](API_CreateCustomKeyStore.md), [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md), and [CreateKey](API_CreateKey.md) operations, the AWS CloudHSM cluster must have at least two active HSMs, each in a different Availability Zone. For the [ConnectCustomKeyStore](#API_ConnectCustomKeyStore) operation, the AWS CloudHSM must contain at least one active HSM.
For information about the requirements for an AWS CloudHSM cluster that is associated with an AWS CloudHSM key store, see [Assemble the Prerequisites](https://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html#before-keystore) in the * AWS Key Management Service Developer Guide*. For information about creating a private subnet for an AWS CloudHSM cluster, see [Create a Private Subnet](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-subnets.html) in the * AWS CloudHSM User Guide*. For information about cluster security groups, see [Configure a Default Security Group](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sg.html) in the * * AWS CloudHSM User Guide* *.
HTTP Status Code: 400

 ** CloudHsmClusterNotActiveException **
The request was rejected because the AWS CloudHSM cluster associated with the AWS CloudHSM key store is not active. Initialize and activate the cluster and try the command again. For detailed instructions, see [Getting Started](https://docs.aws.amazon.com/cloudhsm/latest/userguide/getting-started.html) in the * AWS CloudHSM User Guide*.
HTTP Status Code: 400

 ** CustomKeyStoreInvalidStateException **
The request was rejected because of the `ConnectionState` of the custom key store. To get the `ConnectionState` of a custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.
This exception is thrown under the following conditions:
+ You requested the [ConnectCustomKeyStore](#API_ConnectCustomKeyStore) operation on a custom key store with a `ConnectionState` of `DISCONNECTING` or `FAILED`. This operation is valid for all other `ConnectionState` values. To reconnect a custom key store in a `FAILED` state, disconnect it ([DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md)), then connect it (`ConnectCustomKeyStore`).
+ You requested the [CreateKey](API_CreateKey.md) operation in a custom key store that is not connected. This operations is valid only when the custom key store `ConnectionState` is `CONNECTED`.
+ You requested the [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md) operation on a custom key store with a `ConnectionState` of `DISCONNECTING` or `DISCONNECTED`. This operation is valid for all other `ConnectionState` values.
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
<a name="API_ConnectCustomKeyStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/ConnectCustomKeyStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/ConnectCustomKeyStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/ConnectCustomKeyStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/ConnectCustomKeyStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/ConnectCustomKeyStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/ConnectCustomKeyStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/ConnectCustomKeyStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/ConnectCustomKeyStore)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/ConnectCustomKeyStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/ConnectCustomKeyStore)
