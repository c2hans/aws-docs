---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-clientvpntargetnetworkassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ClientVpnTargetNetworkAssociation
<a name="aws-resource-ec2-clientvpntargetnetworkassociation"></a>

Specifies a target network to associate with a Client VPN endpoint. A target network is a subnet in a VPC. You can associate multiple subnets from the same VPC with a Client VPN endpoint. You can associate only one subnet in each Availability Zone. We recommend that you associate at least two subnets to provide Availability Zone redundancy.

## Syntax
<a name="aws-resource-ec2-clientvpntargetnetworkassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-clientvpntargetnetworkassociation-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::ClientVpnTargetNetworkAssociation",
  "Properties" : {
      "[AvailabilityZone](#cfn-ec2-clientvpntargetnetworkassociation-availabilityzone)" : {{String}},
      "[AvailabilityZoneId](#cfn-ec2-clientvpntargetnetworkassociation-availabilityzoneid)" : {{String}},
      "[ClientVpnEndpointId](#cfn-ec2-clientvpntargetnetworkassociation-clientvpnendpointid)" : {{String}},
      "[SubnetId](#cfn-ec2-clientvpntargetnetworkassociation-subnetid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-clientvpntargetnetworkassociation-syntax.yaml"></a>

```
Type: AWS::EC2::ClientVpnTargetNetworkAssociation
Properties:
  [AvailabilityZone](#cfn-ec2-clientvpntargetnetworkassociation-availabilityzone): {{String}}
  [AvailabilityZoneId](#cfn-ec2-clientvpntargetnetworkassociation-availabilityzoneid): {{String}}
  [ClientVpnEndpointId](#cfn-ec2-clientvpntargetnetworkassociation-clientvpnendpointid): {{String}}
  [SubnetId](#cfn-ec2-clientvpntargetnetworkassociation-subnetid): {{String}}
```

## Properties
<a name="aws-resource-ec2-clientvpntargetnetworkassociation-properties"></a>

`AvailabilityZone`  <a name="cfn-ec2-clientvpntargetnetworkassociation-availabilityzone"></a>
Describes Availability Zones, Local Zones, and Wavelength Zones.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AvailabilityZoneId`  <a name="cfn-ec2-clientvpntargetnetworkassociation-availabilityzoneid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClientVpnEndpointId`  <a name="cfn-ec2-clientvpntargetnetworkassociation-clientvpnendpointid"></a>
The ID of the Client VPN endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetId`  <a name="cfn-ec2-clientvpntargetnetworkassociation-subnetid"></a>
The ID of the subnet to associate with the Client VPN endpoint. Required for VPC-based endpoints. For Transit Gateway-based endpoints, use `AvailabilityZone` or `AvailabilityZoneId` instead.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-clientvpntargetnetworkassociation-return-values"></a>

### Ref
<a name="aws-resource-ec2-clientvpntargetnetworkassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the association ID. For example: `cvpn-assoc-1234567890abcdef0`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-ec2-clientvpntargetnetworkassociation--examples"></a>

### Associate a target subnet with a client VPN endpoint
<a name="aws-resource-ec2-clientvpntargetnetworkassociation--examples--Associate_a_target_subnet_with_a_client_VPN_endpoint"></a>

The following example associates a target network with a client VPN endpoint.

#### YAML
<a name="aws-resource-ec2-clientvpntargetnetworkassociation--examples--Associate_a_target_subnet_with_a_client_VPN_endpoint--yaml"></a>

```
myNetworkAssociation:
  Type: "AWS::EC2::ClientVpnTargetNetworkAssociation"
  Properties:
    ClientVpnEndpointId:
      Ref: myClientVpnEndpoint
    SubnetId:
      Ref: mySubnet
```

#### JSON
<a name="aws-resource-ec2-clientvpntargetnetworkassociation--examples--Associate_a_target_subnet_with_a_client_VPN_endpoint--json"></a>

```
"myNetworkAssociation": {
    "Type": "AWS::EC2::ClientVpnTargetNetworkAssociation",
    "Properties": {
        "ClientVpnEndpointId": {
            "Ref": "myClientVpnEndpoint"
        },
        "SubnetId": {
            "Ref": "mySubnet"
        }
    }
}
```

## See also
<a name="aws-resource-ec2-clientvpntargetnetworkassociation--seealso"></a>
+ [ Getting Started with Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-getting-started.html) in the *AWS Client VPN Administrator Guide*
+ [Target Networks](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target.html) in the *AWS Client VPN Administrator Guide*
