---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-staticfile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard StaticFile
<a name="aws-properties-quicksight-dashboard-staticfile"></a>

The static file.

## Syntax
<a name="aws-properties-quicksight-dashboard-staticfile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-staticfile-syntax.json"></a>

```
{
  "[ImageStaticFile](#cfn-quicksight-dashboard-staticfile-imagestaticfile)" : {{ImageStaticFile}},
  "[SpatialStaticFile](#cfn-quicksight-dashboard-staticfile-spatialstaticfile)" : {{SpatialStaticFile}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-staticfile-syntax.yaml"></a>

```
  [ImageStaticFile](#cfn-quicksight-dashboard-staticfile-imagestaticfile): {{
    ImageStaticFile}}
  [SpatialStaticFile](#cfn-quicksight-dashboard-staticfile-spatialstaticfile): {{
    SpatialStaticFile}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-staticfile-properties"></a>

`ImageStaticFile`  <a name="cfn-quicksight-dashboard-staticfile-imagestaticfile"></a>
The image static file.
*Required*: No
*Type*: [ImageStaticFile](aws-properties-quicksight-dashboard-imagestaticfile.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpatialStaticFile`  <a name="cfn-quicksight-dashboard-staticfile-spatialstaticfile"></a>
The spacial static file.
*Required*: No
*Type*: [SpatialStaticFile](aws-properties-quicksight-dashboard-spatialstaticfile.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
