---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewaytesttrafficheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Gateway GatewayTestTrafficHeader
<a name="aws-properties-ecs-gateway-gatewaytesttrafficheader"></a>

A header-based rule that identifies test traffic for progressive deployments.

## Syntax
<a name="aws-properties-ecs-gateway-gatewaytesttrafficheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-gateway-gatewaytesttrafficheader-syntax.json"></a>

```
{
  "[Name](#cfn-ecs-gateway-gatewaytesttrafficheader-name)" : {{String}},
  "[Values](#cfn-ecs-gateway-gatewaytesttrafficheader-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-gateway-gatewaytesttrafficheader-syntax.yaml"></a>

```
  [Name](#cfn-ecs-gateway-gatewaytesttrafficheader-name): {{String}}
  [Values](#cfn-ecs-gateway-gatewaytesttrafficheader-values): {{
    - String}}
```

## Properties
<a name="aws-properties-ecs-gateway-gatewaytesttrafficheader-properties"></a>

`Name`  <a name="cfn-ecs-gateway-gatewaytesttrafficheader-name"></a>
The name of the header to match for test traffic routing.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-ecs-gateway-gatewaytesttrafficheader-values"></a>
The header values to match for test traffic routing.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
