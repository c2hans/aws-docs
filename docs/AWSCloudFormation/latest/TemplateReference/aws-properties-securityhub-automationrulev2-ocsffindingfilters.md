---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-automationrulev2-ocsffindingfilters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::AutomationRuleV2 OcsfFindingFilters
<a name="aws-properties-securityhub-automationrulev2-ocsffindingfilters"></a>

Specifies the filtering criteria for security findings using OCSF.

## Syntax
<a name="aws-properties-securityhub-automationrulev2-ocsffindingfilters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-automationrulev2-ocsffindingfilters-syntax.json"></a>

```
{
  "[CompositeFilters](#cfn-securityhub-automationrulev2-ocsffindingfilters-compositefilters)" : {{[ CompositeFilter, ... ]}},
  "[CompositeOperator](#cfn-securityhub-automationrulev2-ocsffindingfilters-compositeoperator)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-automationrulev2-ocsffindingfilters-syntax.yaml"></a>

```
  [CompositeFilters](#cfn-securityhub-automationrulev2-ocsffindingfilters-compositefilters): {{
    - CompositeFilter}}
  [CompositeOperator](#cfn-securityhub-automationrulev2-ocsffindingfilters-compositeoperator): {{String}}
```

## Properties
<a name="aws-properties-securityhub-automationrulev2-ocsffindingfilters-properties"></a>

`CompositeFilters`  <a name="cfn-securityhub-automationrulev2-ocsffindingfilters-compositefilters"></a>
Enables the creation of complex filtering conditions by combining filter criteria.
*Required*: No
*Type*: Array of [CompositeFilter](aws-properties-securityhub-automationrulev2-compositefilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CompositeOperator`  <a name="cfn-securityhub-automationrulev2-ocsffindingfilters-compositeoperator"></a>
The logical operators used to combine the filtering on multiple `CompositeFilters`.
*Required*: No
*Type*: String
*Allowed values*: `AND | OR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
