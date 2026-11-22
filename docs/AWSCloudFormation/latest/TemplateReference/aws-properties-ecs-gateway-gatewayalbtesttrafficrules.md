---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewayalbtesttrafficrules.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Gateway GatewayAlbTestTrafficRules

The rules that route test traffic to services behind a gateway during progressive deployments.

## Syntax
<a name="aws-properties-ecs-gateway-gatewayalbtesttrafficrules-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-gateway-gatewayalbtesttrafficrules-syntax.json"></a>

```json
{
  "[Header](#cfn-ecs-gateway-gatewayalbtesttrafficrules-header)" : {{GatewayTestTrafficHeader}}
}
```

### YAML
<a name="aws-properties-ecs-gateway-gatewayalbtesttrafficrules-syntax.yaml"></a>

```yaml
  [Header](#cfn-ecs-gateway-gatewayalbtesttrafficrules-header): {{
    GatewayTestTrafficHeader}}
```

## Properties
<a name="aws-properties-ecs-gateway-gatewayalbtesttrafficrules-properties"></a>

`Header`  <a name="cfn-ecs-gateway-gatewayalbtesttrafficrules-header"></a>
The header-based rule that identifies test traffic.
*Required*: No
*Type*: [GatewayTestTrafficHeader](aws-properties-ecs-gateway-gatewaytesttrafficheader.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
