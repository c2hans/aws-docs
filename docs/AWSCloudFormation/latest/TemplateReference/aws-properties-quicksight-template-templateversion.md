---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-templateversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TemplateVersion
<a name="aws-properties-quicksight-template-templateversion"></a>

A version of a template.

## Syntax
<a name="aws-properties-quicksight-template-templateversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-templateversion-syntax.json"></a>

```
{
  "[CreatedTime](#cfn-quicksight-template-templateversion-createdtime)" : {{String}},
  "[DataSetConfigurations](#cfn-quicksight-template-templateversion-datasetconfigurations)" : {{[ DataSetConfiguration, ... ]}},
  "[Description](#cfn-quicksight-template-templateversion-description)" : {{String}},
  "[Errors](#cfn-quicksight-template-templateversion-errors)" : {{[ TemplateError, ... ]}},
  "[Sheets](#cfn-quicksight-template-templateversion-sheets)" : {{[ Sheet, ... ]}},
  "[SourceEntityArn](#cfn-quicksight-template-templateversion-sourceentityarn)" : {{String}},
  "[Status](#cfn-quicksight-template-templateversion-status)" : {{String}},
  "[ThemeArn](#cfn-quicksight-template-templateversion-themearn)" : {{String}},
  "[VersionNumber](#cfn-quicksight-template-templateversion-versionnumber)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-template-templateversion-syntax.yaml"></a>

```
  [CreatedTime](#cfn-quicksight-template-templateversion-createdtime): {{String}}
  [DataSetConfigurations](#cfn-quicksight-template-templateversion-datasetconfigurations): {{
    - DataSetConfiguration}}
  [Description](#cfn-quicksight-template-templateversion-description): {{String}}
  [Errors](#cfn-quicksight-template-templateversion-errors): {{
    - TemplateError}}
  [Sheets](#cfn-quicksight-template-templateversion-sheets): {{
    - Sheet}}
  [SourceEntityArn](#cfn-quicksight-template-templateversion-sourceentityarn): {{String}}
  [Status](#cfn-quicksight-template-templateversion-status): {{String}}
  [ThemeArn](#cfn-quicksight-template-templateversion-themearn): {{String}}
  [VersionNumber](#cfn-quicksight-template-templateversion-versionnumber): {{
    Number}}
```

## Properties
<a name="aws-properties-quicksight-template-templateversion-properties"></a>

`CreatedTime`  <a name="cfn-quicksight-template-templateversion-createdtime"></a>
The time that this template version was created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetConfigurations`  <a name="cfn-quicksight-template-templateversion-datasetconfigurations"></a>
Schema of the dataset identified by the placeholder. Any dashboard created from this template should be bound to new datasets matching the same schema described through this API operation.
*Required*: No
*Type*: Array of [DataSetConfiguration](aws-properties-quicksight-template-datasetconfiguration.md)
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-quicksight-template-templateversion-description"></a>
The description of the template.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Errors`  <a name="cfn-quicksight-template-templateversion-errors"></a>
Errors associated with this template version.
*Required*: No
*Type*: Array of [TemplateError](aws-properties-quicksight-template-templateerror.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sheets`  <a name="cfn-quicksight-template-templateversion-sheets"></a>
A list of the associated sheets with the unique identifier and name of each sheet.
*Required*: No
*Type*: Array of [Sheet](aws-properties-quicksight-template-sheet.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceEntityArn`  <a name="cfn-quicksight-template-templateversion-sourceentityarn"></a>
The Amazon Resource Name (ARN) of an analysis or template that was used to create this template.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-quicksight-template-templateversion-status"></a>
The status that is associated with the template.
+  `CREATION_IN_PROGRESS`
+  `CREATION_SUCCESSFUL`
+  `CREATION_FAILED`
+  `UPDATE_IN_PROGRESS`
+  `UPDATE_SUCCESSFUL`
+  `UPDATE_FAILED`
+  `DELETED`
*Required*: No
*Type*: String
*Allowed values*: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | PENDING_UPDATE | DELETED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThemeArn`  <a name="cfn-quicksight-template-templateversion-themearn"></a>
The ARN of the theme associated with this version of the template.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionNumber`  <a name="cfn-quicksight-template-templateversion-versionnumber"></a>
The version number of the template version.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
