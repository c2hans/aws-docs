---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-gateway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Gateway
<a name="aws-resource-ecs-gateway"></a>

Creates an Express service that simplifies deploying containerized web applications on Amazon ECS with managed AWS infrastructure. This operation provisions and configures Application Load Balancers, target groups, security groups, and auto-scaling policies automatically.

Specify a primary container configuration with your application image and basic settings. Amazon ECS creates the necessary AWS resources for traffic distribution, health monitoring, network access control, and capacity management.

Provide an execution role for task operations and an infrastructure role for managing AWS resources on your behalf.

## Syntax
<a name="aws-resource-ecs-gateway-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecs-gateway-syntax.json"></a>

```
{
  "Type" : "AWS::ECS::Gateway",
  "Properties" : {
      "[Configuration](#cfn-ecs-gateway-configuration)" : {{GatewayConfiguration}},
      "[DeletionProtection](#cfn-ecs-gateway-deletionprotection)" : {{Boolean}},
      "[GatewayName](#cfn-ecs-gateway-gatewayname)" : {{String}},
      "[InfrastructureRoleArn](#cfn-ecs-gateway-infrastructurerolearn)" : {{String}},
      "[PropagateTags](#cfn-ecs-gateway-propagatetags)" : {{String}},
      "[Tags](#cfn-ecs-gateway-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ecs-gateway-syntax.yaml"></a>

```
Type: AWS::ECS::Gateway
Properties:
  [Configuration](#cfn-ecs-gateway-configuration): {{
    GatewayConfiguration}}
  [DeletionProtection](#cfn-ecs-gateway-deletionprotection): {{Boolean}}
  [GatewayName](#cfn-ecs-gateway-gatewayname): {{String}}
  [InfrastructureRoleArn](#cfn-ecs-gateway-infrastructurerolearn): {{String}}
  [PropagateTags](#cfn-ecs-gateway-propagatetags): {{String}}
  [Tags](#cfn-ecs-gateway-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ecs-gateway-properties"></a>

`Configuration`  <a name="cfn-ecs-gateway-configuration"></a>
Property description not available.
*Required*: Yes
*Type*: [GatewayConfiguration](aws-properties-ecs-gateway-gatewayconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeletionProtection`  <a name="cfn-ecs-gateway-deletionprotection"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GatewayName`  <a name="cfn-ecs-gateway-gatewayname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InfrastructureRoleArn`  <a name="cfn-ecs-gateway-infrastructurerolearn"></a>
The ARN of the infrastructure role that manages AWS resources for the Express service.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropagateTags`  <a name="cfn-ecs-gateway-propagatetags"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `NONE | GATEWAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ecs-gateway-tags"></a>
The metadata applied to the Express service.
*Required*: No
*Type*: Array of [Tag](aws-properties-ecs-gateway-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ecs-gateway-return-values"></a>

### Ref
<a name="aws-resource-ecs-gateway-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ecs-gateway-return-values-fn--getatt"></a>

####
<a name="aws-resource-ecs-gateway-return-values-fn--getatt-fn--getatt"></a>

`AccessType`  <a name="AccessType-fn::getatt"></a>
Property description not available.

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Configuration.HostSharedAlb.CurrentAlbCount`  <a name="Configuration.HostSharedAlb.CurrentAlbCount-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The Unix timestamp for when the Express service was created.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the Express service.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The Unix timestamp for when the Express service was last updated.
