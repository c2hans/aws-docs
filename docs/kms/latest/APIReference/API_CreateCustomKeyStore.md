---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateCustomKeyStore.html
---

# CreateCustomKeyStore
<a name="API_CreateCustomKeyStore"></a>

Creates a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html) backed by a key store that you own and manage. When you use a KMS key in a custom key store for a cryptographic operation, the cryptographic operation is actually performed in your key store using your keys. AWS KMS supports [AWS CloudHSM key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html) backed by an [AWS CloudHSM cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/clusters.html) and [external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html) backed by an external key store proxy and external key manager outside of AWS.

 This operation is part of the custom key stores feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a key store that you own and manage.

Before you create the custom key store, the required elements must be in place and operational. We recommend that you use the test tools that AWS KMS provides to verify the configuration your external key store proxy. For details about the required elements and verification tests, see [Assemble the prerequisites (for AWS CloudHSM key stores)](https://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html#before-keystore) or [Assemble the prerequisites (for external key stores)](https://docs.aws.amazon.com/kms/latest/developerguide/create-xks-keystore.html#xks-requirements) in the * AWS Key Management Service Developer Guide*.

To create a custom key store, use the following parameters.
+ To create an AWS CloudHSM key store, specify the `CustomKeyStoreName`, `CloudHsmClusterId`, `KeyStorePassword`, and `TrustAnchorCertificate`. The `CustomKeyStoreType` parameter is optional for AWS CloudHSM key stores. If you include it, set it to the default value, `AWS_CLOUDHSM`. For help with failures, see [Troubleshooting an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html) in the * AWS Key Management Service Developer Guide*.
+ To create an external key store, specify the `CustomKeyStoreName` and a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE`. Also, specify values for `XksProxyConnectivity`, `XksProxyAuthenticationCredential`, `XksProxyUriEndpoint`, and `XksProxyUriPath`. If your `XksProxyConnectivity` value is `VPC_ENDPOINT_SERVICE`, specify the `XksProxyVpcEndpointServiceName` parameter. For help with failures, see [Troubleshooting an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/xks-troubleshooting.html) in the * AWS Key Management Service Developer Guide*.

**Note**
For external key stores:
Some external key managers provide a simpler method for creating an external key store. For details, see your external key manager documentation.
When creating an external key store in the AWS KMS console, you can upload a JSON-based proxy configuration file with the desired values. You cannot use a proxy configuration with the `CreateCustomKeyStore` operation. However, you can use the values in the file to help you determine the correct values for the `CreateCustomKeyStore` parameters.

When the operation completes successfully, it returns the ID of the new custom key store. Before you can use your new custom key store, you need to use the [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md) operation to connect a new AWS CloudHSM key store to its AWS CloudHSM cluster, or to connect a new external key store to the external key store proxy for your external key manager. Even if you are not going to use your custom key store immediately, you might want to connect it to verify that all settings are correct and then disconnect it until you are ready to use it.

 **Cross-account use**: No. You cannot perform this operation on a custom key store in a different AWS account.

 **Required permissions**: [kms:CreateCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy).

 **Related operations:**
+  [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md)
+  [DeleteCustomKeyStore](API_DeleteCustomKeyStore.md)
+  [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md)
+  [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md)
+  [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_CreateCustomKeyStore_RequestSyntax"></a>

```
{
   "CloudHsmClusterId": "{{string}}",
   "CustomKeyStoreName": "{{string}}",
   "CustomKeyStoreType": "{{string}}",
   "KeyStorePassword": "{{string}}",
   "TrustAnchorCertificate": "{{string}}",
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
<a name="API_CreateCustomKeyStore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [CustomKeyStoreName](#API_CreateCustomKeyStore_RequestSyntax) **   <a name="KMS-CreateCustomKeyStore-request-CustomKeyStoreName"></a>
Specifies a friendly name for the custom key store. The name must be unique in your AWS account and Region. This parameter is required for all custom key stores.
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [CloudHsmClusterId](#API_CreateCustomKeyStore_RequestSyntax) **   <a name="KMS-CreateCustomKeyStore-request-CloudHsmClusterId"></a>
Identifies the AWS CloudHSM cluster for an AWS CloudHSM key store. This parameter is required for custom key stores with `CustomKeyStoreType` of `AWS_CLOUDHSM`.
Enter the cluster ID of any active AWS CloudHSM cluster that is not already associated with a custom key store. To find the cluster ID, use the [DescribeClusters](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html) operation.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 24.
Pattern: `cluster-[2-7a-zA-Z]{11,16}`
Required: No

 ** [CustomKeyStoreType](#API_CreateCustomKeyStore_RequestSyntax) **   <a name="KMS-CreateCustomKeyStore-request-CustomKeyStoreType"></a>
Specifies the type of custom key store. The default value is `AWS_CLOUDHSM`.
For a custom key store backed by an AWS CloudHSM cluster, omit the parameter or enter `AWS_CLOUDHSM`. For a custom key store backed by an external key manager outside of AWS, enter `EXTERNAL_KEY_STORE`. You cannot change this property after the key store is created.
Type: String
Valid Values: `AWS_CLOUDHSM | EXTERNAL_KEY_STORE`
Required: No

 ** [KeyStorePassword](#API_CreateCustomKeyStore_RequestSyntax) **   <a name="KMS-CreateCustomKeyStore-request-KeyStorePassword"></a>
Specifies the `kmsuser` password for an AWS CloudHSM key store. This parameter is required for custom key stores with a `CustomKeyStoreType` of `AWS_CLOUDHSM`.
Enter the password of the [`kmsuser` crypto user (CU) account](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html#concept-kmsuser) in the specified AWS CloudHSM cluster. AWS KMS logs into the cluster as this user to manage key material on your behalf.
The password must be a string of 7 to 32 characters. Its value is case sensitive.
This parameter tells AWS KMS the `kmsuser` account password; it does not change the password in the AWS CloudHSM cluster.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 32.
Required: No

 ** [TrustAnchorCertificate](#API_CreateCustomKeyStore_RequestSyntax) **   <a name="KMS-CreateCustomKeyStore-request-TrustAnchorCertificate"></a>
Specifies the certificate for an AWS CloudHSM key store. This parameter is required for custom key stores with a `CustomKeyStoreType` of `AWS_CLOUDHSM`.
Enter the content of the trust anchor certificate for the AWS CloudHSM cluster. This is the content of the `customerCA.crt` file that you created when you [initialized the cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/initialize-cluster.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.
Required: No

 ** [XksProxyAuthenticationCredential](#API_CreateCustomKeyStore_RequestSyntax) **   <a name="KMS-CreateCustomKeyStore-request-XksProxyAuthenticationCredential"></a>
Specifies an authentication credential for the external key store proxy (XKS proxy). This parameter is required for all custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE`.
The `XksProxyAuthenticationCredential` has two required elements: `RawSecretAccessKey`, a secret key, and `AccessKeyId`, a unique identifier for the `RawSecretAccessKey`. For character requirements, see [XksProxyAuthenticationCredentialType](API_XksProxyAuthenticationCredentialType.html).
 AWS KMS uses this authentication credential to sign requests to the external key store proxy on your behalf. This credential is unrelated to AWS Identity and Access Management (IAM) and AWS credentials.
This parameter doesn't set or change the authentication credentials on the XKS proxy. It just tells AWS KMS the credential that you established on your external key store proxy. If you rotate your proxy authentication credential, use the [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md) operation to provide the new credential to AWS KMS.
Type: [XksProxyAuthenticationCredentialType](API_XksProxyAuthenticationCredentialType.md) object
Required: No

 ** [XksProxyConnectivity](#API_CreateCustomKeyStore_RequestSyntax) **   <a name="KMS-CreateCustomKeyStore-request-XksProxyConnectivity"></a>
Indicates how AWS KMS communicates with the external key store proxy. This parameter is required for custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE`.
If the external key store proxy uses a public endpoint, specify `PUBLIC_ENDPOINT`. If the external key store proxy uses a Amazon VPC endpoint service for communication with AWS KMS, specify `VPC_ENDPOINT_SERVICE`. For help making this choice, see [Choosing a connectivity option](https://docs.aws.amazon.com/kms/latest/developerguide/choose-xks-connectivity.html) in the * AWS Key Management Service Developer Guide*.
An Amazon VPC endpoint service keeps your communication with AWS KMS in a private address space entirely within AWS, but it requires more configuration, including establishing a Amazon VPC with multiple subnets, a VPC endpoint service, a network load balancer, and a verified private DNS name. A public endpoint is simpler to set up, but it might be slower and might not fulfill your security requirements. You might consider testing with a public endpoint, and then establishing a VPC endpoint service for production tasks. Note that this choice does not determine the location of the external key store proxy. Even if you choose a VPC endpoint service, the proxy can be hosted within the VPC or outside of AWS such as in your corporate data center.
Type: String
Valid Values: `PUBLIC_ENDPOINT | VPC_ENDPOINT_SERVICE`
Required: No

 ** [XksProxyUriEndpoint](#API_CreateCustomKeyStore_RequestSyntax) **   <a name="KMS-CreateCustomKeyStore-request-XksProxyUriEndpoint"></a>
Specifies the endpoint that AWS KMS uses to send requests to the external key store proxy (XKS proxy). This parameter is required for custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE`.
The protocol must be HTTPS. AWS KMS communicates on port 443. Do not specify the port in the `XksProxyUriEndpoint` value.
For external key stores with `XksProxyConnectivity` value of `VPC_ENDPOINT_SERVICE`, specify `https://` followed by the private DNS name of the VPC endpoint service.
For external key stores with `PUBLIC_ENDPOINT` connectivity, this endpoint must be reachable before you create the custom key store. AWS KMS connects to the external key store proxy while creating the custom key store. For external key stores with `VPC_ENDPOINT_SERVICE` connectivity, AWS KMS connects when you call the [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md) operation.
The value of this parameter must begin with `https://`. The remainder can contain upper and lower case letters (A-Z and a-z), numbers (0-9), dots (`.`), and hyphens (`-`). Additional slashes (`/` and `\`) are not permitted.
 **Uniqueness requirements: **
+ The combined `XksProxyUriEndpoint` and `XksProxyUriPath` values must be unique in the AWS account and Region.
+ An external key store with `PUBLIC_ENDPOINT` connectivity cannot use the same `XksProxyUriEndpoint` value as an external key store with `VPC_ENDPOINT_SERVICE` connectivity in this AWS Region.
+ Each external key store with `VPC_ENDPOINT_SERVICE` connectivity must have its own private DNS name. The `XksProxyUriEndpoint` value for external key stores with `VPC_ENDPOINT_SERVICE` connectivity (private DNS name) must be unique in the AWS account and Region.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 128.
Pattern: `^https://[a-zA-Z0-9.-]+$`
Required: No

 ** [XksProxyUriPath](#API_CreateCustomKeyStore_RequestSyntax) **   <a name="KMS-CreateCustomKeyStore-request-XksProxyUriPath"></a>
Specifies the base path to the proxy APIs for this external key store. To find this value, see the documentation for your external key store proxy. This parameter is required for all custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE`.
The value must start with `/` and must end with `/kms/xks/v1` where `v1` represents the version of the AWS KMS external key store proxy API. This path can include an optional prefix between the required elements such as `/prefix/kms/xks/v1`.
 **Uniqueness requirements: **
+ The combined `XksProxyUriEndpoint` and `XksProxyUriPath` values must be unique in the AWS account and Region.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 128.
Pattern: `^(/[a-zA-Z0-9\/_-]+/kms/xks/v\d{1,2})$|^(/kms/xks/v\d{1,2})$`
Required: No

 ** [XksProxyVpcEndpointServiceName](#API_CreateCustomKeyStore_RequestSyntax) **   <a name="KMS-CreateCustomKeyStore-request-XksProxyVpcEndpointServiceName"></a>
Specifies the name of the Amazon VPC endpoint service for interface endpoints that is used to communicate with your external key store proxy (XKS proxy). This parameter is required when the value of `CustomKeyStoreType` is `EXTERNAL_KEY_STORE` and the value of `XksProxyConnectivity` is `VPC_ENDPOINT_SERVICE`.
The Amazon VPC endpoint service must [fulfill all requirements](https://docs.aws.amazon.com/kms/latest/developerguide/create-xks-keystore.html#xks-requirements) for use with an external key store.
 **Uniqueness requirements:**
+ External key stores with `VPC_ENDPOINT_SERVICE` connectivity can share an Amazon VPC, but each external key store must have its own VPC endpoint service and private DNS name.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `^(com|eu)\.amazonaws\.vpce\.([a-z]+-){2,3}\d+\.vpce-svc-[0-9a-z]+$`
Required: No

 ** [XksProxyVpcEndpointServiceOwner](#API_CreateCustomKeyStore_RequestSyntax) **   <a name="KMS-CreateCustomKeyStore-request-XksProxyVpcEndpointServiceOwner"></a>
Specifies the AWS account ID that owns the Amazon VPC service endpoint for the interface that is used to communicate with your external key store proxy (XKS proxy). This parameter is optional. If not provided, the AWS account ID calling the action will be used.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

## Response Syntax
<a name="API_CreateCustomKeyStore_ResponseSyntax"></a>

```
{
   "CustomKeyStoreId": "string"
}
```

## Response Elements
<a name="API_CreateCustomKeyStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomKeyStoreId](#API_CreateCustomKeyStore_ResponseSyntax) **   <a name="KMS-CreateCustomKeyStore-response-CustomKeyStoreId"></a>
A unique identifier for the new custom key store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_CreateCustomKeyStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CloudHsmClusterInUseException **
The request was rejected because the specified AWS CloudHSM cluster is already associated with an AWS CloudHSM key store in the account, or it shares a backup history with an AWS CloudHSM key store in the account. Each AWS CloudHSM key store in the account must be associated with a different AWS CloudHSM cluster.
 AWS CloudHSM clusters that share a backup history have the same cluster certificate. To view the cluster certificate of an AWS CloudHSM cluster, use the [DescribeClusters](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html) operation.
HTTP Status Code: 400

 ** CloudHsmClusterInvalidConfigurationException **
The request was rejected because the associated AWS CloudHSM cluster did not meet the configuration requirements for an AWS CloudHSM key store.
+ The AWS CloudHSM cluster must be configured with private subnets in at least two different Availability Zones in the Region.
+ The [security group for the cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sg.html) (cloudhsm-cluster-*<cluster-id>*-sg) must include inbound rules and outbound rules that allow TCP traffic on ports 2223-2225. The **Source** in the inbound rules and the **Destination** in the outbound rules must match the security group ID. These rules are set by default when you create the AWS CloudHSM cluster. Do not delete or change them. To get information about a particular security group, use the [DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html) operation.
+ The AWS CloudHSM cluster must contain at least as many HSMs as the operation requires. To add HSMs, use the AWS CloudHSM [CreateHsm](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateHsm.html) operation.

  For the [CreateCustomKeyStore](#API_CreateCustomKeyStore), [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md), and [CreateKey](API_CreateKey.md) operations, the AWS CloudHSM cluster must have at least two active HSMs, each in a different Availability Zone. For the [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md) operation, the AWS CloudHSM must contain at least one active HSM.
For information about the requirements for an AWS CloudHSM cluster that is associated with an AWS CloudHSM key store, see [Assemble the Prerequisites](https://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html#before-keystore) in the * AWS Key Management Service Developer Guide*. For information about creating a private subnet for an AWS CloudHSM cluster, see [Create a Private Subnet](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-subnets.html) in the * AWS CloudHSM User Guide*. For information about cluster security groups, see [Configure a Default Security Group](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sg.html) in the * * AWS CloudHSM User Guide* *.
HTTP Status Code: 400

 ** CloudHsmClusterNotActiveException **
The request was rejected because the AWS CloudHSM cluster associated with the AWS CloudHSM key store is not active. Initialize and activate the cluster and try the command again. For detailed instructions, see [Getting Started](https://docs.aws.amazon.com/cloudhsm/latest/userguide/getting-started.html) in the * AWS CloudHSM User Guide*.
HTTP Status Code: 400

 ** CloudHsmClusterNotFoundException **
The request was rejected because AWS KMS cannot find the AWS CloudHSM cluster with the specified cluster ID. Retry the request with a different cluster ID.
HTTP Status Code: 400

 ** CustomKeyStoreNameInUseException **
The request was rejected because the specified custom key store name is already assigned to another custom key store in the account. Try again with a custom key store name that is unique in the account.
HTTP Status Code: 400

 ** IncorrectTrustAnchorException **
The request was rejected because the trust anchor certificate in the request to create an AWS CloudHSM key store is not the trust anchor certificate for the specified AWS CloudHSM cluster.
When you [initialize the AWS CloudHSM cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/initialize-cluster.html#sign-csr), you create the trust anchor certificate and save it in the `customerCA.crt` file.
HTTP Status Code: 400

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

 ** LimitExceededException **
The request was rejected because a length constraint or quota was exceeded. For more information, see [Quotas](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html) in the * AWS Key Management Service Developer Guide*.
HTTP Status Code: 400

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
<a name="API_CreateCustomKeyStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/CreateCustomKeyStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/CreateCustomKeyStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/CreateCustomKeyStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/CreateCustomKeyStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/CreateCustomKeyStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/CreateCustomKeyStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/CreateCustomKeyStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/CreateCustomKeyStore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/CreateCustomKeyStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/CreateCustomKeyStore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
