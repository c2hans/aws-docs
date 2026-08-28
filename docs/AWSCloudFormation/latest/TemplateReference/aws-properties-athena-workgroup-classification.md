---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-classification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::WorkGroup Classification
<a name="aws-properties-athena-workgroup-classification"></a>

A classification refers to a set of specific configurations.

## Syntax
<a name="aws-properties-athena-workgroup-classification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-workgroup-classification-syntax.json"></a>

```
{
  "[Name](#cfn-athena-workgroup-classification-name)" : {{String}},
  "[Properties](#cfn-athena-workgroup-classification-properties)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-athena-workgroup-classification-syntax.yaml"></a>

```
  [Name](#cfn-athena-workgroup-classification-name): {{String}}
  [Properties](#cfn-athena-workgroup-classification-properties): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-athena-workgroup-classification-properties"></a>

`Name`  <a name="cfn-athena-workgroup-classification-name"></a>
The name of the configuration classification.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-athena-workgroup-classification-properties"></a>
A set of properties specified within a configuration classification.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
