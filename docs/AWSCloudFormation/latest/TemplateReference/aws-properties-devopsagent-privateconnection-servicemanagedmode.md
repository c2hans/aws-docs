---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-privateconnection-servicemanagedmode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::PrivateConnection ServiceManagedMode
<a name="aws-properties-devopsagent-privateconnection-servicemanagedmode"></a>

Configuration for a private connection in which AWS DevOps Agent creates and manages the resource gateway in your VPC.

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
The DNS resolution mode used to resolve the host address. Defaults to `PUBLIC` if you don't specify a value.
*Required*: No
*Type*: String
*Allowed values*: `PUBLIC | IN_VPC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HostAddress`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-hostaddress"></a>
The IP address or DNS name of the target service.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9.:\-]+$`
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpAddressType`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-ipaddresstype"></a>
The IP address type of the service-managed resource gateway.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | IPV6 | DUAL_STACK`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv4AddressesPerEni`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-ipv4addressespereni"></a>
The number of IPv4 addresses in each elastic network interface of the service-managed resource gateway.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `62`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PortRanges`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-portranges"></a>
The TCP port ranges that a consumer can use to access the target service.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `11`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-securitygroupids"></a>
The security groups to attach to the service-managed resource gateway.
*Required*: No
*Type*: Array of String
*Minimum*: `11 | 1`
*Maximum*: `20 | 5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-subnetids"></a>
The subnets that the service-managed resource gateway spans.
*Required*: No
*Type*: Array of String
*Minimum*: `15 | 1`
*Maximum*: `24 | 20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-devopsagent-privateconnection-servicemanagedmode-vpcid"></a>
The ID of the VPC in which to create the service-managed resource gateway.
*Required*: Yes
*Type*: String
*Pattern*: `^vpc-(([0-9a-z]{8})|([0-9a-z]{17}))$`
*Minimum*: `5`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
