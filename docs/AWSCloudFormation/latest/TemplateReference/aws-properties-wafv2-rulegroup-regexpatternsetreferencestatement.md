---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup RegexPatternSetReferenceStatement
<a name="aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement"></a>

A rule statement used to search web request components for matches with regular expressions. To use this, create a [AWS::WAFv2::RegexPatternSet](aws-resource-wafv2-regexpatternset.md) that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set.

Each regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.

## Syntax
<a name="aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement-syntax.json"></a>

```
{
  "[Arn](#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-arn)" : {{String}},
  "[FieldToMatch](#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-fieldtomatch)" : {{FieldToMatch}},
  "[PreParseTextTransformations](#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-preparsetexttransformations)" : {{[ PreParseTextTransformation, ... ]}},
  "[TextTransformations](#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-texttransformations)" : {{[ TextTransformation, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement-syntax.yaml"></a>

```
  [Arn](#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-arn): {{String}}
  [FieldToMatch](#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-fieldtomatch): {{
    FieldToMatch}}
  [PreParseTextTransformations](#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-preparsetexttransformations): {{
    - PreParseTextTransformation}}
  [TextTransformations](#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-texttransformations): {{
    - TextTransformation}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement-properties"></a>

`Arn`  <a name="cfn-wafv2-rulegroup-regexpatternsetreferencestatement-arn"></a>
The Amazon Resource Name (ARN) of the [AWS::WAFv2::RegexPatternSet](aws-resource-wafv2-regexpatternset.md) that this statement references.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldToMatch`  <a name="cfn-wafv2-rulegroup-regexpatternsetreferencestatement-fieldtomatch"></a>
The part of the web request that you want AWS WAF to inspect.
*Required*: Yes
*Type*: [FieldToMatch](aws-properties-wafv2-rulegroup-fieldtomatch.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreParseTextTransformations`  <a name="cfn-wafv2-rulegroup-regexpatternsetreferencestatement-preparsetexttransformations"></a>
Pre-parse text transformations normalize the raw query string before AWS WAF parses it into individual query arguments. They are applied before the standard text transformations. Pre-parse text transformations are only supported when `FieldToMatch` is `SingleQueryArgument` or `AllQueryArguments`. You can specify up to 10 pre-parse text transformations per rule statement.
*Required*: No
*Type*: Array of [PreParseTextTransformation](aws-properties-wafv2-rulegroup-preparsetexttransformation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextTransformations`  <a name="cfn-wafv2-rulegroup-regexpatternsetreferencestatement-texttransformations"></a>
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by `FieldToMatch`, starting from the lowest priority setting, before inspecting the content for a match.
*Required*: Yes
*Type*: Array of [TextTransformation](aws-properties-wafv2-rulegroup-texttransformation.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
