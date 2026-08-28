---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-regexmatchstatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup RegexMatchStatement
<a name="aws-properties-wafv2-rulegroup-regexmatchstatement"></a>

A rule statement used to search web request components for a match against a single regular expression.

## Syntax
<a name="aws-properties-wafv2-rulegroup-regexmatchstatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-regexmatchstatement-syntax.json"></a>

```
{
  "[FieldToMatch](#cfn-wafv2-rulegroup-regexmatchstatement-fieldtomatch)" : {{FieldToMatch}},
  "[PreParseTextTransformations](#cfn-wafv2-rulegroup-regexmatchstatement-preparsetexttransformations)" : {{[ PreParseTextTransformation, ... ]}},
  "[RegexString](#cfn-wafv2-rulegroup-regexmatchstatement-regexstring)" : {{String}},
  "[TextTransformations](#cfn-wafv2-rulegroup-regexmatchstatement-texttransformations)" : {{[ TextTransformation, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-regexmatchstatement-syntax.yaml"></a>

```
  [FieldToMatch](#cfn-wafv2-rulegroup-regexmatchstatement-fieldtomatch): {{
    FieldToMatch}}
  [PreParseTextTransformations](#cfn-wafv2-rulegroup-regexmatchstatement-preparsetexttransformations): {{
    - PreParseTextTransformation}}
  [RegexString](#cfn-wafv2-rulegroup-regexmatchstatement-regexstring): {{
    String}}
  [TextTransformations](#cfn-wafv2-rulegroup-regexmatchstatement-texttransformations): {{
    - TextTransformation}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-regexmatchstatement-properties"></a>

`FieldToMatch`  <a name="cfn-wafv2-rulegroup-regexmatchstatement-fieldtomatch"></a>
The part of the web request that you want AWS WAF to inspect.
*Required*: Yes
*Type*: [FieldToMatch](aws-properties-wafv2-rulegroup-fieldtomatch.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreParseTextTransformations`  <a name="cfn-wafv2-rulegroup-regexmatchstatement-preparsetexttransformations"></a>
Pre-parse text transformations normalize the raw query string before AWS WAF parses it into individual query arguments. They are applied before the standard text transformations. Pre-parse text transformations are only supported when `FieldToMatch` is `SingleQueryArgument` or `AllQueryArguments`. You can specify up to 10 pre-parse text transformations per rule statement.
*Required*: No
*Type*: Array of [PreParseTextTransformation](aws-properties-wafv2-rulegroup-preparsetexttransformation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegexString`  <a name="cfn-wafv2-rulegroup-regexmatchstatement-regexstring"></a>
The string representing the regular expression. AWS WAF enforces a quota on the maximum number of characters in a regex pattern. For the current limit, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the *AWS WAF Developer Guide*.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextTransformations`  <a name="cfn-wafv2-rulegroup-regexmatchstatement-texttransformations"></a>
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by `FieldToMatch`, starting from the lowest priority setting, before inspecting the content for a match.
*Required*: Yes
*Type*: Array of [TextTransformation](aws-properties-wafv2-rulegroup-texttransformation.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
