---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroup-rangedsocketaddress.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroup RangedSocketAddress
<a name="aws-properties-groundstation-dataflowendpointgroup-rangedsocketaddress"></a>

A socket address with a port range.

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroup-rangedsocketaddress-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroup-rangedsocketaddress-syntax.json"></a>

```
{
  "[Name](#cfn-groundstation-dataflowendpointgroup-rangedsocketaddress-name)" : {{String}},
  "[PortRange](#cfn-groundstation-dataflowendpointgroup-rangedsocketaddress-portrange)" : {{IntegerRange}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroup-rangedsocketaddress-syntax.yaml"></a>

```
  [Name](#cfn-groundstation-dataflowendpointgroup-rangedsocketaddress-name): {{String}}
  [PortRange](#cfn-groundstation-dataflowendpointgroup-rangedsocketaddress-portrange): {{
    IntegerRange}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroup-rangedsocketaddress-properties"></a>

`Name`  <a name="cfn-groundstation-dataflowendpointgroup-rangedsocketaddress-name"></a>
IPv4 socket address.
*Required*: No
*Type*: String
*Pattern*: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`
*Minimum*: `7`
*Maximum*: `16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PortRange`  <a name="cfn-groundstation-dataflowendpointgroup-rangedsocketaddress-portrange"></a>
Port range of a socket address.
*Required*: No
*Type*: [IntegerRange](aws-properties-groundstation-dataflowendpointgroup-integerrange.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
