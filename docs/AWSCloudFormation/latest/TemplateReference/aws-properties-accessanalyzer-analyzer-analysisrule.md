---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accessanalyzer-analyzer-analysisrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccessAnalyzer::Analyzer AnalysisRule
<a name="aws-properties-accessanalyzer-analyzer-analysisrule"></a>

Contains information about analysis rules for the analyzer. Analysis rules determine which entities will generate findings based on the criteria you define when you create the rule.

## Syntax
<a name="aws-properties-accessanalyzer-analyzer-analysisrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accessanalyzer-analyzer-analysisrule-syntax.json"></a>

```
{
  "[Exclusions](#cfn-accessanalyzer-analyzer-analysisrule-exclusions)" : {{[ AnalysisRuleCriteria, ... ]}}
}
```

### YAML
<a name="aws-properties-accessanalyzer-analyzer-analysisrule-syntax.yaml"></a>

```
  [Exclusions](#cfn-accessanalyzer-analyzer-analysisrule-exclusions): {{
    - AnalysisRuleCriteria}}
```

## Properties
<a name="aws-properties-accessanalyzer-analyzer-analysisrule-properties"></a>

`Exclusions`  <a name="cfn-accessanalyzer-analyzer-analysisrule-exclusions"></a>
A list of rules for the analyzer containing criteria to exclude from analysis. Entities that meet the rule criteria will not generate findings.
*Required*: No
*Type*: Array of [AnalysisRuleCriteria](aws-properties-accessanalyzer-analyzer-analysisrulecriteria.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
