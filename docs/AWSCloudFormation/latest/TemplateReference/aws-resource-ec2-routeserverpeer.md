---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-routeserverpeer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::RouteServerPeer
<a name="aws-resource-ec2-routeserverpeer"></a>

Specifies a BGP peer configuration for a route server endpoint.

A route server peer is a session between a route server endpoint and the device deployed in AWS (such as a firewall appliance or other network security function running on an EC2 instance).

## Syntax
<a name="aws-resource-ec2-routeserverpeer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-routeserverpeer-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::RouteServerPeer",
  "Properties" : {
      "[BgpOptions](#cfn-ec2-routeserverpeer-bgpoptions)" : {{BgpOptions}},
      "[PeerAddress](#cfn-ec2-routeserverpeer-peeraddress)" : {{String}},
      "[RouteServerEndpointId](#cfn-ec2-routeserverpeer-routeserverendpointid)" : {{String}},
      "[Tags](#cfn-ec2-routeserverpeer-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-routeserverpeer-syntax.yaml"></a>

```
Type: AWS::EC2::RouteServerPeer
Properties:
  [BgpOptions](#cfn-ec2-routeserverpeer-bgpoptions): {{
    BgpOptions}}
  [PeerAddress](#cfn-ec2-routeserverpeer-peeraddress): {{String}}
  [RouteServerEndpointId](#cfn-ec2-routeserverpeer-routeserverendpointid): {{String}}
  [Tags](#cfn-ec2-routeserverpeer-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-routeserverpeer-properties"></a>

`BgpOptions`  <a name="cfn-ec2-routeserverpeer-bgpoptions"></a>
The BGP configuration options for this peer, including ASN (Autonomous System Number) and BFD (Bidrectional Forwarding Detection) settings.
*Required*: Yes
*Type*: [BgpOptions](aws-properties-ec2-routeserverpeer-bgpoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerAddress`  <a name="cfn-ec2-routeserverpeer-peeraddress"></a>
The IPv4 address of the peer device.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RouteServerEndpointId`  <a name="cfn-ec2-routeserverpeer-routeserverendpointid"></a>
The ID of the route server endpoint associated with this peer.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-routeserverpeer-tags"></a>
Any tags assigned to the route server peer.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-routeserverpeer-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-routeserverpeer-return-values"></a>

### Ref
<a name="aws-resource-ec2-routeserverpeer-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the peer ID.

### Fn::GetAtt
<a name="aws-resource-ec2-routeserverpeer-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-routeserverpeer-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the route server peer.

`EndpointEniAddress`  <a name="EndpointEniAddress-fn::getatt"></a>
The IP address of the Elastic network interface for the route server endpoint.

`EndpointEniId`  <a name="EndpointEniId-fn::getatt"></a>
The ID of the Elastic network interface for the route server endpoint.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the route server peer.

`RouteServerId`  <a name="RouteServerId-fn::getatt"></a>
The ID of the route server associated with this peer.

`SubnetId`  <a name="SubnetId-fn::getatt"></a>
The ID of the subnet containing the route server peer.

`VpcId`  <a name="VpcId-fn::getatt"></a>
The ID of the VPC containing the route server peer.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
