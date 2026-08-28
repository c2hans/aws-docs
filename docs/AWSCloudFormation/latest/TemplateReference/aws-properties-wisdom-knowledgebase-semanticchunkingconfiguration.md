---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-semanticchunkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase SemanticChunkingConfiguration
<a name="aws-properties-wisdom-knowledgebase-semanticchunkingconfiguration"></a>

Settings for semantic document chunking for a data source. Semantic chunking splits a document into smaller documents based on groups of similar content derived from the text with natural language processing.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-semanticchunkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-semanticchunkingconfiguration-syntax.json"></a>

```
{
  "[BreakpointPercentileThreshold](#cfn-wisdom-knowledgebase-semanticchunkingconfiguration-breakpointpercentilethreshold)" : {{Number}},
  "[BufferSize](#cfn-wisdom-knowledgebase-semanticchunkingconfiguration-buffersize)" : {{Number}},
  "[MaxTokens](#cfn-wisdom-knowledgebase-semanticchunkingconfiguration-maxtokens)" : {{Number}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-semanticchunkingconfiguration-syntax.yaml"></a>

```
  [BreakpointPercentileThreshold](#cfn-wisdom-knowledgebase-semanticchunkingconfiguration-breakpointpercentilethreshold): {{Number}}
  [BufferSize](#cfn-wisdom-knowledgebase-semanticchunkingconfiguration-buffersize): {{Number}}
  [MaxTokens](#cfn-wisdom-knowledgebase-semanticchunkingconfiguration-maxtokens): {{Number}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-semanticchunkingconfiguration-properties"></a>

`BreakpointPercentileThreshold`  <a name="cfn-wisdom-knowledgebase-semanticchunkingconfiguration-breakpointpercentilethreshold"></a>
The dissimilarity threshold for splitting chunks.
*Required*: Yes
*Type*: Number
*Minimum*: `50`
*Maximum*: `99`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BufferSize`  <a name="cfn-wisdom-knowledgebase-semanticchunkingconfiguration-buffersize"></a>
The buffer size.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxTokens`  <a name="cfn-wisdom-knowledgebase-semanticchunkingconfiguration-maxtokens"></a>
The maximum number of tokens that a chunk can contain.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
