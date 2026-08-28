---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 UplinkAwsGroundStationAgentEndpointDetails
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails"></a>

Details for an uplink agent endpoint

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-syntax.json"></a>

```
{
  "[AgentStatus](#cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-agentstatus)" : {{String}},
  "[AuditResults](#cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-auditresults)" : {{String}},
  "[DataflowDetails](#cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-dataflowdetails)" : {{UplinkDataflowDetails}},
  "[Name](#cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-syntax.yaml"></a>

```
  [AgentStatus](#cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-agentstatus): {{String}}
  [AuditResults](#cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-auditresults): {{String}}
  [DataflowDetails](#cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-dataflowdetails): {{
    UplinkDataflowDetails}}
  [Name](#cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-name): {{String}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-properties"></a>

`AgentStatus`  <a name="cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-agentstatus"></a>
Status of the agent associated with the uplink dataflow endpoint
*Required*: No
*Type*: String
*Allowed values*: `SUCCESS | FAILED | ACTIVE | INACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuditResults`  <a name="cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-auditresults"></a>
Health audit results for the uplink dataflow endpoint
*Required*: No
*Type*: String
*Allowed values*: `HEALTHY | UNHEALTHY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataflowDetails`  <a name="cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-dataflowdetails"></a>
Dataflow details for the uplink endpoint
*Required*: Yes
*Type*: [UplinkDataflowDetails](aws-properties-groundstation-dataflowendpointgroupv2-uplinkdataflowdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-groundstation-dataflowendpointgroupv2-uplinkawsgroundstationagentendpointdetails-name"></a>
Uplink dataflow endpoint name
*Required*: Yes
*Type*: String
*Pattern*: `^[ a-zA-Z0-9_:-]{1,256}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
