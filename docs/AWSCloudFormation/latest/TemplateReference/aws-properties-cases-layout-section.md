---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-layout-section.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Layout Section
<a name="aws-properties-cases-layout-section"></a>

This represents a sections within a panel or tab of the page layout.

## Syntax
<a name="aws-properties-cases-layout-section-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-layout-section-syntax.json"></a>

```
{
  "[FieldGroup](#cfn-cases-layout-section-fieldgroup)" : {{FieldGroup}}
}
```

### YAML
<a name="aws-properties-cases-layout-section-syntax.yaml"></a>

```
  [FieldGroup](#cfn-cases-layout-section-fieldgroup): {{
    FieldGroup}}
```

## Properties
<a name="aws-properties-cases-layout-section-properties"></a>

`FieldGroup`  <a name="cfn-cases-layout-section-fieldgroup"></a>
Consists of a group of fields and associated properties.
*Required*: Yes
*Type*: [FieldGroup](aws-properties-cases-layout-fieldgroup.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
