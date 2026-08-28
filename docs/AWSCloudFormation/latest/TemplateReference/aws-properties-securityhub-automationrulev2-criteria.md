---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-criteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 Criteria
<a name="aws-properties-securityhub-automationrulev2-criteria"></a>

The filtering type and configuration of the automation rule.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-criteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-criteria-syntax.json"></a>

```
{
  "[OcsfFindingCriteria](#cfn-securityhub-automationrulev2-criteria-ocsffindingcriteria)" : {{OcsfFindingFilters}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-criteria-syntax.yaml"></a>

```
  [OcsfFindingCriteria](#cfn-securityhub-automationrulev2-criteria-ocsffindingcriteria): {{
    OcsfFindingFilters}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-criteria-properties"></a>

`OcsfFindingCriteria`  <a name="cfn-securityhub-automationrulev2-criteria-ocsffindingcriteria"></a>
The filtering conditions that align with OCSF standards.
*Required*: No
*Type*: [OcsfFindingFilters](aws-properties-securityhub-automationrulev2-ocsffindingfilters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
