---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-gatewayconnector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service GatewayConnector
<a name="aws-properties-ecs-service-gatewayconnector"></a>

<a name="aws-properties-ecs-service-gatewayconnector-description"></a>The `GatewayConnector` property type specifies Property description not available. for an [AWS::ECS::Service](aws-resource-ecs-service.md).

## Syntax
<a name="aws-properties-ecs-service-gatewayconnector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-gatewayconnector-syntax.json"></a>

```
{
  "[Filters](#cfn-ecs-service-gatewayconnector-filters)" : {{GatewayConnectorFilters}},
  "[HealthCheck](#cfn-ecs-service-gatewayconnector-healthcheck)" : {{GatewayConnectorHealthCheck}},
  "[PortName](#cfn-ecs-service-gatewayconnector-portname)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-gatewayconnector-syntax.yaml"></a>

```
  [Filters](#cfn-ecs-service-gatewayconnector-filters): {{
    GatewayConnectorFilters}}
  [HealthCheck](#cfn-ecs-service-gatewayconnector-healthcheck): {{
    GatewayConnectorHealthCheck}}
  [PortName](#cfn-ecs-service-gatewayconnector-portname): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-gatewayconnector-properties"></a>

`Filters`  <a name="cfn-ecs-service-gatewayconnector-filters"></a>
Property description not available.
*Required*: No
*Type*: [GatewayConnectorFilters](aws-properties-ecs-service-gatewayconnectorfilters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheck`  <a name="cfn-ecs-service-gatewayconnector-healthcheck"></a>
Property description not available.
*Required*: No
*Type*: [GatewayConnectorHealthCheck](aws-properties-ecs-service-gatewayconnectorhealthcheck.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortName`  <a name="cfn-ecs-service-gatewayconnector-portname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
