---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-rollingdateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template RollingDateConfiguration
<a name="aws-properties-quicksight-template-rollingdateconfiguration"></a>

The rolling date configuration of a date time filter.

## Syntax
<a name="aws-properties-quicksight-template-rollingdateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-rollingdateconfiguration-syntax.json"></a>

```
{
  "[DataSetIdentifier](#cfn-quicksight-template-rollingdateconfiguration-datasetidentifier)" : {{String}},
  "[Expression](#cfn-quicksight-template-rollingdateconfiguration-expression)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-rollingdateconfiguration-syntax.yaml"></a>

```
  [DataSetIdentifier](#cfn-quicksight-template-rollingdateconfiguration-datasetidentifier): {{String}}
  [Expression](#cfn-quicksight-template-rollingdateconfiguration-expression): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-rollingdateconfiguration-properties"></a>

`DataSetIdentifier`  <a name="cfn-quicksight-template-rollingdateconfiguration-datasetidentifier"></a>
The data set that is used in the rolling date configuration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expression`  <a name="cfn-quicksight-template-rollingdateconfiguration-expression"></a>
The expression of the rolling date configuration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
