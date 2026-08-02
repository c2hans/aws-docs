---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-customcontentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template CustomContentConfiguration
<a name="aws-properties-quicksight-template-customcontentconfiguration"></a>

The configuration of a `CustomContentVisual`.

## Syntax
<a name="aws-properties-quicksight-template-customcontentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-customcontentconfiguration-syntax.json"></a>

```
{
  "[ContentType](#cfn-quicksight-template-customcontentconfiguration-contenttype)" : {{String}},
  "[ContentUrl](#cfn-quicksight-template-customcontentconfiguration-contenturl)" : {{String}},
  "[ImageScaling](#cfn-quicksight-template-customcontentconfiguration-imagescaling)" : {{String}},
  "[Interactions](#cfn-quicksight-template-customcontentconfiguration-interactions)" : {{VisualInteractionOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-customcontentconfiguration-syntax.yaml"></a>

```
  [ContentType](#cfn-quicksight-template-customcontentconfiguration-contenttype): {{String}}
  [ContentUrl](#cfn-quicksight-template-customcontentconfiguration-contenturl): {{String}}
  [ImageScaling](#cfn-quicksight-template-customcontentconfiguration-imagescaling): {{String}}
  [Interactions](#cfn-quicksight-template-customcontentconfiguration-interactions): {{
    VisualInteractionOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-customcontentconfiguration-properties"></a>

`ContentType`  <a name="cfn-quicksight-template-customcontentconfiguration-contenttype"></a>
The content type of the custom content visual. You can use this to have the visual render as an image.
*Required*: No
*Type*: String
*Allowed values*: `IMAGE | OTHER_EMBEDDED_CONTENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentUrl`  <a name="cfn-quicksight-template-customcontentconfiguration-contenturl"></a>
The input URL that links to the custom content that you want in the custom visual.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageScaling`  <a name="cfn-quicksight-template-customcontentconfiguration-imagescaling"></a>
The sizing options for the size of the custom content visual. This structure is required when the `ContentType` of the visual is `'IMAGE'`.
*Required*: No
*Type*: String
*Allowed values*: `FIT_TO_HEIGHT | FIT_TO_WIDTH | DO_NOT_SCALE | SCALE_TO_VISUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-template-customcontentconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-template-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
