---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-subnet-blockpublicaccessstates.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Subnet BlockPublicAccessStates
<a name="aws-properties-ec2-subnet-blockpublicaccessstates"></a>

Specifies the state of VPC Block Public Access (BPA).

## Syntax
<a name="aws-properties-ec2-subnet-blockpublicaccessstates-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-subnet-blockpublicaccessstates-syntax.json"></a>

```
{
  "[InternetGatewayBlockMode](#cfn-ec2-subnet-blockpublicaccessstates-internetgatewayblockmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-subnet-blockpublicaccessstates-syntax.yaml"></a>

```
  [InternetGatewayBlockMode](#cfn-ec2-subnet-blockpublicaccessstates-internetgatewayblockmode): {{String}}
```

## Properties
<a name="aws-properties-ec2-subnet-blockpublicaccessstates-properties"></a>

`InternetGatewayBlockMode`  <a name="cfn-ec2-subnet-blockpublicaccessstates-internetgatewayblockmode"></a>
The mode of VPC BPA.
+ `off`: VPC BPA is not enabled and traffic is allowed to and from internet gateways and egress-only internet gateways in this Region.
+ `block-bidirectional`: Block all traffic to and from internet gateways and egress-only internet gateways in this Region (except for excluded VPCs and subnets).
+ `block-ingress`: Block all internet traffic to the VPCs in this Region (except for VPCs or subnets which are excluded). Only traffic to and from NAT gateways and egress-only internet gateways is allowed because these gateways only allow outbound connections to be established.
*Required*: No
*Type*: String
*Allowed values*: `off | block-bidirectional | block-ingress`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
