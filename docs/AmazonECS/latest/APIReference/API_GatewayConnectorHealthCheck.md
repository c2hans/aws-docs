---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayConnectorHealthCheck.html
---

# GatewayConnectorHealthCheck
<a name="API_GatewayConnectorHealthCheck"></a>

The health check configuration that a gateway uses to evaluate the targets associated with a gateway connector.

## Contents
<a name="API_GatewayConnectorHealthCheck_Contents"></a>

 ** healthCheckIntervalSeconds **   <a name="ECS-Type-GatewayConnectorHealthCheck-healthCheckIntervalSeconds"></a>
The approximate amount of time, in seconds, between health checks of an individual target.
Type: Integer
Required: No

 ** healthCheckPath **   <a name="ECS-Type-GatewayConnectorHealthCheck-healthCheckPath"></a>
The destination path for health check requests.
Type: String
Required: No

 ** healthCheckPort **   <a name="ECS-Type-GatewayConnectorHealthCheck-healthCheckPort"></a>
The port that the gateway uses to perform health checks on the targets.
Type: Integer
Required: No

 ** healthCheckProtocol **   <a name="ECS-Type-GatewayConnectorHealthCheck-healthCheckProtocol"></a>
The protocol that the gateway uses to perform health checks.
Valid values:
+  `HTTP` - Health checks are performed over HTTP.
+  `HTTPS` - Health checks are performed over HTTPS.
Type: String
Valid Values: `HTTP | HTTPS`
Required: No

 ** healthCheckTimeoutSeconds **   <a name="ECS-Type-GatewayConnectorHealthCheck-healthCheckTimeoutSeconds"></a>
The amount of time, in seconds, during which no response from a target means a failed health check.
Type: Integer
Required: No

 ** healthyThresholdCount **   <a name="ECS-Type-GatewayConnectorHealthCheck-healthyThresholdCount"></a>
The number of consecutive successful health checks that a target must pass before the gateway considers it healthy.
Type: Integer
Required: No

 ** matcher **   <a name="ECS-Type-GatewayConnectorHealthCheck-matcher"></a>
The HTTP or gRPC codes that indicate a successful health check response from a target.
Type: [GatewayConnectorHealthCheckMatcher](API_GatewayConnectorHealthCheckMatcher.md) object
Required: No

 ** unhealthyThresholdCount **   <a name="ECS-Type-GatewayConnectorHealthCheck-unhealthyThresholdCount"></a>
The number of consecutive failed health checks that a target must fail before the gateway considers it unhealthy.
Type: Integer
Required: No

## See Also
<a name="API_GatewayConnectorHealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayConnectorHealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayConnectorHealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayConnectorHealthCheck)
