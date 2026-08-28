---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-urifragment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL UriFragment
<a name="aws-properties-wafv2-webacl-urifragment"></a>

Inspect fragments of the request URI. You can specify the parts of the URI fragment to inspect and you can narrow the set of URI fragments to inspect by including or excluding specific keys.

This is used to indicate the web request component to inspect, in the [FieldToMatch](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-fieldtomatch) specification.

Example JSON: `"UriFragment": { "MatchPattern": { "All": {} }, "MatchScope": "KEY", "OversizeHandling": "MATCH" }`

## Syntax
<a name="aws-properties-wafv2-webacl-urifragment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-urifragment-syntax.json"></a>

```
{
  "[FallbackBehavior](#cfn-wafv2-webacl-urifragment-fallbackbehavior)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-urifragment-syntax.yaml"></a>

```
  [FallbackBehavior](#cfn-wafv2-webacl-urifragment-fallbackbehavior): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-urifragment-properties"></a>

`FallbackBehavior`  <a name="cfn-wafv2-webacl-urifragment-fallbackbehavior"></a>
What AWS WAF should do if it fails to completely parse the JSON body. The options are the following:
+ `EVALUATE_AS_STRING` - Inspect the body as plain text. AWS WAF applies the text transformations and inspection criteria that you defined for the JSON inspection to the body text string.
+ `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+ `NO_MATCH` - Treat the web request as not matching the rule statement.
If you don't provide this setting, AWS WAF parses and evaluates the content only up to the first parsing failure that it encounters.
Example JSON: `{ "UriFragment": { "FallbackBehavior": "MATCH"} }`
AWS WAF parsing doesn't fully validate the input JSON string, so parsing can succeed even for invalid JSON. When parsing succeeds, AWS WAF doesn't apply the fallback behavior. For more information, see [JSON body](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-fields-list.html#waf-rule-statement-request-component-json-body) in the *AWS WAF Developer Guide*.
*Required*: No
*Type*: String
*Allowed values*: `MATCH | NO_MATCH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
