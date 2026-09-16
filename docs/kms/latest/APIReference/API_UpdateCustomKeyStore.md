---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdateCustomKeyStore.html
---

# UpdateCustomKeyStore
<a name="API_UpdateCustomKeyStore"></a>

Changes the properties of a custom key store. You can use this operation to change the properties of an AWS CloudHSM key store or an external key store.

Use the required `CustomKeyStoreId` parameter to identify the custom key store. Use the remaining optional parameters to change its properties. This operation does not return any property values. To verify the updated property values, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.

 This operation is part of the custom key stores feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a key store that you own and manage.

**Important**
When updating the properties of an external key store, verify that the updated settings connect your key store, via the external key store proxy, to the same external key manager as the previous settings, or to a backup or snapshot of the external key manager with the same cryptographic keys. If the updated connection settings fail, you can fix them and retry, although an extended delay might disrupt AWS services. However, if AWS KMS permanently loses its access to cryptographic keys, ciphertext encrypted under those keys is unrecoverable.

**Note**
For external key stores:
Some external key managers provide a simpler method for updating an external key store. For details, see your external key manager documentation.
When updating an external key store in the AWS KMS console, you can upload a JSON-based proxy configuration file with the desired values. You cannot upload the proxy configuration file to the `UpdateCustomKeyStore` operation. However, you can use the file to help you determine the correct values for the `UpdateCustomKeyStore` parameters.

For an AWS CloudHSM key store, you can use this operation to change the custom key store friendly name (`NewCustomKeyStoreName`), to tell AWS KMS about a change to the `kmsuser` crypto user password (`KeyStorePassword`), or to associate the custom key store with a different, but related, AWS CloudHSM cluster (`CloudHsmClusterId`). To update most properties of an AWS CloudHSM key store, the `ConnectionState` of the AWS CloudHSM key store must be `DISCONNECTED`. However, you can update the `CustomKeyStoreName` of an AWS CloudHSM key store when it is in the `CONNECTED` or `DISCONNECTED` state.

For an external key store, you can use this operation to change the custom key store friendly name (`NewCustomKeyStoreName`), or to tell AWS KMS about a change to the external key store proxy authentication credentials (`XksProxyAuthenticationCredential`), connection method (`XksProxyConnectivity`), external proxy endpoint (`XksProxyUriEndpoint`) and path (`XksProxyUriPath`). For external key stores with an `XksProxyConnectivity` of `VPC_ENDPOINT_SERVICE`, you can also update the Amazon VPC endpoint service name (`XksProxyVpcEndpointServiceName`). To update most properties of an external key store, the `ConnectionState` of the external key store must be `DISCONNECTED`. However, you can update the `CustomKeyStoreName`, `XksProxyAuthenticationCredential`, and `XksProxyUriPath` of an external key store when it is in the CONNECTED or DISCONNECTED state.

If your update requires a `DISCONNECTED` state, before using `UpdateCustomKeyStore`, use the [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md) operation to disconnect the custom key store. After the `UpdateCustomKeyStore` operation completes, use the [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md) to reconnect the custom key store. To find the `ConnectionState` of the custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.

Before updating the custom key store, verify that the new values allow AWS KMS to connect the custom key store to its backing key store. For example, before you change the `XksProxyUriPath` value, verify that the external key store proxy is reachable at the new path.

If the operation succeeds, it returns a JSON object with no properties.

 **Cross-account use**: No. You cannot perform this operation on a custom key store in a different AWS account.

 **Required permissions**: [kms:UpdateCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy)

 **Related operations:**
+  [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md)
+  [CreateCustomKeyStore](API_CreateCustomKeyStore.md)
+  [DeleteCustomKeyStore](API_DeleteCustomKeyStore.md)
+  [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md)
+  [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_UpdateCustomKeyStore_RequestSyntax"></a>

```
{
   "CloudHsmClusterId": "{{string}}",
   "CustomKeyStoreId": "{{string}}",
   "KeyStorePassword": "{{string}}",
   "NewCustomKeyStoreName": "{{string}}",
   "XksProxyAuthenticationCredential": {
      "AccessKeyId": "{{string}}",
      "RawSecretAccessKey": "{{string}}"
   },
   "XksProxyConnectivity": "{{string}}",
   "XksProxyUriEndpoint": "{{string}}",
   "XksProxyUriPath": "{{string}}",
   "XksProxyVpcEndpointServiceName": "{{string}}",
   "XksProxyVpcEndpointServiceOwner": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateCustomKeyStore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [CustomKeyStoreId](#API_UpdateCustomKeyStore_RequestSyntax) **   <a name="KMS-UpdateCustomKeyStore-request-CustomKeyStoreId"></a>
Identifies the custom key store that you want to update. Enter the ID of the custom key store. To find the ID of a custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [CloudHsmClusterId](#API_UpdateCustomKeyStore_RequestSyntax) **   <a name="KMS-UpdateCustomKeyStore-request-CloudHsmClusterId"></a>
Associates the custom key store with a related AWS CloudHSM cluster. This parameter is valid only for custom key stores with a `CustomKeyStoreType` of `AWS_CLOUDHSM`.
Enter the cluster ID of the cluster that you used to create the custom key store or a cluster that shares a backup history and has the same cluster certificate as the original cluster. You cannot use this parameter to associate a custom key store with an unrelated cluster. In addition, the replacement cluster must [fulfill the requirements](https://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html#before-keystore) for a cluster associated with a custom key store. To view the cluster certificate of a cluster, use the [DescribeClusters](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html) operation.
To change this value, the AWS CloudHSM key store must be disconnected.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 24.
Pattern: `cluster-[2-7a-zA-Z]{11,16}`
Required: No

 ** [KeyStorePassword](#API_UpdateCustomKeyStore_RequestSyntax) **   <a name="KMS-UpdateCustomKeyStore-request-KeyStorePassword"></a>
Enter the current password of the `kmsuser` crypto user (CU) in the AWS CloudHSM cluster that is associated with the custom key store. This parameter is valid only for custom key stores with a `CustomKeyStoreType` of `AWS_CLOUDHSM`.
This parameter tells AWS KMS the current password of the `kmsuser` crypto user (CU). It does not set or change the password of any users in the AWS CloudHSM cluster.
To change this value, the AWS CloudHSM key store must be disconnected.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 32.
Required: No

 ** [NewCustomKeyStoreName](#API_UpdateCustomKeyStore_RequestSyntax) **   <a name="KMS-UpdateCustomKeyStore-request-NewCustomKeyStoreName"></a>
Changes the friendly name of the custom key store to the value that you specify. The custom key store name must be unique in the AWS account.
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.
To change this value, the custom key store can be connected or disconnected.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [XksProxyAuthenticationCredential](#API_UpdateCustomKeyStore_RequestSyntax) **   <a name="KMS-UpdateCustomKeyStore-request-XksProxyAuthenticationCredential"></a>
Changes the credentials that AWS KMS uses to sign requests to the external key store proxy (XKS proxy). This parameter is valid only for custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE`.
You must specify both the `AccessKeyId` and `SecretAccessKey` value in the authentication credential, even if you are only updating one value.
This parameter doesn't establish or change your authentication credentials on the proxy. It just tells AWS KMS the credential that you established with your external key store proxy. For example, if you rotate the credential on your external key store proxy, you can use this parameter to update the credential in AWS KMS.
You can change this value when the external key store is connected or disconnected.
Type: [XksProxyAuthenticationCredentialType](API_XksProxyAuthenticationCredentialType.md) object
Required: No

 ** [XksProxyConnectivity](#API_UpdateCustomKeyStore_RequestSyntax) **   <a name="KMS-UpdateCustomKeyStore-request-XksProxyConnectivity"></a>
Changes the connectivity setting for the external key store. To indicate that the external key store proxy uses a Amazon VPC endpoint service to communicate with AWS KMS, specify `VPC_ENDPOINT_SERVICE`. Otherwise, specify `PUBLIC_ENDPOINT`.
If you change the `XksProxyConnectivity` to `VPC_ENDPOINT_SERVICE`, you must also change the `XksProxyUriEndpoint` and add an `XksProxyVpcEndpointServiceName` value.
If you change the `XksProxyConnectivity` to `PUBLIC_ENDPOINT`, you must also change the `XksProxyUriEndpoint` and specify a null or empty string for the `XksProxyVpcEndpointServiceName` value.
To change this value, the external key store must be disconnected.
Type: String
Valid Values: `PUBLIC_ENDPOINT | VPC_ENDPOINT_SERVICE`
Required: No

 ** [XksProxyUriEndpoint](#API_UpdateCustomKeyStore_RequestSyntax) **   <a name="KMS-UpdateCustomKeyStore-request-XksProxyUriEndpoint"></a>
Changes the URI endpoint that AWS KMS uses to connect to your external key store proxy (XKS proxy). This parameter is valid only for custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE`.
For external key stores with an `XksProxyConnectivity` value of `PUBLIC_ENDPOINT`, the protocol must be HTTPS.
For external key stores with an `XksProxyConnectivity` value of `VPC_ENDPOINT_SERVICE`, specify `https://` followed by the private DNS name associated with the VPC endpoint service. Each external key store must use a different private DNS name.
The combined `XksProxyUriEndpoint` and `XksProxyUriPath` values must be unique in the AWS account and Region.
To change this value, the external key store must be disconnected.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 128.
Pattern: `^https://[a-zA-Z0-9.-]+$`
Required: No

 ** [XksProxyUriPath](#API_UpdateCustomKeyStore_RequestSyntax) **   <a name="KMS-UpdateCustomKeyStore-request-XksProxyUriPath"></a>
Changes the base path to the proxy APIs for this external key store. To find this value, see the documentation for your external key manager and external key store proxy (XKS proxy). This parameter is valid only for custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE`.
The value must start with `/` and must end with `/kms/xks/v1`, where `v1` represents the version of the AWS KMS external key store proxy API. You can include an optional prefix between the required elements such as `/example/kms/xks/v1`.
The combined `XksProxyUriEndpoint` and `XksProxyUriPath` values must be unique in the AWS account and Region.
You can change this value when the external key store is connected or disconnected.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 128.
Pattern: `^(/[a-zA-Z0-9\/_-]+/kms/xks/v\d{1,2})$|^(/kms/xks/v\d{1,2})$`
Required: No

 ** [XksProxyVpcEndpointServiceName](#API_UpdateCustomKeyStore_RequestSyntax) **   <a name="KMS-UpdateCustomKeyStore-request-XksProxyVpcEndpointServiceName"></a>
Changes the name that AWS KMS uses to identify the Amazon VPC endpoint service for your external key store proxy (XKS proxy). This parameter is valid when the `CustomKeyStoreType` is `EXTERNAL_KEY_STORE` and the `XksProxyConnectivity` is `VPC_ENDPOINT_SERVICE`.
To change this value, the external key store must be disconnected.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `^(com|eu)\.amazonaws\.vpce\.([a-z]+-){2,3}\d+\.vpce-svc-[0-9a-z]+$`
Required: No

 ** [XksProxyVpcEndpointServiceOwner](#API_UpdateCustomKeyStore_RequestSyntax) **   <a name="KMS-UpdateCustomKeyStore-request-XksProxyVpcEndpointServiceOwner"></a>
Changes the AWS account ID that AWS KMS uses to identify the Amazon VPC endpoint service for your external key store proxy (XKS proxy). This parameter is optional. If not specified, the current AWS account ID for the VPC endpoint service will not be updated.
To change this value, the external key store must be disconnected.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

## Response Elements
<a name="API_UpdateCustomKeyStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateCustomKeyStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CloudHsmClusterInvalidConfigurationException **
The request was rejected because the associated AWS CloudHSM cluster did not meet the configuration requirements for an AWS CloudHSM key store.
+ The AWS CloudHSM cluster must be configured with private subnets in at least two different Availability Zones in the Region.
+ The [security group for the cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sg.html) (cloudhsm-cluster-*<cluster-id>*-sg) must include inbound rules and outbound rules that allow TCP traffic on ports 2223-2225. The **Source** in the inbound rules and the **Destination** in the outbound rules must match the security group ID. These rules are set by default when you create the AWS CloudHSM cluster. Do not delete or change them. To get information about a particular security group, use the [DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html) operation.
+ The AWS CloudHSM cluster must contain at least as many HSMs as the operation requires. To add HSMs, use the AWS CloudHSM [CreateHsm](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateHsm.html) operation.

  For the [CreateCustomKeyStore](API_CreateCustomKeyStore.md), [UpdateCustomKeyStore](#API_UpdateCustomKeyStore), and [CreateKey](API_CreateKey.md) operations, the AWS CloudHSM cluster must have at least two active HSMs, each in a different Availability Zone. For the [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md) operation, the AWS CloudHSM must contain at least one active HSM.
For information about the requirements for an AWS CloudHSM cluster that is associated with an AWS CloudHSM key store, see [Assemble the Prerequisites](https://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html#before-keystore) in the * AWS Key Management Service Developer Guide*. For information about creating a private subnet for an AWS CloudHSM cluster, see [Create a Private Subnet](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-subnets.html) in the * AWS CloudHSM User Guide*. For information about cluster security groups, see [Configure a Default Security Group](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sg.html) in the * * AWS CloudHSM User Guide* *.
HTTP Status Code: 400

 ** CloudHsmClusterNotActiveException **
The request was rejected because the AWS CloudHSM cluster associated with the AWS CloudHSM key store is not active. Initialize and activate the cluster and try the command again. For detailed instructions, see [Getting Started](https://docs.aws.amazon.com/cloudhsm/latest/userguide/getting-started.html) in the * AWS CloudHSM User Guide*.
HTTP Status Code: 400

 ** CloudHsmClusterNotFoundException **
The request was rejected because AWS KMS cannot find the AWS CloudHSM cluster with the specified cluster ID. Retry the request with a different cluster ID.
HTTP Status Code: 400

 ** CloudHsmClusterNotRelatedException **
The request was rejected because the specified AWS CloudHSM cluster has a different cluster certificate than the original cluster. You cannot use the operation to specify an unrelated cluster for an AWS CloudHSM key store.
Specify an AWS CloudHSM cluster that shares a backup history with the original cluster. This includes clusters that were created from a backup of the current cluster, and clusters that were created from the same backup that produced the current cluster.
 AWS CloudHSM clusters that share a backup history have the same cluster certificate. To view the cluster certificate of an AWS CloudHSM cluster, use the [DescribeClusters](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html) operation.
HTTP Status Code: 400

 ** CustomKeyStoreInvalidStateException **
The request was rejected because of the `ConnectionState` of the custom key store. To get the `ConnectionState` of a custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.
This exception is thrown under the following conditions:
+ You requested the [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md) operation on a custom key store with a `ConnectionState` of `DISCONNECTING` or `FAILED`. This operation is valid for all other `ConnectionState` values. To reconnect a custom key store in a `FAILED` state, disconnect it ([DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md)), then connect it (`ConnectCustomKeyStore`).
+ You requested the [CreateKey](API_CreateKey.md) operation in a custom key store that is not connected. This operations is valid only when the custom key store `ConnectionState` is `CONNECTED`.
+ You requested the [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md) operation on a custom key store with a `ConnectionState` of `DISCONNECTING` or `DISCONNECTED`. This operation is valid for all other `ConnectionState` values.
+ You requested the [UpdateCustomKeyStore](#API_UpdateCustomKeyStore) or [DeleteCustomKeyStore](API_DeleteCustomKeyStore.md) operation on a custom key store that is not disconnected. `UpdateCustomKeyStore` can be called on a custom key store in the `CONNECTED` state only to update `NewCustomKeyStoreName`. For all other properties, the custom key store `ConnectionState` must be `DISCONNECTED`.
+ You requested the [GenerateRandom](API_GenerateRandom.md) operation in an AWS CloudHSM key store that is not connected. This operation is valid only when the AWS CloudHSM key store `ConnectionState` is `CONNECTED`.
HTTP Status Code: 400

 ** CustomKeyStoreNameInUseException **
The request was rejected because the specified custom key store name is already assigned to another custom key store in the account. Try again with a custom key store name that is unique in the account.
HTTP Status Code: 400

 ** CustomKeyStoreNotFoundException **
The request was rejected because AWS KMS cannot find a custom key store with the specified key store name or ID.
HTTP Status Code: 400

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

 ** XksProxyIncorrectAuthenticationCredentialException **
The request was rejected because the proxy credentials failed to authenticate to the specified external key store proxy. The specified external key store proxy rejected a status request from AWS KMS due to invalid credentials. This can indicate an error in the credentials or in the identification of the external key store proxy.
HTTP Status Code: 400

 ** XksProxyInvalidConfigurationException **
The request was rejected because the external key store proxy is not configured correctly. To identify the cause, see the error message that accompanies the exception.
HTTP Status Code: 400

 ** XksProxyInvalidResponseException **

 AWS KMS cannot interpret the response it received from the external key store proxy. The problem might be a poorly constructed response, but it could also be a transient network issue. If you see this error repeatedly, report it to the proxy vendor.
HTTP Status Code: 400

 ** XksProxyUriEndpointInUseException **
The request was rejected because the `XksProxyUriEndpoint` is already associated with another external key store in this AWS Region. To identify the cause, see the error message that accompanies the exception.
HTTP Status Code: 400

 ** XksProxyUriInUseException **
The request was rejected because the concatenation of the `XksProxyUriEndpoint` and `XksProxyUriPath` is already associated with another external key store in this AWS Region. Each external key store in a Region must use a unique external key store proxy API address.
HTTP Status Code: 400

 ** XksProxyUriUnreachableException **
 AWS KMS was unable to reach the specified `XksProxyUriPath`. The path must be reachable before you create the external key store or update its settings.
This exception is also thrown when the external key store proxy response to a `GetHealthStatus` request indicates that all external key manager instances are unavailable.
HTTP Status Code: 400

 ** XksProxyVpcEndpointServiceInUseException **
The request was rejected because the specified Amazon VPC endpoint service is already associated with another external key store in this AWS Region. Each external key store in a Region must use a different Amazon VPC endpoint service.
HTTP Status Code: 400

 ** XksProxyVpcEndpointServiceInvalidConfigurationException **
The request was rejected because the Amazon VPC endpoint service configuration does not fulfill the requirements for an external key store. To identify the cause, see the error message that accompanies the exception and [review the requirements](https://docs.aws.amazon.com/kms/latest/developerguide/vpc-connectivity.html#xks-vpc-requirements) for Amazon VPC endpoint service connectivity for an external key store.
HTTP Status Code: 400

 ** XksProxyVpcEndpointServiceNotFoundException **
The request was rejected because AWS KMS could not find the specified VPC endpoint service. Use [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) to verify the VPC endpoint service name for the external key store. Also, confirm that the `Allow principals` list for the VPC endpoint service includes the AWS KMS service principal for the Region, such as `cks.kms.us-east-1.amazonaws.com`.
HTTP Status Code: 400

## See Also
<a name="API_UpdateCustomKeyStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/UpdateCustomKeyStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/UpdateCustomKeyStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/UpdateCustomKeyStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/UpdateCustomKeyStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/UpdateCustomKeyStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/UpdateCustomKeyStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/UpdateCustomKeyStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/UpdateCustomKeyStore)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/UpdateCustomKeyStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/UpdateCustomKeyStore)
