---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 DownlinkAwsGroundStationAgentEndpoint
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpoint"></a>

Definition for a downlink agent endpoint

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpoint-syntax.json"></a>

```
{
  "[DataflowDetails](#cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpoint-dataflowdetails)" : {{DownlinkDataflowDetails}},
  "[Name](#cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpoint-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpoint-syntax.yaml"></a>

```
  [DataflowDetails](#cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpoint-dataflowdetails): {{
    DownlinkDataflowDetails}}
  [Name](#cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpoint-name): {{String}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpoint-properties"></a>

`DataflowDetails`  <a name="cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpoint-dataflowdetails"></a>
Dataflow details for the downlink endpoint
*Required*: Yes
*Type*: [DownlinkDataflowDetails](aws-properties-groundstation-dataflowendpointgroupv2-downlinkdataflowdetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpoint-name"></a>
Downlink dataflow endpoint name
*Required*: Yes
*Type*: String
*Pattern*: `^[ a-zA-Z0-9_:-]{1,256}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
