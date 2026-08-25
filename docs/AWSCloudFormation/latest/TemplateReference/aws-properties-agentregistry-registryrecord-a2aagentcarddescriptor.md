---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-a2aagentcarddescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord A2aAgentCardDescriptor
<a name="aws-properties-agentregistry-registryrecord-a2aagentcarddescriptor"></a>

Descriptor that defines the content of an Agent-to-Agent (A2A) agent card registry record.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-a2aagentcarddescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-a2aagentcarddescriptor-syntax.json"></a>

```
{
  "[Data](#cfn-agentregistry-registryrecord-a2aagentcarddescriptor-data)" : {{String}},
  "[DataSchemaVersion](#cfn-agentregistry-registryrecord-a2aagentcarddescriptor-dataschemaversion)" : {{String}},
  "[Source](#cfn-agentregistry-registryrecord-a2aagentcarddescriptor-source)" : {{DescriptorSource}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-a2aagentcarddescriptor-syntax.yaml"></a>

```
  [Data](#cfn-agentregistry-registryrecord-a2aagentcarddescriptor-data): {{String}}
  [DataSchemaVersion](#cfn-agentregistry-registryrecord-a2aagentcarddescriptor-dataschemaversion): {{String}}
  [Source](#cfn-agentregistry-registryrecord-a2aagentcarddescriptor-source): {{
    DescriptorSource}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-a2aagentcarddescriptor-properties"></a>

`Data`  <a name="cfn-agentregistry-registryrecord-a2aagentcarddescriptor-data"></a>
The A2A agent card content, serialized as descriptor payload data.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `102400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSchemaVersion`  <a name="cfn-agentregistry-registryrecord-a2aagentcarddescriptor-dataschemaversion"></a>
The schema version of the descriptor payload.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-agentregistry-registryrecord-a2aagentcarddescriptor-source"></a>
The optional source configuration used to synchronize the A2A agent card descriptor content.
*Required*: No
*Type*: [DescriptorSource](aws-properties-agentregistry-registryrecord-descriptorsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
