---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-querygenerationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase QueryGenerationConfiguration
<a name="aws-properties-bedrock-knowledgebase-querygenerationconfiguration"></a>

Contains configurations for query generation. For more information, see [Build a knowledge base by connecting to a structured data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html) in the Amazon Bedrock User Guide..

## Syntax
<a name="aws-properties-bedrock-knowledgebase-querygenerationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-querygenerationconfiguration-syntax.json"></a>

```
{
  "[ExecutionTimeoutSeconds](#cfn-bedrock-knowledgebase-querygenerationconfiguration-executiontimeoutseconds)" : {{Integer}},
  "[GenerationContext](#cfn-bedrock-knowledgebase-querygenerationconfiguration-generationcontext)" : {{QueryGenerationContext}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-querygenerationconfiguration-syntax.yaml"></a>

```
  [ExecutionTimeoutSeconds](#cfn-bedrock-knowledgebase-querygenerationconfiguration-executiontimeoutseconds): {{Integer}}
  [GenerationContext](#cfn-bedrock-knowledgebase-querygenerationconfiguration-generationcontext): {{
    QueryGenerationContext}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-querygenerationconfiguration-properties"></a>

`ExecutionTimeoutSeconds`  <a name="cfn-bedrock-knowledgebase-querygenerationconfiguration-executiontimeoutseconds"></a>
The time after which query generation will time out.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GenerationContext`  <a name="cfn-bedrock-knowledgebase-querygenerationconfiguration-generationcontext"></a>
Specifies configurations for context to use during query generation.
*Required*: No
*Type*: [QueryGenerationContext](aws-properties-bedrock-knowledgebase-querygenerationcontext.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
