---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-countaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup CountAction
<a name="aws-properties-wafv2-rulegroup-countaction"></a>

Specifies that AWS WAF should count the request. Optionally defines additional custom handling for the request.

This is used in the context of other settings, for example to specify values for `RuleAction` and web ACL `DefaultAction`.

## Syntax
<a name="aws-properties-wafv2-rulegroup-countaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-countaction-syntax.json"></a>

```
{
  "[CustomRequestHandling](#cfn-wafv2-rulegroup-countaction-customrequesthandling)" : {{CustomRequestHandling}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-countaction-syntax.yaml"></a>

```
  [CustomRequestHandling](#cfn-wafv2-rulegroup-countaction-customrequesthandling): {{
    CustomRequestHandling}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-countaction-properties"></a>

`CustomRequestHandling`  <a name="cfn-wafv2-rulegroup-countaction-customrequesthandling"></a>
Defines custom handling for the web request.
For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the *AWS WAF Developer Guide*.
*Required*: No
*Type*: [CustomRequestHandling](aws-properties-wafv2-rulegroup-customrequesthandling.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
