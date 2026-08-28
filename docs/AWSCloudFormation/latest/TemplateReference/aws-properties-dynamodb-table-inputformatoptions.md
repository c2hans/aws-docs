---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-inputformatoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Table InputFormatOptions
<a name="aws-properties-dynamodb-table-inputformatoptions"></a>

 The format options for the data that was imported into the target table. There is one value, CsvOption.

## Syntax
<a name="aws-properties-dynamodb-table-inputformatoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-table-inputformatoptions-syntax.json"></a>

```
{
  "[Csv](#cfn-dynamodb-table-inputformatoptions-csv)" : {{Csv}}
}
```

### YAML
<a name="aws-properties-dynamodb-table-inputformatoptions-syntax.yaml"></a>

```
  [Csv](#cfn-dynamodb-table-inputformatoptions-csv): {{
    Csv}}
```

## Properties
<a name="aws-properties-dynamodb-table-inputformatoptions-properties"></a>

`Csv`  <a name="cfn-dynamodb-table-inputformatoptions-csv"></a>
 The options for imported source files in CSV format. The values are Delimiter and HeaderList.
*Required*: No
*Type*: [Csv](aws-properties-dynamodb-table-csv.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
