---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-headers.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL Headers
<a name="aws-properties-wafv2-webacl-headers"></a>

Inspect all headers in the web request. You can specify the parts of the headers to inspect and you can narrow the set of headers to inspect by including or excluding specific keys.

This is used to indicate the web request component to inspect, in the `FieldToMatch` specification.

If you want to inspect just the value of a single header, use the `SingleHeader``FieldToMatch` setting instead.

Example JSON: `"Headers": { "MatchPattern": { "All": {} }, "MatchScope": "KEY", "OversizeHandling": "MATCH" }`

## Syntax
<a name="aws-properties-wafv2-webacl-headers-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-headers-syntax.json"></a>

```
{
  "[MatchPattern](#cfn-wafv2-webacl-headers-matchpattern)" : {{HeaderMatchPattern}},
  "[MatchScope](#cfn-wafv2-webacl-headers-matchscope)" : {{String}},
  "[OversizeHandling](#cfn-wafv2-webacl-headers-oversizehandling)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-headers-syntax.yaml"></a>

```
  [MatchPattern](#cfn-wafv2-webacl-headers-matchpattern): {{
    HeaderMatchPattern}}
  [MatchScope](#cfn-wafv2-webacl-headers-matchscope): {{String}}
  [OversizeHandling](#cfn-wafv2-webacl-headers-oversizehandling): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-headers-properties"></a>

`MatchPattern`  <a name="cfn-wafv2-webacl-headers-matchpattern"></a>
The filter to use to identify the subset of headers to inspect in a web request.
You must specify exactly one setting: either `All`, `IncludedHeaders`, or `ExcludedHeaders`.
Example JSON: `"MatchPattern": { "ExcludedHeaders": [ "KeyToExclude1", "KeyToExclude2" ] }`
*Required*: Yes
*Type*: [HeaderMatchPattern](aws-properties-wafv2-webacl-headermatchpattern.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchScope`  <a name="cfn-wafv2-webacl-headers-matchscope"></a>
The parts of the headers to match with the rule inspection criteria. If you specify `ALL`, AWS WAF inspects both keys and values.
`All` does not require a match to be found in the keys and a match to be found in the values. It requires a match to be found in the keys or the values or both. To require a match in the keys and in the values, use a logical `AND` statement to combine two match rules, one that inspects the keys and another that inspects the values.
*Required*: Yes
*Type*: String
*Allowed values*: `ALL | KEY | VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OversizeHandling`  <a name="cfn-wafv2-webacl-headers-oversizehandling"></a>
What AWS WAF should do if the headers determined by your match scope are more numerous or larger than AWS WAF can inspect. AWS WAF does not support inspecting the entire contents of request headers when they exceed 8 KB (8192 bytes) or 200 total headers. The underlying host service forwards a maximum of 200 headers and at most 8 KB of header contents to AWS WAF.
The options for oversize handling are the following:
+ `CONTINUE` - Inspect the available headers normally, according to the rule inspection criteria.
+ `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+ `NO_MATCH` - Treat the web request as not matching the rule statement.
*Required*: Yes
*Type*: String
*Allowed values*: `CONTINUE | MATCH | NO_MATCH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-wafv2-webacl-headers--examples"></a>

### Set the Headers specification
<a name="aws-properties-wafv2-webacl-headers--examples--Set_the_Headers_specification"></a>

The following shows an example Headers field to match specification.

#### YAML
<a name="aws-properties-wafv2-webacl-headers--examples--Set_the_Headers_specification--yaml"></a>

```
FieldToMatch:
  Headers:
    MatchPattern:
      IncludedHeaders:
      - "User-Agent"
      - "Referer"
    MatchScope: ALL
    OversizeHandling: MATCH
```

#### JSON
<a name="aws-properties-wafv2-webacl-headers--examples--Set_the_Headers_specification--json"></a>

```
"FieldToMatch": {
  "Headers": {
    "MatchPattern": {
      "IncludedHeaders": [
        "User-Agent",
        "Referer"
      ]
    },
    "MatchScope": "ALL",
    "OversizeHandling": "MATCH"
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
