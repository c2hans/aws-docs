---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-mcpserversigv4configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association MCPServerSigV4Configuration
<a name="aws-properties-devopsagent-association-mcpserversigv4configuration"></a>

Configuration for SigV4-authenticated MCP server integration. Specifies the available tools to enable the Agent Space to interact with an MCP server that authenticates requests using AWS Signature Version 4.

## Syntax
<a name="aws-properties-devopsagent-association-mcpserversigv4configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-mcpserversigv4configuration-syntax.json"></a>

```
{
  "[Tools](#cfn-devopsagent-association-mcpserversigv4configuration-tools)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-mcpserversigv4configuration-syntax.yaml"></a>

```
  [Tools](#cfn-devopsagent-association-mcpserversigv4configuration-tools): {{
    - String}}
```

## Properties
<a name="aws-properties-devopsagent-association-mcpserversigv4configuration-properties"></a>

`Tools`  <a name="cfn-devopsagent-association-mcpserversigv4configuration-tools"></a>
The list of MCP tools available for the association.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
