---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-knowledgebase-knowledgebaseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::KnowledgeBase KnowledgeBaseConfiguration
<a name="aws-properties-quicksight-knowledgebase-knowledgebaseconfiguration"></a>

The configuration settings for a knowledge base.

## Syntax
<a name="aws-properties-quicksight-knowledgebase-knowledgebaseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-knowledgebase-knowledgebaseconfiguration-syntax.json"></a>

```
{
  "[TemplateConfiguration](#cfn-quicksight-knowledgebase-knowledgebaseconfiguration-templateconfiguration)" : {{KbTemplateConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-knowledgebase-knowledgebaseconfiguration-syntax.yaml"></a>

```
  [TemplateConfiguration](#cfn-quicksight-knowledgebase-knowledgebaseconfiguration-templateconfiguration): {{
    KbTemplateConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-knowledgebase-knowledgebaseconfiguration-properties"></a>

`TemplateConfiguration`  <a name="cfn-quicksight-knowledgebase-knowledgebaseconfiguration-templateconfiguration"></a>
The template configuration that defines how the data source connector crawls and indexes data for the knowledge base. The template structure varies by connector type. See `KbTemplateConfiguration` for connector-specific details.
*Required*: No
*Type*: [KbTemplateConfiguration](aws-properties-quicksight-knowledgebase-kbtemplateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
