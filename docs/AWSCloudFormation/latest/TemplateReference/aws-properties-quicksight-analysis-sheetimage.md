---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-sheetimage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SheetImage
<a name="aws-properties-quicksight-analysis-sheetimage"></a>

An image that is located on a sheet.

## Syntax
<a name="aws-properties-quicksight-analysis-sheetimage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-sheetimage-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-analysis-sheetimage-actions)" : {{[ ImageCustomAction, ... ]}},
  "[ImageContentAltText](#cfn-quicksight-analysis-sheetimage-imagecontentalttext)" : {{String}},
  "[Interactions](#cfn-quicksight-analysis-sheetimage-interactions)" : {{ImageInteractionOptions}},
  "[Scaling](#cfn-quicksight-analysis-sheetimage-scaling)" : {{SheetImageScalingConfiguration}},
  "[SheetImageId](#cfn-quicksight-analysis-sheetimage-sheetimageid)" : {{String}},
  "[Source](#cfn-quicksight-analysis-sheetimage-source)" : {{SheetImageSource}},
  "[Tooltip](#cfn-quicksight-analysis-sheetimage-tooltip)" : {{SheetImageTooltipConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-sheetimage-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-analysis-sheetimage-actions): {{
    - ImageCustomAction}}
  [ImageContentAltText](#cfn-quicksight-analysis-sheetimage-imagecontentalttext): {{String}}
  [Interactions](#cfn-quicksight-analysis-sheetimage-interactions): {{
    ImageInteractionOptions}}
  [Scaling](#cfn-quicksight-analysis-sheetimage-scaling): {{
    SheetImageScalingConfiguration}}
  [SheetImageId](#cfn-quicksight-analysis-sheetimage-sheetimageid): {{String}}
  [Source](#cfn-quicksight-analysis-sheetimage-source): {{
    SheetImageSource}}
  [Tooltip](#cfn-quicksight-analysis-sheetimage-tooltip): {{
    SheetImageTooltipConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-sheetimage-properties"></a>

`Actions`  <a name="cfn-quicksight-analysis-sheetimage-actions"></a>
A list of custom actions that are configured for an image.
*Required*: No
*Type*: Array of [ImageCustomAction](aws-properties-quicksight-analysis-imagecustomaction.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageContentAltText`  <a name="cfn-quicksight-analysis-sheetimage-imagecontentalttext"></a>
The alt text for the image.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-analysis-sheetimage-interactions"></a>
The general image interactions setup for an image.
*Required*: No
*Type*: [ImageInteractionOptions](aws-properties-quicksight-analysis-imageinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scaling`  <a name="cfn-quicksight-analysis-sheetimage-scaling"></a>
Determines how the image is scaled.
*Required*: No
*Type*: [SheetImageScalingConfiguration](aws-properties-quicksight-analysis-sheetimagescalingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetImageId`  <a name="cfn-quicksight-analysis-sheetimage-sheetimageid"></a>
The ID of the sheet image.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-analysis-sheetimage-source"></a>
The source of the image.
*Required*: Yes
*Type*: [SheetImageSource](aws-properties-quicksight-analysis-sheetimagesource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tooltip`  <a name="cfn-quicksight-analysis-sheetimage-tooltip"></a>
The tooltip to be shown when hovering over the image.
*Required*: No
*Type*: [SheetImageTooltipConfiguration](aws-properties-quicksight-analysis-sheetimagetooltipconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
