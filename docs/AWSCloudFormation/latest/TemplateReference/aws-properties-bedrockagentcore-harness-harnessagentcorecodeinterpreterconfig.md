---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessagentcorecodeinterpreterconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessAgentCoreCodeInterpreterConfig
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorecodeinterpreterconfig"></a>

Configuration for AgentCore Code Interpreter.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorecodeinterpreterconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorecodeinterpreterconfig-syntax.json"></a>

```
{
  "[CodeInterpreterArn](#cfn-bedrockagentcore-harness-harnessagentcorecodeinterpreterconfig-codeinterpreterarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorecodeinterpreterconfig-syntax.yaml"></a>

```
  [CodeInterpreterArn](#cfn-bedrockagentcore-harness-harnessagentcorecodeinterpreterconfig-codeinterpreterarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessagentcorecodeinterpreterconfig-properties"></a>

`CodeInterpreterArn`  <a name="cfn-bedrockagentcore-harness-harnessagentcorecodeinterpreterconfig-codeinterpreterarn"></a>
If not populated, the built-in Code Interpreter ARN is used.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):code-interpreter(-custom)?/(aws\.codeinterpreter\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
