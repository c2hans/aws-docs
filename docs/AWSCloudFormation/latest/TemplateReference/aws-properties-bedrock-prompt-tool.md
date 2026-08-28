---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-prompt-tool.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt Tool
<a name="aws-properties-bedrock-prompt-tool"></a>

Information about a tool that you can use with the Converse API. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-prompt-tool-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-prompt-tool-syntax.json"></a>

```
{
  "[CachePoint](#cfn-bedrock-prompt-tool-cachepoint)" : {{CachePointBlock}},
  "[ToolSpec](#cfn-bedrock-prompt-tool-toolspec)" : {{ToolSpecification}}
}
```

### YAML
<a name="aws-properties-bedrock-prompt-tool-syntax.yaml"></a>

```
  [CachePoint](#cfn-bedrock-prompt-tool-cachepoint): {{
    CachePointBlock}}
  [ToolSpec](#cfn-bedrock-prompt-tool-toolspec): {{
    ToolSpecification}}
```

## Properties
<a name="aws-properties-bedrock-prompt-tool-properties"></a>

`CachePoint`  <a name="cfn-bedrock-prompt-tool-cachepoint"></a>
CachePoint to include in the tool configuration.
*Required*: No
*Type*: [CachePointBlock](aws-properties-bedrock-prompt-cachepointblock.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToolSpec`  <a name="cfn-bedrock-prompt-tool-toolspec"></a>
The specfication for the tool.
*Required*: No
*Type*: [ToolSpecification](aws-properties-bedrock-prompt-toolspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
