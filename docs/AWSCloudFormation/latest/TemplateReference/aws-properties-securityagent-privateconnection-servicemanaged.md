---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-privateconnection-servicemanaged.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::PrivateConnection ServiceManaged
<a name="aws-properties-securityagent-privateconnection-servicemanaged"></a>

<a name="aws-properties-securityagent-privateconnection-servicemanaged-description"></a>The `ServiceManaged` property type specifies Property description not available. for an [AWS::SecurityAgent::PrivateConnection](aws-resource-securityagent-privateconnection.md).

## Syntax
<a name="aws-properties-securityagent-privateconnection-servicemanaged-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-privateconnection-servicemanaged-syntax.json"></a>

```
{
  "[DnsResolution](#cfn-securityagent-privateconnection-servicemanaged-dnsresolution)" : {{String}},
  "[HostAddress](#cfn-securityagent-privateconnection-servicemanaged-hostaddress)" : {{String}},
  "[IpAddressType](#cfn-securityagent-privateconnection-servicemanaged-ipaddresstype)" : {{String}},
  "[Ipv4AddressesPerEni](#cfn-securityagent-privateconnection-servicemanaged-ipv4addressespereni)" : {{Integer}},
  "[PortRanges](#cfn-securityagent-privateconnection-servicemanaged-portranges)" : {{[ String, ... ]}},
  "[SecurityGroupIds](#cfn-securityagent-privateconnection-servicemanaged-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-securityagent-privateconnection-servicemanaged-subnetids)" : {{[ String, ... ]}},
  "[VpcId](#cfn-securityagent-privateconnection-servicemanaged-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityagent-privateconnection-servicemanaged-syntax.yaml"></a>

```
  [DnsResolution](#cfn-securityagent-privateconnection-servicemanaged-dnsresolution): {{String}}
  [HostAddress](#cfn-securityagent-privateconnection-servicemanaged-hostaddress): {{String}}
  [IpAddressType](#cfn-securityagent-privateconnection-servicemanaged-ipaddresstype): {{String}}
  [Ipv4AddressesPerEni](#cfn-securityagent-privateconnection-servicemanaged-ipv4addressespereni): {{Integer}}
  [PortRanges](#cfn-securityagent-privateconnection-servicemanaged-portranges): {{
    - String}}
  [SecurityGroupIds](#cfn-securityagent-privateconnection-servicemanaged-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-securityagent-privateconnection-servicemanaged-subnetids): {{
    - String}}
  [VpcId](#cfn-securityagent-privateconnection-servicemanaged-vpcid): {{String}}
```

## Properties
<a name="aws-properties-securityagent-privateconnection-servicemanaged-properties"></a>

`DnsResolution`  <a name="cfn-securityagent-privateconnection-servicemanaged-dnsresolution"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `PUBLIC | IN_VPC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HostAddress`  <a name="cfn-securityagent-privateconnection-servicemanaged-hostaddress"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpAddressType`  <a name="cfn-securityagent-privateconnection-servicemanaged-ipaddresstype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | IPV6 | DUAL_STACK`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv4AddressesPerEni`  <a name="cfn-securityagent-privateconnection-servicemanaged-ipv4addressespereni"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PortRanges`  <a name="cfn-securityagent-privateconnection-servicemanaged-portranges"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-securityagent-privateconnection-servicemanaged-securitygroupids"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-securityagent-privateconnection-servicemanaged-subnetids"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-securityagent-privateconnection-servicemanaged-vpcid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
