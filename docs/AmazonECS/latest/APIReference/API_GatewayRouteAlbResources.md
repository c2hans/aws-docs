---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayRouteAlbResources.html
---

# GatewayRouteAlbResources
<a name="API_GatewayRouteAlbResources"></a>

The Application Load Balancer resources that a gateway manages for a route.

## Contents
<a name="API_GatewayRouteAlbResources_Contents"></a>

 ** acmCertificateArn **   <a name="ECS-Type-GatewayRouteAlbResources-acmCertificateArn"></a>
The Amazon Resource Name (ARN) of the AWS Certificate Manager certificate.
Type: String
Required: No

 ** listenerArn **   <a name="ECS-Type-GatewayRouteAlbResources-listenerArn"></a>
The Amazon Resource Name (ARN) of the listener.
Type: String
Required: No

 ** listenerRuleArn **   <a name="ECS-Type-GatewayRouteAlbResources-listenerRuleArn"></a>
The Amazon Resource Name (ARN) of the listener rule for production traffic.
Type: String
Required: No

 ** loadBalancerArn **   <a name="ECS-Type-GatewayRouteAlbResources-loadBalancerArn"></a>
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: No

 ** loadBalancerSecurityGroups **   <a name="ECS-Type-GatewayRouteAlbResources-loadBalancerSecurityGroups"></a>
The security groups attached to the load balancer.
Type: Array of [GatewayRouteLoadBalancerSecurityGroup](API_GatewayRouteLoadBalancerSecurityGroup.md) objects
Required: No

 ** serviceSecurityGroupArn **   <a name="ECS-Type-GatewayRouteAlbResources-serviceSecurityGroupArn"></a>
The Amazon Resource Name (ARN) of the service security group in which the gateway manages the ingress rule for this route.
Type: String
Required: No

 ** testListenerRuleArns **   <a name="ECS-Type-GatewayRouteAlbResources-testListenerRuleArns"></a>
The Amazon Resource Names (ARNs) of the listener rules for test traffic. There is one rule except when a test header configuration is being changed to another.
Type: Array of strings
Required: No

## See Also
<a name="API_GatewayRouteAlbResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayRouteAlbResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayRouteAlbResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayRouteAlbResources)
