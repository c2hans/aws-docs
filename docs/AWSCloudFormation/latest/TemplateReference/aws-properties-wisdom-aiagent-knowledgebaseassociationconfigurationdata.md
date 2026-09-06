---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent KnowledgeBaseAssociationConfigurationData
<a name="aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata"></a>

The data of the configuration for a `KNOWLEDGE_BASE` type Amazon Q in Connect Assistant Association.

## Syntax
<a name="aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata-syntax.json"></a>

```
{
  "[ContentTagFilter](#cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-contenttagfilter)" : {{TagFilter}},
  "[MaxResults](#cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-maxresults)" : {{Number}},
  "[OverrideKnowledgeBaseSearchType](#cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-overrideknowledgebasesearchtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata-syntax.yaml"></a>

```
  [ContentTagFilter](#cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-contenttagfilter): {{
    TagFilter}}
  [MaxResults](#cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-maxresults): {{Number}}
  [OverrideKnowledgeBaseSearchType](#cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-overrideknowledgebasesearchtype): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata-properties"></a>

`ContentTagFilter`  <a name="cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-contenttagfilter"></a>
An object that can be used to specify Tag conditions.
*Required*: No
*Type*: [TagFilter](aws-properties-wisdom-aiagent-tagfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxResults`  <a name="cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-maxresults"></a>
The maximum number of results to return per page.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverrideKnowledgeBaseSearchType`  <a name="cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-overrideknowledgebasesearchtype"></a>
The search type to be used against the Knowledge Base for this request. The values can be `SEMANTIC` which uses vector embeddings or `HYBRID` which use vector embeddings and raw text
*Required*: No
*Type*: String
*Allowed values*: `HYBRID | SEMANTIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
