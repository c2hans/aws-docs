---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-mcpserverdescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord McpServerDescriptor
<a name="aws-properties-agentregistry-registryrecord-mcpserverdescriptor"></a>

Descriptor that defines the content of a Model Context Protocol (MCP) server registry record, including the server definition and its tool definitions.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-mcpserverdescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-mcpserverdescriptor-syntax.json"></a>

```
{
  "[AdditionalData](#cfn-agentregistry-registryrecord-mcpserverdescriptor-additionaldata)" : {{McpServerAdditionalData}},
  "[Data](#cfn-agentregistry-registryrecord-mcpserverdescriptor-data)" : {{String}},
  "[DataSchemaVersion](#cfn-agentregistry-registryrecord-mcpserverdescriptor-dataschemaversion)" : {{String}},
  "[Source](#cfn-agentregistry-registryrecord-mcpserverdescriptor-source)" : {{DescriptorSource}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-mcpserverdescriptor-syntax.yaml"></a>

```
  [AdditionalData](#cfn-agentregistry-registryrecord-mcpserverdescriptor-additionaldata): {{
    McpServerAdditionalData}}
  [Data](#cfn-agentregistry-registryrecord-mcpserverdescriptor-data): {{String}}
  [DataSchemaVersion](#cfn-agentregistry-registryrecord-mcpserverdescriptor-dataschemaversion): {{String}}
  [Source](#cfn-agentregistry-registryrecord-mcpserverdescriptor-source): {{
    DescriptorSource}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-mcpserverdescriptor-properties"></a>

`AdditionalData`  <a name="cfn-agentregistry-registryrecord-mcpserverdescriptor-additionaldata"></a>
Additional data associated with the MCP server descriptor, such as tool definitions.
*Required*: No
*Type*: [McpServerAdditionalData](aws-properties-agentregistry-registryrecord-mcpserveradditionaldata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Data`  <a name="cfn-agentregistry-registryrecord-mcpserverdescriptor-data"></a>
The MCP server descriptor content, serialized as descriptor payload data.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `102400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSchemaVersion`  <a name="cfn-agentregistry-registryrecord-mcpserverdescriptor-dataschemaversion"></a>
The schema version of the descriptor payload.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-agentregistry-registryrecord-mcpserverdescriptor-source"></a>
The optional source configuration used to synchronize the MCP server descriptor content.
*Required*: No
*Type*: [DescriptorSource](aws-properties-agentregistry-registryrecord-descriptorsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
