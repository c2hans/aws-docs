---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatiallayerjoindefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialLayerJoinDefinition
<a name="aws-properties-quicksight-template-geospatiallayerjoindefinition"></a>

The custom actions for a layer.

## Syntax
<a name="aws-properties-quicksight-template-geospatiallayerjoindefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatiallayerjoindefinition-syntax.json"></a>

```
{
  "[ColorField](#cfn-quicksight-template-geospatiallayerjoindefinition-colorfield)" : {{GeospatialLayerColorField}},
  "[DatasetKeyField](#cfn-quicksight-template-geospatiallayerjoindefinition-datasetkeyfield)" : {{UnaggregatedField}},
  "[ShapeKeyField](#cfn-quicksight-template-geospatiallayerjoindefinition-shapekeyfield)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatiallayerjoindefinition-syntax.yaml"></a>

```
  [ColorField](#cfn-quicksight-template-geospatiallayerjoindefinition-colorfield): {{
    GeospatialLayerColorField}}
  [DatasetKeyField](#cfn-quicksight-template-geospatiallayerjoindefinition-datasetkeyfield): {{
    UnaggregatedField}}
  [ShapeKeyField](#cfn-quicksight-template-geospatiallayerjoindefinition-shapekeyfield): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatiallayerjoindefinition-properties"></a>

`ColorField`  <a name="cfn-quicksight-template-geospatiallayerjoindefinition-colorfield"></a>
The geospatial color field for the join definition.
*Required*: No
*Type*: [GeospatialLayerColorField](aws-properties-quicksight-template-geospatiallayercolorfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatasetKeyField`  <a name="cfn-quicksight-template-geospatiallayerjoindefinition-datasetkeyfield"></a>
Property description not available.
*Required*: No
*Type*: [UnaggregatedField](aws-properties-quicksight-template-unaggregatedfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShapeKeyField`  <a name="cfn-quicksight-template-geospatiallayerjoindefinition-shapekeyfield"></a>
The name of the field or property in the geospatial data source.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
