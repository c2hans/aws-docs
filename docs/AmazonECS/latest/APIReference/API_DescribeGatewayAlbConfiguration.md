---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeGatewayAlbConfiguration.html
---

# DescribeGatewayAlbConfiguration
<a name="API_DescribeGatewayAlbConfiguration"></a>

The configuration for a gateway that uses shared Application Load Balancers, as returned by `DescribeGateway`. This includes the current number of load balancers in addition to the configured settings.

## Contents
<a name="API_DescribeGatewayAlbConfiguration_Contents"></a>

 ** accessLogs **   <a name="ECS-Type-DescribeGatewayAlbConfiguration-accessLogs"></a>
The access log configuration for the load balancers that the gateway manages.
Type: [GatewayElbAccessLogConfiguration](API_GatewayElbAccessLogConfiguration.md) object
Required: No

 ** currentAlbCount **   <a name="ECS-Type-DescribeGatewayAlbConfiguration-currentAlbCount"></a>
The current number of Application Load Balancers that the gateway has allocated.
Type: Integer
Required: No

 ** httpDesync **   <a name="ECS-Type-DescribeGatewayAlbConfiguration-httpDesync"></a>
The desync mitigation mode for the load balancers that the gateway manages.
Type: String
Valid Values: `monitor | defensive | strictest`
Required: No

 ** maxAlbCount **   <a name="ECS-Type-DescribeGatewayAlbConfiguration-maxAlbCount"></a>
The maximum number of Application Load Balancers that the gateway manages.
Type: Integer
Required: No

 ** networkConfiguration **   <a name="ECS-Type-DescribeGatewayAlbConfiguration-networkConfiguration"></a>
The network configuration for the load balancers that the gateway manages.
Type: [GatewayElbNetworkConfiguration](API_GatewayElbNetworkConfiguration.md) object
Required: No

 ** port **   <a name="ECS-Type-DescribeGatewayAlbConfiguration-port"></a>
The port that the load balancer listener uses is 443. The gateway supports only HTTPS at port 443.
Type: Integer
Required: No

 ** protocol **   <a name="ECS-Type-DescribeGatewayAlbConfiguration-protocol"></a>
The protocol for the load balancer listener is `HTTPS`. No other protocol is supported.
Type: String
Valid Values: `HTTP | HTTPS`
Required: No

 ** scheme **   <a name="ECS-Type-DescribeGatewayAlbConfiguration-scheme"></a>
Specifies whether the load balancers the gateway manages are `internet-facing` or `internal`.
Type: String
Valid Values: `internet-facing | internal`
Required: No

 ** testTrafficRules **   <a name="ECS-Type-DescribeGatewayAlbConfiguration-testTrafficRules"></a>
The rules that route test traffic for progressive deployments.
Type: [GatewayAlbTestTrafficRules](API_GatewayAlbTestTrafficRules.md) object
Required: No

 ** webACLArn **   <a name="ECS-Type-DescribeGatewayAlbConfiguration-webACLArn"></a>
The Amazon Resource Name (ARN) of the WAF web ACL associated with the load balancers that the gateway manages.
Type: String
Required: No

## See Also
<a name="API_DescribeGatewayAlbConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeGatewayAlbConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeGatewayAlbConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeGatewayAlbConfiguration)
