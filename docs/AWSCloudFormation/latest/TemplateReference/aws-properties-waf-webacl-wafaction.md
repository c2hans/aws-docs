---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-waf-webacl-wafaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAF::WebACL WafAction
<a name="aws-properties-waf-webacl-wafaction"></a>

**Note**
AWS WAF Classic support will end on September 30, 2025.
This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
**For the latest version of AWS WAF**, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

For the action that is associated with a rule in a `WebACL`, specifies the action that you want AWS WAF to perform when a web request matches all of the conditions in a rule. For the default action in a `WebACL`, specifies the action that you want AWS WAF to take when a web request doesn't match all of the conditions in any of the rules in a `WebACL`.

## Syntax
<a name="aws-properties-waf-webacl-wafaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-waf-webacl-wafaction-syntax.json"></a>

```
{
  "[Type](#cfn-waf-webacl-wafaction-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-waf-webacl-wafaction-syntax.yaml"></a>

```
  [Type](#cfn-waf-webacl-wafaction-type): {{String}}
```

## Properties
<a name="aws-properties-waf-webacl-wafaction-properties"></a>

`Type`  <a name="cfn-waf-webacl-wafaction-type"></a>
Specifies how you want AWS WAF to respond to requests that match the settings in a `Rule`. Valid settings include the following:
+ `ALLOW`: AWS WAF allows requests
+ `BLOCK`: AWS WAF blocks requests
+ `COUNT`: AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify `COUNT` for the default action for a `WebACL`.
*Required*: Yes
*Type*: String
*Allowed values*: `BLOCK | ALLOW | COUNT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
