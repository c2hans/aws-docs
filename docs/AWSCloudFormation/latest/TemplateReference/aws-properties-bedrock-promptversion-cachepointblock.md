---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-promptversion-cachepointblock.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::PromptVersion CachePointBlock
<a name="aws-properties-bedrock-promptversion-cachepointblock"></a>

Defines a section of content to be cached for reuse in subsequent API calls.

## Syntax
<a name="aws-properties-bedrock-promptversion-cachepointblock-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-promptversion-cachepointblock-syntax.json"></a>

```
{
  "[Type](#cfn-bedrock-promptversion-cachepointblock-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-promptversion-cachepointblock-syntax.yaml"></a>

```
  [Type](#cfn-bedrock-promptversion-cachepointblock-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-promptversion-cachepointblock-properties"></a>

`Type`  <a name="cfn-bedrock-promptversion-cachepointblock-type"></a>
Specifies the type of cache point within the CachePointBlock.
*Required*: Yes
*Type*: String
*Allowed values*: `default`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
