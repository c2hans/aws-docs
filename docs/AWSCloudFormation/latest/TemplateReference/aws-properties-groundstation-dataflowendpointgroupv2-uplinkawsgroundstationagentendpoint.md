---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 UplinkAwsGroundStationAgentEndpoint
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpoint"></a>

Definition for an uplink agent endpoint

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpoint-syntax.json"></a>

```
{
  "[DataflowDetails](#cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpoint-dataflowdetails)" : {{UplinkDataflowDetails}},
  "[Name](#cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpoint-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpoint-syntax.yaml"></a>

```
  [DataflowDetails](#cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpoint-dataflowdetails): {{
    UplinkDataflowDetails}}
  [Name](#cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpoint-name): {{String}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpoint-properties"></a>

`DataflowDetails`  <a name="cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpoint-dataflowdetails"></a>
Dataflow details for the uplink endpoint
*Required*: Yes
*Type*: [UplinkDataflowDetails](aws-properties-groundstation-dataflowendpointgroupv2-uplinkdataflowdetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpoint-name"></a>
Uplink dataflow endpoint name
*Required*: Yes
*Type*: String
*Pattern*: `^[ a-zA-Z0-9_:-]{1,256}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
