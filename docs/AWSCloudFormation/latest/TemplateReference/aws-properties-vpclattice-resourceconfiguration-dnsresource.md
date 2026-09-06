---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-resourceconfiguration-dnsresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::ResourceConfiguration DnsResource
<a name="aws-properties-vpclattice-resourceconfiguration-dnsresource"></a>

The domain name of the resource configuration.

## Syntax
<a name="aws-properties-vpclattice-resourceconfiguration-dnsresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-resourceconfiguration-dnsresource-syntax.json"></a>

```
{
  "[DomainName](#cfn-vpclattice-resourceconfiguration-dnsresource-domainname)" : {{String}},
  "[IpAddressType](#cfn-vpclattice-resourceconfiguration-dnsresource-ipaddresstype)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-resourceconfiguration-dnsresource-syntax.yaml"></a>

```
  [DomainName](#cfn-vpclattice-resourceconfiguration-dnsresource-domainname): {{String}}
  [IpAddressType](#cfn-vpclattice-resourceconfiguration-dnsresource-ipaddresstype): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-resourceconfiguration-dnsresource-properties"></a>

`DomainName`  <a name="cfn-vpclattice-resourceconfiguration-dnsresource-domainname"></a>
The domain name of the resource configuration.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-vpclattice-resourceconfiguration-dnsresource-ipaddresstype"></a>
The IP address type for the resource configuration. Dualstack is not currently supported.
*Required*: Yes
*Type*: String
*Allowed values*: `IPV4 | IPV6 | DUALSTACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
