---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-connectiondetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 ConnectionDetails
<a name="aws-properties-groundstation-dataflowendpointgroupv2-connectiondetails"></a>

Egress address of AgentEndpoint with an optional mtu.

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-connectiondetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-connectiondetails-syntax.json"></a>

```
{
  "[Mtu](#cfn-groundstation-dataflowendpointgroupv2-connectiondetails-mtu)" : {{Integer}},
  "[SocketAddress](#cfn-groundstation-dataflowendpointgroupv2-connectiondetails-socketaddress)" : {{SocketAddress}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-connectiondetails-syntax.yaml"></a>

```
  [Mtu](#cfn-groundstation-dataflowendpointgroupv2-connectiondetails-mtu): {{Integer}}
  [SocketAddress](#cfn-groundstation-dataflowendpointgroupv2-connectiondetails-socketaddress): {{
    SocketAddress}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-connectiondetails-properties"></a>

`Mtu`  <a name="cfn-groundstation-dataflowendpointgroupv2-connectiondetails-mtu"></a>
Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.
*Required*: No
*Type*: Integer
*Minimum*: `1400`
*Maximum*: `1500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SocketAddress`  <a name="cfn-groundstation-dataflowendpointgroupv2-connectiondetails-socketaddress"></a>
A socket address.
*Required*: Yes
*Type*: [SocketAddress](aws-properties-groundstation-dataflowendpointgroupv2-socketaddress.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
