---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-rowlevelpermissionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet RowLevelPermissionConfiguration
<a name="aws-properties-quicksight-dataset-rowlevelpermissionconfiguration"></a>

Configuration for row level security.

## Syntax
<a name="aws-properties-quicksight-dataset-rowlevelpermissionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-rowlevelpermissionconfiguration-syntax.json"></a>

```
{
  "[RowLevelPermissionDataSet](#cfn-quicksight-dataset-rowlevelpermissionconfiguration-rowlevelpermissiondataset)" : {{RowLevelPermissionDataSet}},
  "[TagConfiguration](#cfn-quicksight-dataset-rowlevelpermissionconfiguration-tagconfiguration)" : {{RowLevelPermissionTagConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-rowlevelpermissionconfiguration-syntax.yaml"></a>

```
  [RowLevelPermissionDataSet](#cfn-quicksight-dataset-rowlevelpermissionconfiguration-rowlevelpermissiondataset): {{
    RowLevelPermissionDataSet}}
  [TagConfiguration](#cfn-quicksight-dataset-rowlevelpermissionconfiguration-tagconfiguration): {{
    RowLevelPermissionTagConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dataset-rowlevelpermissionconfiguration-properties"></a>

`RowLevelPermissionDataSet`  <a name="cfn-quicksight-dataset-rowlevelpermissionconfiguration-rowlevelpermissiondataset"></a>
Property description not available.
*Required*: No
*Type*: [RowLevelPermissionDataSet](aws-properties-quicksight-dataset-rowlevelpermissiondataset.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagConfiguration`  <a name="cfn-quicksight-dataset-rowlevelpermissionconfiguration-tagconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [RowLevelPermissionTagConfiguration](aws-properties-quicksight-dataset-rowlevelpermissiontagconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
