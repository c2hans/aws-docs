---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialcoordinatebounds.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialCoordinateBounds
<a name="aws-properties-quicksight-analysis-geospatialcoordinatebounds"></a>

The bound options (north, south, west, east) of the geospatial window options.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialcoordinatebounds-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialcoordinatebounds-syntax.json"></a>

```
{
  "[East](#cfn-quicksight-analysis-geospatialcoordinatebounds-east)" : {{Number}},
  "[North](#cfn-quicksight-analysis-geospatialcoordinatebounds-north)" : {{Number}},
  "[South](#cfn-quicksight-analysis-geospatialcoordinatebounds-south)" : {{Number}},
  "[West](#cfn-quicksight-analysis-geospatialcoordinatebounds-west)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialcoordinatebounds-syntax.yaml"></a>

```
  [East](#cfn-quicksight-analysis-geospatialcoordinatebounds-east): {{Number}}
  [North](#cfn-quicksight-analysis-geospatialcoordinatebounds-north): {{Number}}
  [South](#cfn-quicksight-analysis-geospatialcoordinatebounds-south): {{Number}}
  [West](#cfn-quicksight-analysis-geospatialcoordinatebounds-west): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialcoordinatebounds-properties"></a>

`East`  <a name="cfn-quicksight-analysis-geospatialcoordinatebounds-east"></a>
The longitude of the east bound of the geospatial coordinate bounds.
*Required*: Yes
*Type*: Number
*Minimum*: `-1800`
*Maximum*: `1800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`North`  <a name="cfn-quicksight-analysis-geospatialcoordinatebounds-north"></a>
The latitude of the north bound of the geospatial coordinate bounds.
*Required*: Yes
*Type*: Number
*Minimum*: `-90`
*Maximum*: `90`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`South`  <a name="cfn-quicksight-analysis-geospatialcoordinatebounds-south"></a>
The latitude of the south bound of the geospatial coordinate bounds.
*Required*: Yes
*Type*: Number
*Minimum*: `-90`
*Maximum*: `90`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`West`  <a name="cfn-quicksight-analysis-geospatialcoordinatebounds-west"></a>
The longitude of the west bound of the geospatial coordinate bounds.
*Required*: Yes
*Type*: Number
*Minimum*: `-1800`
*Maximum*: `1800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
