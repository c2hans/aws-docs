---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sheetimage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SheetImage
<a name="aws-properties-quicksight-dashboard-sheetimage"></a>

An image that is located on a sheet.

## Syntax
<a name="aws-properties-quicksight-dashboard-sheetimage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sheetimage-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-dashboard-sheetimage-actions)" : {{[ ImageCustomAction, ... ]}},
  "[ImageContentAltText](#cfn-quicksight-dashboard-sheetimage-imagecontentalttext)" : {{String}},
  "[Interactions](#cfn-quicksight-dashboard-sheetimage-interactions)" : {{ImageInteractionOptions}},
  "[Scaling](#cfn-quicksight-dashboard-sheetimage-scaling)" : {{SheetImageScalingConfiguration}},
  "[SheetImageId](#cfn-quicksight-dashboard-sheetimage-sheetimageid)" : {{String}},
  "[Source](#cfn-quicksight-dashboard-sheetimage-source)" : {{SheetImageSource}},
  "[Tooltip](#cfn-quicksight-dashboard-sheetimage-tooltip)" : {{SheetImageTooltipConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sheetimage-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-dashboard-sheetimage-actions): {{
    - ImageCustomAction}}
  [ImageContentAltText](#cfn-quicksight-dashboard-sheetimage-imagecontentalttext): {{String}}
  [Interactions](#cfn-quicksight-dashboard-sheetimage-interactions): {{
    ImageInteractionOptions}}
  [Scaling](#cfn-quicksight-dashboard-sheetimage-scaling): {{
    SheetImageScalingConfiguration}}
  [SheetImageId](#cfn-quicksight-dashboard-sheetimage-sheetimageid): {{String}}
  [Source](#cfn-quicksight-dashboard-sheetimage-source): {{
    SheetImageSource}}
  [Tooltip](#cfn-quicksight-dashboard-sheetimage-tooltip): {{
    SheetImageTooltipConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sheetimage-properties"></a>

`Actions`  <a name="cfn-quicksight-dashboard-sheetimage-actions"></a>
A list of custom actions that are configured for an image.
*Required*: No
*Type*: Array of [ImageCustomAction](aws-properties-quicksight-dashboard-imagecustomaction.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageContentAltText`  <a name="cfn-quicksight-dashboard-sheetimage-imagecontentalttext"></a>
The alt text for the image.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-dashboard-sheetimage-interactions"></a>
The general image interactions setup for an image.
*Required*: No
*Type*: [ImageInteractionOptions](aws-properties-quicksight-dashboard-imageinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scaling`  <a name="cfn-quicksight-dashboard-sheetimage-scaling"></a>
Determines how the image is scaled.
*Required*: No
*Type*: [SheetImageScalingConfiguration](aws-properties-quicksight-dashboard-sheetimagescalingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetImageId`  <a name="cfn-quicksight-dashboard-sheetimage-sheetimageid"></a>
The ID of the sheet image.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-dashboard-sheetimage-source"></a>
The source of the image.
*Required*: Yes
*Type*: [SheetImageSource](aws-properties-quicksight-dashboard-sheetimagesource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tooltip`  <a name="cfn-quicksight-dashboard-sheetimage-tooltip"></a>
The tooltip to be shown when hovering over the image.
*Required*: No
*Type*: [SheetImageTooltipConfiguration](aws-properties-quicksight-dashboard-sheetimagetooltipconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
