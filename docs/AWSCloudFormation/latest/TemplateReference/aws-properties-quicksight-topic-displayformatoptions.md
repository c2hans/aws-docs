---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-displayformatoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic DisplayFormatOptions
<a name="aws-properties-quicksight-topic-displayformatoptions"></a>

A structure that represents additional options for display formatting.

## Syntax
<a name="aws-properties-quicksight-topic-displayformatoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-displayformatoptions-syntax.json"></a>

```
{
  "[BlankCellFormat](#cfn-quicksight-topic-displayformatoptions-blankcellformat)" : {{String}},
  "[CurrencySymbol](#cfn-quicksight-topic-displayformatoptions-currencysymbol)" : {{String}},
  "[DateFormat](#cfn-quicksight-topic-displayformatoptions-dateformat)" : {{String}},
  "[DecimalSeparator](#cfn-quicksight-topic-displayformatoptions-decimalseparator)" : {{String}},
  "[FractionDigits](#cfn-quicksight-topic-displayformatoptions-fractiondigits)" : {{Number}},
  "[GroupingSeparator](#cfn-quicksight-topic-displayformatoptions-groupingseparator)" : {{String}},
  "[NegativeFormat](#cfn-quicksight-topic-displayformatoptions-negativeformat)" : {{NegativeFormat}},
  "[Prefix](#cfn-quicksight-topic-displayformatoptions-prefix)" : {{String}},
  "[Suffix](#cfn-quicksight-topic-displayformatoptions-suffix)" : {{String}},
  "[UnitScaler](#cfn-quicksight-topic-displayformatoptions-unitscaler)" : {{String}},
  "[UseBlankCellFormat](#cfn-quicksight-topic-displayformatoptions-useblankcellformat)" : {{Boolean}},
  "[UseGrouping](#cfn-quicksight-topic-displayformatoptions-usegrouping)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-displayformatoptions-syntax.yaml"></a>

```
  [BlankCellFormat](#cfn-quicksight-topic-displayformatoptions-blankcellformat): {{String}}
  [CurrencySymbol](#cfn-quicksight-topic-displayformatoptions-currencysymbol): {{String}}
  [DateFormat](#cfn-quicksight-topic-displayformatoptions-dateformat): {{String}}
  [DecimalSeparator](#cfn-quicksight-topic-displayformatoptions-decimalseparator): {{String}}
  [FractionDigits](#cfn-quicksight-topic-displayformatoptions-fractiondigits): {{Number}}
  [GroupingSeparator](#cfn-quicksight-topic-displayformatoptions-groupingseparator): {{String}}
  [NegativeFormat](#cfn-quicksight-topic-displayformatoptions-negativeformat): {{
    NegativeFormat}}
  [Prefix](#cfn-quicksight-topic-displayformatoptions-prefix): {{String}}
  [Suffix](#cfn-quicksight-topic-displayformatoptions-suffix): {{String}}
  [UnitScaler](#cfn-quicksight-topic-displayformatoptions-unitscaler): {{String}}
  [UseBlankCellFormat](#cfn-quicksight-topic-displayformatoptions-useblankcellformat): {{Boolean}}
  [UseGrouping](#cfn-quicksight-topic-displayformatoptions-usegrouping): {{Boolean}}
```

## Properties
<a name="aws-properties-quicksight-topic-displayformatoptions-properties"></a>

`BlankCellFormat`  <a name="cfn-quicksight-topic-displayformatoptions-blankcellformat"></a>
Determines the blank cell format.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CurrencySymbol`  <a name="cfn-quicksight-topic-displayformatoptions-currencysymbol"></a>
The currency symbol, such as `USD`.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DateFormat`  <a name="cfn-quicksight-topic-displayformatoptions-dateformat"></a>
Determines the `DateTime` format.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DecimalSeparator`  <a name="cfn-quicksight-topic-displayformatoptions-decimalseparator"></a>
Determines the decimal separator.
*Required*: No
*Type*: String
*Allowed values*: `COMMA | DOT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FractionDigits`  <a name="cfn-quicksight-topic-displayformatoptions-fractiondigits"></a>
Determines the number of fraction digits.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupingSeparator`  <a name="cfn-quicksight-topic-displayformatoptions-groupingseparator"></a>
Determines the grouping separator.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NegativeFormat`  <a name="cfn-quicksight-topic-displayformatoptions-negativeformat"></a>
The negative format.
*Required*: No
*Type*: [NegativeFormat](aws-properties-quicksight-topic-negativeformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-quicksight-topic-displayformatoptions-prefix"></a>
The prefix value for a display format.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Suffix`  <a name="cfn-quicksight-topic-displayformatoptions-suffix"></a>
The suffix value for a display format.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnitScaler`  <a name="cfn-quicksight-topic-displayformatoptions-unitscaler"></a>
The unit scaler. Valid values for this structure are: `NONE`, `AUTO`, `THOUSANDS`, `MILLIONS`, `BILLIONS`, and `TRILLIONS`.
*Required*: No
*Type*: String
*Allowed values*: `NONE | AUTO | THOUSANDS | MILLIONS | BILLIONS | TRILLIONS | LAKHS | CRORES`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseBlankCellFormat`  <a name="cfn-quicksight-topic-displayformatoptions-useblankcellformat"></a>
A Boolean value that indicates whether to use blank cell format.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseGrouping`  <a name="cfn-quicksight-topic-displayformatoptions-usegrouping"></a>
A Boolean value that indicates whether to use grouping.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
