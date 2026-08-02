---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-trafficmirrortarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TrafficMirrorTarget
<a name="aws-resource-ec2-trafficmirrortarget"></a>

Specifies a target for your Traffic Mirror session.

A Traffic Mirror target is the destination for mirrored traffic. The Traffic Mirror source and the Traffic Mirror target (monitoring appliances) can be in the same VPC, or in different VPCs connected via VPC peering or a transit gateway.

A Traffic Mirror target can be a network interface, a Network Load Balancer, or a Gateway Load Balancer endpoint.

To use the target in a Traffic Mirror session, use [AWS::EC2::TrafficMirrorSession](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html).

## Syntax
<a name="aws-resource-ec2-trafficmirrortarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-trafficmirrortarget-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::TrafficMirrorTarget",
  "Properties" : {
      "[Description](#cfn-ec2-trafficmirrortarget-description)" : {{String}},
      "[GatewayLoadBalancerEndpointId](#cfn-ec2-trafficmirrortarget-gatewayloadbalancerendpointid)" : {{String}},
      "[NetworkInterfaceId](#cfn-ec2-trafficmirrortarget-networkinterfaceid)" : {{String}},
      "[NetworkLoadBalancerArn](#cfn-ec2-trafficmirrortarget-networkloadbalancerarn)" : {{String}},
      "[Tags](#cfn-ec2-trafficmirrortarget-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-trafficmirrortarget-syntax.yaml"></a>

```
Type: AWS::EC2::TrafficMirrorTarget
Properties:
  [Description](#cfn-ec2-trafficmirrortarget-description): {{String}}
  [GatewayLoadBalancerEndpointId](#cfn-ec2-trafficmirrortarget-gatewayloadbalancerendpointid): {{String}}
  [NetworkInterfaceId](#cfn-ec2-trafficmirrortarget-networkinterfaceid): {{String}}
  [NetworkLoadBalancerArn](#cfn-ec2-trafficmirrortarget-networkloadbalancerarn): {{String}}
  [Tags](#cfn-ec2-trafficmirrortarget-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-trafficmirrortarget-properties"></a>

`Description`  <a name="cfn-ec2-trafficmirrortarget-description"></a>
The description of the Traffic Mirror target.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GatewayLoadBalancerEndpointId`  <a name="cfn-ec2-trafficmirrortarget-gatewayloadbalancerendpointid"></a>
The ID of the Gateway Load Balancer endpoint.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkInterfaceId`  <a name="cfn-ec2-trafficmirrortarget-networkinterfaceid"></a>
The network interface ID that is associated with the target.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkLoadBalancerArn`  <a name="cfn-ec2-trafficmirrortarget-networkloadbalancerarn"></a>
The Amazon Resource Name (ARN) of the Network Load Balancer that is associated with the target.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-trafficmirrortarget-tags"></a>
The tags to assign to the Traffic Mirror target.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-trafficmirrortarget-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-trafficmirrortarget-return-values"></a>

### Ref
<a name="aws-resource-ec2-trafficmirrortarget-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the Traffic Mirror target.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-ec2-trafficmirrortarget--examples"></a>

**Topics**
+ [Create a traffic mirror target associated with a Network Load Balancer](#aws-resource-ec2-trafficmirrortarget--examples--Create_a_traffic_mirror_target_associated_with_a_Network_Load_Balancer)
+ [Create a traffic mirror target associated with a network interface](#aws-resource-ec2-trafficmirrortarget--examples--Create_a_traffic_mirror_target_associated_with_a_network_interface)

### Create a traffic mirror target associated with a Network Load Balancer
<a name="aws-resource-ec2-trafficmirrortarget--examples--Create_a_traffic_mirror_target_associated_with_a_Network_Load_Balancer"></a>

This is a traffic mirror target associated with a Network Load Balancer.

#### JSON
<a name="aws-resource-ec2-trafficmirrortarget--examples--Create_a_traffic_mirror_target_associated_with_a_Network_Load_Balancer--json"></a>

```
{
  "SampleNLBTrafficMirrorTarget": {
    "Type": "AWS::EC2::TrafficMirrorTarget",
    "Properties": {
      "Description": "Example traffic mirror target associated with a network load balancer",
      "NetworkLoadBalancerArn": "arn:aws:elasticloadbalancing:us-east-1:724145273726:loadbalancer/net/NLB/7cabvhEXAMPLE",
       "Tags": [
        {
          "Key": "Name",
          "Value": "SampleNLBTarget"
        }
      ]
    }
  }
}
```

#### YAML
<a name="aws-resource-ec2-trafficmirrortarget--examples--Create_a_traffic_mirror_target_associated_with_a_Network_Load_Balancer--yaml"></a>

```
SampleNLBTrafficMirrorTarget:
  Type: "AWS::EC2::TrafficMirrorTarget"
  Properties:
    Description: "Example traffic mirror target associated with a network load balancer",
    NetworkLoadBalancerArn: "arn:aws:elasticloadbalancing:us-east-1:724145273726:loadbalancer/net/NLB/7cabvhEXAMPLE"
  Tags:
    - Key: "Name"
      Value: "SampleNLBTarget"
```

### Create a traffic mirror target associated with a network interface
<a name="aws-resource-ec2-trafficmirrortarget--examples--Create_a_traffic_mirror_target_associated_with_a_network_interface"></a>

This is a traffic mirror target associated with a network interface.

#### JSON
<a name="aws-resource-ec2-trafficmirrortarget--examples--Create_a_traffic_mirror_target_associated_with_a_network_interface--json"></a>

```
{
  "SampleNetworkInterfaceTarget": {
    "Type": "AWS::EC2::TrafficMirrorTarget",
    "Properties": {
      "Description": "Example traffic mirror target associated with a network interface",
      "NetworkInterfaceId": "eni-070203a001EXAMPLE",
      "Tags": [
        {
          "Key": "Name",
          "Value": "SampleNetworkInterfaceTarget"
        }
      ]
    }
  }
}
```

#### YAML
<a name="aws-resource-ec2-trafficmirrortarget--examples--Create_a_traffic_mirror_target_associated_with_a_network_interface--yaml"></a>

```
SampleNetworkInterfaceTarget:
  Type: "AWS::EC2::TrafficMirrorTarget"
  Properties:
    Description: "Example traffic mirror target associated with a network interface"
    NetworkInterfaceId: "eni-070203a001EXAMPLE"
    Tags:
    - Key: "Name"
      Value: "SampleNetworkInterfaceTarget"
```

## See also
<a name="aws-resource-ec2-trafficmirrortarget--seealso"></a>
+ [Traffic mirror targets](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-targets.html) in *Traffic Mirroring*
+ [CreateTrafficMirrorTarget](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorTarget.html) in the *Amazon EC2 API Reference*
