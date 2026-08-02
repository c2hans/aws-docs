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
