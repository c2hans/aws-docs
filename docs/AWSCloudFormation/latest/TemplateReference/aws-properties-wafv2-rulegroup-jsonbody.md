---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-jsonbody.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup JsonBody
<a name="aws-properties-wafv2-rulegroup-jsonbody"></a>

Inspect the body of the web request as JSON. The body immediately follows the request headers.

This is used to indicate the web request component to inspect, in the [FieldToMatch](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-fieldtomatch) specification.

Use the specifications in this object to indicate which parts of the JSON body to inspect using the rule's inspection criteria. AWS WAF inspects only the parts of the JSON that result from the matches that you indicate.

Example JSON: `"JsonBody": { "MatchPattern": { "All": {} }, "MatchScope": "ALL" }`

For additional information about this request component option, see [JSON body](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-fields-list.html#waf-rule-statement-request-component-json-body) in the *AWS WAF Developer Guide*.

## Syntax
<a name="aws-properties-wafv2-rulegroup-jsonbody-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-jsonbody-syntax.json"></a>

```
{
  "[InvalidFallbackBehavior](#cfn-wafv2-rulegroup-jsonbody-invalidfallbackbehavior)" : {{String}},
  "[MatchPattern](#cfn-wafv2-rulegroup-jsonbody-matchpattern)" : {{JsonMatchPattern}},
  "[MatchScope](#cfn-wafv2-rulegroup-jsonbody-matchscope)" : {{String}},
  "[OversizeHandling](#cfn-wafv2-rulegroup-jsonbody-oversizehandling)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-jsonbody-syntax.yaml"></a>

```
  [InvalidFallbackBehavior](#cfn-wafv2-rulegroup-jsonbody-invalidfallbackbehavior): {{String}}
  [MatchPattern](#cfn-wafv2-rulegroup-jsonbody-matchpattern): {{
    JsonMatchPattern}}
  [MatchScope](#cfn-wafv2-rulegroup-jsonbody-matchscope): {{String}}
  [OversizeHandling](#cfn-wafv2-rulegroup-jsonbody-oversizehandling): {{String}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-jsonbody-properties"></a>

`InvalidFallbackBehavior`  <a name="cfn-wafv2-rulegroup-jsonbody-invalidfallbackbehavior"></a>
What AWS WAF should do if it fails to completely parse the JSON body. The options are the following:
+ `EVALUATE_AS_STRING` - Inspect the body as plain text. AWS WAF applies the text transformations and inspection criteria that you defined for the JSON inspection to the body text string.
+ `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+ `NO_MATCH` - Treat the web request as not matching the rule statement.
If you don't provide this setting, AWS WAF parses and evaluates the content only up to the first parsing failure that it encounters.
AWS WAF parsing doesn't fully validate the input JSON string, so parsing can succeed even for invalid JSON. When parsing succeeds, AWS WAF doesn't apply the fallback behavior. For more information, see [JSON body](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-fields-list.html#waf-rule-statement-request-component-json-body) in the *AWS WAF Developer Guide*.
*Required*: No
*Type*: String
*Allowed values*: `MATCH | NO_MATCH | EVALUATE_AS_STRING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchPattern`  <a name="cfn-wafv2-rulegroup-jsonbody-matchpattern"></a>
The patterns to look for in the JSON body. AWS WAF inspects the results of these pattern matches against the rule inspection criteria.
*Required*: Yes
*Type*: [JsonMatchPattern](aws-properties-wafv2-rulegroup-jsonmatchpattern.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchScope`  <a name="cfn-wafv2-rulegroup-jsonbody-matchscope"></a>
The parts of the JSON to match against using the `MatchPattern`. If you specify `ALL`, AWS WAF matches against keys and values.
`All` does not require a match to be found in the keys and a match to be found in the values. It requires a match to be found in the keys or the values or both. To require a match in the keys and in the values, use a logical `AND` statement to combine two match rules, one that inspects the keys and another that inspects the values.
*Required*: Yes
*Type*: String
*Allowed values*: `ALL | KEY | VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OversizeHandling`  <a name="cfn-wafv2-rulegroup-jsonbody-oversizehandling"></a>
What AWS WAF should do if the body is larger than AWS WAF can inspect.
AWS WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to AWS WAF for inspection.
+ For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).
+ For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL `AssociationConfig`, for additional processing fees.
+ For AWS Amplify, use the CloudFront limit.
The options for oversize handling are the following:
+ `CONTINUE` - Inspect the available body contents normally, according to the rule inspection criteria.
+ `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+ `NO_MATCH` - Treat the web request as not matching the rule statement.
You can combine the `MATCH` or `NO_MATCH` settings for oversize handling with your rule and web ACL action settings, so that you block any request whose body is over the limit.
Default: `CONTINUE`
*Required*: No
*Type*: String
*Allowed values*: `CONTINUE | MATCH | NO_MATCH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-wafv2-rulegroup-jsonbody--examples"></a>

### Set the JSON body specification
<a name="aws-properties-wafv2-rulegroup-jsonbody--examples--Set_the_JSON_body_specification"></a>

The following shows an example JSON body field to match specification.

#### YAML
<a name="aws-properties-wafv2-rulegroup-jsonbody--examples--Set_the_JSON_body_specification--yaml"></a>

```
FieldToMatch:
  JsonBody:
    MatchPattern:
      IncludedPaths:
      - "/dogs/0/name"
      - "/cats/0/name"
    MatchScope: ALL
    InvalidFallbackBehavior: EVALUATE_AS_STRING
    OversizeHandling: MATCH
```

#### JSON
<a name="aws-properties-wafv2-rulegroup-jsonbody--examples--Set_the_JSON_body_specification--json"></a>

```
"FieldToMatch": {
  "JsonBody": {
    "MatchPattern": {
      "IncludedPaths": [
        "/dogs/0/name",
        "/cats/0/name"
      ]
    },
    "MatchScope": "ALL",
    "InvalidFallbackBehavior": "EVALUATE_AS_STRING",
    "OversizeHandling": "MATCH"
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
