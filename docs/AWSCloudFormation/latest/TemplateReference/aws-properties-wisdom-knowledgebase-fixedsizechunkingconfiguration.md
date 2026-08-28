---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-fixedsizechunkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase FixedSizeChunkingConfiguration
<a name="aws-properties-wisdom-knowledgebase-fixedsizechunkingconfiguration"></a>

Configurations for when you choose fixed-size chunking. If you set the `chunkingStrategy` as `NONE`, exclude this field.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-fixedsizechunkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-fixedsizechunkingconfiguration-syntax.json"></a>

```
{
  "[MaxTokens](#cfn-wisdom-knowledgebase-fixedsizechunkingconfiguration-maxtokens)" : {{Number}},
  "[OverlapPercentage](#cfn-wisdom-knowledgebase-fixedsizechunkingconfiguration-overlappercentage)" : {{Number}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-fixedsizechunkingconfiguration-syntax.yaml"></a>

```
  [MaxTokens](#cfn-wisdom-knowledgebase-fixedsizechunkingconfiguration-maxtokens): {{Number}}
  [OverlapPercentage](#cfn-wisdom-knowledgebase-fixedsizechunkingconfiguration-overlappercentage): {{Number}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-fixedsizechunkingconfiguration-properties"></a>

`MaxTokens`  <a name="cfn-wisdom-knowledgebase-fixedsizechunkingconfiguration-maxtokens"></a>
The maximum number of tokens to include in a chunk.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverlapPercentage`  <a name="cfn-wisdom-knowledgebase-fixedsizechunkingconfiguration-overlappercentage"></a>
The percentage of overlap between adjacent chunks of a data source.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `99`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
