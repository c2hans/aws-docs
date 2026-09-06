---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-knowledgebase-imageextractionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::KnowledgeBase ImageExtractionConfiguration
<a name="aws-properties-quicksight-knowledgebase-imageextractionconfiguration"></a>

The configuration for image extraction from knowledge base documents.

## Syntax
<a name="aws-properties-quicksight-knowledgebase-imageextractionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-knowledgebase-imageextractionconfiguration-syntax.json"></a>

```
{
  "[ImageExtractionStatus](#cfn-quicksight-knowledgebase-imageextractionconfiguration-imageextractionstatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-knowledgebase-imageextractionconfiguration-syntax.yaml"></a>

```
  [ImageExtractionStatus](#cfn-quicksight-knowledgebase-imageextractionconfiguration-imageextractionstatus): {{String}}
```

## Properties
<a name="aws-properties-quicksight-knowledgebase-imageextractionconfiguration-properties"></a>

`ImageExtractionStatus`  <a name="cfn-quicksight-knowledgebase-imageextractionconfiguration-imageextractionstatus"></a>
The status of image extraction. Valid values are ENABLED and DISABLED.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
