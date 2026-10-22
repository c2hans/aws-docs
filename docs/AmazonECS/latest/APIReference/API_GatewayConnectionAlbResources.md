---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayConnectionAlbResources.html
---

# GatewayConnectionAlbResources
<a name="API_GatewayConnectionAlbResources"></a>

The Application Load Balancer resources that a gateway created and manages for a connection.

## Contents
<a name="API_GatewayConnectionAlbResources_Contents"></a>

 ** acmCertificateArn **   <a name="ECS-Type-GatewayConnectionAlbResources-acmCertificateArn"></a>
The Amazon Resource Name (ARN) of the AWS Certificate Manager certificate that is attached to the load balancer listener.
Type: String
Required: No

 ** alternateTargetGroupArn **   <a name="ECS-Type-GatewayConnectionAlbResources-alternateTargetGroupArn"></a>
The Amazon Resource Name (ARN) of the alternate target group that the gateway uses during progressive deployments.
Type: String
Required: No

 ** listenerArn **   <a name="ECS-Type-GatewayConnectionAlbResources-listenerArn"></a>
The Amazon Resource Name (ARN) of the listener on the load balancer.
Type: String
Required: No

 ** listenerRuleArn **   <a name="ECS-Type-GatewayConnectionAlbResources-listenerRuleArn"></a>
The Amazon Resource Name (ARN) of the listener rule that routes production traffic to the service.
Type: String
Required: No

 ** loadBalancerArn **   <a name="ECS-Type-GatewayConnectionAlbResources-loadBalancerArn"></a>
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: No

 ** loadBalancerSecurityGroupArns **   <a name="ECS-Type-GatewayConnectionAlbResources-loadBalancerSecurityGroupArns"></a>
The Amazon Resource Names (ARNs) of the security groups that the gateway attaches to the load balancer.
Type: Array of strings
Required: No

 ** targetGroupArn **   <a name="ECS-Type-GatewayConnectionAlbResources-targetGroupArn"></a>
The Amazon Resource Name (ARN) of the target group that receives production traffic.
Type: String
Required: No

 ** testListenerRuleArn **   <a name="ECS-Type-GatewayConnectionAlbResources-testListenerRuleArn"></a>
The Amazon Resource Name (ARN) of the listener rule that routes test traffic to the service during progressive deployments.
Type: String
Required: No

## See Also
<a name="API_GatewayConnectionAlbResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayConnectionAlbResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayConnectionAlbResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayConnectionAlbResources)
