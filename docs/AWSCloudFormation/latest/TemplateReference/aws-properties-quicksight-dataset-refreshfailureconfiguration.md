---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-refreshfailureconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet RefreshFailureConfiguration
<a name="aws-properties-quicksight-dataset-refreshfailureconfiguration"></a>

The failure configuration of a dataset.

## Syntax
<a name="aws-properties-quicksight-dataset-refreshfailureconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-refreshfailureconfiguration-syntax.json"></a>

```
{
  "[EmailAlert](#cfn-quicksight-dataset-refreshfailureconfiguration-emailalert)" : {{RefreshFailureEmailAlert}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-refreshfailureconfiguration-syntax.yaml"></a>

```
  [EmailAlert](#cfn-quicksight-dataset-refreshfailureconfiguration-emailalert): {{
    RefreshFailureEmailAlert}}
```

## Properties
<a name="aws-properties-quicksight-dataset-refreshfailureconfiguration-properties"></a>

`EmailAlert`  <a name="cfn-quicksight-dataset-refreshfailureconfiguration-emailalert"></a>
The email alert configuration for a dataset refresh failure.
*Required*: No
*Type*: [RefreshFailureEmailAlert](aws-properties-quicksight-dataset-refreshfailureemailalert.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
