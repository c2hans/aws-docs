---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-mcptoolschemaconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget McpToolSchemaConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcptoolschemaconfiguration"></a>

The MCP tool schema configuration for an MCP server target. The tool schema must be aligned with the MCP specification.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcptoolschemaconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcptoolschemaconfiguration-syntax.json"></a>

```
{
  "[InlinePayload](#cfn-bedrockagentcore-gatewaytarget-mcptoolschemaconfiguration-inlinepayload)" : {{String}},
  "[S3](#cfn-bedrockagentcore-gatewaytarget-mcptoolschemaconfiguration-s3)" : {{S3Configuration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcptoolschemaconfiguration-syntax.yaml"></a>

```
  [InlinePayload](#cfn-bedrockagentcore-gatewaytarget-mcptoolschemaconfiguration-inlinepayload): {{String}}
  [S3](#cfn-bedrockagentcore-gatewaytarget-mcptoolschemaconfiguration-s3): {{
    S3Configuration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcptoolschemaconfiguration-properties"></a>

`InlinePayload`  <a name="cfn-bedrockagentcore-gatewaytarget-mcptoolschemaconfiguration-inlinepayload"></a>
The inline payload containing the MCP tool schema definition.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3`  <a name="cfn-bedrockagentcore-gatewaytarget-mcptoolschemaconfiguration-s3"></a>
The Amazon S3 location of the tool schema. This location contains the schema definition file.
*Required*: No
*Type*: [S3Configuration](aws-properties-bedrockagentcore-gatewaytarget-s3configuration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
