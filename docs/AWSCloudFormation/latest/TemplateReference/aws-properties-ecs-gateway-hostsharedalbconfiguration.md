---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-hostsharedalbconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Gateway HostSharedAlbConfiguration
<a name="aws-properties-ecs-gateway-hostsharedalbconfiguration"></a>

The configuration for a gateway that uses shared Application Load Balancers with host-based routing. Where they apply, the field names and values are kept consistent with the Elastic Load Balancing API.

## Syntax
<a name="aws-properties-ecs-gateway-hostsharedalbconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-gateway-hostsharedalbconfiguration-syntax.json"></a>

```
{
  "[AccessLogs](#cfn-ecs-gateway-hostsharedalbconfiguration-accesslogs)" : {{GatewayElbAccessLogConfiguration}},
  "[CurrentAlbCount](#cfn-ecs-gateway-hostsharedalbconfiguration-currentalbcount)" : {{Integer}},
  "[HttpDesync](#cfn-ecs-gateway-hostsharedalbconfiguration-httpdesync)" : {{String}},
  "[MaxAlbCount](#cfn-ecs-gateway-hostsharedalbconfiguration-maxalbcount)" : {{Integer}},
  "[NetworkConfiguration](#cfn-ecs-gateway-hostsharedalbconfiguration-networkconfiguration)" : {{GatewayElbNetworkConfiguration}},
  "[Port](#cfn-ecs-gateway-hostsharedalbconfiguration-port)" : {{Integer}},
  "[Protocol](#cfn-ecs-gateway-hostsharedalbconfiguration-protocol)" : {{String}},
  "[Scheme](#cfn-ecs-gateway-hostsharedalbconfiguration-scheme)" : {{String}},
  "[TestTrafficRules](#cfn-ecs-gateway-hostsharedalbconfiguration-testtrafficrules)" : {{GatewayAlbTestTrafficRules}},
  "[WebACLArn](#cfn-ecs-gateway-hostsharedalbconfiguration-webaclarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-gateway-hostsharedalbconfiguration-syntax.yaml"></a>

```
  [AccessLogs](#cfn-ecs-gateway-hostsharedalbconfiguration-accesslogs): {{
    GatewayElbAccessLogConfiguration}}
  [CurrentAlbCount](#cfn-ecs-gateway-hostsharedalbconfiguration-currentalbcount): {{Integer}}
  [HttpDesync](#cfn-ecs-gateway-hostsharedalbconfiguration-httpdesync): {{String}}
  [MaxAlbCount](#cfn-ecs-gateway-hostsharedalbconfiguration-maxalbcount): {{Integer}}
  [NetworkConfiguration](#cfn-ecs-gateway-hostsharedalbconfiguration-networkconfiguration): {{
    GatewayElbNetworkConfiguration}}
  [Port](#cfn-ecs-gateway-hostsharedalbconfiguration-port): {{Integer}}
  [Protocol](#cfn-ecs-gateway-hostsharedalbconfiguration-protocol): {{String}}
  [Scheme](#cfn-ecs-gateway-hostsharedalbconfiguration-scheme): {{String}}
  [TestTrafficRules](#cfn-ecs-gateway-hostsharedalbconfiguration-testtrafficrules): {{
    GatewayAlbTestTrafficRules}}
  [WebACLArn](#cfn-ecs-gateway-hostsharedalbconfiguration-webaclarn): {{String}}
```

## Properties
<a name="aws-properties-ecs-gateway-hostsharedalbconfiguration-properties"></a>

`AccessLogs`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-accesslogs"></a>
The access log configuration for the load balancers that the gateway manages.
*Required*: No
*Type*: [GatewayElbAccessLogConfiguration](aws-properties-ecs-gateway-gatewayelbaccesslogconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CurrentAlbCount`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-currentalbcount"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpDesync`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-httpdesync"></a>
The desync mitigation mode for the load balancers that the gateway manages, which determines how the load balancers handle requests that might pose a security risk. The default is `defensive`.
*Required*: No
*Type*: String
*Allowed values*: `monitor | defensive | strictest`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxAlbCount`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-maxalbcount"></a>
The maximum number of Application Load Balancers that the gateway manages. The default is 10.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkConfiguration`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-networkconfiguration"></a>
The network configuration for the load balancers that the gateway manages.
*Required*: No
*Type*: [GatewayElbNetworkConfiguration](aws-properties-ecs-gateway-gatewayelbnetworkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-port"></a>
The port that the load balancer listener uses is 443. The gateway supports only HTTPS at port 443.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Protocol`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-protocol"></a>
The protocol for the load balancer listener is `HTTPS`. No other protocol is supported.
*Required*: No
*Type*: String
*Allowed values*: `HTTP | HTTPS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Scheme`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-scheme"></a>
Specifies whether the load balancers the gateway manages are `internet-facing` or `internal`. The default is `internet-facing`.
*Required*: No
*Type*: String
*Allowed values*: `internet-facing | internal`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TestTrafficRules`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-testtrafficrules"></a>
The rules that route test traffic for progressive deployments. During a progressive deployment, requests whose headers match these rules are routed to the new service revision so that it can be validated before production traffic shifts to it.
*Required*: No
*Type*: [GatewayAlbTestTrafficRules](aws-properties-ecs-gateway-gatewayalbtesttrafficrules.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebACLArn`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-webaclarn"></a>
The Amazon Resource Name (ARN) of the WAF web ACL to associate with the load balancers that the gateway manages.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
