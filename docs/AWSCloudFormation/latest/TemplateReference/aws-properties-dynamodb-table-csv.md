---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-csv.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Table Csv
<a name="aws-properties-dynamodb-table-csv"></a>

 The options for imported source files in CSV format. The values are Delimiter and HeaderList.

## Syntax
<a name="aws-properties-dynamodb-table-csv-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-table-csv-syntax.json"></a>

```
{
  "[Delimiter](#cfn-dynamodb-table-csv-delimiter)" : {{String}},
  "[HeaderList](#cfn-dynamodb-table-csv-headerlist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-dynamodb-table-csv-syntax.yaml"></a>

```
  [Delimiter](#cfn-dynamodb-table-csv-delimiter): {{String}}
  [HeaderList](#cfn-dynamodb-table-csv-headerlist): {{
    - String}}
```

## Properties
<a name="aws-properties-dynamodb-table-csv-properties"></a>

`Delimiter`  <a name="cfn-dynamodb-table-csv-delimiter"></a>
 The delimiter used for separating items in the CSV file being imported.
*Required*: No
*Type*: String
*Pattern*: `[,;:|\t ]`
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HeaderList`  <a name="cfn-dynamodb-table-csv-headerlist"></a>
 List of the headers used to specify a common header for all source CSV files being imported. If this field is specified then the first line of each CSV file is treated as data instead of the header. If this field is not specified the the first line of each CSV file is treated as the header.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
