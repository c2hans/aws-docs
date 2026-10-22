---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateGatewayAlbConfiguration.html
---

# UpdateGatewayAlbConfiguration
<a name="API_UpdateGatewayAlbConfiguration"></a>

The mutable configuration fields for a gateway that uses shared Application Load Balancers. Only fields that can be changed without interrupting traffic are included.

## Contents
<a name="API_UpdateGatewayAlbConfiguration_Contents"></a>

 ** accessLogs **   <a name="ECS-Type-UpdateGatewayAlbConfiguration-accessLogs"></a>
The access log configuration for the load balancers that the gateway manages.
Type: [GatewayElbAccessLogConfiguration](API_GatewayElbAccessLogConfiguration.md) object
Required: No

 ** httpDesync **   <a name="ECS-Type-UpdateGatewayAlbConfiguration-httpDesync"></a>
The desync mitigation mode for the load balancers that the gateway manages.
Type: String
Valid Values: `monitor | defensive | strictest`
Required: No

 ** maxAlbCount **   <a name="ECS-Type-UpdateGatewayAlbConfiguration-maxAlbCount"></a>
The maximum number of Application Load Balancers that the gateway manages.
Type: Integer
Required: No

 ** networkConfiguration **   <a name="ECS-Type-UpdateGatewayAlbConfiguration-networkConfiguration"></a>
The mutable network configuration for the load balancers that the gateway manages.
Type: [UpdateGatewayNetworkConfiguration](API_UpdateGatewayNetworkConfiguration.md) object
Required: No

 ** testTrafficRules **   <a name="ECS-Type-UpdateGatewayAlbConfiguration-testTrafficRules"></a>
The rules that route test traffic for progressive deployments.
Type: [GatewayAlbTestTrafficRules](API_GatewayAlbTestTrafficRules.md) object
Required: No

 ** webACLArn **   <a name="ECS-Type-UpdateGatewayAlbConfiguration-webACLArn"></a>
The Amazon Resource Name (ARN) of the WAF web ACL to associate with the load balancers that the gateway manages.
Type: String
Required: No

## See Also
<a name="API_UpdateGatewayAlbConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/UpdateGatewayAlbConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/UpdateGatewayAlbConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/UpdateGatewayAlbConfiguration)
