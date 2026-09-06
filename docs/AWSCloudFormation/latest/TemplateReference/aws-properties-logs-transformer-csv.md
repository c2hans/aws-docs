---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-csv.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer Csv
<a name="aws-properties-logs-transformer-csv"></a>

The `CSV` processor parses comma-separated values (CSV) from the log events into columns.

For more information about this processor including examples, see [ csv](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-csv) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-csv-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-csv-syntax.json"></a>

```
{
  "[Columns](#cfn-logs-transformer-csv-columns)" : {{[ String, ... ]}},
  "[Delimiter](#cfn-logs-transformer-csv-delimiter)" : {{String}},
  "[QuoteCharacter](#cfn-logs-transformer-csv-quotecharacter)" : {{String}},
  "[Source](#cfn-logs-transformer-csv-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-csv-syntax.yaml"></a>

```
  [Columns](#cfn-logs-transformer-csv-columns): {{
    - String}}
  [Delimiter](#cfn-logs-transformer-csv-delimiter): {{String}}
  [QuoteCharacter](#cfn-logs-transformer-csv-quotecharacter): {{String}}
  [Source](#cfn-logs-transformer-csv-source): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-csv-properties"></a>

`Columns`  <a name="cfn-logs-transformer-csv-columns"></a>
An array of names to use for the columns in the transformed log event.
If you omit this, default column names (`[column_1, column_2 ...]`) are used.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Delimiter`  <a name="cfn-logs-transformer-csv-delimiter"></a>
The character used to separate each column in the original comma-separated value log event. If you omit this, the processor looks for the comma `,` character as the delimiter.
*Required*: No
*Type*: String
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QuoteCharacter`  <a name="cfn-logs-transformer-csv-quotecharacter"></a>
The character used used as a text qualifier for a single column of data. If you omit this, the double quotation mark `"` character is used.
*Required*: No
*Type*: String
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-logs-transformer-csv-source"></a>
The path to the field in the log event that has the comma separated values to be parsed. If you omit this value, the whole log message is processed.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
