---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-knowledgebase-audioextractionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::KnowledgeBase AudioExtractionConfiguration

The configuration for audio extraction from knowledge base documents.

## Syntax
<a name="aws-properties-quicksight-knowledgebase-audioextractionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-knowledgebase-audioextractionconfiguration-syntax.json"></a>

```json
{
  "[AudioExtractionStatus](#cfn-quicksight-knowledgebase-audioextractionconfiguration-audioextractionstatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-knowledgebase-audioextractionconfiguration-syntax.yaml"></a>

```yaml
  [AudioExtractionStatus](#cfn-quicksight-knowledgebase-audioextractionconfiguration-audioextractionstatus): {{String}}
```

## Properties
<a name="aws-properties-quicksight-knowledgebase-audioextractionconfiguration-properties"></a>

`AudioExtractionStatus`  <a name="cfn-quicksight-knowledgebase-audioextractionconfiguration-audioextractionstatus"></a>
The status of audio extraction. Valid values are ENABLED and DISABLED.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
