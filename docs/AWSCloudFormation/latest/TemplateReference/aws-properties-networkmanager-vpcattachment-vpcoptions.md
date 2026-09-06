---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-vpcattachment-vpcoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::VpcAttachment VpcOptions
<a name="aws-properties-networkmanager-vpcattachment-vpcoptions"></a>

Describes the VPC options.

## Syntax
<a name="aws-properties-networkmanager-vpcattachment-vpcoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-vpcattachment-vpcoptions-syntax.json"></a>

```
{
  "[ApplianceModeSupport](#cfn-networkmanager-vpcattachment-vpcoptions-appliancemodesupport)" : {{Boolean}},
  "[DnsSupport](#cfn-networkmanager-vpcattachment-vpcoptions-dnssupport)" : {{Boolean}},
  "[Ipv6Support](#cfn-networkmanager-vpcattachment-vpcoptions-ipv6support)" : {{Boolean}},
  "[SecurityGroupReferencingSupport](#cfn-networkmanager-vpcattachment-vpcoptions-securitygroupreferencingsupport)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-networkmanager-vpcattachment-vpcoptions-syntax.yaml"></a>

```
  [ApplianceModeSupport](#cfn-networkmanager-vpcattachment-vpcoptions-appliancemodesupport): {{Boolean}}
  [DnsSupport](#cfn-networkmanager-vpcattachment-vpcoptions-dnssupport): {{Boolean}}
  [Ipv6Support](#cfn-networkmanager-vpcattachment-vpcoptions-ipv6support): {{Boolean}}
  [SecurityGroupReferencingSupport](#cfn-networkmanager-vpcattachment-vpcoptions-securitygroupreferencingsupport): {{Boolean}}
```

## Properties
<a name="aws-properties-networkmanager-vpcattachment-vpcoptions-properties"></a>

`ApplianceModeSupport`  <a name="cfn-networkmanager-vpcattachment-vpcoptions-appliancemodesupport"></a>
Indicates whether appliance mode is supported. If enabled, traffic flow between a source and destination use the same Availability Zone for the VPC attachment for the lifetime of that flow. The default value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DnsSupport`  <a name="cfn-networkmanager-vpcattachment-vpcoptions-dnssupport"></a>
Indicates whether DNS is supported.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6Support`  <a name="cfn-networkmanager-vpcattachment-vpcoptions-ipv6support"></a>
Indicates whether IPv6 is supported.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupReferencingSupport`  <a name="cfn-networkmanager-vpcattachment-vpcoptions-securitygroupreferencingsupport"></a>
Indicates whether security group referencing is enabled for this VPC attachment. The default is `true`. However, at the core network policy-level the default is set to `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
