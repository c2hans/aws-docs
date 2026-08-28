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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
