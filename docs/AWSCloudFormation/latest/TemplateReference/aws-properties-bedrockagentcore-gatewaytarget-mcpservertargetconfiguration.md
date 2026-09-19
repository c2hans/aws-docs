---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget McpServerTargetConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration"></a>

The configuration for an MCP server target.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-syntax.json"></a>

```
{
  "[Endpoint](#cfn-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-endpoint)" : {{String}},
  "[ListingMode](#cfn-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-listingmode)" : {{String}},
  "[McpToolSchema](#cfn-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-mcptoolschema)" : {{McpToolSchemaConfiguration}},
  "[ResourcePriority](#cfn-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-resourcepriority)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-syntax.yaml"></a>

```
  [Endpoint](#cfn-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-endpoint): {{String}}
  [ListingMode](#cfn-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-listingmode): {{String}}
  [McpToolSchema](#cfn-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-mcptoolschema): {{
    McpToolSchemaConfiguration}}
  [ResourcePriority](#cfn-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-resourcepriority): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-properties"></a>

`Endpoint`  <a name="cfn-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-endpoint"></a>
The endpoint URL for the MCP server.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ListingMode`  <a name="cfn-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-listingmode"></a>
The listing mode for the MCP server target configuration. MCP resources for default targets are cached at the control plane for faster access. MCP resources for dynamic targets will be dynamically retrieved when listing tools.
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT | DYNAMIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`McpToolSchema`  <a name="cfn-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-mcptoolschema"></a>
A static tool list for the MCP server target. It is supported for all credential providers. Dynamic tool discovery/synchronization will be disabled when a target is configured with mcpToolSchema.
*Required*: No
*Type*: [McpToolSchemaConfiguration](aws-properties-bedrockagentcore-gatewaytarget-mcptoolschemaconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourcePriority`  <a name="cfn-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-resourcepriority"></a>
Priority for resolving MCP server targets with shared resource URIs. Lower values take precedence. Defaults to 1000 when not set.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
