---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrule-numberfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRule NumberFilter
<a name="aws-properties-securityhub-automationrule-numberfilter"></a>

A number filter for querying findings.

## Syntax
<a name="aws-properties-securityhub-automationrule-numberfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrule-numberfilter-syntax.json"></a>

```
{
  "[Eq](#cfn-securityhub-automationrule-numberfilter-eq)" : {{Number}},
  "[Gte](#cfn-securityhub-automationrule-numberfilter-gte)" : {{Number}},
  "[Lte](#cfn-securityhub-automationrule-numberfilter-lte)" : {{Number}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrule-numberfilter-syntax.yaml"></a>

```
  [Eq](#cfn-securityhub-automationrule-numberfilter-eq): {{Number}}
  [Gte](#cfn-securityhub-automationrule-numberfilter-gte): {{Number}}
  [Lte](#cfn-securityhub-automationrule-numberfilter-lte): {{Number}}
```

## Properties
<a name="aws-properties-securityhub-automationrule-numberfilter-properties"></a>

`Eq`  <a name="cfn-securityhub-automationrule-numberfilter-eq"></a>
The equal-to condition to be applied to a single field when querying for findings.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Gte`  <a name="cfn-securityhub-automationrule-numberfilter-gte"></a>
The greater-than-equal condition to be applied to a single field when querying for findings.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lte`  <a name="cfn-securityhub-automationrule-numberfilter-lte"></a>
The less-than-equal condition to be applied to a single field when querying for findings.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
