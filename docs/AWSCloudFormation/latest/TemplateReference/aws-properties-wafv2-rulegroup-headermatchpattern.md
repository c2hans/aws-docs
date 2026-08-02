---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-headermatchpattern.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup HeaderMatchPattern
<a name="aws-properties-wafv2-rulegroup-headermatchpattern"></a>

The filter to use to identify the subset of headers to inspect in a web request.

You must specify exactly one setting: either `All`, `IncludedHeaders`, or `ExcludedHeaders`.

Example JSON: `"MatchPattern": { "ExcludedHeaders": [ "KeyToExclude1", "KeyToExclude2" ] }`

## Syntax
<a name="aws-properties-wafv2-rulegroup-headermatchpattern-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-headermatchpattern-syntax.json"></a>

```
{
  "[All](#cfn-wafv2-rulegroup-headermatchpattern-all)" : {{Json}},
  "[ExcludedHeaders](#cfn-wafv2-rulegroup-headermatchpattern-excludedheaders)" : {{[ String, ... ]}},
  "[IncludedHeaders](#cfn-wafv2-rulegroup-headermatchpattern-includedheaders)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-headermatchpattern-syntax.yaml"></a>

```
  [All](#cfn-wafv2-rulegroup-headermatchpattern-all): {{Json}}
  [ExcludedHeaders](#cfn-wafv2-rulegroup-headermatchpattern-excludedheaders): {{
    - String}}
  [IncludedHeaders](#cfn-wafv2-rulegroup-headermatchpattern-includedheaders): {{
    - String}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-headermatchpattern-properties"></a>

`All`  <a name="cfn-wafv2-rulegroup-headermatchpattern-all"></a>
Inspect all headers.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludedHeaders`  <a name="cfn-wafv2-rulegroup-headermatchpattern-excludedheaders"></a>
Inspect only the headers whose keys don't match any of the strings specified here.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `64 | 199`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludedHeaders`  <a name="cfn-wafv2-rulegroup-headermatchpattern-includedheaders"></a>
Inspect only the headers that have a key that matches one of the strings specified here.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `64 | 199`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-wafv2-rulegroup-headermatchpattern--examples"></a>

**Topics**
+ [Set a header match pattern for all paths](#aws-properties-wafv2-rulegroup-headermatchpattern--examples--Set_a_header_match_pattern_for_all_paths)
+ [Set a header match pattern with included paths](#aws-properties-wafv2-rulegroup-headermatchpattern--examples--Set_a_header_match_pattern_with_included_paths)

### Set a header match pattern for all paths
<a name="aws-properties-wafv2-rulegroup-headermatchpattern--examples--Set_a_header_match_pattern_for_all_paths"></a>

The following shows an example header match pattern specification for all headers.

#### YAML
<a name="aws-properties-wafv2-rulegroup-headermatchpattern--examples--Set_a_header_match_pattern_for_all_paths--yaml"></a>

```
MatchPattern:
  All: {}
```

#### JSON
<a name="aws-properties-wafv2-rulegroup-headermatchpattern--examples--Set_a_header_match_pattern_for_all_paths--json"></a>

```
"MatchPattern": {
  "All": {}
}
```

### Set a header match pattern with included paths
<a name="aws-properties-wafv2-rulegroup-headermatchpattern--examples--Set_a_header_match_pattern_with_included_paths"></a>

The following shows an example header match pattern specification with included keys.

#### YAML
<a name="aws-properties-wafv2-rulegroup-headermatchpattern--examples--Set_a_header_match_pattern_with_included_paths--yaml"></a>

```
MatchPattern:
  IncludedHeaders:
      - "User-Agent"
      - "Referer"
```

#### JSON
<a name="aws-properties-wafv2-rulegroup-headermatchpattern--examples--Set_a_header_match_pattern_with_included_paths--json"></a>

```
"MatchPattern": {
  "IncludedHeaders": [
    "User-Agent",
    "Referer"
  ]
}
```
