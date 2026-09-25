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
  "[DataSetReferences](#cfn-quicksight-dashboard-dashboardsourcetemplate-datasetreferences)" : {{[ DataSetReference, ... ]}},
  "[TopicReferences](#cfn-quicksight-dashboard-dashboardsourcetemplate-topicreferences)" : {{[ TopicReference, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-dashboardsourcetemplate-syntax.yaml"></a>

```
  [Arn](#cfn-quicksight-dashboard-dashboardsourcetemplate-arn): {{String}}
  [DataSetReferences](#cfn-quicksight-dashboard-dashboardsourcetemplate-datasetreferences): {{
    - DataSetReference}}
  [TopicReferences](#cfn-quicksight-dashboard-dashboardsourcetemplate-topicreferences): {{
    - TopicReference}}
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
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicReferences`  <a name="cfn-quicksight-dashboard-dashboardsourcetemplate-topicreferences"></a>
The topic references for the source template of a dashboard.
*Required*: No
*Type*: Array of [TopicReference](aws-properties-quicksight-dashboard-topicreference.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
