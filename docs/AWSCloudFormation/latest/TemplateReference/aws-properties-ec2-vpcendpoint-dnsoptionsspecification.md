---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-vpcendpoint-dnsoptionsspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPCEndpoint DnsOptionsSpecification
<a name="aws-properties-ec2-vpcendpoint-dnsoptionsspecification"></a>

Describes the DNS options for an endpoint.

## Syntax
<a name="aws-properties-ec2-vpcendpoint-dnsoptionsspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-vpcendpoint-dnsoptionsspecification-syntax.json"></a>

```
{
  "[DnsRecordIpType](#cfn-ec2-vpcendpoint-dnsoptionsspecification-dnsrecordiptype)" : {{String}},
  "[PrivateDnsOnlyForInboundResolverEndpoint](#cfn-ec2-vpcendpoint-dnsoptionsspecification-privatednsonlyforinboundresolverendpoint)" : {{String}},
  "[PrivateDnsPreference](#cfn-ec2-vpcendpoint-dnsoptionsspecification-privatednspreference)" : {{String}},
  "[PrivateDnsSpecifiedDomains](#cfn-ec2-vpcendpoint-dnsoptionsspecification-privatednsspecifieddomains)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-vpcendpoint-dnsoptionsspecification-syntax.yaml"></a>

```
  [DnsRecordIpType](#cfn-ec2-vpcendpoint-dnsoptionsspecification-dnsrecordiptype): {{String}}
  [PrivateDnsOnlyForInboundResolverEndpoint](#cfn-ec2-vpcendpoint-dnsoptionsspecification-privatednsonlyforinboundresolverendpoint): {{String}}
  [PrivateDnsPreference](#cfn-ec2-vpcendpoint-dnsoptionsspecification-privatednspreference): {{String}}
  [PrivateDnsSpecifiedDomains](#cfn-ec2-vpcendpoint-dnsoptionsspecification-privatednsspecifieddomains): {{
    - String}}
```

## Properties
<a name="aws-properties-ec2-vpcendpoint-dnsoptionsspecification-properties"></a>

`DnsRecordIpType`  <a name="cfn-ec2-vpcendpoint-dnsoptionsspecification-dnsrecordiptype"></a>
The DNS records created for the endpoint.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | ipv6 | dualstack | service-defined | not-specified`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateDnsOnlyForInboundResolverEndpoint`  <a name="cfn-ec2-vpcendpoint-dnsoptionsspecification-privatednsonlyforinboundresolverendpoint"></a>
Indicates whether to enable private DNS only for inbound endpoints. This option is available only for services that support both gateway and interface endpoints. It routes traffic that originates from the VPC to the gateway endpoint and traffic that originates from on-premises to the interface endpoint.
*Required*: No
*Type*: String
*Allowed values*: `OnlyInboundResolver | AllResolvers | NotSpecified`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateDnsPreference`  <a name="cfn-ec2-vpcendpoint-dnsoptionsspecification-privatednspreference"></a>
The preference for which private domains have a private hosted zone created for and associated with the specified VPC. Only supported when private DNS is enabled and when the VPC endpoint type is ServiceNetwork or Resource.
*Required*: No
*Type*: String
*Allowed values*: `VERIFIED_DOMAINS_ONLY | ALL_DOMAINS | VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS | SPECIFIED_DOMAINS_ONLY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivateDnsSpecifiedDomains`  <a name="cfn-ec2-vpcendpoint-dnsoptionsspecification-privatednsspecifieddomains"></a>
Indicates which of the private domains to create private hosted zones for and associate with the specified VPC. Only supported when private DNS is enabled and the private DNS preference is `VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS` or `SPECIFIED_DOMAINS_ONLY`.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
