---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-rowlevelpermissiontagconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet RowLevelPermissionTagConfiguration
<a name="aws-properties-quicksight-dataset-rowlevelpermissiontagconfiguration"></a>

The element you can use to define tags for row-level security.

## Syntax
<a name="aws-properties-quicksight-dataset-rowlevelpermissiontagconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-rowlevelpermissiontagconfiguration-syntax.json"></a>

```
{
  "[Status](#cfn-quicksight-dataset-rowlevelpermissiontagconfiguration-status)" : {{String}},
  "[TagRuleConfigurations](#cfn-quicksight-dataset-rowlevelpermissiontagconfiguration-tagruleconfigurations)" : {{[ [ , ... ], ... ]}},
  "[TagRules](#cfn-quicksight-dataset-rowlevelpermissiontagconfiguration-tagrules)" : {{[ RowLevelPermissionTagRule, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-rowlevelpermissiontagconfiguration-syntax.yaml"></a>

```
  [Status](#cfn-quicksight-dataset-rowlevelpermissiontagconfiguration-status): {{String}}
  [TagRuleConfigurations](#cfn-quicksight-dataset-rowlevelpermissiontagconfiguration-tagruleconfigurations): {{
    -
    - }}
  [TagRules](#cfn-quicksight-dataset-rowlevelpermissiontagconfiguration-tagrules): {{
    - RowLevelPermissionTagRule}}
```

## Properties
<a name="aws-properties-quicksight-dataset-rowlevelpermissiontagconfiguration-properties"></a>

`Status`  <a name="cfn-quicksight-dataset-rowlevelpermissiontagconfiguration-status"></a>
The status of row-level security tags. If enabled, the status is `ENABLED`. If disabled, the status is `DISABLED`.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagRuleConfigurations`  <a name="cfn-quicksight-dataset-rowlevelpermissiontagconfiguration-tagruleconfigurations"></a>
The configuration of tags on a dataset to set row-level security.
*Required*: No
*Type*: Array of Array
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagRules`  <a name="cfn-quicksight-dataset-rowlevelpermissiontagconfiguration-tagrules"></a>
A set of rules associated with row-level security, such as the tag names and columns that they are assigned to.
*Required*: Yes
*Type*: Array of [RowLevelPermissionTagRule](aws-properties-quicksight-dataset-rowlevelpermissiontagrule.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
