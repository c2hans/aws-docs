---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-egressonlyinternetgateway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EgressOnlyInternetGateway
<a name="aws-resource-ec2-egressonlyinternetgateway"></a>

[IPv6 only] Specifies an egress-only internet gateway for your VPC. An egress-only internet gateway is used to enable outbound communication over IPv6 from instances in your VPC to the internet, and prevents hosts outside of your VPC from initiating an IPv6 connection with your instance.

For more information, see [Egress-only internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-resource-ec2-egressonlyinternetgateway-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-egressonlyinternetgateway-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::EgressOnlyInternetGateway",
  "Properties" : {
      "[Tags](#cfn-ec2-egressonlyinternetgateway-tags)" : {{[ Tag, ... ]}},
      "[VpcId](#cfn-ec2-egressonlyinternetgateway-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-egressonlyinternetgateway-syntax.yaml"></a>

```
Type: AWS::EC2::EgressOnlyInternetGateway
Properties:
  [Tags](#cfn-ec2-egressonlyinternetgateway-tags): {{
    - Tag}}
  [VpcId](#cfn-ec2-egressonlyinternetgateway-vpcid): {{String}}
```

## Properties
<a name="aws-resource-ec2-egressonlyinternetgateway-properties"></a>

`Tags`  <a name="cfn-ec2-egressonlyinternetgateway-tags"></a>
The tags assigned to the egress-only internet gateway.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-egressonlyinternetgateway-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-ec2-egressonlyinternetgateway-vpcid"></a>
The ID of the VPC for which to create the egress-only internet gateway.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-egressonlyinternetgateway-return-values"></a>

### Ref
<a name="aws-resource-ec2-egressonlyinternetgateway-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the egress-only internet gateway (the physical resource ID).

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-egressonlyinternetgateway-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-egressonlyinternetgateway-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The ID of the egress-only internet gateway.

## Examples
<a name="aws-resource-ec2-egressonlyinternetgateway--examples"></a>

### Create an egress-only internet gateway
<a name="aws-resource-ec2-egressonlyinternetgateway--examples--Create_an_egress-only_internet_gateway"></a>

The following example creates an egress-only internet gateway for the specified VPC.

#### YAML
<a name="aws-resource-ec2-egressonlyinternetgateway--examples--Create_an_egress-only_internet_gateway--yaml"></a>

```
myEgressOnlyInternetGateway:
    Type: AWS::EC2::EgressOnlyInternetGateway
    Properties:
        VpcId: vpc-1a2b3c4d
```

#### JSON
<a name="aws-resource-ec2-egressonlyinternetgateway--examples--Create_an_egress-only_internet_gateway--json"></a>

```
{
    "myEgressOnlyInternetGateway" : {
        "Type" : "AWS::EC2::EgressOnlyInternetGateway",
        "Properties" : {
            "VpcId" : "vpc-1a2b3c4d"
        }
    }
}
```

## See also
<a name="aws-resource-ec2-egressonlyinternetgateway--seealso"></a>
+ [CreateEgressOnlyInternetGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-CreateEgressOnlyInternetGateway.html) in the *Amazon EC2 API Reference*
