---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-multiplevaluessetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot MultipleValuesSetting
<a name="aws-properties-lex-bot-multiplevaluessetting"></a>

Indicates whether a slot can return multiple values.

## Syntax
<a name="aws-properties-lex-bot-multiplevaluessetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-multiplevaluessetting-syntax.json"></a>

```
{
  "[AllowMultipleValues](#cfn-lex-bot-multiplevaluessetting-allowmultiplevalues)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-lex-bot-multiplevaluessetting-syntax.yaml"></a>

```
  [AllowMultipleValues](#cfn-lex-bot-multiplevaluessetting-allowmultiplevalues): {{Boolean}}
```

## Properties
<a name="aws-properties-lex-bot-multiplevaluessetting-properties"></a>

`AllowMultipleValues`  <a name="cfn-lex-bot-multiplevaluessetting-allowmultiplevalues"></a>
Indicates whether a slot can return multiple values. When `true`, the slot may return more than one value in a response. When `false`, the slot returns only a single value.
Multi-value slots are only available in the en-US locale. If you set this value to `true` in any other locale, Amazon Lex throws a `ValidationException`.
If the `allowMutlipleValues` is not set, the default value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
