---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayConnector.html
---

# GatewayConnector
<a name="API_GatewayConnector"></a>

A gateway connector that attaches an Amazon ECS service to a gateway ingress path. The connector specifies the service port that receives gateway-managed ingress traffic, along with the health check and traffic filters that the gateway applies. A service can have at most one gateway connector.

## Contents
<a name="API_GatewayConnector_Contents"></a>

 ** portName **   <a name="ECS-Type-GatewayConnector-portName"></a>
The name of the service port that the gateway routes ingress traffic to.
Type: String
Required: Yes

 ** filters **   <a name="ECS-Type-GatewayConnector-filters"></a>
The filters that control which gateway ingress paths the connector applies to.
Type: [GatewayConnectorFilters](API_GatewayConnectorFilters.md) object
Required: No

 ** healthCheck **   <a name="ECS-Type-GatewayConnector-healthCheck"></a>
The health check that the gateway uses to determine whether the targets for this connector are healthy.
Type: [GatewayConnectorHealthCheck](API_GatewayConnectorHealthCheck.md) object
Required: No

## See Also
<a name="API_GatewayConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayConnector)
