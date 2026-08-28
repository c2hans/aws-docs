---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-agentknowledgebase.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent AgentKnowledgeBase
<a name="aws-properties-bedrock-agent-agentknowledgebase"></a>

Contains details about a knowledge base that is associated with an agent.

## Syntax
<a name="aws-properties-bedrock-agent-agentknowledgebase-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-agentknowledgebase-syntax.json"></a>

```
{
  "[Description](#cfn-bedrock-agent-agentknowledgebase-description)" : {{String}},
  "[KnowledgeBaseId](#cfn-bedrock-agent-agentknowledgebase-knowledgebaseid)" : {{String}},
  "[KnowledgeBaseState](#cfn-bedrock-agent-agentknowledgebase-knowledgebasestate)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-agentknowledgebase-syntax.yaml"></a>

```
  [Description](#cfn-bedrock-agent-agentknowledgebase-description): {{String}}
  [KnowledgeBaseId](#cfn-bedrock-agent-agentknowledgebase-knowledgebaseid): {{String}}
  [KnowledgeBaseState](#cfn-bedrock-agent-agentknowledgebase-knowledgebasestate): {{String}}
```

## Properties
<a name="aws-properties-bedrock-agent-agentknowledgebase-properties"></a>

`Description`  <a name="cfn-bedrock-agent-agentknowledgebase-description"></a>
The description of the association between the agent and the knowledge base.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnowledgeBaseId`  <a name="cfn-bedrock-agent-agentknowledgebase-knowledgebaseid"></a>
The unique identifier of the association between the agent and the knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z]{10}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnowledgeBaseState`  <a name="cfn-bedrock-agent-agentknowledgebase-knowledgebasestate"></a>
Specifies whether to use the knowledge base or not when sending an [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) request.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
