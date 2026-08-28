---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-preparsetexttransformation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL PreParseTextTransformation
<a name="aws-properties-wafv2-webacl-preparsetexttransformation"></a>

A pre-parse text transformation that normalizes the raw query string before AWS WAF parses it into individual query arguments. Pre-parse text transformations are only supported when `FieldToMatch` is `SingleQueryArgument` or `AllQueryArguments`.

## Syntax
<a name="aws-properties-wafv2-webacl-preparsetexttransformation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-preparsetexttransformation-syntax.json"></a>

```
{
  "[Priority](#cfn-wafv2-webacl-preparsetexttransformation-priority)" : {{Integer}},
  "[Type](#cfn-wafv2-webacl-preparsetexttransformation-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-preparsetexttransformation-syntax.yaml"></a>

```
  [Priority](#cfn-wafv2-webacl-preparsetexttransformation-priority): {{Integer}}
  [Type](#cfn-wafv2-webacl-preparsetexttransformation-type): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-preparsetexttransformation-properties"></a>

`Priority`  <a name="cfn-wafv2-webacl-preparsetexttransformation-priority"></a>
Sets the relative processing order for the pre-parse text transformations that you define. AWS WAF processes all transformations, from lowest priority value to highest, before inspecting the transformed content.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-wafv2-webacl-preparsetexttransformation-type"></a>
The type of pre-parse text transformation to apply to the raw query string.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | URL_DECODE | URL_DECODE_UNI | COMBINE_DUPLICATE_QUERY_ARGS_BY_COMMA | REPLACE_SEMICOLONS_WITH_AMPERSANDS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
