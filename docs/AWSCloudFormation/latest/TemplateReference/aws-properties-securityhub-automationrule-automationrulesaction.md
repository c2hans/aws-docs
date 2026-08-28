---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrule-automationrulesaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRule AutomationRulesAction
<a name="aws-properties-securityhub-automationrule-automationrulesaction"></a>

 One or more actions that AWS Security Hub CSPM takes when a finding matches the defined criteria of a rule.

## Syntax
<a name="aws-properties-securityhub-automationrule-automationrulesaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrule-automationrulesaction-syntax.json"></a>

```
{
  "[FindingFieldsUpdate](#cfn-securityhub-automationrule-automationrulesaction-findingfieldsupdate)" : {{AutomationRulesFindingFieldsUpdate}},
  "[Type](#cfn-securityhub-automationrule-automationrulesaction-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrule-automationrulesaction-syntax.yaml"></a>

```
  [FindingFieldsUpdate](#cfn-securityhub-automationrule-automationrulesaction-findingfieldsupdate): {{
    AutomationRulesFindingFieldsUpdate}}
  [Type](#cfn-securityhub-automationrule-automationrulesaction-type): {{String}}
```

## Properties
<a name="aws-properties-securityhub-automationrule-automationrulesaction-properties"></a>

`FindingFieldsUpdate`  <a name="cfn-securityhub-automationrule-automationrulesaction-findingfieldsupdate"></a>
 Specifies that the automation rule action is an update to a finding field.
*Required*: Yes
*Type*: [AutomationRulesFindingFieldsUpdate](aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-securityhub-automationrule-automationrulesaction-type"></a>
 Specifies the type of action that Security Hub CSPM takes when a finding matches the defined criteria of a rule.
*Required*: Yes
*Type*: String
*Allowed values*: `FINDING_FIELDS_UPDATE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
