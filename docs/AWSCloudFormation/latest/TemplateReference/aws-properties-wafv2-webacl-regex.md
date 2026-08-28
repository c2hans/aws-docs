---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-regex.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL Regex
<a name="aws-properties-wafv2-webacl-regex"></a>

A single regular expression. This is used in a [AWS::WAFv2::RegexPatternSet](aws-resource-wafv2-regexpatternset.md) and also in the configuration for the AWS Managed Rules rule group `AWSManagedRulesAntiDDoSRuleSet`.

## Syntax
<a name="aws-properties-wafv2-webacl-regex-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-regex-syntax.json"></a>

```
{
  "[RegexString](#cfn-wafv2-webacl-regex-regexstring)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-regex-syntax.yaml"></a>

```
  [RegexString](#cfn-wafv2-webacl-regex-regexstring): {{
    String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-regex-properties"></a>

`RegexString`  <a name="cfn-wafv2-webacl-regex-regexstring"></a>
The string representing the regular expression. AWS WAF enforces a quota on the maximum number of characters in a regex pattern. For the current limit, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the *AWS WAF Developer Guide*.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
