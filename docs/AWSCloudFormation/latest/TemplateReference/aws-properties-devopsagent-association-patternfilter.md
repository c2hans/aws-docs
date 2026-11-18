---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-patternfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association PatternFilter
<a name="aws-properties-devopsagent-association-patternfilter"></a>

A match condition based on regular expressions. The condition passes when the value matches any of the patterns.

## Syntax
<a name="aws-properties-devopsagent-association-patternfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-patternfilter-syntax.json"></a>

```
{
  "[Patterns](#cfn-devopsagent-association-patternfilter-patterns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-patternfilter-syntax.yaml"></a>

```
  [Patterns](#cfn-devopsagent-association-patternfilter-patterns): {{
    - String}}
```

## Properties
<a name="aws-properties-devopsagent-association-patternfilter-properties"></a>

`Patterns`  <a name="cfn-devopsagent-association-patternfilter-patterns"></a>
The regular expression patterns. Each pattern must match the entire value, for example `main` or `release/.*`.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `256 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
