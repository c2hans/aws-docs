---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-job-columnselector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Job ColumnSelector
<a name="aws-properties-databrew-job-columnselector"></a>

Selector of a column from a dataset for profile job configuration. One selector includes either a column name or a regular expression.

## Syntax
<a name="aws-properties-databrew-job-columnselector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-job-columnselector-syntax.json"></a>

```
{
  "[Name](#cfn-databrew-job-columnselector-name)" : {{String}},
  "[Regex](#cfn-databrew-job-columnselector-regex)" : {{String}}
}
```

### YAML
<a name="aws-properties-databrew-job-columnselector-syntax.yaml"></a>

```
  [Name](#cfn-databrew-job-columnselector-name): {{String}}
  [Regex](#cfn-databrew-job-columnselector-regex): {{String}}
```

## Properties
<a name="aws-properties-databrew-job-columnselector-properties"></a>

`Name`  <a name="cfn-databrew-job-columnselector-name"></a>
The name of a column from a dataset.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regex`  <a name="cfn-databrew-job-columnselector-regex"></a>
A regular expression for selecting a column from a dataset.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
