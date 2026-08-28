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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
