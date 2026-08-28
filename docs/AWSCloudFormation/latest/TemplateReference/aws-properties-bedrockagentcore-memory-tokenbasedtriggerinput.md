---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory TokenBasedTriggerInput
<a name="aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput"></a>

The token based trigger input.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput-syntax.json"></a>

```
{
  "[TokenCount](#cfn-bedrockagentcore-memory-tokenbasedtriggerinput-tokencount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput-syntax.yaml"></a>

```
  [TokenCount](#cfn-bedrockagentcore-memory-tokenbasedtriggerinput-tokencount): {{Integer}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput-properties"></a>

`TokenCount`  <a name="cfn-bedrockagentcore-memory-tokenbasedtriggerinput-tokencount"></a>
The token based trigger token count.
*Required*: No
*Type*: Integer
*Minimum*: `100`
*Maximum*: `500000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
