---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-imagestaticfile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ImageStaticFile
<a name="aws-properties-quicksight-dashboard-imagestaticfile"></a>

A static file that contains an image.

## Syntax
<a name="aws-properties-quicksight-dashboard-imagestaticfile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-imagestaticfile-syntax.json"></a>

```
{
  "[Source](#cfn-quicksight-dashboard-imagestaticfile-source)" : {{StaticFileSource}},
  "[StaticFileId](#cfn-quicksight-dashboard-imagestaticfile-staticfileid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-imagestaticfile-syntax.yaml"></a>

```
  [Source](#cfn-quicksight-dashboard-imagestaticfile-source): {{
    StaticFileSource}}
  [StaticFileId](#cfn-quicksight-dashboard-imagestaticfile-staticfileid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-imagestaticfile-properties"></a>

`Source`  <a name="cfn-quicksight-dashboard-imagestaticfile-source"></a>
The source of the image static file.
*Required*: No
*Type*: [StaticFileSource](aws-properties-quicksight-dashboard-staticfilesource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticFileId`  <a name="cfn-quicksight-dashboard-imagestaticfile-staticfileid"></a>
The ID of the static file that contains an image.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
