---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-gatewayconnector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service GatewayConnector
<a name="aws-properties-ecs-service-gatewayconnector"></a>

A gateway connector that attaches an Amazon ECS service to a gateway ingress path. The connector specifies the service port that receives gateway-managed ingress traffic, along with the health check and traffic filters that the gateway applies. A service can have at most one gateway connector.

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
The filters that control which gateway ingress paths the connector applies to.
*Required*: No
*Type*: [GatewayConnectorFilters](aws-properties-ecs-service-gatewayconnectorfilters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheck`  <a name="cfn-ecs-service-gatewayconnector-healthcheck"></a>
The health check that the gateway uses to determine whether the targets for this connector are healthy.
*Required*: No
*Type*: [GatewayConnectorHealthCheck](aws-properties-ecs-service-gatewayconnectorhealthcheck.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortName`  <a name="cfn-ecs-service-gatewayconnector-portname"></a>
The name of the service port that the gateway routes ingress traffic to.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
