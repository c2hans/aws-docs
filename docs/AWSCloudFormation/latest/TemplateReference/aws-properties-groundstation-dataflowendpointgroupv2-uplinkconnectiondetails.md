---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroupv2-uplinkconnectiondetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroupV2 UplinkConnectionDetails
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkconnectiondetails"></a>

Connection details for customer to Agent and Agent to Ground Station

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkconnectiondetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkconnectiondetails-syntax.json"></a>

```
{
  "[AgentIpAndPortAddress](#cfn-groundstation-dataflowendpointgroupv2-uplinkconnectiondetails-agentipandportaddress)" : {{RangedConnectionDetails}},
  "[IngressAddressAndPort](#cfn-groundstation-dataflowendpointgroupv2-uplinkconnectiondetails-ingressaddressandport)" : {{ConnectionDetails}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkconnectiondetails-syntax.yaml"></a>

```
  [AgentIpAndPortAddress](#cfn-groundstation-dataflowendpointgroupv2-uplinkconnectiondetails-agentipandportaddress): {{
    RangedConnectionDetails}}
  [IngressAddressAndPort](#cfn-groundstation-dataflowendpointgroupv2-uplinkconnectiondetails-ingressaddressandport): {{
    ConnectionDetails}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroupv2-uplinkconnectiondetails-properties"></a>

`AgentIpAndPortAddress`  <a name="cfn-groundstation-dataflowendpointgroupv2-uplinkconnectiondetails-agentipandportaddress"></a>
Agent IP and port address for the uplink connection.
*Required*: Yes
*Type*: [RangedConnectionDetails](aws-properties-groundstation-dataflowendpointgroupv2-rangedconnectiondetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IngressAddressAndPort`  <a name="cfn-groundstation-dataflowendpointgroupv2-uplinkconnectiondetails-ingressaddressandport"></a>
Ingress address and port for the uplink connection.
*Required*: Yes
*Type*: [ConnectionDetails](aws-properties-groundstation-dataflowendpointgroupv2-connectiondetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
