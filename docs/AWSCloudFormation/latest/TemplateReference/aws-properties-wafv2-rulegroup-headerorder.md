---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-headerorder.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup HeaderOrder
<a name="aws-properties-wafv2-rulegroup-headerorder"></a>

Inspect a string containing the list of the request's header names, ordered as they appear in the web request that AWS WAF receives for inspection. AWS WAF generates the string and then uses that as the field to match component in its inspection. AWS WAF separates the header names in the string using colons and no added spaces, for example `host:user-agent:accept:authorization:referer`.

## Syntax
<a name="aws-properties-wafv2-rulegroup-headerorder-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-headerorder-syntax.json"></a>

```
{
  "[OversizeHandling](#cfn-wafv2-rulegroup-headerorder-oversizehandling)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-headerorder-syntax.yaml"></a>

```
  [OversizeHandling](#cfn-wafv2-rulegroup-headerorder-oversizehandling): {{String}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-headerorder-properties"></a>

`OversizeHandling`  <a name="cfn-wafv2-rulegroup-headerorder-oversizehandling"></a>
What AWS WAF should do if the headers determined by your match scope are more numerous or larger than AWS WAF can inspect. AWS WAF does not support inspecting the entire contents of request headers when they exceed 8 KB (8192 bytes) or 200 total headers. The underlying host service forwards a maximum of 200 headers and at most 8 KB of header contents to AWS WAF.
The options for oversize handling are the following:
+ `CONTINUE` - Inspect the available headers normally, according to the rule inspection criteria.
+ `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+ `NO_MATCH` - Treat the web request as not matching the rule statement.
*Required*: Yes
*Type*: String
*Allowed values*: `CONTINUE | MATCH | NO_MATCH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
