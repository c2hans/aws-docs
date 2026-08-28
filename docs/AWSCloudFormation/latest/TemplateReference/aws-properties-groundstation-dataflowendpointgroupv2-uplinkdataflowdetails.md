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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
