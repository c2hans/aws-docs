---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnesstoolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessToolConfiguration
<a name="aws-properties-bedrockagentcore-harness-harnesstoolconfiguration"></a>

Configuration union for different tool types.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnesstoolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnesstoolconfiguration-syntax.json"></a>

```
{
  "[AgentCoreBrowser](#cfn-bedrockagentcore-harness-harnesstoolconfiguration-agentcorebrowser)" : {{HarnessAgentCoreBrowserConfig}},
  "[AgentCoreCodeInterpreter](#cfn-bedrockagentcore-harness-harnesstoolconfiguration-agentcorecodeinterpreter)" : {{HarnessAgentCoreCodeInterpreterConfig}},
  "[AgentCoreGateway](#cfn-bedrockagentcore-harness-harnesstoolconfiguration-agentcoregateway)" : {{HarnessAgentCoreGatewayConfig}},
  "[InlineFunction](#cfn-bedrockagentcore-harness-harnesstoolconfiguration-inlinefunction)" : {{HarnessInlineFunctionConfig}},
  "[RemoteMcp](#cfn-bedrockagentcore-harness-harnesstoolconfiguration-remotemcp)" : {{HarnessRemoteMcpConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnesstoolconfiguration-syntax.yaml"></a>

```
  [AgentCoreBrowser](#cfn-bedrockagentcore-harness-harnesstoolconfiguration-agentcorebrowser): {{
    HarnessAgentCoreBrowserConfig}}
  [AgentCoreCodeInterpreter](#cfn-bedrockagentcore-harness-harnesstoolconfiguration-agentcorecodeinterpreter): {{
    HarnessAgentCoreCodeInterpreterConfig}}
  [AgentCoreGateway](#cfn-bedrockagentcore-harness-harnesstoolconfiguration-agentcoregateway): {{
    HarnessAgentCoreGatewayConfig}}
  [InlineFunction](#cfn-bedrockagentcore-harness-harnesstoolconfiguration-inlinefunction): {{
    HarnessInlineFunctionConfig}}
  [RemoteMcp](#cfn-bedrockagentcore-harness-harnesstoolconfiguration-remotemcp): {{
    HarnessRemoteMcpConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnesstoolconfiguration-properties"></a>

`AgentCoreBrowser`  <a name="cfn-bedrockagentcore-harness-harnesstoolconfiguration-agentcorebrowser"></a>
Configuration for AgentCore Browser.
*Required*: No
*Type*: [HarnessAgentCoreBrowserConfig](aws-properties-bedrockagentcore-harness-harnessagentcorebrowserconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentCoreCodeInterpreter`  <a name="cfn-bedrockagentcore-harness-harnesstoolconfiguration-agentcorecodeinterpreter"></a>
Configuration for AgentCore Code Interpreter.
*Required*: No
*Type*: [HarnessAgentCoreCodeInterpreterConfig](aws-properties-bedrockagentcore-harness-harnessagentcorecodeinterpreterconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentCoreGateway`  <a name="cfn-bedrockagentcore-harness-harnesstoolconfiguration-agentcoregateway"></a>
Configuration for AgentCore Gateway.
*Required*: No
*Type*: [HarnessAgentCoreGatewayConfig](aws-properties-bedrockagentcore-harness-harnessagentcoregatewayconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InlineFunction`  <a name="cfn-bedrockagentcore-harness-harnesstoolconfiguration-inlinefunction"></a>
Configuration for an inline function tool.
*Required*: No
*Type*: [HarnessInlineFunctionConfig](aws-properties-bedrockagentcore-harness-harnessinlinefunctionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RemoteMcp`  <a name="cfn-bedrockagentcore-harness-harnesstoolconfiguration-remotemcp"></a>
Configuration for remote MCP server.
*Required*: No
*Type*: [HarnessRemoteMcpConfig](aws-properties-bedrockagentcore-harness-harnessremotemcpconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
