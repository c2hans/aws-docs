---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-endpointdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 EndpointDetails
<a name="aws-properties-groundstation-dataflowendpointgroupv2-endpointdetails"></a>

Information about the endpoint details.

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-endpointdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-endpointdetails-syntax.json"></a>

```
{
  "[DownlinkAwsGroundStationAgentEndpoint](#cfn-groundstation-dataflowendpointgroupv2-endpointdetails-downlinkawsgroundstationagentendpoint)" : {{DownlinkAwsGroundStationAgentEndpointDetails}},
  "[UplinkAwsGroundStationAgentEndpoint](#cfn-groundstation-dataflowendpointgroupv2-endpointdetails-uplinkawsgroundstationagentendpoint)" : {{UplinkAwsGroundStationAgentEndpointDetails}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-endpointdetails-syntax.yaml"></a>

```
  [DownlinkAwsGroundStationAgentEndpoint](#cfn-groundstation-dataflowendpointgroupv2-endpointdetails-downlinkawsgroundstationagentendpoint): {{
    DownlinkAwsGroundStationAgentEndpointDetails}}
  [UplinkAwsGroundStationAgentEndpoint](#cfn-groundstation-dataflowendpointgroupv2-endpointdetails-uplinkawsgroundstationagentendpoint): {{
    UplinkAwsGroundStationAgentEndpointDetails}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-endpointdetails-properties"></a>

`DownlinkAwsGroundStationAgentEndpoint`  <a name="cfn-groundstation-dataflowendpointgroupv2-endpointdetails-downlinkawsgroundstationagentendpoint"></a>
Definition for a downlink agent endpoint
*Required*: No
*Type*: [DownlinkAwsGroundStationAgentEndpointDetails](aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UplinkAwsGroundStationAgentEndpoint`  <a name="cfn-groundstation-dataflowendpointgroupv2-endpointdetails-uplinkawsgroundstationagentendpoint"></a>
Definition for an uplink agent endpoint
*Required*: No
*Type*: [UplinkAwsGroundStationAgentEndpointDetails](aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
