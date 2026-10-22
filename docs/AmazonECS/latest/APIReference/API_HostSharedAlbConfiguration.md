---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_HostSharedAlbConfiguration.html
---

# HostSharedAlbConfiguration
<a name="API_HostSharedAlbConfiguration"></a>

The configuration for a gateway that uses shared Application Load Balancers with host-based routing. Where they apply, the field names and values are kept consistent with the Elastic Load Balancing API.

## Contents
<a name="API_HostSharedAlbConfiguration_Contents"></a>

 ** accessLogs **   <a name="ECS-Type-HostSharedAlbConfiguration-accessLogs"></a>
The access log configuration for the load balancers that the gateway manages.
Type: [GatewayElbAccessLogConfiguration](API_GatewayElbAccessLogConfiguration.md) object
Required: No

 ** httpDesync **   <a name="ECS-Type-HostSharedAlbConfiguration-httpDesync"></a>
The desync mitigation mode for the load balancers that the gateway manages, which determines how the load balancers handle requests that might pose a security risk. The default is `defensive`.
Type: String
Valid Values: `monitor | defensive | strictest`
Required: No

 ** maxAlbCount **   <a name="ECS-Type-HostSharedAlbConfiguration-maxAlbCount"></a>
The maximum number of Application Load Balancers that the gateway manages. The default is 10.
Type: Integer
Required: No

 ** networkConfiguration **   <a name="ECS-Type-HostSharedAlbConfiguration-networkConfiguration"></a>
The network configuration for the load balancers that the gateway manages.
Type: [GatewayElbNetworkConfiguration](API_GatewayElbNetworkConfiguration.md) object
Required: No

 ** port **   <a name="ECS-Type-HostSharedAlbConfiguration-port"></a>
The port that the load balancer listener uses is 443. The gateway supports only HTTPS at port 443.
Type: Integer
Required: No

 ** protocol **   <a name="ECS-Type-HostSharedAlbConfiguration-protocol"></a>
The protocol for the load balancer listener is `HTTPS`. No other protocol is supported.
Type: String
Valid Values: `HTTP | HTTPS`
Required: No

 ** scheme **   <a name="ECS-Type-HostSharedAlbConfiguration-scheme"></a>
Specifies whether the load balancers the gateway manages are `internet-facing` or `internal`. The default is `internet-facing`.
Type: String
Valid Values: `internet-facing | internal`
Required: No

 ** testTrafficRules **   <a name="ECS-Type-HostSharedAlbConfiguration-testTrafficRules"></a>
The rules that route test traffic for progressive deployments. During a progressive deployment, requests whose headers match these rules are routed to the new service revision so that it can be validated before production traffic shifts to it.
Type: [GatewayAlbTestTrafficRules](API_GatewayAlbTestTrafficRules.md) object
Required: No

 ** webACLArn **   <a name="ECS-Type-HostSharedAlbConfiguration-webACLArn"></a>
The Amazon Resource Name (ARN) of the WAF web ACL to associate with the load balancers that the gateway manages.
Type: String
Required: No

## See Also
<a name="API_HostSharedAlbConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/HostSharedAlbConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/HostSharedAlbConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/HostSharedAlbConfiguration)
