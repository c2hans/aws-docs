---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-downlinkconnectiondetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 DownlinkConnectionDetails
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkconnectiondetails"></a>

Connection details for Ground Station to Agent and Agent to customer

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkconnectiondetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkconnectiondetails-syntax.json"></a>

```
{
  "[AgentIpAndPortAddress](#cfn-groundstation-dataflowendpointgroupv2-downlinkconnectiondetails-agentipandportaddress)" : {{RangedConnectionDetails}},
  "[EgressAddressAndPort](#cfn-groundstation-dataflowendpointgroupv2-downlinkconnectiondetails-egressaddressandport)" : {{ConnectionDetails}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkconnectiondetails-syntax.yaml"></a>

```
  [AgentIpAndPortAddress](#cfn-groundstation-dataflowendpointgroupv2-downlinkconnectiondetails-agentipandportaddress): {{
    RangedConnectionDetails}}
  [EgressAddressAndPort](#cfn-groundstation-dataflowendpointgroupv2-downlinkconnectiondetails-egressaddressandport): {{
    ConnectionDetails}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkconnectiondetails-properties"></a>

`AgentIpAndPortAddress`  <a name="cfn-groundstation-dataflowendpointgroupv2-downlinkconnectiondetails-agentipandportaddress"></a>
Agent IP and port address for the downlink connection.
*Required*: Yes
*Type*: [RangedConnectionDetails](aws-properties-groundstation-dataflowendpointgroupv2-rangedconnectiondetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EgressAddressAndPort`  <a name="cfn-groundstation-dataflowendpointgroupv2-downlinkconnectiondetails-egressaddressandport"></a>
Egress address and port for the downlink connection.
*Required*: Yes
*Type*: [ConnectionDetails](aws-properties-groundstation-dataflowendpointgroupv2-connectiondetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
