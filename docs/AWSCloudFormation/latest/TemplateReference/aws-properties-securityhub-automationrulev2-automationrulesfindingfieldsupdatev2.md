---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 AutomationRulesFindingFieldsUpdateV2
<a name="aws-properties-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2"></a>

Allows you to define the structure for modifying specific fields in security findings.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2-syntax.json"></a>

```
{
  "[Comment](#cfn-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2-comment)" : {{String}},
  "[SeverityId](#cfn-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2-severityid)" : {{Integer}},
  "[StatusId](#cfn-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2-statusid)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2-syntax.yaml"></a>

```
  [Comment](#cfn-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2-comment): {{String}}
  [SeverityId](#cfn-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2-severityid): {{Integer}}
  [StatusId](#cfn-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2-statusid): {{Integer}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2-properties"></a>

`Comment`  <a name="cfn-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2-comment"></a>
Notes or contextual information for findings that are modified by the automation rule.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SeverityId`  <a name="cfn-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2-severityid"></a>
The severity level to be assigned to findings that match the automation rule criteria.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusId`  <a name="cfn-securityhub-automationrulev2-automationrulesfindingfieldsupdatev2-statusid"></a>
The status to be applied to findings that match automation rule criteria.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
