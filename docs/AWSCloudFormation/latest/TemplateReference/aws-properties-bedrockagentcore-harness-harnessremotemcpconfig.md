---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessremotemcpconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessRemoteMcpConfig
<a name="aws-properties-bedrockagentcore-harness-harnessremotemcpconfig"></a>

Configuration for connecting to a remote MCP server.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessremotemcpconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessremotemcpconfig-syntax.json"></a>

```
{
  "[Headers](#cfn-bedrockagentcore-harness-harnessremotemcpconfig-headers)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Url](#cfn-bedrockagentcore-harness-harnessremotemcpconfig-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessremotemcpconfig-syntax.yaml"></a>

```
  [Headers](#cfn-bedrockagentcore-harness-harnessremotemcpconfig-headers): {{
    {{Key}}: {{Value}}}}
  [Url](#cfn-bedrockagentcore-harness-harnessremotemcpconfig-url): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessremotemcpconfig-properties"></a>

`Headers`  <a name="cfn-bedrockagentcore-harness-harnessremotemcpconfig-headers"></a>
Custom headers to include when connecting to the remote MCP server.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\s\S]*$`
*Minimum*: `1`
*Maximum*: `16383`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-bedrockagentcore-harness-harnessremotemcpconfig-url"></a>
URL of the MCP endpoint.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `16383`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
