---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnesstool.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessTool
<a name="aws-properties-bedrockagentcore-harness-harnesstool"></a>

A tool available to the agent loop.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnesstool-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnesstool-syntax.json"></a>

```
{
  "[Config](#cfn-bedrockagentcore-harness-harnesstool-config)" : {{HarnessToolConfiguration}},
  "[Name](#cfn-bedrockagentcore-harness-harnesstool-name)" : {{String}},
  "[Type](#cfn-bedrockagentcore-harness-harnesstool-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnesstool-syntax.yaml"></a>

```
  [Config](#cfn-bedrockagentcore-harness-harnesstool-config): {{
    HarnessToolConfiguration}}
  [Name](#cfn-bedrockagentcore-harness-harnesstool-name): {{String}}
  [Type](#cfn-bedrockagentcore-harness-harnesstool-type): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnesstool-properties"></a>

`Config`  <a name="cfn-bedrockagentcore-harness-harnesstool-config"></a>
Tool-specific configuration.
*Required*: No
*Type*: [HarnessToolConfiguration](aws-properties-bedrockagentcore-harness-harnesstoolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-harness-harnesstool-name"></a>
Unique name for the tool. If not provided, a name will be inferred or generated.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrockagentcore-harness-harnesstool-type"></a>
The type of tool.
*Required*: Yes
*Type*: String
*Allowed values*: `remote_mcp | agentcore_browser | agentcore_gateway | inline_function | agentcore_code_interpreter`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
