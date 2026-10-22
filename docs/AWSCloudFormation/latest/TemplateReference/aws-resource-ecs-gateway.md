---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-gateway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Gateway
<a name="aws-resource-ecs-gateway"></a>

The details of a gateway, including its configuration, status, and the infrastructure settings for its type.

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
The type-specific configuration for the gateway.
*Required*: Yes
*Type*: [GatewayConfiguration](aws-properties-ecs-gateway-gatewayconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeletionProtection`  <a name="cfn-ecs-gateway-deletionprotection"></a>
Specifies whether deletion protection is enabled for the gateway.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GatewayName`  <a name="cfn-ecs-gateway-gatewayname"></a>
The name of the gateway.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InfrastructureRoleArn`  <a name="cfn-ecs-gateway-infrastructurerolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that the gateway uses to manage infrastructure on your behalf.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropagateTags`  <a name="cfn-ecs-gateway-propagatetags"></a>
Specifies whether the gateway propagates its tags to the infrastructure it manages.
*Required*: No
*Type*: String
*Allowed values*: `NONE | GATEWAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ecs-gateway-tags"></a>
The metadata applied to the gateway. Each tag consists of a key and an optional value.
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
Specifies whether the gateway is publicly accessible (`PUBLIC`) or private (`PRIVATE`). The gateway derives this value from its scheme when you create the gateway, and the value is immutable.

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the security group.

`Configuration.HostSharedAlb.CurrentAlbCount`  <a name="Configuration.HostSharedAlb.CurrentAlbCount-fn::getatt"></a>
The current number of Application Load Balancers that the gateway has allocated.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The Unix timestamp for the time when the gateway was created.

`Status`  <a name="Status-fn::getatt"></a>
The status of the gateway.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The Unix timestamp for the time when the gateway was last updated.
