---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-createendpointdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 CreateEndpointDetails
<a name="aws-properties-groundstation-dataflowendpointgroupv2-createendpointdetails"></a>

Endpoint definition used for creating a dataflow endpoint

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-createendpointdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-createendpointdetails-syntax.json"></a>

```
{
  "[DownlinkAwsGroundStationAgentEndpoint](#cfn-groundstation-dataflowendpointgroupv2-createendpointdetails-downlinkawsgroundstationagentendpoint)" : {{DownlinkAwsGroundStationAgentEndpoint}},
  "[UplinkAwsGroundStationAgentEndpoint](#cfn-groundstation-dataflowendpointgroupv2-createendpointdetails-uplinkawsgroundstationagentendpoint)" : {{UplinkAwsGroundStationAgentEndpoint}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-createendpointdetails-syntax.yaml"></a>

```
  [DownlinkAwsGroundStationAgentEndpoint](#cfn-groundstation-dataflowendpointgroupv2-createendpointdetails-downlinkawsgroundstationagentendpoint): {{
    DownlinkAwsGroundStationAgentEndpoint}}
  [UplinkAwsGroundStationAgentEndpoint](#cfn-groundstation-dataflowendpointgroupv2-createendpointdetails-uplinkawsgroundstationagentendpoint): {{
    UplinkAwsGroundStationAgentEndpoint}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-createendpointdetails-properties"></a>

`DownlinkAwsGroundStationAgentEndpoint`  <a name="cfn-groundstation-dataflowendpointgroupv2-createendpointdetails-downlinkawsgroundstationagentendpoint"></a>
Definition for a downlink agent endpoint
*Required*: No
*Type*: [DownlinkAwsGroundStationAgentEndpoint](aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpoint.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UplinkAwsGroundStationAgentEndpoint`  <a name="cfn-groundstation-dataflowendpointgroupv2-createendpointdetails-uplinkawsgroundstationagentendpoint"></a>
Definition for an uplink agent endpoint
*Required*: No
*Type*: [UplinkAwsGroundStationAgentEndpoint](aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpoint.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
