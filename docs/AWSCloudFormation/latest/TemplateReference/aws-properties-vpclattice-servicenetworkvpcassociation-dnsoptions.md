---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-servicenetworkvpcassociation-dnsoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::ServiceNetworkVpcAssociation DnsOptions
<a name="aws-properties-vpclattice-servicenetworkvpcassociation-dnsoptions"></a>

The DNS configuration options.

## Syntax
<a name="aws-properties-vpclattice-servicenetworkvpcassociation-dnsoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-servicenetworkvpcassociation-dnsoptions-syntax.json"></a>

```
{
  "[PrivateDnsPreference](#cfn-vpclattice-servicenetworkvpcassociation-dnsoptions-privatednspreference)" : {{String}},
  "[PrivateDnsSpecifiedDomains](#cfn-vpclattice-servicenetworkvpcassociation-dnsoptions-privatednsspecifieddomains)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-vpclattice-servicenetworkvpcassociation-dnsoptions-syntax.yaml"></a>

```
  [PrivateDnsPreference](#cfn-vpclattice-servicenetworkvpcassociation-dnsoptions-privatednspreference): {{String}}
  [PrivateDnsSpecifiedDomains](#cfn-vpclattice-servicenetworkvpcassociation-dnsoptions-privatednsspecifieddomains): {{
    - String}}
```

## Properties
<a name="aws-properties-vpclattice-servicenetworkvpcassociation-dnsoptions-properties"></a>

`PrivateDnsPreference`  <a name="cfn-vpclattice-servicenetworkvpcassociation-dnsoptions-privatednspreference"></a>
The preference for which private domains have a private hosted zone created for and associated with the specified VPC. Only supported when private DNS is enabled and when the VPC endpoint type is ServiceNetwork or Resource.
*Required*: No
*Type*: String
*Allowed values*: `VERIFIED_DOMAINS_ONLY | ALL_DOMAINS | VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS | SPECIFIED_DOMAINS_ONLY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateDnsSpecifiedDomains`  <a name="cfn-vpclattice-servicenetworkvpcassociation-dnsoptions-privatednsspecifieddomains"></a>
Indicates which of the private domains to create private hosted zones for and associate with the specified VPC. Only supported when private DNS is enabled and the private DNS preference is `VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS` or `SPECIFIED_DOMAINS_ONLY`.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
