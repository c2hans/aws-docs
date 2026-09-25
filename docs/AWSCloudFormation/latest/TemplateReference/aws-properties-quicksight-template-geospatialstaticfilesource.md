---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialstaticfilesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialStaticFileSource
<a name="aws-properties-quicksight-template-geospatialstaticfilesource"></a>

The source properties for a geospatial static file.

## Syntax
<a name="aws-properties-quicksight-template-geospatialstaticfilesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialstaticfilesource-syntax.json"></a>

```
{
  "[StaticFileId](#cfn-quicksight-template-geospatialstaticfilesource-staticfileid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialstaticfilesource-syntax.yaml"></a>

```
  [StaticFileId](#cfn-quicksight-template-geospatialstaticfilesource-staticfileid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialstaticfilesource-properties"></a>

`StaticFileId`  <a name="cfn-quicksight-template-geospatialstaticfilesource-staticfileid"></a>
The ID of the static file.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
