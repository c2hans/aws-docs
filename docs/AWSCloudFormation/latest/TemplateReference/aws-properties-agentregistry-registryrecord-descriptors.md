---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-descriptors.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord Descriptors
<a name="aws-properties-agentregistry-registryrecord-descriptors"></a>

The typed set of descriptors for a registry record. Exactly one descriptor field is populated based on the record type.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-descriptors-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-descriptors-syntax.json"></a>

```
{
  "[A2aAgentCard](#cfn-agentregistry-registryrecord-descriptors-a2aagentcard)" : {{A2aAgentCardDescriptor}},
  "[AgentSkillsDefinition](#cfn-agentregistry-registryrecord-descriptors-agentskillsdefinition)" : {{AgentSkillsDefinitionDescriptor}},
  "[Agui](#cfn-agentregistry-registryrecord-descriptors-agui)" : {{AgUiDescriptor}},
  "[Custom](#cfn-agentregistry-registryrecord-descriptors-custom)" : {{CustomDescriptor}},
  "[Http](#cfn-agentregistry-registryrecord-descriptors-http)" : {{HttpDescriptor}},
  "[McpServer](#cfn-agentregistry-registryrecord-descriptors-mcpserver)" : {{McpServerDescriptor}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-descriptors-syntax.yaml"></a>

```
  [A2aAgentCard](#cfn-agentregistry-registryrecord-descriptors-a2aagentcard): {{
    A2aAgentCardDescriptor}}
  [AgentSkillsDefinition](#cfn-agentregistry-registryrecord-descriptors-agentskillsdefinition): {{
    AgentSkillsDefinitionDescriptor}}
  [Agui](#cfn-agentregistry-registryrecord-descriptors-agui): {{
    AgUiDescriptor}}
  [Custom](#cfn-agentregistry-registryrecord-descriptors-custom): {{
    CustomDescriptor}}
  [Http](#cfn-agentregistry-registryrecord-descriptors-http): {{
    HttpDescriptor}}
  [McpServer](#cfn-agentregistry-registryrecord-descriptors-mcpserver): {{
    McpServerDescriptor}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-descriptors-properties"></a>

`A2aAgentCard`  <a name="cfn-agentregistry-registryrecord-descriptors-a2aagentcard"></a>
The Agent-to-Agent (A2A) agent card descriptor, populated when the record type is `AGENT`.
*Required*: No
*Type*: [A2aAgentCardDescriptor](aws-properties-agentregistry-registryrecord-a2aagentcarddescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentSkillsDefinition`  <a name="cfn-agentregistry-registryrecord-descriptors-agentskillsdefinition"></a>
The agent skills definition descriptor, populated when the record type is `SKILL`.
*Required*: No
*Type*: [AgentSkillsDefinitionDescriptor](aws-properties-agentregistry-registryrecord-agentskillsdefinitiondescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Agui`  <a name="cfn-agentregistry-registryrecord-descriptors-agui"></a>
The AG-UI descriptor, populated for records detected from an AG-UI protocol source.
*Required*: No
*Type*: [AgUiDescriptor](aws-properties-agentregistry-registryrecord-aguidescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Custom`  <a name="cfn-agentregistry-registryrecord-descriptors-custom"></a>
The custom descriptor, populated when the record type is `CUSTOM`.
*Required*: No
*Type*: [CustomDescriptor](aws-properties-agentregistry-registryrecord-customdescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Http`  <a name="cfn-agentregistry-registryrecord-descriptors-http"></a>
The HTTP descriptor, populated for records detected from an HTTP protocol source.
*Required*: No
*Type*: [HttpDescriptor](aws-properties-agentregistry-registryrecord-httpdescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`McpServer`  <a name="cfn-agentregistry-registryrecord-descriptors-mcpserver"></a>
The Model Context Protocol (MCP) server descriptor, populated when the record type is `MCP`.
*Required*: No
*Type*: [McpServerDescriptor](aws-properties-agentregistry-registryrecord-mcpserverdescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
