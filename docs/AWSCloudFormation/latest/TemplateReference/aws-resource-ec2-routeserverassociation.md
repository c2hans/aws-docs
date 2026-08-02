---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-routeserverassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::RouteServerAssociation
<a name="aws-resource-ec2-routeserverassociation"></a>

Specifies the association between a route server and a VPC.

A route server association is the connection established between a route server and a VPC.

## Syntax
<a name="aws-resource-ec2-routeserverassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-routeserverassociation-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::RouteServerAssociation",
  "Properties" : {
      "[RouteServerId](#cfn-ec2-routeserverassociation-routeserverid)" : {{String}},
      "[VpcId](#cfn-ec2-routeserverassociation-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-routeserverassociation-syntax.yaml"></a>

```
Type: AWS::EC2::RouteServerAssociation
Properties:
  [RouteServerId](#cfn-ec2-routeserverassociation-routeserverid): {{String}}
  [VpcId](#cfn-ec2-routeserverassociation-vpcid): {{String}}
```

## Properties
<a name="aws-resource-ec2-routeserverassociation-properties"></a>

`RouteServerId`  <a name="cfn-ec2-routeserverassociation-routeserverid"></a>
The ID of the associated route server.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-ec2-routeserverassociation-vpcid"></a>
The ID of the associated VPC.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-routeserverassociation-return-values"></a>

### Ref
<a name="aws-resource-ec2-routeserverassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the route server ID and VPC ID separated by the pipe symbol (\|).
