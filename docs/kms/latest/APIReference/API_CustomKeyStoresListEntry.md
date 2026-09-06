---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_CustomKeyStoresListEntry.html
---

# CustomKeyStoresListEntry
<a name="API_CustomKeyStoresListEntry"></a>

Contains information about each custom key store in the custom key store list.

## Contents
<a name="API_CustomKeyStoresListEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CloudHsmClusterId **   <a name="KMS-Type-CustomKeyStoresListEntry-CloudHsmClusterId"></a>
A unique identifier for the AWS CloudHSM cluster that is associated with an AWS CloudHSM key store. This field appears only when the `CustomKeyStoreType` is `AWS_CLOUDHSM`.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 24.
Pattern: `cluster-[2-7a-zA-Z]{11,16}`
Required: No

 ** ConnectionErrorCode **   <a name="KMS-Type-CustomKeyStoresListEntry-ConnectionErrorCode"></a>
Describes the connection error. This field appears in the response only when the `ConnectionState` is `FAILED`.
Many failures can be resolved by updating the properties of the custom key store. To update a custom key store, disconnect it ([DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md)), correct the errors ([UpdateCustomKeyStore](API_UpdateCustomKeyStore.md)), and try to connect again ([ConnectCustomKeyStore](API_ConnectCustomKeyStore.md)). For additional help resolving these errors, see [How to Fix a Connection Failure](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#fix-keystore-failed) in * AWS Key Management Service Developer Guide*.
 **All custom key stores:**
+  `INTERNAL_ERROR` — AWS KMS could not complete the request due to an internal error. Retry the request. For `ConnectCustomKeyStore` requests, disconnect the custom key store before trying to connect again.
+  `NETWORK_ERRORS` — Network errors are preventing AWS KMS from connecting the custom key store to its backing key store.
 ** AWS CloudHSM key stores:**
+  `CLUSTER_NOT_FOUND` — AWS KMS cannot find the AWS CloudHSM cluster with the specified cluster ID.
+  `INSUFFICIENT_CLOUDHSM_HSMS` — The associated AWS CloudHSM cluster does not contain any active HSMs. To connect a custom key store to its AWS CloudHSM cluster, the cluster must contain at least one active HSM.
+  `INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET` — At least one private subnet associated with the AWS CloudHSM cluster doesn't have any available IP addresses. A AWS CloudHSM key store connection requires one free IP address in each of the associated private subnets, although two are preferable. For details, see [How to Fix a Connection Failure](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#fix-keystore-failed) in the * AWS Key Management Service Developer Guide*.
+  `INVALID_CREDENTIALS` — The `KeyStorePassword` for the custom key store doesn't match the current password of the `kmsuser` crypto user in the AWS CloudHSM cluster. Before you can connect your custom key store to its AWS CloudHSM cluster, you must change the `kmsuser` account password and update the `KeyStorePassword` value for the custom key store.
+  `SUBNET_NOT_FOUND` — A subnet in the AWS CloudHSM cluster configuration was deleted. If AWS KMS cannot find all of the subnets in the cluster configuration, attempts to connect the custom key store to the AWS CloudHSM cluster fail. To fix this error, create a cluster from a recent backup and associate it with your custom key store. (This process creates a new cluster configuration with a VPC and private subnets.) For details, see [How to Fix a Connection Failure](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#fix-keystore-failed) in the * AWS Key Management Service Developer Guide*.
+  `USER_LOCKED_OUT` — The `kmsuser` CU account is locked out of the associated AWS CloudHSM cluster due to too many failed password attempts. Before you can connect your custom key store to its AWS CloudHSM cluster, you must change the `kmsuser` account password and update the key store password value for the custom key store.
+  `USER_LOGGED_IN` — The `kmsuser` CU account is logged into the associated AWS CloudHSM cluster. This prevents AWS KMS from rotating the `kmsuser` account password and logging into the cluster. Before you can connect your custom key store to its AWS CloudHSM cluster, you must log the `kmsuser` CU out of the cluster. If you changed the `kmsuser` password to log into the cluster, you must also and update the key store password value for the custom key store. For help, see [How to Log Out and Reconnect](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#login-kmsuser-2) in the * AWS Key Management Service Developer Guide*.
+  `USER_NOT_FOUND` — AWS KMS cannot find a `kmsuser` CU account in the associated AWS CloudHSM cluster. Before you can connect your custom key store to its AWS CloudHSM cluster, you must create a `kmsuser` CU account in the cluster, and then update the key store password value for the custom key store.
 **External key stores:**
+  `INVALID_CREDENTIALS` — One or both of the `XksProxyAuthenticationCredential` values is not valid on the specified external key store proxy.
+  `XKS_PROXY_ACCESS_DENIED` — AWS KMS requests are denied access to the external key store proxy. If the external key store proxy has authorization rules, verify that they permit AWS KMS to communicate with the proxy on your behalf.
+  `XKS_PROXY_INVALID_CONFIGURATION` — A configuration error is preventing the external key store from connecting to its proxy. Verify the value of the `XksProxyUriPath`.
+  `XKS_PROXY_INVALID_RESPONSE` — AWS KMS cannot interpret the response from the external key store proxy. If you see this connection error code repeatedly, notify your external key store proxy vendor.
+  `XKS_PROXY_INVALID_TLS_CONFIGURATION` — AWS KMS cannot connect to the external key store proxy because the TLS configuration is invalid. Verify that the XKS proxy supports TLS 1.2 or 1.3. Also, verify that the TLS certificate is not expired, and that it matches the hostname in the `XksProxyUriEndpoint` value, and that it is signed by a certificate authority included in the [Trusted Certificate Authorities](https://github.com/aws/aws-kms-xksproxy-api-spec/blob/main/TrustedCertificateAuthorities) list.
+  `XKS_PROXY_NOT_REACHABLE` — AWS KMS can't communicate with your external key store proxy. Verify that the `XksProxyUriEndpoint` and `XksProxyUriPath` are correct. Use the tools for your external key store proxy to verify that the proxy is active and available on its network. Also, verify that your external key manager instances are operating properly. Connection attempts fail with this connection error code if the proxy reports that all external key manager instances are unavailable.
+  `XKS_PROXY_TIMED_OUT` — AWS KMS can connect to the external key store proxy, but the proxy does not respond to AWS KMS in the time allotted. If you see this connection error code repeatedly, notify your external key store proxy vendor.
+  `XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION` — The Amazon VPC endpoint service configuration doesn't conform to the requirements for an AWS KMS external key store.
  + The VPC endpoint service must be an endpoint service for interface endpoints in the caller's AWS account.
  + It must have a network load balancer (NLB) connected to at least two subnets, each in a different Availability Zone.
  + The `Allow principals` list must include the AWS KMS service principal for the Region, `cks.kms.<region>.amazonaws.com`, such as `cks.kms.us-east-1.amazonaws.com`.
  + It must *not* require [acceptance](https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html) of connection requests.
  + It must have a private DNS name. The private DNS name for an external key store with `VPC_ENDPOINT_SERVICE` connectivity must be unique in its AWS Region.
  + The domain of the private DNS name must have a [verification status](https://docs.aws.amazon.com/vpc/latest/privatelink/verify-domains.html) of `verified`.
  + The [TLS certificate](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html) specifies the private DNS hostname at which the endpoint is reachable.
+  `XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND` — AWS KMS can't find the VPC endpoint service that it uses to communicate with the external key store proxy. Verify that the `XksProxyVpcEndpointServiceName` is correct and the AWS KMS service principal has service consumer permissions on the Amazon VPC endpoint service.
Type: String
Valid Values: `INVALID_CREDENTIALS | CLUSTER_NOT_FOUND | NETWORK_ERRORS | INTERNAL_ERROR | INSUFFICIENT_CLOUDHSM_HSMS | USER_LOCKED_OUT | USER_NOT_FOUND | USER_LOGGED_IN | SUBNET_NOT_FOUND | INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET | XKS_PROXY_ACCESS_DENIED | XKS_PROXY_NOT_REACHABLE | XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND | XKS_PROXY_INVALID_RESPONSE | XKS_PROXY_INVALID_CONFIGURATION | XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION | XKS_PROXY_TIMED_OUT | XKS_PROXY_INVALID_TLS_CONFIGURATION`
Required: No

 ** ConnectionState **   <a name="KMS-Type-CustomKeyStoresListEntry-ConnectionState"></a>
Indicates whether the custom key store is connected to its backing key store. For an AWS CloudHSM key store, the `ConnectionState` indicates whether it is connected to its AWS CloudHSM cluster. For an external key store, the `ConnectionState` indicates whether it is connected to the external key store proxy that communicates with your external key manager.
You can create and use KMS keys in your custom key stores only when its `ConnectionState` is `CONNECTED`.
The `ConnectionState` value is `DISCONNECTED` only if the key store has never been connected or you use the [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md) operation to disconnect it. If the value is `CONNECTED` but you are having trouble using the custom key store, make sure that the backing key store is reachable and active. For an AWS CloudHSM key store, verify that its associated AWS CloudHSM cluster is active and contains at least one active HSM. For an external key store, verify that the external key store proxy and external key manager are connected and enabled.
A value of `FAILED` indicates that an attempt to connect was unsuccessful. The `ConnectionErrorCode` field in the response indicates the cause of the failure. For help resolving a connection failure, see [Troubleshooting a custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html) in the * AWS Key Management Service Developer Guide*.
Type: String
Valid Values: `CONNECTED | CONNECTING | FAILED | DISCONNECTED | DISCONNECTING`
Required: No

 ** CreationDate **   <a name="KMS-Type-CustomKeyStoresListEntry-CreationDate"></a>
The date and time when the custom key store was created.
Type: Timestamp
Required: No

 ** CustomKeyStoreId **   <a name="KMS-Type-CustomKeyStoresListEntry-CustomKeyStoreId"></a>
A unique identifier for the custom key store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** CustomKeyStoreName **   <a name="KMS-Type-CustomKeyStoresListEntry-CustomKeyStoreName"></a>
The user-specified friendly name for the custom key store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** CustomKeyStoreType **   <a name="KMS-Type-CustomKeyStoresListEntry-CustomKeyStoreType"></a>
Indicates the type of the custom key store. `AWS_CLOUDHSM` indicates a custom key store backed by an AWS CloudHSM cluster. `EXTERNAL_KEY_STORE` indicates a custom key store backed by an external key store proxy and external key manager outside of AWS.
Type: String
Valid Values: `AWS_CLOUDHSM | EXTERNAL_KEY_STORE`
Required: No

 ** TrustAnchorCertificate **   <a name="KMS-Type-CustomKeyStoresListEntry-TrustAnchorCertificate"></a>
The trust anchor certificate of the AWS CloudHSM cluster associated with an AWS CloudHSM key store. When you [initialize the cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/initialize-cluster.html#sign-csr), you create this certificate and save it in the `customerCA.crt` file.
This field appears only when the `CustomKeyStoreType` is `AWS_CLOUDHSM`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.
Required: No

 ** XksProxyConfiguration **   <a name="KMS-Type-CustomKeyStoresListEntry-XksProxyConfiguration"></a>
Configuration settings for the external key store proxy (XKS proxy). The external key store proxy translates AWS KMS requests into a format that your external key manager can understand. The proxy configuration includes connection information that AWS KMS requires.
This field appears only when the `CustomKeyStoreType` is `EXTERNAL_KEY_STORE`.
Type: [XksProxyConfigurationType](API_XksProxyConfigurationType.md) object
Required: No

## See Also
<a name="API_CustomKeyStoresListEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/CustomKeyStoresListEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/CustomKeyStoresListEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/CustomKeyStoresListEntry)
