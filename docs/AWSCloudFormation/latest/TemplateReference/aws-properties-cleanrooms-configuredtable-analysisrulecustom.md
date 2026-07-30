---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-analysisrulecustom.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable AnalysisRuleCustom
<a name="aws-properties-cleanrooms-configuredtable-analysisrulecustom"></a>

A type of analysis rule that enables the table owner to approve custom SQL queries on their configured tables. It supports differential privacy.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-analysisrulecustom-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-analysisrulecustom-syntax.json"></a>

```
{
  "[AdditionalAnalyses](#cfn-cleanrooms-configuredtable-analysisrulecustom-additionalanalyses)" : {{String}},
  "[AllowedAnalyses](#cfn-cleanrooms-configuredtable-analysisrulecustom-allowedanalyses)" : {{[ String, ... ]}},
  "[AllowedAnalysisProviders](#cfn-cleanrooms-configuredtable-analysisrulecustom-allowedanalysisproviders)" : {{[ String, ... ]}},
  "[DifferentialPrivacy](#cfn-cleanrooms-configuredtable-analysisrulecustom-differentialprivacy)" : {{DifferentialPrivacy}},
  "[DisallowedOutputColumns](#cfn-cleanrooms-configuredtable-analysisrulecustom-disallowedoutputcolumns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-analysisrulecustom-syntax.yaml"></a>

```
  [AdditionalAnalyses](#cfn-cleanrooms-configuredtable-analysisrulecustom-additionalanalyses): {{String}}
  [AllowedAnalyses](#cfn-cleanrooms-configuredtable-analysisrulecustom-allowedanalyses): {{
    - String}}
  [AllowedAnalysisProviders](#cfn-cleanrooms-configuredtable-analysisrulecustom-allowedanalysisproviders): {{
    - String}}
  [DifferentialPrivacy](#cfn-cleanrooms-configuredtable-analysisrulecustom-differentialprivacy): {{
    DifferentialPrivacy}}
  [DisallowedOutputColumns](#cfn-cleanrooms-configuredtable-analysisrulecustom-disallowedoutputcolumns): {{
    - String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-analysisrulecustom-properties"></a>

`AdditionalAnalyses`  <a name="cfn-cleanrooms-configuredtable-analysisrulecustom-additionalanalyses"></a>
 An indicator as to whether additional analyses (such as AWS Clean Rooms ML) can be applied to the output of the direct query.
*Required*: No
*Type*: String
*Allowed values*: `ALLOWED | REQUIRED | NOT_ALLOWED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedAnalyses`  <a name="cfn-cleanrooms-configuredtable-analysisrulecustom-allowedanalyses"></a>
The ARN of the analysis templates that are allowed by the custom analysis rule.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedAnalysisProviders`  <a name="cfn-cleanrooms-configuredtable-analysisrulecustom-allowedanalysisproviders"></a>
The IDs of the AWS accounts that are allowed to query by the custom analysis rule. Required when `allowedAnalyses` is `ANY_QUERY`.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DifferentialPrivacy`  <a name="cfn-cleanrooms-configuredtable-analysisrulecustom-differentialprivacy"></a>
The differential privacy configuration.
*Required*: No
*Type*: [DifferentialPrivacy](aws-properties-cleanrooms-configuredtable-differentialprivacy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisallowedOutputColumns`  <a name="cfn-cleanrooms-configuredtable-analysisrulecustom-disallowedoutputcolumns"></a>
 A list of columns that aren't allowed to be shown in the query output.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
