---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-worker-ipaddresses.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Worker IpAddresses
<a name="aws-properties-deadline-worker-ipaddresses"></a>

The IP addresses for a host.

## Syntax
<a name="aws-properties-deadline-worker-ipaddresses-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-worker-ipaddresses-syntax.json"></a>

```
{
  "[IpV4Addresses](#cfn-deadline-worker-ipaddresses-ipv4addresses)" : {{[ String, ... ]}},
  "[IpV6Addresses](#cfn-deadline-worker-ipaddresses-ipv6addresses)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-deadline-worker-ipaddresses-syntax.yaml"></a>

```
  [IpV4Addresses](#cfn-deadline-worker-ipaddresses-ipv4addresses): {{
    - String}}
  [IpV6Addresses](#cfn-deadline-worker-ipaddresses-ipv6addresses): {{
    - String}}
```

## Properties
<a name="aws-properties-deadline-worker-ipaddresses-properties"></a>

`IpV4Addresses`  <a name="cfn-deadline-worker-ipaddresses-ipv4addresses"></a>
The IpV4 address of the network.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpV6Addresses`  <a name="cfn-deadline-worker-ipaddresses-ipv6addresses"></a>
The IpV6 address for the network and node component.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
