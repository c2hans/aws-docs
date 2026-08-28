---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-rangedconnectiondetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 RangedConnectionDetails
<a name="aws-properties-groundstation-dataflowendpointgroupv2-rangedconnectiondetails"></a>

Ingress address of AgentEndpoint with a port range and an optional mtu.

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-rangedconnectiondetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-rangedconnectiondetails-syntax.json"></a>

```
{
  "[Mtu](#cfn-groundstation-dataflowendpointgroupv2-rangedconnectiondetails-mtu)" : {{Integer}},
  "[SocketAddress](#cfn-groundstation-dataflowendpointgroupv2-rangedconnectiondetails-socketaddress)" : {{RangedSocketAddress}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-rangedconnectiondetails-syntax.yaml"></a>

```
  [Mtu](#cfn-groundstation-dataflowendpointgroupv2-rangedconnectiondetails-mtu): {{Integer}}
  [SocketAddress](#cfn-groundstation-dataflowendpointgroupv2-rangedconnectiondetails-socketaddress): {{
    RangedSocketAddress}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-rangedconnectiondetails-properties"></a>

`Mtu`  <a name="cfn-groundstation-dataflowendpointgroupv2-rangedconnectiondetails-mtu"></a>
Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.
*Required*: No
*Type*: Integer
*Minimum*: `1400`
*Maximum*: `1500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SocketAddress`  <a name="cfn-groundstation-dataflowendpointgroupv2-rangedconnectiondetails-socketaddress"></a>
A ranged socket address.
*Required*: Yes
*Type*: [RangedSocketAddress](aws-properties-groundstation-dataflowendpointgroupv2-rangedsocketaddress.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
