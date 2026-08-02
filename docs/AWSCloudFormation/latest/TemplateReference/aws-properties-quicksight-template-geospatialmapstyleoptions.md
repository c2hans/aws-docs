---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialmapstyleoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialMapStyleOptions
<a name="aws-properties-quicksight-template-geospatialmapstyleoptions"></a>

The map style options of the geospatial map.

## Syntax
<a name="aws-properties-quicksight-template-geospatialmapstyleoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialmapstyleoptions-syntax.json"></a>

```
{
  "[BaseMapStyle](#cfn-quicksight-template-geospatialmapstyleoptions-basemapstyle)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialmapstyleoptions-syntax.yaml"></a>

```
  [BaseMapStyle](#cfn-quicksight-template-geospatialmapstyleoptions-basemapstyle): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialmapstyleoptions-properties"></a>

`BaseMapStyle`  <a name="cfn-quicksight-template-geospatialmapstyleoptions-basemapstyle"></a>
The base map style of the geospatial map.
*Required*: No
*Type*: String
*Allowed values*: `LIGHT_GRAY | DARK_GRAY | STREET | IMAGERY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
