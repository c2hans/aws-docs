---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-routeserverendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::RouteServerEndpoint
<a name="aws-resource-ec2-routeserverendpoint"></a>

Creates a new endpoint for a route server in a specified subnet.

A route server endpoint is an AWS-managed component inside a subnet that facilitates [BGP (Border Gateway Protocol)](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) connections between your route server and your BGP peers.

For more information see [Dynamic routing in your VPC with VPC Route Server](https://docs.aws.amazon.com/vpc/latest/userguide/dynamic-routing-route-server.html) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-resource-ec2-routeserverendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-routeserverendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::RouteServerEndpoint",
  "Properties" : {
      "[RouteServerId](#cfn-ec2-routeserverendpoint-routeserverid)" : {{String}},
      "[SubnetId](#cfn-ec2-routeserverendpoint-subnetid)" : {{String}},
      "[Tags](#cfn-ec2-routeserverendpoint-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-routeserverendpoint-syntax.yaml"></a>

```
Type: AWS::EC2::RouteServerEndpoint
Properties:
  [RouteServerId](#cfn-ec2-routeserverendpoint-routeserverid): {{String}}
  [SubnetId](#cfn-ec2-routeserverendpoint-subnetid): {{String}}
  [Tags](#cfn-ec2-routeserverendpoint-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-routeserverendpoint-properties"></a>

`RouteServerId`  <a name="cfn-ec2-routeserverendpoint-routeserverid"></a>
The ID of the route server associated with this endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetId`  <a name="cfn-ec2-routeserverendpoint-subnetid"></a>
The ID of the subnet to place the route server endpoint into.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-routeserverendpoint-tags"></a>
Any tags assigned to the route server endpoint.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-routeserverendpoint-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-routeserverendpoint-return-values"></a>

### Ref
<a name="aws-resource-ec2-routeserverendpoint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the endpoint ID.

### Fn::GetAtt
<a name="aws-resource-ec2-routeserverendpoint-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-routeserverendpoint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN for the endpoint.

`EniAddress`  <a name="EniAddress-fn::getatt"></a>
The IP address of the Elastic network interface for the endpoint.

`EniId`  <a name="EniId-fn::getatt"></a>
The ID of the Elastic network interface for the endpoint.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the route server endpoint.

`VpcId`  <a name="VpcId-fn::getatt"></a>
The ID of the VPC containing the endpoint.
