---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-downlinkdataflowdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 DownlinkDataflowDetails
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkdataflowdetails"></a>

Dataflow details for a downlink endpoint

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkdataflowdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkdataflowdetails-syntax.json"></a>

```
{
  "[AgentConnectionDetails](#cfn-groundstation-dataflowendpointgroupv2-downlinkdataflowdetails-agentconnectiondetails)" : {{DownlinkConnectionDetails}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkdataflowdetails-syntax.yaml"></a>

```
  [AgentConnectionDetails](#cfn-groundstation-dataflowendpointgroupv2-downlinkdataflowdetails-agentconnectiondetails): {{
    DownlinkConnectionDetails}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-downlinkdataflowdetails-properties"></a>

`AgentConnectionDetails`  <a name="cfn-groundstation-dataflowendpointgroupv2-downlinkdataflowdetails-agentconnectiondetails"></a>
Downlink connection details for customer to Agent and Agent to Ground Station
*Required*: No
*Type*: [DownlinkConnectionDetails](aws-properties-groundstation-dataflowendpointgroupv2-downlinkconnectiondetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
