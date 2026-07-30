---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accessanalyzer-analyzer-internalaccessanalysisrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccessAnalyzer::Analyzer InternalAccessAnalysisRule
<a name="aws-properties-accessanalyzer-analyzer-internalaccessanalysisrule"></a>

Contains information about analysis rules for the internal access analyzer. Analysis rules determine which entities will generate findings based on the criteria you define when you create the rule.

## Syntax
<a name="aws-properties-accessanalyzer-analyzer-internalaccessanalysisrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accessanalyzer-analyzer-internalaccessanalysisrule-syntax.json"></a>

```
{
  "[Inclusions](#cfn-accessanalyzer-analyzer-internalaccessanalysisrule-inclusions)" : {{[ InternalAccessAnalysisRuleCriteria, ... ]}}
}
```

### YAML
<a name="aws-properties-accessanalyzer-analyzer-internalaccessanalysisrule-syntax.yaml"></a>

```
  [Inclusions](#cfn-accessanalyzer-analyzer-internalaccessanalysisrule-inclusions): {{
    - InternalAccessAnalysisRuleCriteria}}
```

## Properties
<a name="aws-properties-accessanalyzer-analyzer-internalaccessanalysisrule-properties"></a>

`Inclusions`  <a name="cfn-accessanalyzer-analyzer-internalaccessanalysisrule-inclusions"></a>
A list of rules for the internal access analyzer containing criteria to include in analysis. Only resources that meet the rule criteria will generate findings.
*Required*: No
*Type*: Array of [InternalAccessAnalysisRuleCriteria](aws-properties-accessanalyzer-analyzer-internalaccessanalysisrulecriteria.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
