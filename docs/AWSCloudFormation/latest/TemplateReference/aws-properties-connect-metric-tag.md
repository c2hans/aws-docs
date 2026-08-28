---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-metric-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Metric Tag
<a name="aws-properties-connect-metric-tag"></a>

<a name="aws-properties-connect-metric-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::Connect::Metric](aws-resource-connect-metric.md).

## Syntax
<a name="aws-properties-connect-metric-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-metric-tag-syntax.json"></a>

```
{
  "[Key](#cfn-connect-metric-tag-key)" : {{String}},
  "[Value](#cfn-connect-metric-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-metric-tag-syntax.yaml"></a>

```
  [Key](#cfn-connect-metric-tag-key): {{String}}
  [Value](#cfn-connect-metric-tag-value): {{String}}
```

## Properties
<a name="aws-properties-connect-metric-tag-properties"></a>

`Key`  <a name="cfn-connect-metric-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-connect-metric-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
