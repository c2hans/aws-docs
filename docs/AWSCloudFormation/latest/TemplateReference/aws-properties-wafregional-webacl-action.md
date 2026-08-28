---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafregional-webacl-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFRegional::WebACL Action
<a name="aws-properties-wafregional-webacl-action"></a>

Specifies the action AWS WAF takes when a web request matches or doesn't match all rule conditions.

## Syntax
<a name="aws-properties-wafregional-webacl-action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafregional-webacl-action-syntax.json"></a>

```
{
  "[Type](#cfn-wafregional-webacl-action-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafregional-webacl-action-syntax.yaml"></a>

```
  [Type](#cfn-wafregional-webacl-action-type): {{String}}
```

## Properties
<a name="aws-properties-wafregional-webacl-action-properties"></a>

`Type`  <a name="cfn-wafregional-webacl-action-type"></a>
For actions that are associated with a rule, the action that AWS WAF takes when a web request matches all conditions in a rule.
For the default action of a web access control list (ACL), the action that AWS WAF takes when a web request doesn't match all conditions in any rule.
Valid settings include the following:
+ `ALLOW`: AWS WAF allows requests
+ `BLOCK`: AWS WAF blocks requests
+ `COUNT`: AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify `COUNT` for the default action for a WebACL.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
