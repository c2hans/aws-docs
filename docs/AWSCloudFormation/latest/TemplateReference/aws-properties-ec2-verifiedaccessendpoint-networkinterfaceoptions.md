---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccessendpoint-networkinterfaceoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessEndpoint NetworkInterfaceOptions
<a name="aws-properties-ec2-verifiedaccessendpoint-networkinterfaceoptions"></a>

Describes the network interface options when creating an AWS Verified Access endpoint using the `network-interface` type.

## Syntax
<a name="aws-properties-ec2-verifiedaccessendpoint-networkinterfaceoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccessendpoint-networkinterfaceoptions-syntax.json"></a>

```
{
  "[NetworkInterfaceId](#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-networkinterfaceid)" : {{String}},
  "[Port](#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-port)" : {{Integer}},
  "[PortRanges](#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-portranges)" : {{[ PortRange, ... ]}},
  "[Protocol](#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-protocol)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccessendpoint-networkinterfaceoptions-syntax.yaml"></a>

```
  [NetworkInterfaceId](#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-networkinterfaceid): {{String}}
  [Port](#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-port): {{Integer}}
  [PortRanges](#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-portranges): {{
    - PortRange}}
  [Protocol](#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-protocol): {{String}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccessendpoint-networkinterfaceoptions-properties"></a>

`NetworkInterfaceId`  <a name="cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-networkinterfaceid"></a>
The ID of the network interface.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Port`  <a name="cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-port"></a>
The IP port number.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortRanges`  <a name="cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-portranges"></a>
The port ranges.
*Required*: No
*Type*: Array of [PortRange](aws-properties-ec2-verifiedaccessendpoint-portrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-protocol"></a>
The IP protocol.
*Required*: No
*Type*: String
*Allowed values*: `http | https | tcp`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
