---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-case-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Case Tag
<a name="aws-properties-cases-case-tag"></a>

<a name="aws-properties-cases-case-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::Cases::Case](aws-resource-cases-case.md).

## Syntax
<a name="aws-properties-cases-case-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-case-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cases-case-tag-key)" : {{String}},
  "[Value](#cfn-cases-case-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cases-case-tag-syntax.yaml"></a>

```
  [Key](#cfn-cases-case-tag-key): {{String}}
  [Value](#cfn-cases-case-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cases-case-tag-properties"></a>

`Key`  <a name="cfn-cases-case-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?![aA][wW][sS]:)[a-zA-Z0-9 _.:/=+\-@]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cases-case-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9 _.:/=+\-@]*)$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
