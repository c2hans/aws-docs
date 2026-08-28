---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_VpcRouterNetworkInterfaceConfiguration.html
---

# VpcRouterNetworkInterfaceConfiguration
<a name="API_VpcRouterNetworkInterfaceConfiguration"></a>

The configuration settings for a router network interface within a VPC, including the security group IDs and subnet ID.

## Contents
<a name="API_VpcRouterNetworkInterfaceConfiguration_Contents"></a>

 ** securityGroupIds **   <a name="mediaconnect-Type-VpcRouterNetworkInterfaceConfiguration-securityGroupIds"></a>
The IDs of the security groups to associate with the router network interface within the VPC.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** subnetId **   <a name="mediaconnect-Type-VpcRouterNetworkInterfaceConfiguration-subnetId"></a>
The ID of the subnet within the VPC to associate the router network interface with.
Type: String
Required: Yes

## See Also
<a name="API_VpcRouterNetworkInterfaceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/VpcRouterNetworkInterfaceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/VpcRouterNetworkInterfaceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/VpcRouterNetworkInterfaceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
