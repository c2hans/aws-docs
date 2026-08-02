---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-entity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis Entity
<a name="aws-properties-quicksight-analysis-entity"></a>

An object, structure, or sub-structure of an analysis, template, or dashboard.

## Syntax
<a name="aws-properties-quicksight-analysis-entity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-entity-syntax.json"></a>

```
{
  "[Path](#cfn-quicksight-analysis-entity-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-entity-syntax.yaml"></a>

```
  [Path](#cfn-quicksight-analysis-entity-path): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-entity-properties"></a>

`Path`  <a name="cfn-quicksight-analysis-entity-path"></a>
The hierarchical path of the entity within the analysis, template, or dashboard definition tree.
*Required*: No
*Type*: String
*Pattern*: `\S`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
