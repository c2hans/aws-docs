---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accessanalyzer-analyzer-archiverule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccessAnalyzer::Analyzer ArchiveRule
<a name="aws-properties-accessanalyzer-analyzer-archiverule"></a>

Contains information about an archive rule. Archive rules automatically archive new findings that meet the criteria you define when you create the rule.

## Syntax
<a name="aws-properties-accessanalyzer-analyzer-archiverule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accessanalyzer-analyzer-archiverule-syntax.json"></a>

```
{
  "[Filter](#cfn-accessanalyzer-analyzer-archiverule-filter)" : {{[ Filter, ... ]}},
  "[RuleName](#cfn-accessanalyzer-analyzer-archiverule-rulename)" : {{String}}
}
```

### YAML
<a name="aws-properties-accessanalyzer-analyzer-archiverule-syntax.yaml"></a>

```
  [Filter](#cfn-accessanalyzer-analyzer-archiverule-filter): {{
    - Filter}}
  [RuleName](#cfn-accessanalyzer-analyzer-archiverule-rulename): {{String}}
```

## Properties
<a name="aws-properties-accessanalyzer-analyzer-archiverule-properties"></a>

`Filter`  <a name="cfn-accessanalyzer-analyzer-archiverule-filter"></a>
The criteria for the rule.
*Required*: Yes
*Type*: [Array](aws-properties-accessanalyzer-analyzer-filter.md) of [Filter](aws-properties-accessanalyzer-analyzer-filter.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleName`  <a name="cfn-accessanalyzer-analyzer-archiverule-rulename"></a>
The name of the rule to create.
*Required*: Yes
*Type*: String
*Pattern*: `[A-Za-z][A-Za-z0-9_.-]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
