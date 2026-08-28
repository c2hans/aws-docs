---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-rowalternatecoloroptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis RowAlternateColorOptions
<a name="aws-properties-quicksight-analysis-rowalternatecoloroptions"></a>

Determines the row alternate color options.

## Syntax
<a name="aws-properties-quicksight-analysis-rowalternatecoloroptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-rowalternatecoloroptions-syntax.json"></a>

```
{
  "[RowAlternateColors](#cfn-quicksight-analysis-rowalternatecoloroptions-rowalternatecolors)" : {{[ String, ... ]}},
  "[Status](#cfn-quicksight-analysis-rowalternatecoloroptions-status)" : {{String}},
  "[UsePrimaryBackgroundColor](#cfn-quicksight-analysis-rowalternatecoloroptions-useprimarybackgroundcolor)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-rowalternatecoloroptions-syntax.yaml"></a>

```
  [RowAlternateColors](#cfn-quicksight-analysis-rowalternatecoloroptions-rowalternatecolors): {{
    - String}}
  [Status](#cfn-quicksight-analysis-rowalternatecoloroptions-status): {{String}}
  [UsePrimaryBackgroundColor](#cfn-quicksight-analysis-rowalternatecoloroptions-useprimarybackgroundcolor): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-rowalternatecoloroptions-properties"></a>

`RowAlternateColors`  <a name="cfn-quicksight-analysis-rowalternatecoloroptions-rowalternatecolors"></a>
Determines the list of row alternate colors.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-quicksight-analysis-rowalternatecoloroptions-status"></a>
Determines the widget status.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UsePrimaryBackgroundColor`  <a name="cfn-quicksight-analysis-rowalternatecoloroptions-useprimarybackgroundcolor"></a>
The primary background color options for alternate rows.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
