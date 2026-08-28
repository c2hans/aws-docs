---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinterface-publicipdnsnameoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInterface PublicIpDnsNameOptions
<a name="aws-properties-ec2-networkinterface-publicipdnsnameoptions"></a>

Public hostname type options. For more information, see [EC2 instance hostnames, DNS names, and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon EC2 User Guide*.

## Syntax
<a name="aws-properties-ec2-networkinterface-publicipdnsnameoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinterface-publicipdnsnameoptions-syntax.json"></a>

```
{
  "[DnsHostnameType](#cfn-ec2-networkinterface-publicipdnsnameoptions-dnshostnametype)" : {{String}},
  "[PublicDualStackDnsName](#cfn-ec2-networkinterface-publicipdnsnameoptions-publicdualstackdnsname)" : {{String}},
  "[PublicIpv4DnsName](#cfn-ec2-networkinterface-publicipdnsnameoptions-publicipv4dnsname)" : {{String}},
  "[PublicIpv6DnsName](#cfn-ec2-networkinterface-publicipdnsnameoptions-publicipv6dnsname)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-networkinterface-publicipdnsnameoptions-syntax.yaml"></a>

```
  [DnsHostnameType](#cfn-ec2-networkinterface-publicipdnsnameoptions-dnshostnametype): {{String}}
  [PublicDualStackDnsName](#cfn-ec2-networkinterface-publicipdnsnameoptions-publicdualstackdnsname): {{String}}
  [PublicIpv4DnsName](#cfn-ec2-networkinterface-publicipdnsnameoptions-publicipv4dnsname): {{String}}
  [PublicIpv6DnsName](#cfn-ec2-networkinterface-publicipdnsnameoptions-publicipv6dnsname): {{String}}
```

## Properties
<a name="aws-properties-ec2-networkinterface-publicipdnsnameoptions-properties"></a>

`DnsHostnameType`  <a name="cfn-ec2-networkinterface-publicipdnsnameoptions-dnshostnametype"></a>
The public hostname type. For more information, see [EC2 instance hostnames, DNS names, and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublicDualStackDnsName`  <a name="cfn-ec2-networkinterface-publicipdnsnameoptions-publicdualstackdnsname"></a>
A dual-stack public hostname for a network interface. Requests from within the VPC resolve to both the private IPv4 address and the IPv6 Global Unicast Address of the network interface. Requests from the internet resolve to both the public IPv4 and the IPv6 GUA address of the network interface.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublicIpv4DnsName`  <a name="cfn-ec2-networkinterface-publicipdnsnameoptions-publicipv4dnsname"></a>
An IPv4-enabled public hostname for a network interface. Requests from within the VPC resolve to the private primary IPv4 address of the network interface. Requests from the internet resolve to the public IPv4 address of the network interface.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublicIpv6DnsName`  <a name="cfn-ec2-networkinterface-publicipdnsnameoptions-publicipv6dnsname"></a>
An IPv6-enabled public hostname for a network interface. Requests from within the VPC or from the internet resolve to the IPv6 GUA of the network interface.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
