---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-dashboardsourcetemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DashboardSourceTemplate
<a name="aws-properties-quicksight-dashboard-dashboardsourcetemplate"></a>

Dashboard source template.

## Syntax
<a name="aws-properties-quicksight-dashboard-dashboardsourcetemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-dashboardsourcetemplate-syntax.json"></a>

```
{
  "[Arn](#cfn-quicksight-dashboard-dashboardsourcetemplate-arn)" : {{String}},
  "[DataSetReferences](#cfn-quicksight-dashboard-dashboardsourcetemplate-datasetreferences)" : {{[ DataSetReference, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-dashboardsourcetemplate-syntax.yaml"></a>

```
  [Arn](#cfn-quicksight-dashboard-dashboardsourcetemplate-arn): {{String}}
  [DataSetReferences](#cfn-quicksight-dashboard-dashboardsourcetemplate-datasetreferences): {{
    - DataSetReference}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-dashboardsourcetemplate-properties"></a>

`Arn`  <a name="cfn-quicksight-dashboard-dashboardsourcetemplate-arn"></a>
The Amazon Resource Name (ARN) of the resource.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetReferences`  <a name="cfn-quicksight-dashboard-dashboardsourcetemplate-datasetreferences"></a>
Dataset references.
*Required*: Yes
*Type*: Array of [DataSetReference](aws-properties-quicksight-dashboard-datasetreference.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
