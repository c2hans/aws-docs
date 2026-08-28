---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-newdefaultvalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet NewDefaultValues
<a name="aws-properties-quicksight-dataset-newdefaultvalues"></a>

The new default values for the parameter.

## Syntax
<a name="aws-properties-quicksight-dataset-newdefaultvalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-newdefaultvalues-syntax.json"></a>

```
{
  "[DateTimeStaticValues](#cfn-quicksight-dataset-newdefaultvalues-datetimestaticvalues)" : {{[ String, ... ]}},
  "[DecimalStaticValues](#cfn-quicksight-dataset-newdefaultvalues-decimalstaticvalues)" : {{[ Number, ... ]}},
  "[IntegerStaticValues](#cfn-quicksight-dataset-newdefaultvalues-integerstaticvalues)" : {{[ Integer, ... ]}},
  "[StringStaticValues](#cfn-quicksight-dataset-newdefaultvalues-stringstaticvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-newdefaultvalues-syntax.yaml"></a>

```
  [DateTimeStaticValues](#cfn-quicksight-dataset-newdefaultvalues-datetimestaticvalues): {{
    - String}}
  [DecimalStaticValues](#cfn-quicksight-dataset-newdefaultvalues-decimalstaticvalues): {{
    - Number}}
  [IntegerStaticValues](#cfn-quicksight-dataset-newdefaultvalues-integerstaticvalues): {{
    - Integer}}
  [StringStaticValues](#cfn-quicksight-dataset-newdefaultvalues-stringstaticvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-newdefaultvalues-properties"></a>

`DateTimeStaticValues`  <a name="cfn-quicksight-dataset-newdefaultvalues-datetimestaticvalues"></a>
A list of static default values for a given date time parameter. The valid format for this property is `yyyy-MM-dd’T’HH:mm:ss’Z’`.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DecimalStaticValues`  <a name="cfn-quicksight-dataset-newdefaultvalues-decimalstaticvalues"></a>
A list of static default values for a given decimal parameter.
*Required*: No
*Type*: Array of Number
*Minimum*: `0`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegerStaticValues`  <a name="cfn-quicksight-dataset-newdefaultvalues-integerstaticvalues"></a>
A list of static default values for a given integer parameter.
*Required*: No
*Type*: Array of Integer
*Minimum*: `0`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringStaticValues`  <a name="cfn-quicksight-dataset-newdefaultvalues-stringstaticvalues"></a>
A list of static default values for a given string parameter.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `512 | 32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
