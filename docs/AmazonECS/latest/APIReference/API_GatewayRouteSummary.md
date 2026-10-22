---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayRouteSummary.html
---

# GatewayRouteSummary
<a name="API_GatewayRouteSummary"></a>

A summary of a gateway route that is returned by the `ListGatewayRoutes` operation.

## Contents
<a name="API_GatewayRouteSummary_Contents"></a>

 ** clusterArn **   <a name="ECS-Type-GatewayRouteSummary-clusterArn"></a>
The Amazon Resource Name (ARN) of the cluster.
Type: String
Required: No

 ** gatewayArn **   <a name="ECS-Type-GatewayRouteSummary-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.
Type: String
Required: No

 ** gatewayRouteArn **   <a name="ECS-Type-GatewayRouteSummary-gatewayRouteArn"></a>
The Amazon Resource Name (ARN) of the gateway route.
Type: String
Required: No

 ** serviceArn **   <a name="ECS-Type-GatewayRouteSummary-serviceArn"></a>
The Amazon Resource Name (ARN) of the service.
Type: String
Required: No

 ** serviceContainerPortName **   <a name="ECS-Type-GatewayRouteSummary-serviceContainerPortName"></a>
The task definition container port name that the route targets on the service.
Type: String
Required: No

 ** status **   <a name="ECS-Type-GatewayRouteSummary-status"></a>
The status of the gateway route.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | CREATE_FAILED | UPDATE_IN_PROGRESS | UPDATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: No

## See Also
<a name="API_GatewayRouteSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayRouteSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayRouteSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayRouteSummary)
