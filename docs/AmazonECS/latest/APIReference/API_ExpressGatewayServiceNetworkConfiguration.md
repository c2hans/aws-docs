---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ExpressGatewayServiceNetworkConfiguration.html
---

# ExpressGatewayServiceNetworkConfiguration
<a name="API_ExpressGatewayServiceNetworkConfiguration"></a>

The network configuration for an Express service. By default, an Express service utilizes subnets and security groups associated with the default VPC.

## Contents
<a name="API_ExpressGatewayServiceNetworkConfiguration_Contents"></a>

 ** securityGroups **   <a name="ECS-Type-ExpressGatewayServiceNetworkConfiguration-securityGroups"></a>
The IDs of the security groups associated with the Express service.
Type: Array of strings
Required: No

 ** subnets **   <a name="ECS-Type-ExpressGatewayServiceNetworkConfiguration-subnets"></a>
The IDs of the subnets associated with the Express service.
Type: Array of strings
Required: No

## See Also
<a name="API_ExpressGatewayServiceNetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ExpressGatewayServiceNetworkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ExpressGatewayServiceNetworkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ExpressGatewayServiceNetworkConfiguration)
