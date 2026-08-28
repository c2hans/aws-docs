---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-associationconfigurationdata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent AssociationConfigurationData
<a name="aws-properties-wisdom-aiagent-associationconfigurationdata"></a>

A typed union of the data of the configuration for an Amazon Q in Connect Assistant Association.

## Syntax
<a name="aws-properties-wisdom-aiagent-associationconfigurationdata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-associationconfigurationdata-syntax.json"></a>

```
{
  "[KnowledgeBaseAssociationConfigurationData](#cfn-wisdom-aiagent-associationconfigurationdata-knowledgebaseassociationconfigurationdata)" : {{KnowledgeBaseAssociationConfigurationData}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-associationconfigurationdata-syntax.yaml"></a>

```
  [KnowledgeBaseAssociationConfigurationData](#cfn-wisdom-aiagent-associationconfigurationdata-knowledgebaseassociationconfigurationdata): {{
    KnowledgeBaseAssociationConfigurationData}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-associationconfigurationdata-properties"></a>

`KnowledgeBaseAssociationConfigurationData`  <a name="cfn-wisdom-aiagent-associationconfigurationdata-knowledgebaseassociationconfigurationdata"></a>
The data of the configuration for a `KNOWLEDGE_BASE` type Amazon Q in Connect Assistant Association.
*Required*: Yes
*Type*: [KnowledgeBaseAssociationConfigurationData](aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
