---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatialcoordinatebounds.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialCoordinateBounds
<a name="aws-properties-quicksight-dashboard-geospatialcoordinatebounds"></a>

The bound options (north, south, west, east) of the geospatial window options.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatialcoordinatebounds-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatialcoordinatebounds-syntax.json"></a>

```
{
  "[East](#cfn-quicksight-dashboard-geospatialcoordinatebounds-east)" : {{Number}},
  "[North](#cfn-quicksight-dashboard-geospatialcoordinatebounds-north)" : {{Number}},
  "[South](#cfn-quicksight-dashboard-geospatialcoordinatebounds-south)" : {{Number}},
  "[West](#cfn-quicksight-dashboard-geospatialcoordinatebounds-west)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatialcoordinatebounds-syntax.yaml"></a>

```
  [East](#cfn-quicksight-dashboard-geospatialcoordinatebounds-east): {{Number}}
  [North](#cfn-quicksight-dashboard-geospatialcoordinatebounds-north): {{Number}}
  [South](#cfn-quicksight-dashboard-geospatialcoordinatebounds-south): {{Number}}
  [West](#cfn-quicksight-dashboard-geospatialcoordinatebounds-west): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatialcoordinatebounds-properties"></a>

`East`  <a name="cfn-quicksight-dashboard-geospatialcoordinatebounds-east"></a>
The longitude of the east bound of the geospatial coordinate bounds.
*Required*: Yes
*Type*: Number
*Minimum*: `-1800`
*Maximum*: `1800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`North`  <a name="cfn-quicksight-dashboard-geospatialcoordinatebounds-north"></a>
The latitude of the north bound of the geospatial coordinate bounds.
*Required*: Yes
*Type*: Number
*Minimum*: `-90`
*Maximum*: `90`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`South`  <a name="cfn-quicksight-dashboard-geospatialcoordinatebounds-south"></a>
The latitude of the south bound of the geospatial coordinate bounds.
*Required*: Yes
*Type*: Number
*Minimum*: `-90`
*Maximum*: `90`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`West`  <a name="cfn-quicksight-dashboard-geospatialcoordinatebounds-west"></a>
The longitude of the west bound of the geospatial coordinate bounds.
*Required*: Yes
*Type*: Number
*Minimum*: `-1800`
*Maximum*: `1800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
