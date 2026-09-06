---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-uplinkdataflowdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 UplinkDataflowDetails
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkdataflowdetails"></a>

Dataflow details for an uplink endpoint

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkdataflowdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkdataflowdetails-syntax.json"></a>

```
{
  "[AgentConnectionDetails](#cfn-groundstation-dataflowendpointgroupv2-uplinkdataflowdetails-agentconnectiondetails)" : {{UplinkConnectionDetails}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkdataflowdetails-syntax.yaml"></a>

```
  [AgentConnectionDetails](#cfn-groundstation-dataflowendpointgroupv2-uplinkdataflowdetails-agentconnectiondetails): {{
    UplinkConnectionDetails}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkdataflowdetails-properties"></a>

`AgentConnectionDetails`  <a name="cfn-groundstation-dataflowendpointgroupv2-uplinkdataflowdetails-agentconnectiondetails"></a>
Uplink connection details for customer to Agent and Agent to Ground Station
*Required*: No
*Type*: [UplinkConnectionDetails](aws-properties-groundstation-dataflowendpointgroupv2-uplinkconnectiondetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
