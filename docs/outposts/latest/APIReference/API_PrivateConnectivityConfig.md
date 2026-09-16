---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_PrivateConnectivityConfig.html
---

# PrivateConnectivityConfig
<a name="API_PrivateConnectivityConfig"></a>

Information about the private connectivity configuration for an Outpost.

## Contents
<a name="API_PrivateConnectivityConfig_Contents"></a>

 ** PrivateConnectivityStatus **   <a name="outposts-Type-PrivateConnectivityConfig-PrivateConnectivityStatus"></a>
The status of private connectivity for the Outpost. Valid values are `ENABLED` and `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** ProvisioningRoleArn **   <a name="outposts-Type-PrivateConnectivityConfig-ProvisioningRoleArn"></a>
The Amazon Resource Name (ARN) of the provisioning role in your account that AWS Outposts uses to establish the service link connection during Outpost installation. This field is present only when VPC endpoint-based provisioning is configured.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `^arn:aws([a-z-]+)?:iam::\d{12}:role\/[a-zA-Z_0-9+=,.@\-_\/]+`
Required: No

 ** RoleArn **   <a name="outposts-Type-PrivateConnectivityConfig-RoleArn"></a>
The Amazon Resource Name (ARN) of the service-linked role that AWS Outposts creates and uses to provision and attach the network interfaces for private connectivity in your VPC. The role's permissions are scoped to the specific Outpost and VPC.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `^arn:aws([a-z-]+)?:iam::\d{12}:role\/[a-zA-Z_0-9+=,.@\-_\/]+`
Required: No

 ** VpcInformationList **   <a name="outposts-Type-PrivateConnectivityConfig-VpcInformationList"></a>
Information about the VPC used for private connectivity.
Type: Array of [VpcInformation](API_VpcInformation.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_PrivateConnectivityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/PrivateConnectivityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/PrivateConnectivityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/PrivateConnectivityConfig)
