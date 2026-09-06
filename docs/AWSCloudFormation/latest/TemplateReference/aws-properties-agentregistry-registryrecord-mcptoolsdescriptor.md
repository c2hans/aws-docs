---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-mcptoolsdescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord McpToolsDescriptor
<a name="aws-properties-agentregistry-registryrecord-mcptoolsdescriptor"></a>

The Model Context Protocol (MCP) tools descriptor.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-mcptoolsdescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-mcptoolsdescriptor-syntax.json"></a>

```
{
  "[Data](#cfn-agentregistry-registryrecord-mcptoolsdescriptor-data)" : {{String}},
  "[DataSchemaVersion](#cfn-agentregistry-registryrecord-mcptoolsdescriptor-dataschemaversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-mcptoolsdescriptor-syntax.yaml"></a>

```
  [Data](#cfn-agentregistry-registryrecord-mcptoolsdescriptor-data): {{String}}
  [DataSchemaVersion](#cfn-agentregistry-registryrecord-mcptoolsdescriptor-dataschemaversion): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-mcptoolsdescriptor-properties"></a>

`Data`  <a name="cfn-agentregistry-registryrecord-mcptoolsdescriptor-data"></a>
The MCP tools descriptor content, serialized as descriptor payload data.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `102400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSchemaVersion`  <a name="cfn-agentregistry-registryrecord-mcptoolsdescriptor-dataschemaversion"></a>
The schema version of the tools descriptor payload.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
