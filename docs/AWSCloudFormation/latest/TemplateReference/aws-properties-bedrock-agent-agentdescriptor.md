---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-agentdescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent AgentDescriptor
<a name="aws-properties-bedrock-agent-agentdescriptor"></a>

An agent descriptor.

## Syntax
<a name="aws-properties-bedrock-agent-agentdescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-agentdescriptor-syntax.json"></a>

```
{
  "[AliasArn](#cfn-bedrock-agent-agentdescriptor-aliasarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-agentdescriptor-syntax.yaml"></a>

```
  [AliasArn](#cfn-bedrock-agent-agentdescriptor-aliasarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-agent-agentdescriptor-properties"></a>

`AliasArn`  <a name="cfn-bedrock-agent-agentdescriptor-aliasarn"></a>
The agent's alias ARN.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent-alias/[0-9a-zA-Z]{10}/[0-9a-zA-Z]{10}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
