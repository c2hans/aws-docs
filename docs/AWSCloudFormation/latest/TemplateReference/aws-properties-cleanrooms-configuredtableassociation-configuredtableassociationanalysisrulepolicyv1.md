---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTableAssociation ConfiguredTableAssociationAnalysisRulePolicyV1
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1"></a>

 Controls on the query specifications that can be run on an associated configured table.

## Syntax
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-syntax.json"></a>

```
{
  "[Aggregation](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-aggregation)" : {{ConfiguredTableAssociationAnalysisRuleAggregation}},
  "[Custom](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-custom)" : {{ConfiguredTableAssociationAnalysisRuleCustom}},
  "[List](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-list)" : {{ConfiguredTableAssociationAnalysisRuleList}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-syntax.yaml"></a>

```
  [Aggregation](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-aggregation): {{
    ConfiguredTableAssociationAnalysisRuleAggregation}}
  [Custom](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-custom): {{
    ConfiguredTableAssociationAnalysisRuleCustom}}
  [List](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-list): {{
    ConfiguredTableAssociationAnalysisRuleList}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-properties"></a>

`Aggregation`  <a name="cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-aggregation"></a>
 Analysis rule type that enables only aggregation queries on a configured table.
*Required*: No
*Type*: [ConfiguredTableAssociationAnalysisRuleAggregation](aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Custom`  <a name="cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-custom"></a>
 Analysis rule type that enables the table owner to approve custom SQL queries on their configured tables. It supports differential privacy.
*Required*: No
*Type*: [ConfiguredTableAssociationAnalysisRuleCustom](aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulecustom.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`List`  <a name="cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-list"></a>
 Analysis rule type that enables only list queries on a configured table.
*Required*: No
*Type*: [ConfiguredTableAssociationAnalysisRuleList](aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulelist.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
