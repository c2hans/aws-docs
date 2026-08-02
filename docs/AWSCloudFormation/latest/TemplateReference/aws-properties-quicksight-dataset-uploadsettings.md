---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-uploadsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet UploadSettings
<a name="aws-properties-quicksight-dataset-uploadsettings"></a>

Information about the format for a source file or files.

## Syntax
<a name="aws-properties-quicksight-dataset-uploadsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-uploadsettings-syntax.json"></a>

```
{
  "[ContainsHeader](#cfn-quicksight-dataset-uploadsettings-containsheader)" : {{Boolean}},
  "[Delimiter](#cfn-quicksight-dataset-uploadsettings-delimiter)" : {{String}},
  "[Format](#cfn-quicksight-dataset-uploadsettings-format)" : {{String}},
  "[StartFromRow](#cfn-quicksight-dataset-uploadsettings-startfromrow)" : {{Number}},
  "[TextQualifier](#cfn-quicksight-dataset-uploadsettings-textqualifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-uploadsettings-syntax.yaml"></a>

```
  [ContainsHeader](#cfn-quicksight-dataset-uploadsettings-containsheader): {{Boolean}}
  [Delimiter](#cfn-quicksight-dataset-uploadsettings-delimiter): {{String}}
  [Format](#cfn-quicksight-dataset-uploadsettings-format): {{String}}
  [StartFromRow](#cfn-quicksight-dataset-uploadsettings-startfromrow): {{Number}}
  [TextQualifier](#cfn-quicksight-dataset-uploadsettings-textqualifier): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-uploadsettings-properties"></a>

`ContainsHeader`  <a name="cfn-quicksight-dataset-uploadsettings-containsheader"></a>
Whether the file has a header row, or the files each have a header row.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Delimiter`  <a name="cfn-quicksight-dataset-uploadsettings-delimiter"></a>
The delimiter between values in the file.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-quicksight-dataset-uploadsettings-format"></a>
File format.
*Required*: No
*Type*: String
*Allowed values*: `CSV | TSV | CLF | ELF | XLSX | JSON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartFromRow`  <a name="cfn-quicksight-dataset-uploadsettings-startfromrow"></a>
A row number to start reading data from.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextQualifier`  <a name="cfn-quicksight-dataset-uploadsettings-textqualifier"></a>
Text qualifier.
*Required*: No
*Type*: String
*Allowed values*: `DOUBLE_QUOTE | SINGLE_QUOTE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
