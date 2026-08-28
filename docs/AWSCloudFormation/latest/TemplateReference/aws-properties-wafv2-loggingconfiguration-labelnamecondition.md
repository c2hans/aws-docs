---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-loggingconfiguration-labelnamecondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::LoggingConfiguration LabelNameCondition
<a name="aws-properties-wafv2-loggingconfiguration-labelnamecondition"></a>

A single label name condition for a condition in a logging filter.

## Syntax
<a name="aws-properties-wafv2-loggingconfiguration-labelnamecondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-loggingconfiguration-labelnamecondition-syntax.json"></a>

```
{
  "[LabelName](#cfn-wafv2-loggingconfiguration-labelnamecondition-labelname)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-loggingconfiguration-labelnamecondition-syntax.yaml"></a>

```
  [LabelName](#cfn-wafv2-loggingconfiguration-labelnamecondition-labelname): {{String}}
```

## Properties
<a name="aws-properties-wafv2-loggingconfiguration-labelnamecondition-properties"></a>

`LabelName`  <a name="cfn-wafv2-loggingconfiguration-labelnamecondition-labelname"></a>
The label name that a log record must contain in order to meet the condition. This must be a fully qualified label name. Fully qualified labels have a prefix, optional namespaces, and label name. The prefix identifies the rule group or web ACL context of the rule that added the label.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z_\-:]+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
