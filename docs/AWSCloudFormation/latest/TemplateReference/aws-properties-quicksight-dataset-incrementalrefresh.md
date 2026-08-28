---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-incrementalrefresh.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet IncrementalRefresh
<a name="aws-properties-quicksight-dataset-incrementalrefresh"></a>

The incremental refresh configuration for a dataset.

## Syntax
<a name="aws-properties-quicksight-dataset-incrementalrefresh-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-incrementalrefresh-syntax.json"></a>

```
{
  "[LookbackWindow](#cfn-quicksight-dataset-incrementalrefresh-lookbackwindow)" : {{LookbackWindow}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-incrementalrefresh-syntax.yaml"></a>

```
  [LookbackWindow](#cfn-quicksight-dataset-incrementalrefresh-lookbackwindow): {{
    LookbackWindow}}
```

## Properties
<a name="aws-properties-quicksight-dataset-incrementalrefresh-properties"></a>

`LookbackWindow`  <a name="cfn-quicksight-dataset-incrementalrefresh-lookbackwindow"></a>
The lookback window setup for an incremental refresh configuration.
*Required*: Yes
*Type*: [LookbackWindow](aws-properties-quicksight-dataset-lookbackwindow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
