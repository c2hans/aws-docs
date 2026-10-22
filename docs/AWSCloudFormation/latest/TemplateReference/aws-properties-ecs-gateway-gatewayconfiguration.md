---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewayconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Gateway GatewayConfiguration
<a name="aws-properties-ecs-gateway-gatewayconfiguration"></a>

The type-specific configuration for a gateway that you provide when you create it. Exactly one variant is set, and it determines the gateway type.

## Syntax
<a name="aws-properties-ecs-gateway-gatewayconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-gateway-gatewayconfiguration-syntax.json"></a>

```
{
  "[HostSharedAlb](#cfn-ecs-gateway-gatewayconfiguration-hostsharedalb)" : {{HostSharedAlbConfiguration}}
}
```

### YAML
<a name="aws-properties-ecs-gateway-gatewayconfiguration-syntax.yaml"></a>

```
  [HostSharedAlb](#cfn-ecs-gateway-gatewayconfiguration-hostsharedalb): {{
    HostSharedAlbConfiguration}}
```

## Properties
<a name="aws-properties-ecs-gateway-gatewayconfiguration-properties"></a>

`HostSharedAlb`  <a name="cfn-ecs-gateway-gatewayconfiguration-hostsharedalb"></a>
The configuration for a host-based, shared Application Load Balancer gateway. Each service that uses the gateway is assigned a unique DNS host name.
*Required*: Yes
*Type*: [HostSharedAlbConfiguration](aws-properties-ecs-gateway-hostsharedalbconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
