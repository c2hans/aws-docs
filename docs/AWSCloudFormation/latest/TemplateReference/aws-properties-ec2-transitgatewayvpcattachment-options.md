---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-transitgatewayvpcattachment-options.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayVpcAttachment Options
<a name="aws-properties-ec2-transitgatewayvpcattachment-options"></a>

Describes the VPC attachment options.

## Syntax
<a name="aws-properties-ec2-transitgatewayvpcattachment-options-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-transitgatewayvpcattachment-options-syntax.json"></a>

```
{
  "[ApplianceModeSupport](#cfn-ec2-transitgatewayvpcattachment-options-appliancemodesupport)" : {{String}},
  "[DnsSupport](#cfn-ec2-transitgatewayvpcattachment-options-dnssupport)" : {{String}},
  "[Ipv6Support](#cfn-ec2-transitgatewayvpcattachment-options-ipv6support)" : {{String}},
  "[SecurityGroupReferencingSupport](#cfn-ec2-transitgatewayvpcattachment-options-securitygroupreferencingsupport)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-transitgatewayvpcattachment-options-syntax.yaml"></a>

```
  [ApplianceModeSupport](#cfn-ec2-transitgatewayvpcattachment-options-appliancemodesupport): {{String}}
  [DnsSupport](#cfn-ec2-transitgatewayvpcattachment-options-dnssupport): {{String}}
  [Ipv6Support](#cfn-ec2-transitgatewayvpcattachment-options-ipv6support): {{String}}
  [SecurityGroupReferencingSupport](#cfn-ec2-transitgatewayvpcattachment-options-securitygroupreferencingsupport): {{String}}
```

## Properties
<a name="aws-properties-ec2-transitgatewayvpcattachment-options-properties"></a>

`ApplianceModeSupport`  <a name="cfn-ec2-transitgatewayvpcattachment-options-appliancemodesupport"></a>
Enable or disable appliance mode support. The default is `disable`.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DnsSupport`  <a name="cfn-ec2-transitgatewayvpcattachment-options-dnssupport"></a>
Enable or disable DNS support. The default is `disable`.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6Support`  <a name="cfn-ec2-transitgatewayvpcattachment-options-ipv6support"></a>
Enable or disable IPv6 support. The default is `disable`.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupReferencingSupport`  <a name="cfn-ec2-transitgatewayvpcattachment-options-securitygroupreferencingsupport"></a>
Enables you to reference a security group across VPCs attached to a transit gateway (TGW). Use this option to simplify security group management and control of instance-to-instance traffic across VPCs that are connected by transit gateway. You can also use this option to migrate from VPC peering (which was the only option that supported security group referencing) to transit gateways (which now also support security group referencing). This option is disabled by default and there are no additional costs to use this feature.
For important information about this feature, see [Create a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#create-tgw) in the *AWS Transit Gateway Guide*.
*Required*: No
*Type*: String
*Allowed values*: `enable | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
