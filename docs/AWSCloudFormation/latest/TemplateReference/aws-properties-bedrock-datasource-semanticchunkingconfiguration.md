---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-semanticchunkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource SemanticChunkingConfiguration
<a name="aws-properties-bedrock-datasource-semanticchunkingconfiguration"></a>

Settings for semantic document chunking for a data source. Semantic chunking splits a document into into smaller documents based on groups of similar content derived from the text with natural language processing.

With semantic chunking, each sentence is compared to the next to determine how similar they are. You specify a threshold in the form of a percentile, where adjacent sentences that are less similar than that percentage of sentence pairs are divided into separate chunks. For example, if you set the threshold to 90, then the 10 percent of sentence pairs that are least similar are split. So if you have 101 sentences, 100 sentence pairs are compared, and the 10 with the least similarity are split, creating 11 chunks. These chunks are further split if they exceed the max token size.

You must also specify a buffer size, which determines whether sentences are compared in isolation, or within a moving context window that includes the previous and following sentence. For example, if you set the buffer size to `1`, the embedding for sentence 10 is derived from sentences 9, 10, and 11 combined.

## Syntax
<a name="aws-properties-bedrock-datasource-semanticchunkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-semanticchunkingconfiguration-syntax.json"></a>

```
{
  "[BreakpointPercentileThreshold](#cfn-bedrock-datasource-semanticchunkingconfiguration-breakpointpercentilethreshold)" : {{Integer}},
  "[BufferSize](#cfn-bedrock-datasource-semanticchunkingconfiguration-buffersize)" : {{Integer}},
  "[MaxTokens](#cfn-bedrock-datasource-semanticchunkingconfiguration-maxtokens)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-semanticchunkingconfiguration-syntax.yaml"></a>

```
  [BreakpointPercentileThreshold](#cfn-bedrock-datasource-semanticchunkingconfiguration-breakpointpercentilethreshold): {{Integer}}
  [BufferSize](#cfn-bedrock-datasource-semanticchunkingconfiguration-buffersize): {{Integer}}
  [MaxTokens](#cfn-bedrock-datasource-semanticchunkingconfiguration-maxtokens): {{Integer}}
```

## Properties
<a name="aws-properties-bedrock-datasource-semanticchunkingconfiguration-properties"></a>

`BreakpointPercentileThreshold`  <a name="cfn-bedrock-datasource-semanticchunkingconfiguration-breakpointpercentilethreshold"></a>
The dissimilarity threshold for splitting chunks.
*Required*: Yes
*Type*: Integer
*Minimum*: `50`
*Maximum*: `99`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BufferSize`  <a name="cfn-bedrock-datasource-semanticchunkingconfiguration-buffersize"></a>
The buffer size.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxTokens`  <a name="cfn-bedrock-datasource-semanticchunkingconfiguration-maxtokens"></a>
The maximum number of tokens that a chunk can contain.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
