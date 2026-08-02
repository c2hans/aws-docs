---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-privateconnection-servicemanagedmode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::PrivateConnection ServiceManagedMode
<a name="aws-properties-devopsagent-privateconnection-servicemanagedmode"></a>

<a name="aws-properties-devopsagent-privateconnection-servicemanagedmode-description"></a>The `ServiceManagedMode` property type specifies Property description not available. for an [AWS::DevOpsAgent::PrivateConnection](aws-resource-devopsagent-privateconnection.md).

## Syntax
<a name="aws-properties-devopsagent-privateconnection-servicemanagedmode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-privateconnection-servicemanagedmode-syntax.json"></a>

```
{
  "[DnsResolution](#cfn-devopsagent-privateconnection-servicemanagedmode-dnsresolution)" : {{String}},
  "[HostAddress](#cfn-devopsagent-privateconnection-servicemanagedmode-hostaddress)" : {{String}},
  "[IpAddressType](#cfn-devopsagent-privateconnection-servicemanagedmode-ipaddresstype)" : {{String}},
  "[Ipv4AddressesPerEni](#cfn-devopsagent-privateconnection-servicemanagedmode-ipv4addressespereni)" : {{Integer}},
  "[PortRanges](#cfn-devopsagent-privateconnection-servicemanagedmode-portranges)" : {{[ String, ... ]}},
  "[SecurityGroupIds](#cfn-devopsagent-privateconnection-servicemanagedmode-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-devopsagent-privateconnection-servicemanagedmode-subnetids)" : {{[ String, ... ]}},
  "[VpcId](#cfn-devopsagent-privateconnection-servicemanagedmode-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-privateconnection-servicemanagedmode-syntax.yaml"></a>

```
  [DnsResolution](#cfn-devopsagent-privateconnection-servicemanagedmode-dnsresolution): {{String}}
  [HostAddress](#cfn-devopsagent-privateconnection-servicemanagedmode-hostaddress): {{String}}
  [IpAddressType](#cfn-devopsagent-privateconnection-servicemanagedmode-ipaddresstype): {{String}}
  [Ipv4AddressesPerEni](#cfn-devopsagent-privateconnection-servicemanagedmode-ipv4addressespereni): {{Integer}}
  [PortRanges](#cfn-devopsagent-privateconnection-servicemanagedmode-portranges): {{
    - String}}
  [SecurityGroupIds](#cfn-devopsagent-privateconnection-servicemanagedmode-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-devopsagent-privateconnection-servicemanagedmode-subnetids): {{
    - String}}
  [VpcId](#cfn-devopsagent-privateconnection-servicemanagedmode-vpcid): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-privateconnection-servicemanagedmode-properties"></a>

`DnsResolution`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-dnsresolution"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `PUBLIC | IN_VPC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HostAddress`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-hostaddress"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9.:\-]+$`
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpAddressType`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-ipaddresstype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | IPV6 | DUAL_STACK`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv4AddressesPerEni`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-ipv4addressespereni"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `62`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PortRanges`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-portranges"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `11`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-securitygroupids"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `11 | 1`
*Maximum*: `20 | 5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-subnetids"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `15 | 1`
*Maximum*: `24 | 20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-vpcid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^vpc-(([0-9a-z]{8})|([0-9a-z]{17}))$`
*Minimum*: `5`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
