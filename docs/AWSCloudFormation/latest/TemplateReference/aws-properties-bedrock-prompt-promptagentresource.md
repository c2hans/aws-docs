---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-prompt-promptagentresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt PromptAgentResource
<a name="aws-properties-bedrock-prompt-promptagentresource"></a>

Contains specifications for an Amazon Bedrock agent with which to use the prompt. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) and [Automate tasks in your application using conversational agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html).

## Syntax
<a name="aws-properties-bedrock-prompt-promptagentresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-prompt-promptagentresource-syntax.json"></a>

```
{
  "[AgentIdentifier](#cfn-bedrock-prompt-promptagentresource-agentidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-prompt-promptagentresource-syntax.yaml"></a>

```
  [AgentIdentifier](#cfn-bedrock-prompt-promptagentresource-agentidentifier): {{String}}
```

## Properties
<a name="aws-properties-bedrock-prompt-promptagentresource-properties"></a>

`AgentIdentifier`  <a name="cfn-bedrock-prompt-promptagentresource-agentidentifier"></a>
The ARN of the agent with which to use the prompt.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent-alias/[0-9a-zA-Z]{10}/[0-9a-zA-Z]{10}$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
