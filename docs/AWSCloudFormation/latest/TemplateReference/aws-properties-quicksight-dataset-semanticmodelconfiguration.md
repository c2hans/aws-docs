---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-semanticmodelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet SemanticModelConfiguration
<a name="aws-properties-quicksight-dataset-semanticmodelconfiguration"></a>

Configuration for the semantic model that defines how prepared data is structured for analysis and reporting.

## Syntax
<a name="aws-properties-quicksight-dataset-semanticmodelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-semanticmodelconfiguration-syntax.json"></a>

```
{
  "[SemanticMetadata](#cfn-quicksight-dataset-semanticmodelconfiguration-semanticmetadata)" : {{[ DataSetSemanticMetadata, ... ]}},
  "[TableMap](#cfn-quicksight-dataset-semanticmodelconfiguration-tablemap)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-semanticmodelconfiguration-syntax.yaml"></a>

```
  [SemanticMetadata](#cfn-quicksight-dataset-semanticmodelconfiguration-semanticmetadata): {{
    - DataSetSemanticMetadata}}
  [TableMap](#cfn-quicksight-dataset-semanticmodelconfiguration-tablemap): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-quicksight-dataset-semanticmodelconfiguration-properties"></a>

`SemanticMetadata`  <a name="cfn-quicksight-dataset-semanticmodelconfiguration-semanticmetadata"></a>
The dataset-level semantic metadata, including a description and custom instructions.
*Required*: No
*Type*: Array of [DataSetSemanticMetadata](aws-properties-quicksight-dataset-datasetsemanticmetadata.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableMap`  <a name="cfn-quicksight-dataset-semanticmodelconfiguration-tablemap"></a>
A map of semantic tables that define the analytical structure.
*Required*: No
*Type*: Object of [SemanticTable](aws-properties-quicksight-dataset-semantictable.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
