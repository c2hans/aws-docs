---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accessanalyzer-analyzer-unusedaccessconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccessAnalyzer::Analyzer UnusedAccessConfiguration
<a name="aws-properties-accessanalyzer-analyzer-unusedaccessconfiguration"></a>

Contains information about an unused access analyzer.

## Syntax
<a name="aws-properties-accessanalyzer-analyzer-unusedaccessconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accessanalyzer-analyzer-unusedaccessconfiguration-syntax.json"></a>

```
{
  "[AnalysisRule](#cfn-accessanalyzer-analyzer-unusedaccessconfiguration-analysisrule)" : {{AnalysisRule}},
  "[UnusedAccessAge](#cfn-accessanalyzer-analyzer-unusedaccessconfiguration-unusedaccessage)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-accessanalyzer-analyzer-unusedaccessconfiguration-syntax.yaml"></a>

```
  [AnalysisRule](#cfn-accessanalyzer-analyzer-unusedaccessconfiguration-analysisrule): {{
    AnalysisRule}}
  [UnusedAccessAge](#cfn-accessanalyzer-analyzer-unusedaccessconfiguration-unusedaccessage): {{Integer}}
```

## Properties
<a name="aws-properties-accessanalyzer-analyzer-unusedaccessconfiguration-properties"></a>

`AnalysisRule`  <a name="cfn-accessanalyzer-analyzer-unusedaccessconfiguration-analysisrule"></a>
Contains information about analysis rules for the analyzer. Analysis rules determine which entities will generate findings based on the criteria you define when you create the rule.
*Required*: No
*Type*: [AnalysisRule](aws-properties-accessanalyzer-analyzer-analysisrule.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`UnusedAccessAge`  <a name="cfn-accessanalyzer-analyzer-unusedaccessconfiguration-unusedaccessage"></a>
The specified access age in days for which to generate findings for unused access. For example, if you specify 90 days, the analyzer will generate findings for IAM entities within the accounts of the selected organization for any access that hasn't been used in 90 or more days since the analyzer's last scan. You can choose a value between 1 and 365 days.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `365`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
