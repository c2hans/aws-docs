---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewayelbaccesslogconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Gateway GatewayElbAccessLogConfiguration
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogconfiguration"></a>

The access log configuration for the load balancers that a gateway manages.

## Syntax
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogconfiguration-syntax.json"></a>

```
{
  "[Destination](#cfn-ecs-gateway-gatewayelbaccesslogconfiguration-destination)" : {{GatewayElbAccessLogDestination}}
}
```

### YAML
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogconfiguration-syntax.yaml"></a>

```
  [Destination](#cfn-ecs-gateway-gatewayelbaccesslogconfiguration-destination): {{
    GatewayElbAccessLogDestination}}
```

## Properties
<a name="aws-properties-ecs-gateway-gatewayelbaccesslogconfiguration-properties"></a>

`Destination`  <a name="cfn-ecs-gateway-gatewayelbaccesslogconfiguration-destination"></a>
The destination where access logs are delivered.
*Required*: No
*Type*: [GatewayElbAccessLogDestination](aws-properties-ecs-gateway-gatewayelbaccesslogdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
