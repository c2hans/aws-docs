---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-compositefilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 CompositeFilter
<a name="aws-properties-securityhub-automationrulev2-compositefilter"></a>

Enables the creation of filtering criteria for security findings.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-compositefilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-compositefilter-syntax.json"></a>

```
{
  "[BooleanFilters](#cfn-securityhub-automationrulev2-compositefilter-booleanfilters)" : {{[ OcsfBooleanFilter, ... ]}},
  "[DateFilters](#cfn-securityhub-automationrulev2-compositefilter-datefilters)" : {{[ OcsfDateFilter, ... ]}},
  "[MapFilters](#cfn-securityhub-automationrulev2-compositefilter-mapfilters)" : {{[ OcsfMapFilter, ... ]}},
  "[NumberFilters](#cfn-securityhub-automationrulev2-compositefilter-numberfilters)" : {{[ OcsfNumberFilter, ... ]}},
  "[Operator](#cfn-securityhub-automationrulev2-compositefilter-operator)" : {{String}},
  "[StringFilters](#cfn-securityhub-automationrulev2-compositefilter-stringfilters)" : {{[ OcsfStringFilter, ... ]}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-compositefilter-syntax.yaml"></a>

```
  [BooleanFilters](#cfn-securityhub-automationrulev2-compositefilter-booleanfilters): {{
    - OcsfBooleanFilter}}
  [DateFilters](#cfn-securityhub-automationrulev2-compositefilter-datefilters): {{
    - OcsfDateFilter}}
  [MapFilters](#cfn-securityhub-automationrulev2-compositefilter-mapfilters): {{
    - OcsfMapFilter}}
  [NumberFilters](#cfn-securityhub-automationrulev2-compositefilter-numberfilters): {{
    - OcsfNumberFilter}}
  [Operator](#cfn-securityhub-automationrulev2-compositefilter-operator): {{String}}
  [StringFilters](#cfn-securityhub-automationrulev2-compositefilter-stringfilters): {{
    - OcsfStringFilter}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-compositefilter-properties"></a>

`BooleanFilters`  <a name="cfn-securityhub-automationrulev2-compositefilter-booleanfilters"></a>
Enables filtering based on boolean field values.
*Required*: No
*Type*: Array of [OcsfBooleanFilter](aws-properties-securityhub-automationrulev2-ocsfbooleanfilter.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DateFilters`  <a name="cfn-securityhub-automationrulev2-compositefilter-datefilters"></a>
Enables filtering based on date and timestamp fields.
*Required*: No
*Type*: Array of [OcsfDateFilter](aws-properties-securityhub-automationrulev2-ocsfdatefilter.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MapFilters`  <a name="cfn-securityhub-automationrulev2-compositefilter-mapfilters"></a>
Enables the creation of filtering criteria for security findings.
*Required*: No
*Type*: Array of [OcsfMapFilter](aws-properties-securityhub-automationrulev2-ocsfmapfilter.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberFilters`  <a name="cfn-securityhub-automationrulev2-compositefilter-numberfilters"></a>
Enables filtering based on numerical field values.
*Required*: No
*Type*: Array of [OcsfNumberFilter](aws-properties-securityhub-automationrulev2-ocsfnumberfilter.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-securityhub-automationrulev2-compositefilter-operator"></a>
The logical operator used to combine multiple filter conditions.
*Required*: No
*Type*: String
*Allowed values*: `AND | OR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringFilters`  <a name="cfn-securityhub-automationrulev2-compositefilter-stringfilters"></a>
Enables filtering based on string field values.
*Required*: No
*Type*: Array of [OcsfStringFilter](aws-properties-securityhub-automationrulev2-ocsfstringfilter.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
