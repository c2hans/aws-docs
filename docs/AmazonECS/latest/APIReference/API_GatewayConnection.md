---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayConnection.html
---

# GatewayConnection
<a name="API_GatewayConnection"></a>

A gateway-managed connection for a service revision. A connection represents the association between the service's gateway connector and a specific gateway, along with the infrastructure that the gateway created for it.

## Contents
<a name="API_GatewayConnection_Contents"></a>

 ** accessType **   <a name="ECS-Type-GatewayConnection-accessType"></a>
The access type of the gateway ingress path.
Valid values:
+  `PUBLIC` - The ingress path is publicly accessible.
+  `PRIVATE` - The ingress path is only accessible privately.
Type: String
Valid Values: `PUBLIC | PRIVATE`
Required: No

 ** gatewayArn **   <a name="ECS-Type-GatewayConnection-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.
Type: String
Required: No

 ** gatewayRouteArn **   <a name="ECS-Type-GatewayConnection-gatewayRouteArn"></a>
The Amazon Resource Name (ARN) of the gateway route for the connection.
Type: String
Required: No

 ** portName **   <a name="ECS-Type-GatewayConnection-portName"></a>
The name of the service port that receives gateway-managed ingress traffic.
Type: String
Required: No

 ** resources **   <a name="ECS-Type-GatewayConnection-resources"></a>
The gateway-managed infrastructure resources for the connection.
Type: [GatewayConnectionResources](API_GatewayConnectionResources.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** serviceUrl **   <a name="ECS-Type-GatewayConnection-serviceUrl"></a>
The URL that the gateway uses to route ingress traffic to the service.
Type: String
Required: No

 ** status **   <a name="ECS-Type-GatewayConnection-status"></a>
The status of the gateway route for the connection.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | CREATE_FAILED | UPDATE_IN_PROGRESS | UPDATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: No

## See Also
<a name="API_GatewayConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayConnection)
