---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-analysistemplate-syntheticdatacolumnproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate SyntheticDataColumnProperties
<a name="aws-properties-cleanrooms-analysistemplate-syntheticdatacolumnproperties"></a>

Properties that define how a specific data column should be handled during synthetic data generation, including its name, type, and role in predictive modeling.

## Syntax
<a name="aws-properties-cleanrooms-analysistemplate-syntheticdatacolumnproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-analysistemplate-syntheticdatacolumnproperties-syntax.json"></a>

```
{
  "[ColumnName](#cfn-cleanrooms-analysistemplate-syntheticdatacolumnproperties-columnname)" : {{String}},
  "[ColumnType](#cfn-cleanrooms-analysistemplate-syntheticdatacolumnproperties-columntype)" : {{String}},
  "[IsPredictiveValue](#cfn-cleanrooms-analysistemplate-syntheticdatacolumnproperties-ispredictivevalue)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cleanrooms-analysistemplate-syntheticdatacolumnproperties-syntax.yaml"></a>

```
  [ColumnName](#cfn-cleanrooms-analysistemplate-syntheticdatacolumnproperties-columnname): {{String}}
  [ColumnType](#cfn-cleanrooms-analysistemplate-syntheticdatacolumnproperties-columntype): {{String}}
  [IsPredictiveValue](#cfn-cleanrooms-analysistemplate-syntheticdatacolumnproperties-ispredictivevalue): {{Boolean}}
```

## Properties
<a name="aws-properties-cleanrooms-analysistemplate-syntheticdatacolumnproperties-properties"></a>

`ColumnName`  <a name="cfn-cleanrooms-analysistemplate-syntheticdatacolumnproperties-columnname"></a>
The name of the data column as it appears in the dataset.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9_](([a-z0-9_]+-)*([a-z0-9_]+))?$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ColumnType`  <a name="cfn-cleanrooms-analysistemplate-syntheticdatacolumnproperties-columntype"></a>
The data type of the column, which determines how the synthetic data generation algorithm processes and synthesizes values for this column.
*Required*: Yes
*Type*: String
*Allowed values*: `CATEGORICAL | NUMERICAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsPredictiveValue`  <a name="cfn-cleanrooms-analysistemplate-syntheticdatacolumnproperties-ispredictivevalue"></a>
Indicates if this column contains predictive values that should be treated as target variables in machine learning models. This affects how the synthetic data generation preserves statistical relationships.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
