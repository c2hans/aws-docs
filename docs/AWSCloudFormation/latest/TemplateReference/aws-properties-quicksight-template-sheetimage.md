---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-sheetimage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template SheetImage
<a name="aws-properties-quicksight-template-sheetimage"></a>

An image that is located on a sheet.

## Syntax
<a name="aws-properties-quicksight-template-sheetimage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-sheetimage-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-template-sheetimage-actions)" : {{[ ImageCustomAction, ... ]}},
  "[ImageContentAltText](#cfn-quicksight-template-sheetimage-imagecontentalttext)" : {{String}},
  "[Interactions](#cfn-quicksight-template-sheetimage-interactions)" : {{ImageInteractionOptions}},
  "[Scaling](#cfn-quicksight-template-sheetimage-scaling)" : {{SheetImageScalingConfiguration}},
  "[SheetImageId](#cfn-quicksight-template-sheetimage-sheetimageid)" : {{String}},
  "[Source](#cfn-quicksight-template-sheetimage-source)" : {{SheetImageSource}},
  "[Tooltip](#cfn-quicksight-template-sheetimage-tooltip)" : {{SheetImageTooltipConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-sheetimage-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-template-sheetimage-actions): {{
    - ImageCustomAction}}
  [ImageContentAltText](#cfn-quicksight-template-sheetimage-imagecontentalttext): {{String}}
  [Interactions](#cfn-quicksight-template-sheetimage-interactions): {{
    ImageInteractionOptions}}
  [Scaling](#cfn-quicksight-template-sheetimage-scaling): {{
    SheetImageScalingConfiguration}}
  [SheetImageId](#cfn-quicksight-template-sheetimage-sheetimageid): {{String}}
  [Source](#cfn-quicksight-template-sheetimage-source): {{
    SheetImageSource}}
  [Tooltip](#cfn-quicksight-template-sheetimage-tooltip): {{
    SheetImageTooltipConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-sheetimage-properties"></a>

`Actions`  <a name="cfn-quicksight-template-sheetimage-actions"></a>
A list of custom actions that are configured for an image.
*Required*: No
*Type*: Array of [ImageCustomAction](aws-properties-quicksight-template-imagecustomaction.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageContentAltText`  <a name="cfn-quicksight-template-sheetimage-imagecontentalttext"></a>
The alt text for the image.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-template-sheetimage-interactions"></a>
The general image interactions setup for an image.
*Required*: No
*Type*: [ImageInteractionOptions](aws-properties-quicksight-template-imageinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scaling`  <a name="cfn-quicksight-template-sheetimage-scaling"></a>
Determines how the image is scaled.
*Required*: No
*Type*: [SheetImageScalingConfiguration](aws-properties-quicksight-template-sheetimagescalingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetImageId`  <a name="cfn-quicksight-template-sheetimage-sheetimageid"></a>
The ID of the sheet image.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-template-sheetimage-source"></a>
The source of the image.
*Required*: Yes
*Type*: [SheetImageSource](aws-properties-quicksight-template-sheetimagesource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tooltip`  <a name="cfn-quicksight-template-sheetimage-tooltip"></a>
The tooltip to be shown when hovering over the image.
*Required*: No
*Type*: [SheetImageTooltipConfiguration](aws-properties-quicksight-template-sheetimagetooltipconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
