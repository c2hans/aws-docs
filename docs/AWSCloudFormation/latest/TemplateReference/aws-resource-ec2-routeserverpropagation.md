---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-routeserverpropagation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::RouteServerPropagation
<a name="aws-resource-ec2-routeserverpropagation"></a>

Specifies route propagation from a route server to a route table.

For more information see [Dynamic routing in your VPC with VPC Route Server](https://docs.aws.amazon.com/vpc/latest/userguide/dynamic-routing-route-server.html) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-resource-ec2-routeserverpropagation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-routeserverpropagation-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::RouteServerPropagation",
  "Properties" : {
      "[RouteServerId](#cfn-ec2-routeserverpropagation-routeserverid)" : {{String}},
      "[RouteTableId](#cfn-ec2-routeserverpropagation-routetableid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-routeserverpropagation-syntax.yaml"></a>

```
Type: AWS::EC2::RouteServerPropagation
Properties:
  [RouteServerId](#cfn-ec2-routeserverpropagation-routeserverid): {{String}}
  [RouteTableId](#cfn-ec2-routeserverpropagation-routetableid): {{String}}
```

## Properties
<a name="aws-resource-ec2-routeserverpropagation-properties"></a>

`RouteServerId`  <a name="cfn-ec2-routeserverpropagation-routeserverid"></a>
The ID of the route server configured for route propagation.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RouteTableId`  <a name="cfn-ec2-routeserverpropagation-routetableid"></a>
The ID of the route table configured for route server propagation.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-routeserverpropagation-return-values"></a>

### Ref
<a name="aws-resource-ec2-routeserverpropagation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the route server ID and route table ID separated by the pipe symbol (\|).
