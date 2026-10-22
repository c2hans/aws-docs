---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ElbGatewayResources.html
---

# ElbGatewayResources
<a name="API_ElbGatewayResources"></a>

An Application Load Balancer and its associated resources that a gateway manages.

## Contents
<a name="API_ElbGatewayResources_Contents"></a>

 ** gatewayRouteArns **   <a name="ECS-Type-ElbGatewayResources-gatewayRouteArns"></a>
The Amazon Resource Names (ARNs) of the gateway routes that use this load balancer for ingress.
Type: Array of strings
Required: No

 ** listenerArn **   <a name="ECS-Type-ElbGatewayResources-listenerArn"></a>
The Amazon Resource Name (ARN) of the listener on the load balancer.
Type: String
Required: No

 ** loadBalancerArn **   <a name="ECS-Type-ElbGatewayResources-loadBalancerArn"></a>
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: No

 ** securityGroup **   <a name="ECS-Type-ElbGatewayResources-securityGroup"></a>
The ID of the security group attached to the load balancer.
Type: String
Required: No

## See Also
<a name="API_ElbGatewayResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ElbGatewayResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ElbGatewayResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ElbGatewayResources)
