---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-applicationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL ApplicationConfig
<a name="aws-properties-wafv2-webacl-applicationconfig"></a>

A list of `ApplicationAttribute`s that contains information about the application.

## Syntax
<a name="aws-properties-wafv2-webacl-applicationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-applicationconfig-syntax.json"></a>

```
{
  "[Attributes](#cfn-wafv2-webacl-applicationconfig-attributes)" : {{[ ApplicationAttribute, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-applicationconfig-syntax.yaml"></a>

```
  [Attributes](#cfn-wafv2-webacl-applicationconfig-attributes): {{
    - ApplicationAttribute}}
```

## Properties
<a name="aws-properties-wafv2-webacl-applicationconfig-properties"></a>

`Attributes`  <a name="cfn-wafv2-webacl-applicationconfig-attributes"></a>
Contains the attribute name and a list of values for that attribute.
*Required*: Yes
*Type*: Array of [ApplicationAttribute](aws-properties-wafv2-webacl-applicationattribute.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
