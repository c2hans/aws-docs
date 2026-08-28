---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpcgatewayattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPCGatewayAttachment
<a name="aws-resource-ec2-vpcgatewayattachment"></a>

Attaches an internet gateway, or a virtual private gateway to a VPC, enabling connectivity between the internet and the VPC.

## Syntax
<a name="aws-resource-ec2-vpcgatewayattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-vpcgatewayattachment-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::VPCGatewayAttachment",
  "Properties" : {
      "[InternetGatewayId](#cfn-ec2-vpcgatewayattachment-internetgatewayid)" : {{String}},
      "[VpcId](#cfn-ec2-vpcgatewayattachment-vpcid)" : {{String}},
      "[VpnGatewayId](#cfn-ec2-vpcgatewayattachment-vpngatewayid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-vpcgatewayattachment-syntax.yaml"></a>

```
Type: AWS::EC2::VPCGatewayAttachment
Properties:
  [InternetGatewayId](#cfn-ec2-vpcgatewayattachment-internetgatewayid): {{String}}
  [VpcId](#cfn-ec2-vpcgatewayattachment-vpcid): {{String}}
  [VpnGatewayId](#cfn-ec2-vpcgatewayattachment-vpngatewayid): {{String}}
```

## Properties
<a name="aws-resource-ec2-vpcgatewayattachment-properties"></a>

`InternetGatewayId`  <a name="cfn-ec2-vpcgatewayattachment-internetgatewayid"></a>
The ID of the internet gateway.
You must specify either `InternetGatewayId` or `VpnGatewayId`, but not both.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-ec2-vpcgatewayattachment-vpcid"></a>
The ID of the VPC.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpnGatewayId`  <a name="cfn-ec2-vpcgatewayattachment-vpngatewayid"></a>
The ID of the virtual private gateway.
You must specify either `InternetGatewayId` or `VpnGatewayId`, but not both.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-vpcgatewayattachment-return-values"></a>

### Ref
<a name="aws-resource-ec2-vpcgatewayattachment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the VPC gateway attachment.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-ec2-vpcgatewayattachment--examples"></a>

### VPN gateway attachment
<a name="aws-resource-ec2-vpcgatewayattachment--examples--VPN_gateway_attachment"></a>

To attach both an Internet gateway and a VPN gateway to a VPC, you must specify two separate AWS::EC2::VPCGatewayAttachment resources:

#### JSON
<a name="aws-resource-ec2-vpcgatewayattachment--examples--VPN_gateway_attachment--json"></a>

```
"AttachGateway" : {
   "Type" : "AWS::EC2::VPCGatewayAttachment",
   "Properties" : {
      "VpcId" : { "Ref" : "VPC" },
      "InternetGatewayId" : { "Ref" : "myInternetGateway" }
    }
},

"AttachVpnGateway" : {
   "Type" : "AWS::EC2::VPCGatewayAttachment",
   "Properties" : {
      "VpcId" : { "Ref" : "VPC" },
      "VpnGatewayId" : { "Ref" : "myVPNGateway" }
   }
}
```

#### YAML
<a name="aws-resource-ec2-vpcgatewayattachment--examples--VPN_gateway_attachment--yaml"></a>

```
AttachGateway:
  Type: AWS::EC2::VPCGatewayAttachment
  Properties:
    VpcId:
       Ref: VPC
    InternetGatewayId:
       Ref: myInternetGateway
AttachVpnGateway:
  Type: AWS::EC2::VPCGatewayAttachment
  Properties:
    VpcId:
       Ref: VPC
    VpnGatewayId:
       Ref: myVPNGateway
```

## See also
<a name="aws-resource-ec2-vpcgatewayattachment--seealso"></a>
+ [AttachVpnGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachVpnGateway.html) in the *Amazon EC2 API Reference*
+ [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
