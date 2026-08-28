---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkfirewall-vpcendpointassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::VpcEndpointAssociation
<a name="aws-resource-networkfirewall-vpcendpointassociation"></a>

A VPC endpoint association defines a single subnet to use for a firewall endpoint for a `Firewall`. You can define VPC endpoint associations only in the Availability Zones that already have a subnet mapping defined in the `Firewall` resource.

**Note**
You can retrieve the list of Availability Zones that are available for use by calling `DescribeFirewallMetadata`.

To manage firewall endpoints, first, in the `Firewall` specification, you specify a single VPC and one subnet for each of the Availability Zones where you want to use the firewall. Then you can define additional endpoints as VPC endpoint associations.

You can use VPC endpoint associations to expand the protections of the firewall as follows:
+ **Protect multiple VPCs with a single firewall** - You can use the firewall to protect other VPCs, either in your account or in accounts where the firewall is shared. You can only specify Availability Zones that already have a firewall endpoint defined in the `Firewall` subnet mappings.
+ **Define multiple firewall endpoints for a VPC in an Availability Zone** - You can create additional firewall endpoints for the VPC that you have defined in the firewall, in any Availability Zone that already has an endpoint defined in the `Firewall` subnet mappings. You can create multiple VPC endpoint associations for any other VPC where you use the firewall.

You can use AWS Resource Access Manager to share a `Firewall` that you own with other accounts, which gives them the ability to use the firewall to create VPC endpoint associations. For information about sharing a firewall, see `PutResourcePolicy` in this guide and see [Sharing Network Firewall resources](https://docs.aws.amazon.com/network-firewall/latest/developerguide/sharing.html) in the *AWS Network Firewall Developer Guide*.

The status of the VPC endpoint association, which indicates whether it's ready to filter network traffic, is provided in the corresponding VPC endpoint association status. You can retrieve both the association and its status by calling `DescribeVpcEndpointAssociation`.

## Syntax
<a name="aws-resource-networkfirewall-vpcendpointassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networkfirewall-vpcendpointassociation-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkFirewall::VpcEndpointAssociation",
  "Properties" : {
      "[Description](#cfn-networkfirewall-vpcendpointassociation-description)" : {{String}},
      "[FirewallArn](#cfn-networkfirewall-vpcendpointassociation-firewallarn)" : {{String}},
      "[SubnetMapping](#cfn-networkfirewall-vpcendpointassociation-subnetmapping)" : {{SubnetMapping}},
      "[Tags](#cfn-networkfirewall-vpcendpointassociation-tags)" : {{[ Tag, ... ]}},
      "[VpcId](#cfn-networkfirewall-vpcendpointassociation-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-networkfirewall-vpcendpointassociation-syntax.yaml"></a>

```
Type: AWS::NetworkFirewall::VpcEndpointAssociation
Properties:
  [Description](#cfn-networkfirewall-vpcendpointassociation-description): {{String}}
  [FirewallArn](#cfn-networkfirewall-vpcendpointassociation-firewallarn): {{String}}
  [SubnetMapping](#cfn-networkfirewall-vpcendpointassociation-subnetmapping): {{
    SubnetMapping}}
  [Tags](#cfn-networkfirewall-vpcendpointassociation-tags): {{
    - Tag}}
  [VpcId](#cfn-networkfirewall-vpcendpointassociation-vpcid): {{String}}
```

## Properties
<a name="aws-resource-networkfirewall-vpcendpointassociation-properties"></a>

`Description`  <a name="cfn-networkfirewall-vpcendpointassociation-description"></a>
A description of the VPC endpoint association.
*Required*: No
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FirewallArn`  <a name="cfn-networkfirewall-vpcendpointassociation-firewallarn"></a>
The Amazon Resource Name (ARN) of the firewall.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws.*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetMapping`  <a name="cfn-networkfirewall-vpcendpointassociation-subnetmapping"></a>
The ID for a subnet that's used in an association with a firewall. This is used in `CreateFirewall`, `AssociateSubnets`, and `CreateVpcEndpointAssociation`. AWS Network Firewall creates an instance of the associated firewall in each subnet that you specify, to filter traffic in the subnet's Availability Zone.
*Required*: Yes
*Type*: [SubnetMapping](aws-properties-networkfirewall-vpcendpointassociation-subnetmapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-networkfirewall-vpcendpointassociation-tags"></a>
The key:value pairs to associate with the resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkfirewall-vpcendpointassociation-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-networkfirewall-vpcendpointassociation-vpcid"></a>
The unique identifier of the VPC for the endpoint association.
*Required*: Yes
*Type*: String
*Pattern*: `^vpc-[0-9a-f]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-networkfirewall-vpcendpointassociation-return-values"></a>

### Ref
<a name="aws-resource-networkfirewall-vpcendpointassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the firewall. For example:

 `{ "Ref": "arn:aws:network-firewall:us-east-1:123456789012:vpc-endpoint-association/UUID" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-networkfirewall-vpcendpointassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-networkfirewall-vpcendpointassociation-return-values-fn--getatt-fn--getatt"></a>

`EndpointId`  <a name="EndpointId-fn::getatt"></a>
The unique ID of the firewall endpoint for the subnet that you attached to the firewall.For example: "vpce-111122223333"

`VpcEndpointAssociationArn`  <a name="VpcEndpointAssociationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of a VPC endpoint association.

`VpcEndpointAssociationId`  <a name="VpcEndpointAssociationId-fn::getatt"></a>
The unique identifier of the VPC endpoint association.

## Examples
<a name="aws-resource-networkfirewall-vpcendpointassociation--examples"></a>

### Create a VPC Endpoint Association
<a name="aws-resource-networkfirewall-vpcendpointassociation--examples--Create_a_VPC_Endpoint_Association"></a>

The following shows example VPC Endpoint Association specifications.

#### JSON
<a name="aws-resource-networkfirewall-vpcendpointassociation--examples--Create_a_VPC_Endpoint_Association--json"></a>

```
"SampleVpcEndpointAssociation": {
    "Type": "AWS::NetworkFirewall::VpcEndpointAssociation",
    "Properties": {
        "Description": "VpcEndpointAssociation description goes here",
        "FirewallArn": {
            "Ref": "SampleFirewall"
        },
        "SubnetMapping": {
            "SubnetId": {
                "Ref": "SampleSubnet"
            }
        },
        "VpcId": {
            "Ref": "SampleVPC"
        },
        "Tags": [
            {
                "Key": "Foo",
                "Value": "Bar"
            }
        ]
    }
}
```

#### YAML
<a name="aws-resource-networkfirewall-vpcendpointassociation--examples--Create_a_VPC_Endpoint_Association--yaml"></a>

```
SampleVpcEndpointAssociation:
  Type: AWS::NetworkFirewall::VpcEndpointAssociation
  Properties:
    FirewallArn: !Ref SampleFirewall
    VpcId: !Ref SampleVPC
    SubnetMapping:
      SubnetId: !Ref SampleSubnet
    Description: VpcEndpointAssociation description goes here
    Tags:
      - Key: Foo
        Value: Bar
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
