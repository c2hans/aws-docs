---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-agentcollaborator.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent AgentCollaborator
<a name="aws-properties-bedrock-agent-agentcollaborator"></a>

An agent collaborator.

## Syntax
<a name="aws-properties-bedrock-agent-agentcollaborator-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-agentcollaborator-syntax.json"></a>

```
{
  "[AgentDescriptor](#cfn-bedrock-agent-agentcollaborator-agentdescriptor)" : {{AgentDescriptor}},
  "[CollaborationInstruction](#cfn-bedrock-agent-agentcollaborator-collaborationinstruction)" : {{String}},
  "[CollaboratorName](#cfn-bedrock-agent-agentcollaborator-collaboratorname)" : {{String}},
  "[RelayConversationHistory](#cfn-bedrock-agent-agentcollaborator-relayconversationhistory)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-agentcollaborator-syntax.yaml"></a>

```
  [AgentDescriptor](#cfn-bedrock-agent-agentcollaborator-agentdescriptor): {{
    AgentDescriptor}}
  [CollaborationInstruction](#cfn-bedrock-agent-agentcollaborator-collaborationinstruction): {{String}}
  [CollaboratorName](#cfn-bedrock-agent-agentcollaborator-collaboratorname): {{String}}
  [RelayConversationHistory](#cfn-bedrock-agent-agentcollaborator-relayconversationhistory): {{String}}
```

## Properties
<a name="aws-properties-bedrock-agent-agentcollaborator-properties"></a>

`AgentDescriptor`  <a name="cfn-bedrock-agent-agentcollaborator-agentdescriptor"></a>
The collaborator's agent descriptor.
*Required*: Yes
*Type*: [AgentDescriptor](aws-properties-bedrock-agent-agentdescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CollaborationInstruction`  <a name="cfn-bedrock-agent-agentcollaborator-collaborationinstruction"></a>
The collaborator's instructions.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CollaboratorName`  <a name="cfn-bedrock-agent-agentcollaborator-collaboratorname"></a>
The collaborator's collaborator name.
*Required*: Yes
*Type*: String
*Pattern*: `([0-9a-zA-Z][_-]?){1,100}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelayConversationHistory`  <a name="cfn-bedrock-agent-agentcollaborator-relayconversationhistory"></a>
The collaborator's relay conversation history.
*Required*: No
*Type*: String
*Allowed values*: `TO_COLLABORATOR | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
