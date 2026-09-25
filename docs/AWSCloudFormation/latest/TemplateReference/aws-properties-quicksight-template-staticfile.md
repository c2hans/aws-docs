---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-staticfile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template StaticFile
<a name="aws-properties-quicksight-template-staticfile"></a>

The static file.

## Syntax
<a name="aws-properties-quicksight-template-staticfile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-staticfile-syntax.json"></a>

```
{
  "[ImageStaticFile](#cfn-quicksight-template-staticfile-imagestaticfile)" : {{ImageStaticFile}},
  "[SpatialStaticFile](#cfn-quicksight-template-staticfile-spatialstaticfile)" : {{SpatialStaticFile}}
}
```

### YAML
<a name="aws-properties-quicksight-template-staticfile-syntax.yaml"></a>

```
  [ImageStaticFile](#cfn-quicksight-template-staticfile-imagestaticfile): {{
    ImageStaticFile}}
  [SpatialStaticFile](#cfn-quicksight-template-staticfile-spatialstaticfile): {{
    SpatialStaticFile}}
```

## Properties
<a name="aws-properties-quicksight-template-staticfile-properties"></a>

`ImageStaticFile`  <a name="cfn-quicksight-template-staticfile-imagestaticfile"></a>
The image static file.
*Required*: No
*Type*: [ImageStaticFile](aws-properties-quicksight-template-imagestaticfile.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpatialStaticFile`  <a name="cfn-quicksight-template-staticfile-spatialstaticfile"></a>
The spacial static file.
*Required*: No
*Type*: [SpatialStaticFile](aws-properties-quicksight-template-spatialstaticfile.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
