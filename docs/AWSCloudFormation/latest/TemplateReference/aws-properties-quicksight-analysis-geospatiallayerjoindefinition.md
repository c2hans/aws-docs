---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatiallayerjoindefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialLayerJoinDefinition
<a name="aws-properties-quicksight-analysis-geospatiallayerjoindefinition"></a>

The custom actions for a layer.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatiallayerjoindefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatiallayerjoindefinition-syntax.json"></a>

```
{
  "[ColorField](#cfn-quicksight-analysis-geospatiallayerjoindefinition-colorfield)" : {{GeospatialLayerColorField}},
  "[DatasetKeyField](#cfn-quicksight-analysis-geospatiallayerjoindefinition-datasetkeyfield)" : {{UnaggregatedField}},
  "[ShapeKeyField](#cfn-quicksight-analysis-geospatiallayerjoindefinition-shapekeyfield)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatiallayerjoindefinition-syntax.yaml"></a>

```
  [ColorField](#cfn-quicksight-analysis-geospatiallayerjoindefinition-colorfield): {{
    GeospatialLayerColorField}}
  [DatasetKeyField](#cfn-quicksight-analysis-geospatiallayerjoindefinition-datasetkeyfield): {{
    UnaggregatedField}}
  [ShapeKeyField](#cfn-quicksight-analysis-geospatiallayerjoindefinition-shapekeyfield): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatiallayerjoindefinition-properties"></a>

`ColorField`  <a name="cfn-quicksight-analysis-geospatiallayerjoindefinition-colorfield"></a>
The geospatial color field for the join definition.
*Required*: No
*Type*: [GeospatialLayerColorField](aws-properties-quicksight-analysis-geospatiallayercolorfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatasetKeyField`  <a name="cfn-quicksight-analysis-geospatiallayerjoindefinition-datasetkeyfield"></a>
Property description not available.
*Required*: No
*Type*: [UnaggregatedField](aws-properties-quicksight-analysis-unaggregatedfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShapeKeyField`  <a name="cfn-quicksight-analysis-geospatiallayerjoindefinition-shapekeyfield"></a>
The name of the field or property in the geospatial data source.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
