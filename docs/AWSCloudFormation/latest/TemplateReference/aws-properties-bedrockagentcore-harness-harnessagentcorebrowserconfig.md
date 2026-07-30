---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessagentcorebrowserconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessAgentCoreBrowserConfig
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorebrowserconfig"></a>

Configuration for AgentCore Browser.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorebrowserconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorebrowserconfig-syntax.json"></a>

```
{
  "[BrowserArn](#cfn-bedrockagentcore-harness-harnessagentcorebrowserconfig-browserarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorebrowserconfig-syntax.yaml"></a>

```
  [BrowserArn](#cfn-bedrockagentcore-harness-harnessagentcorebrowserconfig-browserarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorebrowserconfig-properties"></a>

`BrowserArn`  <a name="cfn-bedrockagentcore-harness-harnessagentcorebrowserconfig-browserarn"></a>
If not populated, the built-in Browser ARN is used.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):browser(-custom)?/(aws\.browser\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
