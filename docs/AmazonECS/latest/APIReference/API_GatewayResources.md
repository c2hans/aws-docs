---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayResources.html
---

# GatewayResources
<a name="API_GatewayResources"></a>

 `DescribeGatewayResources` returns the gateway-managed infrastructure, grouped by gateway type.

## Contents
<a name="API_GatewayResources_Contents"></a>

 ** gatewayArn **   <a name="ECS-Type-GatewayResources-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.
Type: String
Required: No

 ** resources **   <a name="ECS-Type-GatewayResources-resources"></a>
The infrastructure resources that the gateway manages.
Type: [GatewayInfrastructureResources](API_GatewayInfrastructureResources.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_GatewayResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayResources)
