---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accessanalyzer-analyzer-internalaccessconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccessAnalyzer::Analyzer InternalAccessConfiguration
<a name="aws-properties-accessanalyzer-analyzer-internalaccessconfiguration"></a>

Specifies the configuration of an internal access analyzer for an AWS organization or account. This configuration determines how the analyzer evaluates internal access within your AWS environment.

## Syntax
<a name="aws-properties-accessanalyzer-analyzer-internalaccessconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accessanalyzer-analyzer-internalaccessconfiguration-syntax.json"></a>

```
{
  "[InternalAccessAnalysisRule](#cfn-accessanalyzer-analyzer-internalaccessconfiguration-internalaccessanalysisrule)" : {{InternalAccessAnalysisRule}}
}
```

### YAML
<a name="aws-properties-accessanalyzer-analyzer-internalaccessconfiguration-syntax.yaml"></a>

```
  [InternalAccessAnalysisRule](#cfn-accessanalyzer-analyzer-internalaccessconfiguration-internalaccessanalysisrule): {{
    InternalAccessAnalysisRule}}
```

## Properties
<a name="aws-properties-accessanalyzer-analyzer-internalaccessconfiguration-properties"></a>

`InternalAccessAnalysisRule`  <a name="cfn-accessanalyzer-analyzer-internalaccessconfiguration-internalaccessanalysisrule"></a>
Contains information about analysis rules for the internal access analyzer. These rules determine which resources and access patterns will be analyzed.
*Required*: No
*Type*: [InternalAccessAnalysisRule](aws-properties-accessanalyzer-analyzer-internalaccessanalysisrule.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
