---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-hierarchicalchunkinglevelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource HierarchicalChunkingLevelConfiguration
<a name="aws-properties-bedrock-datasource-hierarchicalchunkinglevelconfiguration"></a>

Token settings for a layer in a hierarchical chunking configuration.

## Syntax
<a name="aws-properties-bedrock-datasource-hierarchicalchunkinglevelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-hierarchicalchunkinglevelconfiguration-syntax.json"></a>

```
{
  "[MaxTokens](#cfn-bedrock-datasource-hierarchicalchunkinglevelconfiguration-maxtokens)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-hierarchicalchunkinglevelconfiguration-syntax.yaml"></a>

```
  [MaxTokens](#cfn-bedrock-datasource-hierarchicalchunkinglevelconfiguration-maxtokens): {{Integer}}
```

## Properties
<a name="aws-properties-bedrock-datasource-hierarchicalchunkinglevelconfiguration-properties"></a>

`MaxTokens`  <a name="cfn-bedrock-datasource-hierarchicalchunkinglevelconfiguration-maxtokens"></a>
The maximum number of tokens that a chunk can contain in this layer.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
