---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayRoute.html
---

# GatewayRoute
<a name="API_GatewayRoute"></a>

A gateway route, which represents the association between a service and a gateway and the service-specific infrastructure that the gateway manages for the service's revisions.

## Contents
<a name="API_GatewayRoute_Contents"></a>

 ** gatewayRouteArn **   <a name="ECS-Type-GatewayRoute-gatewayRouteArn"></a>
The Amazon Resource Name (ARN) of the gateway route.
Type: String
Required: No

 ** resources **   <a name="ECS-Type-GatewayRoute-resources"></a>
The service-specific infrastructure that the gateway manages for the route, keyed by gateway type.
Type: [GatewayRouteResources](API_GatewayRouteResources.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** serviceArn **   <a name="ECS-Type-GatewayRoute-serviceArn"></a>
The Amazon Resource Name (ARN) of the service associated with the route.
Type: String
Required: No

 ** serviceContainerPortName **   <a name="ECS-Type-GatewayRoute-serviceContainerPortName"></a>
The task definition container port name that the route targets on the service.
Type: String
Required: No

 ** serviceUrl **   <a name="ECS-Type-GatewayRoute-serviceUrl"></a>
The URL for accessing the service, including the `https://` scheme.
Type: String
Required: No

 ** status **   <a name="ECS-Type-GatewayRoute-status"></a>
The status of the gateway route.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | CREATE_FAILED | UPDATE_IN_PROGRESS | UPDATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: No

## See Also
<a name="API_GatewayRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayRoute)
