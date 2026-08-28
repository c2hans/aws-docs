---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function VpcConfig
<a name="aws-properties-lambda-function-vpcconfig"></a>

The VPC security groups and subnets that are attached to a Lambda function. When you connect a function to a VPC, Lambda creates an elastic network interface for each combination of security group and subnet in the function's VPC configuration. The function can only access resources and the internet through that VPC. For more information, see [VPC Settings](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html).

**Note**
When you delete a function, CloudFormation monitors the state of its network interfaces and waits for Lambda to delete them before proceeding. If the VPC is defined in the same stack, the network interfaces need to be deleted by Lambda before CloudFormation can delete the VPC's resources.
To monitor network interfaces, CloudFormation needs the `ec2:DescribeNetworkInterfaces` permission. It obtains this from the user or role that modifies the stack. If you don't provide this permission, CloudFormation does not wait for network interfaces to be deleted.

## Syntax
<a name="aws-properties-lambda-function-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-vpcconfig-syntax.json"></a>

```
{
  "[Ipv6AllowedForDualStack](#cfn-lambda-function-vpcconfig-ipv6allowedfordualstack)" : {{Boolean}},
  "[SecurityGroupIds](#cfn-lambda-function-vpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-lambda-function-vpcconfig-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-lambda-function-vpcconfig-syntax.yaml"></a>

```
  [Ipv6AllowedForDualStack](#cfn-lambda-function-vpcconfig-ipv6allowedfordualstack): {{Boolean}}
  [SecurityGroupIds](#cfn-lambda-function-vpcconfig-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-lambda-function-vpcconfig-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-lambda-function-vpcconfig-properties"></a>

`Ipv6AllowedForDualStack`  <a name="cfn-lambda-function-vpcconfig-ipv6allowedfordualstack"></a>
Allows outbound IPv6 traffic on VPC functions that are connected to dual-stack subnets.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-lambda-function-vpcconfig-securitygroupids"></a>
A list of VPC security group IDs.
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-lambda-function-vpcconfig-subnetids"></a>
A list of VPC subnet IDs.
*Required*: No
*Type*: Array of String
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-lambda-function-vpcconfig--examples"></a>

### VPC Configuration
<a name="aws-properties-lambda-function-vpcconfig--examples--VPC_Configuration"></a>

Connect a function to a VPC.

#### YAML
<a name="aws-properties-lambda-function-vpcconfig--examples--VPC_Configuration--yaml"></a>

```
      VpcConfig:
        SecurityGroupIds:
          - sg-085912345678492fb
        SubnetIds:
          - subnet-071f712345678e7c8
          - subnet-07fd123456788a036
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
