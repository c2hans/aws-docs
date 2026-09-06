---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 DownlinkAwsGroundStationAgentEndpointDetails
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails"></a>

Details for a downlink agent endpoint

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-syntax.json"></a>

```
{
  "[AgentStatus](#cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-agentstatus)" : {{String}},
  "[AuditResults](#cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-auditresults)" : {{String}},
  "[DataflowDetails](#cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-dataflowdetails)" : {{DownlinkDataflowDetails}},
  "[Name](#cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-syntax.yaml"></a>

```
  [AgentStatus](#cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-agentstatus): {{String}}
  [AuditResults](#cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-auditresults): {{String}}
  [DataflowDetails](#cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-dataflowdetails): {{
    DownlinkDataflowDetails}}
  [Name](#cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-name): {{String}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-properties"></a>

`AgentStatus`  <a name="cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-agentstatus"></a>
Status of the agent associated with the downlink dataflow endpoint
*Required*: No
*Type*: String
*Allowed values*: `SUCCESS | FAILED | ACTIVE | INACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuditResults`  <a name="cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-auditresults"></a>
Health audit results for the downlink dataflow endpoint
*Required*: No
*Type*: String
*Allowed values*: `HEALTHY | UNHEALTHY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataflowDetails`  <a name="cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-dataflowdetails"></a>
Dataflow details for the downlink endpoint
*Required*: Yes
*Type*: [DownlinkDataflowDetails](aws-properties-groundstation-dataflowendpointgroupv2-downlinkdataflowdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-groundstation-dataflowendpointgroupv2-downlinkawsgroundstationagentendpointdetails-name"></a>
Downlink dataflow endpoint name
*Required*: Yes
*Type*: String
*Pattern*: `^[ a-zA-Z0-9_:-]{1,256}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
