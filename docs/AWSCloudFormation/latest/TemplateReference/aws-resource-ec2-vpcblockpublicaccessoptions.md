---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpcblockpublicaccessoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPCBlockPublicAccessOptions
<a name="aws-resource-ec2-vpcblockpublicaccessoptions"></a>

VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. To learn more about VPC BPA, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-resource-ec2-vpcblockpublicaccessoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-vpcblockpublicaccessoptions-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::VPCBlockPublicAccessOptions",
  "Properties" : {
      "[InternetGatewayBlockMode](#cfn-ec2-vpcblockpublicaccessoptions-internetgatewayblockmode)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-vpcblockpublicaccessoptions-syntax.yaml"></a>

```
Type: AWS::EC2::VPCBlockPublicAccessOptions
Properties:
  [InternetGatewayBlockMode](#cfn-ec2-vpcblockpublicaccessoptions-internetgatewayblockmode): {{String}}
```

## Properties
<a name="aws-resource-ec2-vpcblockpublicaccessoptions-properties"></a>

`InternetGatewayBlockMode`  <a name="cfn-ec2-vpcblockpublicaccessoptions-internetgatewayblockmode"></a>
The desired VPC Block Public Access mode for internet gateways in your account. We do not allow you to create this resource type in an "off" mode since off is the default value.
+ `block-bidirectional`: Block all traffic to and from internet gateways and egress-only internet gateways in this Region (except for excluded VPCs and subnets).
+ `block-ingress`: Block all internet traffic to the VPCs in this Region (except for VPCs or subnets which are excluded). Only traffic to and from NAT gateways and egress-only internet gateways is allowed because these gateways only allow outbound connections to be established.
*Required*: Yes
*Type*: String
*Allowed values*: `block-bidirectional | block-ingress`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-vpcblockpublicaccessoptions-return-values"></a>

### Ref
<a name="aws-resource-ec2-vpcblockpublicaccessoptions-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns your account ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-vpcblockpublicaccessoptions-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-vpcblockpublicaccessoptions-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
The ID of the AWS account.

`ExclusionsAllowed`  <a name="ExclusionsAllowed-fn::getatt"></a>
Property description not available.
