---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTableAssociation ConfiguredTableAssociationAnalysisRulePolicy
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy"></a>

 Controls on the query specifications that can be run on an associated configured table.

## Syntax
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy-syntax.json"></a>

```
{
  "[V1](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy-v1)" : {{ConfiguredTableAssociationAnalysisRulePolicyV1}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy-syntax.yaml"></a>

```
  [V1](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy-v1): {{
    ConfiguredTableAssociationAnalysisRulePolicyV1}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy-properties"></a>

`V1`  <a name="cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy-v1"></a>
 The policy for the configured table association analysis rule.
*Required*: Yes
*Type*: [ConfiguredTableAssociationAnalysisRulePolicyV1](aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
