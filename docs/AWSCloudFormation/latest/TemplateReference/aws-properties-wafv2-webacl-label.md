---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-label.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL Label
<a name="aws-properties-wafv2-webacl-label"></a>

A single label container. This is used as an element of a label array in `RuleLabels` inside a rule.

## Syntax
<a name="aws-properties-wafv2-webacl-label-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-label-syntax.json"></a>

```
{
  "[Name](#cfn-wafv2-webacl-label-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-label-syntax.yaml"></a>

```
  [Name](#cfn-wafv2-webacl-label-name): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-label-properties"></a>

`Name`  <a name="cfn-wafv2-webacl-label-name"></a>
The label string.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z_:-]{1,1024}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
