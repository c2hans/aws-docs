---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accessanalyzer-analyzer-analysisrulecriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccessAnalyzer::Analyzer AnalysisRuleCriteria
<a name="aws-properties-accessanalyzer-analyzer-analysisrulecriteria"></a>

The criteria for an analysis rule for an analyzer. The criteria determine which entities will generate findings.

## Syntax
<a name="aws-properties-accessanalyzer-analyzer-analysisrulecriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accessanalyzer-analyzer-analysisrulecriteria-syntax.json"></a>

```
{
  "[AccountIds](#cfn-accessanalyzer-analyzer-analysisrulecriteria-accountids)" : {{[ String, ... ]}},
  "[ResourceTags](#cfn-accessanalyzer-analyzer-analysisrulecriteria-resourcetags)" : {{[ [ , ... ], ... ]}}
}
```

### YAML
<a name="aws-properties-accessanalyzer-analyzer-analysisrulecriteria-syntax.yaml"></a>

```
  [AccountIds](#cfn-accessanalyzer-analyzer-analysisrulecriteria-accountids): {{
    - String}}
  [ResourceTags](#cfn-accessanalyzer-analyzer-analysisrulecriteria-resourcetags): {{
    -
    - }}
```

## Properties
<a name="aws-properties-accessanalyzer-analyzer-analysisrulecriteria-properties"></a>

`AccountIds`  <a name="cfn-accessanalyzer-analyzer-analysisrulecriteria-accountids"></a>
A list of AWS account IDs to apply to the analysis rule criteria. The accounts cannot include the organization analyzer owner account. Account IDs can only be applied to the analysis rule criteria for organization-level analyzers. The list cannot include more than 2,000 account IDs.
*Required*: No
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ResourceTags`  <a name="cfn-accessanalyzer-analyzer-analysisrulecriteria-resourcetags"></a>
An array of key-value pairs to match for your resources. You can use the set of Unicode letters, digits, whitespace, `_`, `.`, `/`, `=`, `+`, and `-`.
For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with `aws:`.
For the tag value, you can specify a value that is 0 to 256 characters in length. If the specified tag value is 0 characters, the rule is applied to all principals with the specified tag key.
*Required*: No
*Type*: Array of Array
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
