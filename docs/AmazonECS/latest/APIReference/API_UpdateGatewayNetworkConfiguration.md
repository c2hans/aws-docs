---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateGatewayNetworkConfiguration.html
---

# UpdateGatewayNetworkConfiguration
<a name="API_UpdateGatewayNetworkConfiguration"></a>

The mutable network configuration for the load balancers that a gateway manages.

## Contents
<a name="API_UpdateGatewayNetworkConfiguration_Contents"></a>

 ** inboundSecurityGroup **   <a name="ECS-Type-UpdateGatewayNetworkConfiguration-inboundSecurityGroup"></a>
The ID of a security group that you provide to control inbound traffic to the load balancers that the gateway manages. When you specify a security group, the gateway doesn't create inbound rules on the security group it manages.
Type: String
Required: No

## See Also
<a name="API_UpdateGatewayNetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/UpdateGatewayNetworkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/UpdateGatewayNetworkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/UpdateGatewayNetworkConfiguration)
