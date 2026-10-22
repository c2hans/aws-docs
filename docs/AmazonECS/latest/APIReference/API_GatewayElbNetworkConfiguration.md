---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayElbNetworkConfiguration.html
---

# GatewayElbNetworkConfiguration
<a name="API_GatewayElbNetworkConfiguration"></a>

The network configuration for the load balancers that a gateway manages.

## Contents
<a name="API_GatewayElbNetworkConfiguration_Contents"></a>

 ** inboundSecurityGroup **   <a name="ECS-Type-GatewayElbNetworkConfiguration-inboundSecurityGroup"></a>
The ID of a security group that you provide to control inbound traffic to the load balancers that the gateway manages. When you specify a security group, the gateway doesn't create inbound rules on the security group it manages.
Type: String
Required: No

 ** ipAddressType **   <a name="ECS-Type-GatewayElbNetworkConfiguration-ipAddressType"></a>
The IP address type for the load balancers that the gateway manages. The default is `dualstack`.
Type: String
Valid Values: `ipv4 | dualstack | dualstack-without-public-ipv4`
Required: No

 ** subnets **   <a name="ECS-Type-GatewayElbNetworkConfiguration-subnets"></a>
The subnets for the load balancers that the gateway manages. The default is the subnets in the default VPC.
Type: Array of strings
Required: No

## See Also
<a name="API_GatewayElbNetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayElbNetworkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayElbNetworkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayElbNetworkConfiguration)
