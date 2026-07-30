---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accessanalyzer-analyzer-internalaccessanalysisrulecriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccessAnalyzer::Analyzer InternalAccessAnalysisRuleCriteria
<a name="aws-properties-accessanalyzer-analyzer-internalaccessanalysisrulecriteria"></a>

The criteria for an analysis rule for an internal access analyzer.

## Syntax
<a name="aws-properties-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-syntax.json"></a>

```
{
  "[AccountIds](#cfn-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-accountids)" : {{[ String, ... ]}},
  "[ResourceArns](#cfn-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-resourcearns)" : {{[ String, ... ]}},
  "[ResourceTypes](#cfn-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-resourcetypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-syntax.yaml"></a>

```
  [AccountIds](#cfn-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-accountids): {{
    - String}}
  [ResourceArns](#cfn-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-resourcearns): {{
    - String}}
  [ResourceTypes](#cfn-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-resourcetypes): {{
    - String}}
```

## Properties
<a name="aws-properties-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-properties"></a>

`AccountIds`  <a name="cfn-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-accountids"></a>
A list of AWS account IDs to apply to the internal access analysis rule criteria. Account IDs can only be applied to the analysis rule criteria for organization-level analyzers.
*Required*: No
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ResourceArns`  <a name="cfn-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-resourcearns"></a>
A list of resource ARNs to apply to the internal access analysis rule criteria. The analyzer will only generate findings for resources that match these ARNs.
*Required*: No
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ResourceTypes`  <a name="cfn-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-resourcetypes"></a>
A list of resource types to apply to the internal access analysis rule criteria. The analyzer will only generate findings for resources of these types. These resource types are currently supported for internal access analyzers:
+  `AWS::S3::Bucket`
+  `AWS::RDS::DBSnapshot`
+  `AWS::RDS::DBClusterSnapshot`
+  `AWS::S3Express::DirectoryBucket`
+  `AWS::DynamoDB::Table`
+  `AWS::DynamoDB::Stream`
*Required*: No
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
