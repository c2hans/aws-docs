---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-hostsharedalbconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Gateway HostSharedAlbConfiguration
<a name="aws-properties-ecs-gateway-hostsharedalbconfiguration"></a>

<a name="aws-properties-ecs-gateway-hostsharedalbconfiguration-description"></a>The `HostSharedAlbConfiguration` property type specifies Property description not available. for an [AWS::ECS::Gateway](aws-resource-ecs-gateway.md).

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
Property description not available.
*Required*: No
*Type*: [GatewayElbAccessLogConfiguration](aws-properties-ecs-gateway-gatewayelbaccesslogconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CurrentAlbCount`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-currentalbcount"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpDesync`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-httpdesync"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `monitor | defensive | strictest`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxAlbCount`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-maxalbcount"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkConfiguration`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-networkconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [GatewayElbNetworkConfiguration](aws-properties-ecs-gateway-gatewayelbnetworkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-port"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Protocol`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-protocol"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `HTTP | HTTPS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Scheme`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-scheme"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `internet-facing | internal`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TestTrafficRules`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-testtrafficrules"></a>
Property description not available.
*Required*: No
*Type*: [GatewayAlbTestTrafficRules](aws-properties-ecs-gateway-gatewayalbtesttrafficrules.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebACLArn`  <a name="cfn-ecs-gateway-hostsharedalbconfiguration-webaclarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
