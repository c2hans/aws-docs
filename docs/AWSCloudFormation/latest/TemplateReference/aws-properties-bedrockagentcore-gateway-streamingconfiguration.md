---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-streamingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway StreamingConfiguration
<a name="aws-properties-bedrockagentcore-gateway-streamingconfiguration"></a>

The streaming configuration for an MCP gateway. This structure defines settings that control response streaming behavior.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-streamingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-streamingconfiguration-syntax.json"></a>

```
{
  "[EnableResponseStreaming](#cfn-bedrockagentcore-gateway-streamingconfiguration-enableresponsestreaming)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-streamingconfiguration-syntax.yaml"></a>

```
  [EnableResponseStreaming](#cfn-bedrockagentcore-gateway-streamingconfiguration-enableresponsestreaming): {{Boolean}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-streamingconfiguration-properties"></a>

`EnableResponseStreaming`  <a name="cfn-bedrockagentcore-gateway-streamingconfiguration-enableresponsestreaming"></a>
Indicates whether response streaming is enabled for the gateway. When set to `true`, the gateway streams responses from targets back to the client.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
