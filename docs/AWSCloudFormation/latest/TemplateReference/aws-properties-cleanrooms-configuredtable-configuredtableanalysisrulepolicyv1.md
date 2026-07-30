---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable ConfiguredTableAnalysisRulePolicyV1
<a name="aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1"></a>

Controls on the query specifications that can be run on a configured table.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-syntax.json"></a>

```
{
  "[Aggregation](#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-aggregation)" : {{AnalysisRuleAggregation}},
  "[Custom](#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-custom)" : {{AnalysisRuleCustom}},
  "[List](#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-list)" : {{AnalysisRuleList}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-syntax.yaml"></a>

```
  [Aggregation](#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-aggregation): {{
    AnalysisRuleAggregation}}
  [Custom](#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-custom): {{
    AnalysisRuleCustom}}
  [List](#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-list): {{
    AnalysisRuleList}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-properties"></a>

`Aggregation`  <a name="cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-aggregation"></a>
Analysis rule type that enables only aggregation queries on a configured table.
*Required*: No
*Type*: [AnalysisRuleAggregation](aws-properties-cleanrooms-configuredtable-analysisruleaggregation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Custom`  <a name="cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-custom"></a>
Analysis rule type that enables custom SQL queries on a configured table.
*Required*: No
*Type*: [AnalysisRuleCustom](aws-properties-cleanrooms-configuredtable-analysisrulecustom.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`List`  <a name="cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-list"></a>
Analysis rule type that enables only list queries on a configured table.
*Required*: No
*Type*: [AnalysisRuleList](aws-properties-cleanrooms-configuredtable-analysisrulelist.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
