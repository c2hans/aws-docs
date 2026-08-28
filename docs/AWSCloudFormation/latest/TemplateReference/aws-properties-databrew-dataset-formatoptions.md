---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-dataset-formatoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Dataset FormatOptions
<a name="aws-properties-databrew-dataset-formatoptions"></a>

Represents a set of options that define the structure of either comma-separated value (CSV), Excel, or JSON input.

## Syntax
<a name="aws-properties-databrew-dataset-formatoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-dataset-formatoptions-syntax.json"></a>

```
{
  "[Csv](#cfn-databrew-dataset-formatoptions-csv)" : {{CsvOptions}},
  "[Excel](#cfn-databrew-dataset-formatoptions-excel)" : {{ExcelOptions}},
  "[Json](#cfn-databrew-dataset-formatoptions-json)" : {{JsonOptions}}
}
```

### YAML
<a name="aws-properties-databrew-dataset-formatoptions-syntax.yaml"></a>

```
  [Csv](#cfn-databrew-dataset-formatoptions-csv): {{
    CsvOptions}}
  [Excel](#cfn-databrew-dataset-formatoptions-excel): {{
    ExcelOptions}}
  [Json](#cfn-databrew-dataset-formatoptions-json): {{
    JsonOptions}}
```

## Properties
<a name="aws-properties-databrew-dataset-formatoptions-properties"></a>

`Csv`  <a name="cfn-databrew-dataset-formatoptions-csv"></a>
Options that define how CSV input is to be interpreted by DataBrew.
*Required*: No
*Type*: [CsvOptions](aws-properties-databrew-dataset-csvoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Excel`  <a name="cfn-databrew-dataset-formatoptions-excel"></a>
Options that define how Excel input is to be interpreted by DataBrew.
*Required*: No
*Type*: [ExcelOptions](aws-properties-databrew-dataset-exceloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Json`  <a name="cfn-databrew-dataset-formatoptions-json"></a>
Options that define how JSON input is to be interpreted by DataBrew.
*Required*: No
*Type*: [JsonOptions](aws-properties-databrew-dataset-jsonoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
