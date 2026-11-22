---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53globalresolver-corenetworkendpoint-ipaddress.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53GlobalResolver::CoreNetworkEndpoint IpAddress

A DNS IP address configuration that you provide when you create a core network endpoint. Each item specifies an IP address for the endpoint to receive DNS queries, along with its DNS label, and the scope and AWS Regions in which the address applies.

## Syntax
<a name="aws-properties-route53globalresolver-corenetworkendpoint-ipaddress-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53globalresolver-corenetworkendpoint-ipaddress-syntax.json"></a>

```json
{
  "[DnsLabel](#cfn-route53globalresolver-corenetworkendpoint-ipaddress-dnslabel)" : {{String}},
  "[Ipv4Address](#cfn-route53globalresolver-corenetworkendpoint-ipaddress-ipv4address)" : {{String}},
  "[Ipv6Address](#cfn-route53globalresolver-corenetworkendpoint-ipaddress-ipv6address)" : {{String}},
  "[Regions](#cfn-route53globalresolver-corenetworkendpoint-ipaddress-regions)" : {{[ String, ... ]}},
  "[RegionScope](#cfn-route53globalresolver-corenetworkendpoint-ipaddress-regionscope)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53globalresolver-corenetworkendpoint-ipaddress-syntax.yaml"></a>

```yaml
  [DnsLabel](#cfn-route53globalresolver-corenetworkendpoint-ipaddress-dnslabel): {{String}}
  [Ipv4Address](#cfn-route53globalresolver-corenetworkendpoint-ipaddress-ipv4address): {{String}}
  [Ipv6Address](#cfn-route53globalresolver-corenetworkendpoint-ipaddress-ipv6address): {{String}}
  [Regions](#cfn-route53globalresolver-corenetworkendpoint-ipaddress-regions): {{
    - String}}
  [RegionScope](#cfn-route53globalresolver-corenetworkendpoint-ipaddress-regionscope): {{String}}
```

## Properties
<a name="aws-properties-route53globalresolver-corenetworkendpoint-ipaddress-properties"></a>

`DnsLabel`  <a name="cfn-route53globalresolver-corenetworkendpoint-ipaddress-dnslabel"></a>
The DNS label to associate with the IP address.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!-)[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv4Address`  <a name="cfn-route53globalresolver-corenetworkendpoint-ipaddress-ipv4address"></a>
The IPv4 address for the core network endpoint to receive DNS queries.
*Required*: No
*Type*: String
*Pattern*: `^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$`
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6Address`  <a name="cfn-route53globalresolver-corenetworkendpoint-ipaddress-ipv6address"></a>
The IPv6 address for the core network endpoint to receive DNS queries.
*Required*: No
*Type*: String
*Pattern*: `^(?:[A-Fa-f0-9]{0,4}:){2,7}[A-Fa-f0-9]{1,4}$`
*Minimum*: `1`
*Maximum*: `39`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regions`  <a name="cfn-route53globalresolver-corenetworkendpoint-ipaddress-regions"></a>
The AWS Regions in which the IP address applies when the region scope is `REGIONAL`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionScope`  <a name="cfn-route53globalresolver-corenetworkendpoint-ipaddress-regionscope"></a>
Indicates whether the IP address applies to all AWS Regions or only to the specific Regions that you identify. When the value is `REGIONAL`, the Regions are listed in the `regions` field.
*Required*: Yes
*Type*: String
*Allowed values*: `ALL | REGIONAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
