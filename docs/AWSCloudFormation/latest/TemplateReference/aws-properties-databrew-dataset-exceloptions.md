---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-dataset-exceloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Dataset ExcelOptions
<a name="aws-properties-databrew-dataset-exceloptions"></a>

Represents a set of options that define how DataBrew will interpret a Microsoft Excel file when creating a dataset from that file.

## Syntax
<a name="aws-properties-databrew-dataset-exceloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-dataset-exceloptions-syntax.json"></a>

```
{
  "[HeaderRow](#cfn-databrew-dataset-exceloptions-headerrow)" : {{Boolean}},
  "[SheetIndexes](#cfn-databrew-dataset-exceloptions-sheetindexes)" : {{[ Integer, ... ]}},
  "[SheetNames](#cfn-databrew-dataset-exceloptions-sheetnames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-databrew-dataset-exceloptions-syntax.yaml"></a>

```
  [HeaderRow](#cfn-databrew-dataset-exceloptions-headerrow): {{Boolean}}
  [SheetIndexes](#cfn-databrew-dataset-exceloptions-sheetindexes): {{
    - Integer}}
  [SheetNames](#cfn-databrew-dataset-exceloptions-sheetnames): {{
    - String}}
```

## Properties
<a name="aws-properties-databrew-dataset-exceloptions-properties"></a>

`HeaderRow`  <a name="cfn-databrew-dataset-exceloptions-headerrow"></a>
A variable that specifies whether the first row in the file is parsed as the header. If this value is false, column names are auto-generated.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetIndexes`  <a name="cfn-databrew-dataset-exceloptions-sheetindexes"></a>
One or more sheet numbers in the Excel file that will be included in the dataset.
*Required*: No
*Type*: Array of Integer
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetNames`  <a name="cfn-databrew-dataset-exceloptions-sheetnames"></a>
One or more named sheets in the Excel file that will be included in the dataset.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
