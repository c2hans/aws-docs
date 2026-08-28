---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-classifier-csvclassifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Classifier CsvClassifier
<a name="aws-properties-glue-classifier-csvclassifier"></a>

A classifier for custom `CSV` content.

## Syntax
<a name="aws-properties-glue-classifier-csvclassifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-classifier-csvclassifier-syntax.json"></a>

```
{
  "[AllowSingleColumn](#cfn-glue-classifier-csvclassifier-allowsinglecolumn)" : {{Boolean}},
  "[ContainsCustomDatatype](#cfn-glue-classifier-csvclassifier-containscustomdatatype)" : {{[ String, ... ]}},
  "[ContainsHeader](#cfn-glue-classifier-csvclassifier-containsheader)" : {{String}},
  "[CustomDatatypeConfigured](#cfn-glue-classifier-csvclassifier-customdatatypeconfigured)" : {{Boolean}},
  "[Delimiter](#cfn-glue-classifier-csvclassifier-delimiter)" : {{String}},
  "[DisableValueTrimming](#cfn-glue-classifier-csvclassifier-disablevaluetrimming)" : {{Boolean}},
  "[Header](#cfn-glue-classifier-csvclassifier-header)" : {{[ String, ... ]}},
  "[Name](#cfn-glue-classifier-csvclassifier-name)" : {{String}},
  "[QuoteSymbol](#cfn-glue-classifier-csvclassifier-quotesymbol)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-classifier-csvclassifier-syntax.yaml"></a>

```
  [AllowSingleColumn](#cfn-glue-classifier-csvclassifier-allowsinglecolumn): {{Boolean}}
  [ContainsCustomDatatype](#cfn-glue-classifier-csvclassifier-containscustomdatatype): {{
    - String}}
  [ContainsHeader](#cfn-glue-classifier-csvclassifier-containsheader): {{String}}
  [CustomDatatypeConfigured](#cfn-glue-classifier-csvclassifier-customdatatypeconfigured): {{Boolean}}
  [Delimiter](#cfn-glue-classifier-csvclassifier-delimiter): {{String}}
  [DisableValueTrimming](#cfn-glue-classifier-csvclassifier-disablevaluetrimming): {{Boolean}}
  [Header](#cfn-glue-classifier-csvclassifier-header): {{
    - String}}
  [Name](#cfn-glue-classifier-csvclassifier-name): {{String}}
  [QuoteSymbol](#cfn-glue-classifier-csvclassifier-quotesymbol): {{String}}
```

## Properties
<a name="aws-properties-glue-classifier-csvclassifier-properties"></a>

`AllowSingleColumn`  <a name="cfn-glue-classifier-csvclassifier-allowsinglecolumn"></a>
Enables the processing of files that contain only one column.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainsCustomDatatype`  <a name="cfn-glue-classifier-csvclassifier-containscustomdatatype"></a>
Indicates whether the CSV file contains custom data types.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainsHeader`  <a name="cfn-glue-classifier-csvclassifier-containsheader"></a>
Indicates whether the CSV file contains a header.
A value of `UNKNOWN` specifies that the classifier will detect whether the CSV file contains headings.
A value of `PRESENT` specifies that the CSV file contains headings.
A value of `ABSENT` specifies that the CSV file does not contain headings.
*Required*: No
*Type*: String
*Allowed values*: `UNKNOWN | PRESENT | ABSENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomDatatypeConfigured`  <a name="cfn-glue-classifier-csvclassifier-customdatatypeconfigured"></a>
Enables the configuration of custom data types.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Delimiter`  <a name="cfn-glue-classifier-csvclassifier-delimiter"></a>
A custom symbol to denote what separates each column entry in the row.
*Required*: No
*Type*: String
*Pattern*: `[^\r\n]`
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisableValueTrimming`  <a name="cfn-glue-classifier-csvclassifier-disablevaluetrimming"></a>
Specifies not to trim values before identifying the type of column values. The default value is `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Header`  <a name="cfn-glue-classifier-csvclassifier-header"></a>
A list of strings representing column names.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-glue-classifier-csvclassifier-name"></a>
The name of the classifier.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QuoteSymbol`  <a name="cfn-glue-classifier-csvclassifier-quotesymbol"></a>
A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.
*Required*: No
*Type*: String
*Pattern*: `[^\r\n]`
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-glue-classifier-csvclassifier--examples"></a>

### Create a custom classifier test
<a name="aws-properties-glue-classifier-csvclassifier--examples--Create_a_custom_classifier_test"></a>

With `AWS::Glue::Classifier` you can create a custom classifier test.

#### JSON
<a name="aws-properties-glue-classifier-csvclassifier--examples--Create_a_custom_classifier_test--json"></a>

```
{
    "Description": "AWS Glue custom classifier test",
    "Resources": {
        "MyCSVclassifier": {
            "Type": "AWS::Glue::Classifier",
            "Properties": {
                "CsvClassifier": {
                    "AllowSingleColumn": true,
                    "ContainsHeader": "PRESENT",
                    "Delimiter": ",",
                    "Header": [
                        "id",
                        "name"
                    ],
                    "Name": "csvclassify",
                    "QuoteSymbol": "\""
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-properties-glue-classifier-csvclassifier--examples--Create_a_custom_classifier_test--yaml"></a>

```
Description: AWS Glue custom classifier test
Resources:
  MyCSVclassifier:
    Type: 'AWS::Glue::Classifier'
    Properties:
      CsvClassifier:
        AllowSingleColumn: true
        ContainsHeader: PRESENT
        Delimiter: ','
        Header:
          - id
          - name
        Name: csvclassify
        QuoteSymbol: '"'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
