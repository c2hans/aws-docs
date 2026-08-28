---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-analysistemplate-mlsyntheticdataparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate MLSyntheticDataParameters
<a name="aws-properties-cleanrooms-analysistemplate-mlsyntheticdataparameters"></a>

Parameters that control the generation of synthetic data for machine learning, including privacy settings and column classification details.

## Syntax
<a name="aws-properties-cleanrooms-analysistemplate-mlsyntheticdataparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-analysistemplate-mlsyntheticdataparameters-syntax.json"></a>

```
{
  "[ColumnClassification](#cfn-cleanrooms-analysistemplate-mlsyntheticdataparameters-columnclassification)" : {{ColumnClassificationDetails}},
  "[Epsilon](#cfn-cleanrooms-analysistemplate-mlsyntheticdataparameters-epsilon)" : {{Number}},
  "[MaxMembershipInferenceAttackScore](#cfn-cleanrooms-analysistemplate-mlsyntheticdataparameters-maxmembershipinferenceattackscore)" : {{Number}}
}
```

### YAML
<a name="aws-properties-cleanrooms-analysistemplate-mlsyntheticdataparameters-syntax.yaml"></a>

```
  [ColumnClassification](#cfn-cleanrooms-analysistemplate-mlsyntheticdataparameters-columnclassification): {{
    ColumnClassificationDetails}}
  [Epsilon](#cfn-cleanrooms-analysistemplate-mlsyntheticdataparameters-epsilon): {{Number}}
  [MaxMembershipInferenceAttackScore](#cfn-cleanrooms-analysistemplate-mlsyntheticdataparameters-maxmembershipinferenceattackscore): {{Number}}
```

## Properties
<a name="aws-properties-cleanrooms-analysistemplate-mlsyntheticdataparameters-properties"></a>

`ColumnClassification`  <a name="cfn-cleanrooms-analysistemplate-mlsyntheticdataparameters-columnclassification"></a>
Classification details for data columns that specify how each column should be treated during synthetic data generation.
*Required*: Yes
*Type*: [ColumnClassificationDetails](aws-properties-cleanrooms-analysistemplate-columnclassificationdetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Epsilon`  <a name="cfn-cleanrooms-analysistemplate-mlsyntheticdataparameters-epsilon"></a>
The epsilon value for differential privacy when generating synthetic data. Lower values provide stronger privacy guarantees but may reduce data utility.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxMembershipInferenceAttackScore`  <a name="cfn-cleanrooms-analysistemplate-mlsyntheticdataparameters-maxmembershipinferenceattackscore"></a>
The maximum acceptable score for membership inference attack vulnerability. Synthetic data generation fails if the score for the resulting data exceeds this threshold.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
