---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroup AwsGroundStationAgentEndpoint
<a name="aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint"></a>

Information about AwsGroundStationAgentEndpoint.

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-syntax.json"></a>

```
{
  "[AgentStatus](#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-agentstatus)" : {{String}},
  "[AuditResults](#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-auditresults)" : {{String}},
  "[EgressAddress](#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-egressaddress)" : {{ConnectionDetails}},
  "[IngressAddress](#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-ingressaddress)" : {{RangedConnectionDetails}},
  "[Name](#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-syntax.yaml"></a>

```
  [AgentStatus](#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-agentstatus): {{String}}
  [AuditResults](#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-auditresults): {{String}}
  [EgressAddress](#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-egressaddress): {{
    ConnectionDetails}}
  [IngressAddress](#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-ingressaddress): {{
    RangedConnectionDetails}}
  [Name](#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-name): {{String}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-properties"></a>

`AgentStatus`  <a name="cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-agentstatus"></a>
The status of AgentEndpoint.
*Required*: No
*Type*: String
*Allowed values*: `SUCCESS | FAILED | ACTIVE | INACTIVE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AuditResults`  <a name="cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-auditresults"></a>
The results of the audit.
*Required*: No
*Type*: String
*Allowed values*: `HEALTHY | UNHEALTHY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EgressAddress`  <a name="cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-egressaddress"></a>
The egress address of AgentEndpoint.
*Required*: No
*Type*: [ConnectionDetails](aws-properties-groundstation-dataflowendpointgroup-connectiondetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IngressAddress`  <a name="cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-ingressaddress"></a>
The ingress address of AgentEndpoint.
*Required*: No
*Type*: [RangedConnectionDetails](aws-properties-groundstation-dataflowendpointgroup-rangedconnectiondetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-name"></a>
Name string associated with AgentEndpoint. Used as a human-readable identifier for AgentEndpoint.
*Required*: No
*Type*: String
*Pattern*: `^[ a-zA-Z0-9_:-]{1,256}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
