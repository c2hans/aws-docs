---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-mcpserveradditionaldata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord McpServerAdditionalData
<a name="aws-properties-agentregistry-registryrecord-mcpserveradditionaldata"></a>

Additional data associated with a Model Context Protocol (MCP) server descriptor.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-mcpserveradditionaldata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-mcpserveradditionaldata-syntax.json"></a>

```
{
  "[Tools](#cfn-agentregistry-registryrecord-mcpserveradditionaldata-tools)" : {{McpToolsDescriptor}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-mcpserveradditionaldata-syntax.yaml"></a>

```
  [Tools](#cfn-agentregistry-registryrecord-mcpserveradditionaldata-tools): {{
    McpToolsDescriptor}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-mcpserveradditionaldata-properties"></a>

`Tools`  <a name="cfn-agentregistry-registryrecord-mcpserveradditionaldata-tools"></a>
The MCP tools descriptor that defines the tools provided by the MCP server.
*Required*: No
*Type*: [McpToolsDescriptor](aws-properties-agentregistry-registryrecord-mcptoolsdescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
