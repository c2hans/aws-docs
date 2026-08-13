---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-ippoolroutetableassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::IpPoolRouteTableAssociation
<a name="aws-resource-ec2-ippoolroutetableassociation"></a>

A route server association is the connection established between a route server and a VPC.

## Syntax
<a name="aws-resource-ec2-ippoolroutetableassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-ippoolroutetableassociation-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::IpPoolRouteTableAssociation",
  "Properties" : {
      "[PublicIpv4Pool](#cfn-ec2-ippoolroutetableassociation-publicipv4pool)" : {{String}},
      "[RouteTableId](#cfn-ec2-ippoolroutetableassociation-routetableid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-ippoolroutetableassociation-syntax.yaml"></a>

```
Type: AWS::EC2::IpPoolRouteTableAssociation
Properties:
  [PublicIpv4Pool](#cfn-ec2-ippoolroutetableassociation-publicipv4pool): {{String}}
  [RouteTableId](#cfn-ec2-ippoolroutetableassociation-routetableid): {{String}}
```

## Properties
<a name="aws-resource-ec2-ippoolroutetableassociation-properties"></a>

`PublicIpv4Pool`  <a name="cfn-ec2-ippoolroutetableassociation-publicipv4pool"></a>
The ID of a public IPv4 address pool.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RouteTableId`  <a name="cfn-ec2-ippoolroutetableassociation-routetableid"></a>
The ID of a route table.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-ippoolroutetableassociation-return-values"></a>

### Ref
<a name="aws-resource-ec2-ippoolroutetableassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the route table association ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-ippoolroutetableassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-ippoolroutetableassociation-return-values-fn--getatt-fn--getatt"></a>

`AssociationId`  <a name="AssociationId-fn::getatt"></a>
The ID of a route table association.
