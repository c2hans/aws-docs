---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkfirewall-firewall.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::Firewall
<a name="aws-resource-networkfirewall-firewall"></a>

Use the firewall to provide stateful, managed, network firewall and intrusion detection and prevention filtering for your VPCs in Amazon VPC.

The firewall defines the configuration settings for an AWS Network Firewall firewall. The settings include the firewall policy, the subnets in your VPC to use for the firewall endpoints, and any tags that are attached to the firewall AWS resource.

## Syntax
<a name="aws-resource-networkfirewall-firewall-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networkfirewall-firewall-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkFirewall::Firewall",
  "Properties" : {
      "[AvailabilityZoneChangeProtection](#cfn-networkfirewall-firewall-availabilityzonechangeprotection)" : {{Boolean}},
      "[AvailabilityZoneMappings](#cfn-networkfirewall-firewall-availabilityzonemappings)" : {{[ AvailabilityZoneMapping, ... ]}},
      "[DeleteProtection](#cfn-networkfirewall-firewall-deleteprotection)" : {{Boolean}},
      "[Description](#cfn-networkfirewall-firewall-description)" : {{String}},
      "[EnabledAnalysisTypes](#cfn-networkfirewall-firewall-enabledanalysistypes)" : {{[ String, ... ]}},
      "[FirewallName](#cfn-networkfirewall-firewall-firewallname)" : {{String}},
      "[FirewallPolicyArn](#cfn-networkfirewall-firewall-firewallpolicyarn)" : {{String}},
      "[FirewallPolicyChangeProtection](#cfn-networkfirewall-firewall-firewallpolicychangeprotection)" : {{Boolean}},
      "[SubnetChangeProtection](#cfn-networkfirewall-firewall-subnetchangeprotection)" : {{Boolean}},
      "[SubnetMappings](#cfn-networkfirewall-firewall-subnetmappings)" : {{[ SubnetMapping, ... ]}},
      "[Tags](#cfn-networkfirewall-firewall-tags)" : {{[ Tag, ... ]}},
      "[TransitGatewayId](#cfn-networkfirewall-firewall-transitgatewayid)" : {{String}},
      "[VpcId](#cfn-networkfirewall-firewall-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-networkfirewall-firewall-syntax.yaml"></a>

```
Type: AWS::NetworkFirewall::Firewall
Properties:
  [AvailabilityZoneChangeProtection](#cfn-networkfirewall-firewall-availabilityzonechangeprotection): {{Boolean}}
  [AvailabilityZoneMappings](#cfn-networkfirewall-firewall-availabilityzonemappings): {{
    - AvailabilityZoneMapping}}
  [DeleteProtection](#cfn-networkfirewall-firewall-deleteprotection): {{Boolean}}
  [Description](#cfn-networkfirewall-firewall-description): {{String}}
  [EnabledAnalysisTypes](#cfn-networkfirewall-firewall-enabledanalysistypes): {{
    - String}}
  [FirewallName](#cfn-networkfirewall-firewall-firewallname): {{String}}
  [FirewallPolicyArn](#cfn-networkfirewall-firewall-firewallpolicyarn): {{String}}
  [FirewallPolicyChangeProtection](#cfn-networkfirewall-firewall-firewallpolicychangeprotection): {{Boolean}}
  [SubnetChangeProtection](#cfn-networkfirewall-firewall-subnetchangeprotection): {{Boolean}}
  [SubnetMappings](#cfn-networkfirewall-firewall-subnetmappings): {{
    - SubnetMapping}}
  [Tags](#cfn-networkfirewall-firewall-tags): {{
    - Tag}}
  [TransitGatewayId](#cfn-networkfirewall-firewall-transitgatewayid): {{String}}
  [VpcId](#cfn-networkfirewall-firewall-vpcid): {{String}}
```

## Properties
<a name="aws-resource-networkfirewall-firewall-properties"></a>

`AvailabilityZoneChangeProtection`  <a name="cfn-networkfirewall-firewall-availabilityzonechangeprotection"></a>
A setting indicating whether the firewall is protected against changes to its Availability Zone configuration. When set to `TRUE`, you must first disable this protection before adding or removing Availability Zones.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailabilityZoneMappings`  <a name="cfn-networkfirewall-firewall-availabilityzonemappings"></a>
The Availability Zones where the firewall endpoints are created for a transit gateway-attached firewall. Each mapping specifies an Availability Zone where the firewall processes traffic.
*Required*: No
*Type*: Array of [AvailabilityZoneMapping](aws-properties-networkfirewall-firewall-availabilityzonemapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeleteProtection`  <a name="cfn-networkfirewall-firewall-deleteprotection"></a>
A flag indicating whether it is possible to delete the firewall. A setting of `TRUE` indicates that the firewall is protected against deletion. Use this setting to protect against accidentally deleting a firewall that is in use. When you create a firewall, the operation initializes this flag to `TRUE`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-networkfirewall-firewall-description"></a>
A description of the firewall.
*Required*: No
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnabledAnalysisTypes`  <a name="cfn-networkfirewall-firewall-enabledanalysistypes"></a>
An optional setting indicating the specific traffic analysis types to enable on the firewall.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallName`  <a name="cfn-networkfirewall-firewall-firewallname"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FirewallPolicyArn`  <a name="cfn-networkfirewall-firewall-firewallpolicyarn"></a>
The Amazon Resource Name (ARN) of the firewall policy.
The relationship of firewall to firewall policy is many to one. Each firewall requires one firewall policy association, and you can use the same firewall policy for multiple firewalls.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws.*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallPolicyChangeProtection`  <a name="cfn-networkfirewall-firewall-firewallpolicychangeprotection"></a>
A setting indicating whether the firewall is protected against a change to the firewall policy association. Use this setting to protect against accidentally modifying the firewall policy for a firewall that is in use. When you create a firewall, the operation initializes this setting to `TRUE`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetChangeProtection`  <a name="cfn-networkfirewall-firewall-subnetchangeprotection"></a>
A setting indicating whether the firewall is protected against changes to the subnet associations. Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to `TRUE`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetMappings`  <a name="cfn-networkfirewall-firewall-subnetmappings"></a>
The primary public subnets that Network Firewall is using for the firewall. Network Firewall creates a firewall endpoint in each subnet. Create a subnet mapping for each Availability Zone where you want to use the firewall.
These subnets are all defined for a single, primary VPC, and each must belong to a different Availability Zone. Each of these subnets establishes the availability of the firewall in its Availability Zone.
In addition to these subnets, you can define other endpoints for the firewall in `VpcEndpointAssociation` resources. You can define these additional endpoints for any VPC, and for any of the Availability Zones where the firewall resource already has a subnet mapping. VPC endpoint associations give you the ability to protect multiple VPCs using a single firewall, and to define multiple firewall endpoints for a VPC in a single Availability Zone.
*Required*: No
*Type*: Array of [SubnetMapping](aws-properties-networkfirewall-firewall-subnetmapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-networkfirewall-firewall-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-networkfirewall-firewall-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitGatewayId`  <a name="cfn-networkfirewall-firewall-transitgatewayid"></a>
The unique identifier of the transit gateway associated with this firewall. This field is only present for transit gateway-attached firewalls.
*Required*: No
*Type*: String
*Pattern*: `^tgw-[0-9a-z]+$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-networkfirewall-firewall-vpcid"></a>
The unique identifier of the VPC where the firewall is in use. You can't change the VPC of a firewall after you create the firewall.
*Required*: No
*Type*: String
*Pattern*: `^vpc-[0-9a-f]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-networkfirewall-firewall-return-values"></a>

### Ref
<a name="aws-resource-networkfirewall-firewall-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the firewall. For example:

 `{ "Ref": "arn:aws:network-firewall:us-east-1:012345678901:firewall/myFirewallName" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-networkfirewall-firewall-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-networkfirewall-firewall-return-values-fn--getatt-fn--getatt"></a>

`EndpointIds`  <a name="EndpointIds-fn::getatt"></a>
The unique IDs of the firewall endpoints for all of the subnets that you attached to the firewall. The subnets are not listed in any particular order. For example: `["us-west-2c:vpce-111122223333", "us-west-2a:vpce-987654321098", "us-west-2b:vpce-012345678901"]`.

`FirewallArn`  <a name="FirewallArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the firewall.

`FirewallId`  <a name="FirewallId-fn::getatt"></a>
The name of the firewallresource.

`TransitGatewayAttachmentId`  <a name="TransitGatewayAttachmentId-fn::getatt"></a>
The unique identifier of the transit gateway attachment associated with this firewall. This field is only present for transit gateway-attached firewalls.

## Examples
<a name="aws-resource-networkfirewall-firewall--examples"></a>

### Create a firewall
<a name="aws-resource-networkfirewall-firewall--examples--Create_a_firewall"></a>

The following shows example firewall specifications.

#### JSON
<a name="aws-resource-networkfirewall-firewall--examples--Create_a_firewall--json"></a>

```
"SampleFirewall": {
    "Type": "AWS::NetworkFirewall::Firewall",
    "Properties": {
        "FirewallName": "SampleFirewallName",
        "FirewallPolicyArn": {
            "Ref": "SampleFirewallPolicy"
        },
        "VpcId": {
            "Ref": "SampleVPC"
        },
        "SubnetMappings": [
            {
                "SubnetId": {
                    "Ref": "SampleSubnet1"
                }
            },
            {
                "SubnetId": {
                    "Ref": "SampleSubnet2"
                }
            }
        ],
        "Description": "Firewall description goes here",
        "Tags": [
            {
                "Key": "Foo",
                "Value": "Bar"
            }
        ]
    }
```

#### YAML
<a name="aws-resource-networkfirewall-firewall--examples--Create_a_firewall--yaml"></a>

```
SampleFirewall:
  Type: AWS::NetworkFirewall::Firewall
  Properties:
    FirewallName: SampleFirewallName
    FirewallPolicyArn: !Ref SampleFirewallPolicy
    VpcId: !Ref SampleVPC
    SubnetMappings:
      - SubnetId: !Ref SampleSubnet1
      - SubnetId: !Ref SampleSubnet2
    Description: Firewall description goes here
    Tags:
      - Key: Foo
                Value: Bar
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
