---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTableAssociation ConfiguredTableAssociationAnalysisRule
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule"></a>

An analysis rule for a configured table association. This analysis rule specifies how data from the table can be used within its associated collaboration. In the console, the `ConfiguredTableAssociationAnalysisRule` is referred to as the *collaboration analysis rule*.

## Syntax
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule-syntax.json"></a>

```
{
  "[Policy](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule-policy)" : {{ConfiguredTableAssociationAnalysisRulePolicy}},
  "[Type](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule-syntax.yaml"></a>

```
  [Policy](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule-policy): {{
    ConfiguredTableAssociationAnalysisRulePolicy}}
  [Type](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule-type): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule-properties"></a>

`Policy`  <a name="cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule-policy"></a>
 The policy of the configured table association analysis rule.
*Required*: Yes
*Type*: [ConfiguredTableAssociationAnalysisRulePolicy](aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule-type"></a>
 The type of the configured table association analysis rule.
*Required*: Yes
*Type*: String
*Allowed values*: `AGGREGATION | LIST | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
