---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-vpclatticeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service VpcLatticeConfiguration
<a name="aws-properties-ecs-service-vpclatticeconfiguration"></a>

The VPC Lattice configuration for your service that holds the information for the target group(s) Amazon ECS tasks will be registered to.

## Syntax
<a name="aws-properties-ecs-service-vpclatticeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-vpclatticeconfiguration-syntax.json"></a>

```
{
  "[AdvancedConfiguration](#cfn-ecs-service-vpclatticeconfiguration-advancedconfiguration)" : {{VpcLatticeAdvancedConfiguration}},
  "[PortName](#cfn-ecs-service-vpclatticeconfiguration-portname)" : {{String}},
  "[RoleArn](#cfn-ecs-service-vpclatticeconfiguration-rolearn)" : {{String}},
  "[TargetGroupArn](#cfn-ecs-service-vpclatticeconfiguration-targetgrouparn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-vpclatticeconfiguration-syntax.yaml"></a>

```
  [AdvancedConfiguration](#cfn-ecs-service-vpclatticeconfiguration-advancedconfiguration): {{
    VpcLatticeAdvancedConfiguration}}
  [PortName](#cfn-ecs-service-vpclatticeconfiguration-portname): {{String}}
  [RoleArn](#cfn-ecs-service-vpclatticeconfiguration-rolearn): {{String}}
  [TargetGroupArn](#cfn-ecs-service-vpclatticeconfiguration-targetgrouparn): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-vpclatticeconfiguration-properties"></a>

`AdvancedConfiguration`  <a name="cfn-ecs-service-vpclatticeconfiguration-advancedconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [VpcLatticeAdvancedConfiguration](aws-properties-ecs-service-vpclatticeadvancedconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortName`  <a name="cfn-ecs-service-vpclatticeconfiguration-portname"></a>
The name of the port mapping to register in the VPC Lattice target group. This is the name of the `portMapping` you defined in your task definition.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ecs-service-vpclatticeconfiguration-rolearn"></a>
The ARN of the IAM role to associate with this VPC Lattice configuration. This is the Amazon ECS infrastructure IAM role that is used to manage your VPC Lattice infrastructure.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetGroupArn`  <a name="cfn-ecs-service-vpclatticeconfiguration-targetgrouparn"></a>
The full Amazon Resource Name (ARN) of the target group or groups associated with the VPC Lattice configuration that the Amazon ECS tasks will be registered to.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
