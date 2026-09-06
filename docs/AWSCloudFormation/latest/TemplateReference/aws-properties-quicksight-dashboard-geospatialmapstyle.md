---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatialmapstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialMapStyle
<a name="aws-properties-quicksight-dashboard-geospatialmapstyle"></a>

The map style properties for a map.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatialmapstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatialmapstyle-syntax.json"></a>

```
{
  "[BackgroundColor](#cfn-quicksight-dashboard-geospatialmapstyle-backgroundcolor)" : {{String}},
  "[BaseMapStyle](#cfn-quicksight-dashboard-geospatialmapstyle-basemapstyle)" : {{String}},
  "[BaseMapVisibility](#cfn-quicksight-dashboard-geospatialmapstyle-basemapvisibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatialmapstyle-syntax.yaml"></a>

```
  [BackgroundColor](#cfn-quicksight-dashboard-geospatialmapstyle-backgroundcolor): {{String}}
  [BaseMapStyle](#cfn-quicksight-dashboard-geospatialmapstyle-basemapstyle): {{String}}
  [BaseMapVisibility](#cfn-quicksight-dashboard-geospatialmapstyle-basemapvisibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatialmapstyle-properties"></a>

`BackgroundColor`  <a name="cfn-quicksight-dashboard-geospatialmapstyle-backgroundcolor"></a>
The background color and opacity values for a map.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaseMapStyle`  <a name="cfn-quicksight-dashboard-geospatialmapstyle-basemapstyle"></a>
The selected base map style.
*Required*: No
*Type*: String
*Allowed values*: `LIGHT_GRAY | DARK_GRAY | STREET | IMAGERY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaseMapVisibility`  <a name="cfn-quicksight-dashboard-geospatialmapstyle-basemapvisibility"></a>
The state of visibility for the base map.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
