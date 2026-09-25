---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-decalsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DecalSettings
<a name="aws-properties-quicksight-template-decalsettings"></a>

Decal settings for accessibility features that define visual patterns and styling for data elements.

## Syntax
<a name="aws-properties-quicksight-template-decalsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-decalsettings-syntax.json"></a>

```
{
  "[DecalColor](#cfn-quicksight-template-decalsettings-decalcolor)" : {{String}},
  "[DecalPatternType](#cfn-quicksight-template-decalsettings-decalpatterntype)" : {{String}},
  "[DecalStyleType](#cfn-quicksight-template-decalsettings-decalstyletype)" : {{String}},
  "[DecalVisibility](#cfn-quicksight-template-decalsettings-decalvisibility)" : {{String}},
  "[ElementValue](#cfn-quicksight-template-decalsettings-elementvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-decalsettings-syntax.yaml"></a>

```
  [DecalColor](#cfn-quicksight-template-decalsettings-decalcolor): {{String}}
  [DecalPatternType](#cfn-quicksight-template-decalsettings-decalpatterntype): {{String}}
  [DecalStyleType](#cfn-quicksight-template-decalsettings-decalstyletype): {{String}}
  [DecalVisibility](#cfn-quicksight-template-decalsettings-decalvisibility): {{String}}
  [ElementValue](#cfn-quicksight-template-decalsettings-elementvalue): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-decalsettings-properties"></a>

`DecalColor`  <a name="cfn-quicksight-template-decalsettings-decalcolor"></a>
Color configuration for the decal pattern.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DecalPatternType`  <a name="cfn-quicksight-template-decalsettings-decalpatterntype"></a>
Type of pattern used for the decal, such as solid, diagonal, or circular patterns in various sizes.
+ `SOLID`: Solid fill pattern.
+ `DIAGONAL_SMALL`: Small diagonal stripes pattern.
+ `DIAGONAL_MEDIUM`: Medium diagonal stripes pattern.
+ `DIAGONAL_LARGE`: Large diagonal stripes pattern.
+ `DIAGONAL_OPPOSITE_SMALL`: Small cross-diagonal stripes pattern.
+ `DIAGONAL_OPPOSITE_MEDIUM`: Medium cross-diagonal stripes pattern.
+ `DIAGONAL_OPPOSITE_LARGE`: Large cross-diagonal stripes pattern.
+ `CIRCLE_SMALL`: Small circle pattern.
+ `CIRCLE_MEDIUM`: Medium circle pattern.
+ `CIRCLE_LARGE`: Large circle pattern.
+ `DIAMOND_SMALL`: Small diamonds pattern.
+ `DIAMOND_MEDIUM`: Medium diamonds pattern.
+ `DIAMOND_LARGE`: Large diamonds pattern.
+ `DIAMOND_GRID_SMALL`: Small diamond grid pattern.
+ `DIAMOND_GRID_MEDIUM`: Medium diamond grid pattern.
+ `DIAMOND_GRID_LARGE`: Large diamond grid pattern.
+ `CHECKERBOARD_SMALL`: Small checkerboard pattern.
+ `CHECKERBOARD_MEDIUM`: Medium checkerboard pattern.
+ `CHECKERBOARD_LARGE`: Large checkerboard pattern.
+ `TRIANGLE_SMALL`: Small triangles pattern.
+ `TRIANGLE_MEDIUM`: Medium triangles pattern.
+ `TRIANGLE_LARGE`: Large triangles pattern.
*Required*: No
*Type*: String
*Allowed values*: `SOLID | DIAGONAL_MEDIUM | CIRCLE_MEDIUM | DIAMOND_GRID_MEDIUM | CHECKERBOARD_MEDIUM | TRIANGLE_MEDIUM | DIAGONAL_OPPOSITE_MEDIUM | DIAMOND_MEDIUM | DIAGONAL_LARGE | CIRCLE_LARGE | DIAMOND_GRID_LARGE | CHECKERBOARD_LARGE | TRIANGLE_LARGE | DIAGONAL_OPPOSITE_LARGE | DIAMOND_LARGE | DIAGONAL_SMALL | CIRCLE_SMALL | DIAMOND_GRID_SMALL | CHECKERBOARD_SMALL | TRIANGLE_SMALL | DIAGONAL_OPPOSITE_SMALL | DIAMOND_SMALL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DecalStyleType`  <a name="cfn-quicksight-template-decalsettings-decalstyletype"></a>
Style type for the decal, which can be either manual or automatic. This field is only applicable for line series.
+ `Manual`: Apply manual line and marker configuration for line series.
+ `Auto`: Apply automatic line and marker configuration for line series.
*Required*: No
*Type*: String
*Allowed values*: `Manual | Auto`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DecalVisibility`  <a name="cfn-quicksight-template-decalsettings-decalvisibility"></a>
Visibility setting for the decal pattern.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ElementValue`  <a name="cfn-quicksight-template-decalsettings-elementvalue"></a>
Field value of the field that you are setting the decal pattern to. Applicable only for field level settings.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
